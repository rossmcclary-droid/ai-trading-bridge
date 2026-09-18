"""Patch 002C measurement-only timing schema."""
from __future__ import annotations
def n(v):
 try:return round(float(v or 0),3)
 except (TypeError,ValueError):return 0.0
def build_patch002c(*,scan,stages,discovery,qn,qwall,qfail,rows,raw,unique,dups):
 ds=discovery or {};d=n(sum(n(v) for v in ds.values()))
 s=n((stages or {}).get("stage_3_scanner",0));r=n(max(0,scan-d));a=n(max(0,r-s))
 b=[{"name":"market_discovery","ms":d},{"name":"scanner_per_symbol","ms":s},{"name":"analysis_enrichment_sizing_truth_bootstrap_serialize","ms":a}]
 rs=[x for x in (rows or []) if isinstance(x,dict)];ts=[n(x.get("total_ms",0)) for x in rs]
 return {"wall":{"created_to_ready_ms":n(scan),"export_ai_scan_ms":n(scan),"queue_ms":0.0,"scope":"in-process export; READY boundary unavailable"},"non_overlapping_export_buckets":b,"discovery_substages":[{"name":str(k),"ms":n(v)} for k,v in ds.items()],"quote_gather":{"n_tasks":int(qn or 0),"gather_wall_ms":n(qwall),"failures":int(qfail or 0)},"per_symbol":rs,"aggregates":{"sum_ms":n(sum(ts)),"max_ms":n(max(ts) if ts else 0),"slowest_ms":n(max(ts) if ts else 0),"execution_mode":"sequential scan loop"},"duplicates":{"raw":int(raw or 0),"unique":int(unique or 0),"dups":list(dups or []),"list_build":"requested_symbols/market_discovery shortlist"},"residual_ms":r,"residual_pct":n(r/scan*100 if scan else 0),"attributed_pct_of_created_to_ready":n(sum(x["ms"] for x in b)/scan*100 if scan else 0),"measurement_only":True}
