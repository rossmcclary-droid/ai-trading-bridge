# DIRECTIVE 003 - Controlled Export Evidence

Date: 2026-09-13 UTC-4
Mode: LIVE_OK; health checks were read-only.

OUTCOME
No safe non-Challenge live export was completed. Read-only discovery found Demo1 and Challenge in export history/config context. One Demo1 start was attempted as the non-Challenge smoke candidate; it reached FAILED. No Challenge POST was made.

Exact Challenge export count this run: 0.
Status: CHALLENGE_SKIPPED_NEED_AUTH.

SYNTHETIC FINALIZE/PERSIST PROOF
The real app.services.export_timings.build_patch002dj was invoked with a synthetic full-finalize job clock and patch002dj_timings_ms payload. Evidence: /tmp/keystone-d003/synthetic_patch002dj.json.

Buckets (ms):
payload_assembly_serialization: 1.25
durable_result_write: 2.5
durable_ready_transition: 10.0
logical_complete_to_visible_ready: 10.0
top_level_sum_ms: 53.75
residual_ms: null; residual_pct: 0.0
coverage_pct: 0.0 (synthetic fixture has no discovery-stage timings)

Lifecycle buckets are sourced from clock.logical_complete_to_ready_visible; persist buckets are sourced from job timing fields. This proves non-zero wiring, not broker/live latency.

DECISION
Do not authorize a Challenge export from this run. One Challenge export is not justified because it would violate the Challenge=0 constraint and no auth-backed non-Challenge path was available. The synthetic result localizes instrumentation but does not explain the historical ~97s.
