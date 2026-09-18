from __future__ import annotations
import inspect
from datetime import datetime,timezone
from typing import Any,Mapping
NOT_TRADABLE_ON_ACCOUNT="NOT_TRADABLE_ON_ACCOUNT"
TRADABILITY_UNVERIFIED="TRADABILITY_UNVERIFIED"
TRADABLE_ON_ACCOUNT="TRADABLE_ON_ACCOUNT"
def _sym(x:Any)->str:return str(x or "").strip().upper()
def _v(o:Any,*ns:str)->Any:
    for n in ns:
        v=o.get(n) if isinstance(o,Mapping) else getattr(o,n,None)
        if v is not None:return v
    return None
async def verify_symbol_tradable_on_account(*,client:Any,account:Any,symbol:str,resolved:Any|None=None,allow_cache:bool=False):
    s=_sym(symbol);d={"symbol":s,"allow_cache":bool(allow_cache)}
    if not s:return False,TRADABILITY_UNVERIFIED,{**d,"error":"empty_symbol"}
    if client is None or account is None:return False,TRADABILITY_UNVERIFIED,{**d,"error":"missing_client_or_account"}
    aid=_v(account,"external_account_id","id","account_id","accountId");an=_v(account,"external_account_number","accNum","acc_num","account_number");d.update(account_id=aid,acc_num=an)
    if aid is None or an is None:return False,TRADABILITY_UNVERIFIED,{**d,"error":"missing_account_identity"}
    iid=_v(resolved,"tradable_instrument_id","tradableInstrumentId","id");rid=_v(resolved,"route_id","routeId")
    if iid is None or rid is None:
        try:
            from app.services.tradelocker_resolver import resolve_tradelocker_instrument
            instrument_response = client.get_available_instruments(
            account_id=aid, acc_num=an
        )
            if inspect.isawaitable(instrument_response):
                    instrument_response = await instrument_response
            r = resolve_tradelocker_instrument(instrument_response, s)
            if inspect.isawaitable(r):r=await r
            if r is None:return False,NOT_TRADABLE_ON_ACCOUNT,{**d,"error":"resolver_miss"}
            iid=_v(r,"tradable_instrument_id","tradableInstrumentId","id");rid=_v(r,"route_id","routeId")
        except Exception as e:return False,TRADABILITY_UNVERIFIED,{**d,"error":f"resolve_failed:{type(e).__name__}"}
    if iid is None or rid is None:return False,TRADABILITY_UNVERIFIED,{**d,"error":"resolution_missing"}
    d.update(tradable_instrument_id=iid,route_id=rid)
    try:
        x=client.get_instrument_details(
            tradable_instrument_id=iid, route_id=rid, acc_num=an
        )
        if inspect.isawaitable(x):x=await x
    except Exception as e:return False,TRADABILITY_UNVERIFIED,{**d,"error":f"details_failed:{type(e).__name__}"}
    if not x:return False,NOT_TRADABLE_ON_ACCOUNT,{**d,"error":"empty_instrument_details"}
    if isinstance(x,Mapping) and any(k in x for k in ("error","errors")) and not any(k in x for k in ("id","symbol","name","tradableInstrumentId","tradable_instrument_id")):return False,NOT_TRADABLE_ON_ACCOUNT,{**d,"error":"error_payload"}
    d["verified_at"]=datetime.now(timezone.utc).isoformat();return True,TRADABLE_ON_ACCOUNT,d
async def assert_pending_instrument_tradable(pending:Mapping[str,Any]|None,*,client:Any=None,account:Any=None,resolved:Any|None=None,scan_result:Mapping[str,Any]|None=None):
    if client is not None and account is not None:return await verify_symbol_tradable_on_account(client=client,account=account,symbol=_v(pending or {},"instrument") or "",resolved=resolved)
    if not isinstance(pending,Mapping) or not isinstance(scan_result,Mapping):return False,TRADABILITY_UNVERIFIED,{"error":"missing_live_scan_evidence"}
    e=pending.get("tradability");sid=scan_result.get("tradability_scan_id")
    if not isinstance(e,Mapping) or e.get("status")!=TRADABLE_ON_ACCOUNT:return False,NOT_TRADABLE_ON_ACCOUNT,{"error":"missing_or_negative_tradability_evidence"}
    if not sid or e.get("scan_id")!=sid:return False,TRADABILITY_UNVERIFIED,{"error":"stale_tradability_evidence"}
    return True,TRADABLE_ON_ACCOUNT,{"scan_id":sid,"instrument":_sym(pending.get("instrument"))}
