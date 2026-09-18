from __future__ import annotations
import time
from contextlib import ContextDecorator
from typing import Any

def _num(v):
    try: return round(float(v or 0), 3)
    except (TypeError, ValueError): return 0.0

class StageTimer(ContextDecorator):
    def __init__(self, sink, name, *, nested=True):
        self.sink, self.name, self.nested = sink, name, nested
        self.started = 0.0
        self.ms = 0.0
    def __enter__(self):
        self.started = time.perf_counter(); return self
    def __exit__(self, exc_type, exc, tb):
        self.ms = (time.perf_counter()-self.started)*1000
        self.sink.append({"name":self.name,"ms":_num(self.ms),"nested":self.nested})
        return False

def record_span(sink, name, *, nested=True):
    return StageTimer(sink, name,nested=nested)

def build_patch002c(*,scan,stages,discovery,qn,qwall,qfail,rows,raw,unique,dups):
 ds=discovery or {};d=_num(sum(_num(v) for v in ds.values()))
 s=_num((stages or {}).get("stage_3_scanner",0));r=_num(max(0,scan-d));a=_num(max(0,r-s))
 b=[{"name":"market_discovery","ms":d},{"name":"scanner_per_symbol","ms":s},{"name":"analysis_enrichment_sizing_truth_bootstrap_serialize","ms":a}]
 rs=[x for x in (rows or []) if isinstance(x,dict)];ts=[_num(x.get("total_ms",0)) for x in rs]
 return {"wall":{"created_to_ready_ms":_num(scan),"export_ai_scan_ms":_num(scan),"queue_ms":0.0,"scope":"in-process export; READY boundary unavailable"},"non_overlapping_export_buckets":b,"discovery_substages":[{"name":str(k),"ms":_num(v)} for k,v in ds.items()],"quote_gather":{"n_tasks":int(qn or 0),"gather_wall_ms":_num(qwall),"failures":int(qfail or 0)},"per_symbol":rs,"aggregates":{"sum_ms":_num(sum(ts)),"max_ms":_num(max(ts) if ts else 0),"slowest_ms":_num(max(ts) if ts else 0),"execution_mode":"sequential scan loop"},"duplicates":{"raw":int(raw or 0),"unique":int(unique or 0),"dups":list(dups or []),"list_build":"requested_symbols/market_discovery shortlist"},"residual_ms":r,"residual_pct":_num(r/scan*100 if scan else 0),"attributed_pct_of_created_to_ready":_num(sum(x["ms"] for x in b)/scan*100 if scan else 0),"measurement_only":True}

def build_patch002d(**k):
    stages=k.get("stages") or {}; q=k.get("quote") or {}; h=k.get("history") or {}; wall=_num(k.get("wall_created_to_ready_ms"));
    def c(xs,n=True): return [{"name":str(x.get("name","unknown")),"ms":_num(x.get("ms")),"nested":n} for x in (xs or []) if isinstance(x,dict)]
    mega=c(k.get("mega_bucket_split")); other=c(k.get("other_discovery_split")); top=c(k.get("top_level"),False) if isinstance(k.get("top_level"),list) else [{"name":str(a),"ms":_num(b),"nested":False} for a,b in stages.items() if _num(b)>0]
    if not top and wall: top=[{"name":"unattributed_export","ms":wall,"nested":False}]
    atoms=mega+other; qw=0; qs=0; qt=len(k.get("raw") or []); hn=0; hd=0; hp=0; sm=sum(x.get("ms",0) for x in top); rank=sorted(atoms+top,key=lambda x:x.get("ms",0),reverse=True)
    qitems=[x for x in atoms if "quote" in str(x.get("name","")).lower()]
    qs=_num(q.get("gather_wall_ms"))
    task_elapsed = q.get("task_elapsed_ms") if isinstance(q.get("task_elapsed_ms"), list) else []
    task_elapsed = [_num(v) for v in task_elapsed]
    max_task_ms = max(task_elapsed) if task_elapsed else 0.0
    qt=int(q.get("n_tasks") or q.get("task_count") or len(k.get("raw") or []) or len(qitems))
    hn=_num(h.get("history_network_ms")); hd=_num(h.get("history_delay_sleep_ms")); hp=_num(h.get("history_processing_ms"))
    sm=_num(sum(x.get("ms",0) for x in top)); rank=sorted(atoms+top,key=lambda x:x.get("ms",0),reverse=True)
    def p(i): x=rank[i] if len(rank)>i else {"name":None,"ms":0}; return {"name":x.get("name"),"ms":_num(x.get("ms"))}
    return {"schema":"patch002d","measurement_only":True,"wall_created_to_ready_ms":wall,"top_level":top,"top_level_non_overlapping":True,"top_level_sum_ms":sm,"top_level_coverage_pct":_num(sm/wall*100 if wall else 0),"mega_bucket_split":mega,"other_discovery_split":other,"quote":{"n_tasks":qt,"gather_wall_ms":qs,"task_elapsed_ms":task_elapsed,"max_task_elapsed_ms":max_task_ms,"slowest_ms_invalid_legacy":q.get("slowest_ms_invalid_legacy"),"consistency_note":q.get("consistency_note") or "gather_wall_ms, max_task_elapsed_ms, and Semaphore(6) are different quantities."},"history":{"history_network_ms":hn,"history_delay_sleep_ms":hd,"history_processing_ms":hp,"total_ms":_num(hn+hd+hp)},"history_aggregates":{"network_ms":hn,"delay_sleep_ms":hd,"processing_ms":hp,"total_ms":_num(hn+hd+hp)},"per_symbol":[x for x in (k.get("rows") or []) if isinstance(x,dict)],"duplicates":k.get("duplicates") or [],"events":k.get("events") or [],"largest_atomic":p(0),"second_largest_atomic":p(1),"residual_ms":_num(max(wall-sm,0)),"nested_spans_are_not_in_top_level":True}


def build_patch002dj(job, *, export_payload=None):
    """Build one canonical 002D-J report from existing measurements only."""
    payload = export_payload if isinstance(export_payload, dict) else {}
    clock = job.get("_patch002dj_clock", {}) if isinstance(job, dict) else {}

    def number(value):
        try:
            return round(float(value), 3)
        except (TypeError, ValueError):
            return None

    def delta(begin, end):
        left = number(clock.get(begin))
        right = number(clock.get(end))
        if left is None or right is None:
            return None
        return round(max(right - left, 0.0), 3)

    legacy = payload.get("patch002dj_timings_ms")
    if not isinstance(legacy, dict):
        legacy = payload.get("patch002_timings_ms")
    if not isinstance(legacy, dict):
        legacy = payload.get("_timings_ms")
    if not isinstance(legacy, dict):
        legacy = payload.get("timing_ms", {})
    if not isinstance(legacy, dict):
        legacy = payload
    stage = payload.get("stage") or payload.get("stages") or payload
    if not isinstance(stage, dict):
        stage = {}

    def measured(*names):
        for name in names:
            value = number(legacy.get(name))
            if value is None:
                value = number(stage.get(name))
            if value is not None:
                return value, name
        return None, None

    def job_measure(*names):
        for name in names:
            value = number(job.get(name)) if isinstance(job, dict) else None
            if value is not None:
                return value, f"job.{name}"
        return None, None

    top_sources = {
        "job_creation": (delta("created", "queued"), "clock.created_to_queued"),
        "accepted_queued": (delta("queued", "task_start"), "clock.queued_to_task_start"),
        "export_function_start": (delta("task_start", "export_start"), "clock.task_start_to_export_start"),
        "discovery": measured("stage_2_market_discovery", "market_discovery", "discovery"),
        "quote_gather": measured("quote_gather", "quote_gather_ms"),
        "shortlist_selection": measured("shortlist_selection", "shortlist_selection_ms", "shortlist_ms"),
        "deep_analysis": measured("stage_4_analysis", "candidate_analysis", "deep_analysis", "deep_analysis_ms"),
        "per_symbol_history_timeframe_fetches": measured("stage_3_scan", "history_retrieval", "per_symbol_history_timeframe_fetches"),
        "enrichment": measured("enrichment", "enrichment_ms"),
        "truth_layer": measured("stage_6_truth_layer", "truth_layer", "truth_layer_ms"),
        "bootstrap_verification": measured("stage_7_bootstrap_and_response", "bootstrap_status", "bootstrap_verification"),
        "payload_assembly_serialization": job_measure("payload_assembly_serialization_ms") or measured("stage_5_payload_assembly", "payload_assembly", "payload_assembly_serialization"),
        "durable_result_write": job_measure("durable_result_write_ms", "post_export_write_prepare_ms", "post_export_prepare_ms"),
        "durable_ready_transition": (delta("logical_complete", "ready_visible"), "clock.logical_complete_to_ready_visible"),
        "logical_complete_to_visible_ready": (delta("logical_complete", "ready_visible"), "clock.logical_complete_to_ready_visible"),
    }
    top_level = {
        name: {"ms": value, "source": source}
        for name, (value, source) in top_sources.items()
    }
    nested_timings = {
        name: {"ms": value, "nested": True}
        for name, value in stage.items()
        if number(value) is not None
    }
    top_sum = round(sum(item["ms"] for item in top_level.values() if item["ms"] is not None), 3)
    total = number(clock.get("created_to_ready_ms"))
    if total is None:
        total = number(clock.get("created_to_ready"))
    if total is None and isinstance(job, dict):
        total = number(job.get("total_created_to_ready_ms"))
    if total is None and isinstance(job, dict):
        total = number(job.get("ready_visible"))
    residual = round(total - top_sum, 3) if total is not None else None
    coverage = round((top_sum / total) * 100, 3) if total not in (None, 0) else 0.0
    return {
        "patch": "002D-J",
        "clock": {"time_source": "perf_counter", "created_to_ready_ms": total},
        "top_level": top_level,
        "top_level_sum_ms": top_sum,
        "nested_timings": nested_timings,
        "nested_spans_are_not_in_top_level": True,
        "residual_ms": residual,
        "residual_pct": round((residual / total) * 100, 3) if total not in (None, 0) and residual is not None else 0.0,
        "coverage_pct": coverage,
        "non_overlapping": True,
        "unmapped_top_level_buckets": [name for name, item in top_level.items() if item["ms"] is None],
        "source_timing_key": "patch002dj_timings_ms",
    }
