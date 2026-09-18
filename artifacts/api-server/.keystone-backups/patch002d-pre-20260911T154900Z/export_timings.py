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

def build_patch002d(**k):
    stages=k.get("stages") or {}; q=k.get("quote") or {}; h=k.get("history") or {}; wall=_num(k.get("wall_created_to_ready_ms"));
    def c(xs,n=True): return [{"name":str(x.get("name","unknown")),"ms":_num(x.get("ms")),"nested":n} for x in (xs or []) if isinstance(x,dict)]
    mega=c(k.get("mega_bucket_split")); other=c(k.get("other_discovery_split")); top=c(k.get("top_level"),False) if isinstance(k.get("top_level"),list) else [{"name":str(a),"ms":_num(b),"nested":False} for a,b in stages.items() if _num(b)>0]
    if not top and wall: top=[{"name":"unattributed_export","ms":wall,"nested":False}]
    atoms=mega+other; qw=0; qs=0; qt=len(k.get("raw") or []); hn=0; hd=0; hp=0; sm=sum(x.get("ms",0) for x in top); rank=sorted(atoms+top,key=lambda x:x.get("ms",0),reverse=True)
    def p(i): x=rank[i] if len(rank)>i else {"name":None,"ms":0}; return {"name":x.get("name"),"ms":_num(x.get("ms"))}
    return {"schema":"patch002d","measurement_only":True,"wall_created_to_ready_ms":wall,"top_level":top,"top_level_non_overlapping":True,"top_level_sum_ms":sm,"top_level_coverage_pct":_num(sm/wall*100 if wall else 0),"mega_bucket_split":mega,"other_discovery_split":other,"quote":{"n_tasks":qt,"wall_ms":qw,"slowest_ms":qs},"history":{"history_network_ms":hn,"history_delay_sleep_ms":hd,"history_processing_ms":hp,"total_ms":_num(hn+hd+hp)},"history_aggregates":{"network_ms":hn,"delay_sleep_ms":hd,"processing_ms":hp,"total_ms":_num(hn+hd+hp)},"per_symbol":[x for x in (k.get("rows") or []) if instance(x,dict)],"duplicates":k.get("duplicates") or [],"events":k.get("events") or [],"largest_atomic":p(0),"second_largest_atomic":p(1),"residual_ms":_num(max(wall-sm,0)),"nested_spans_are_not_in_top_level":True}
