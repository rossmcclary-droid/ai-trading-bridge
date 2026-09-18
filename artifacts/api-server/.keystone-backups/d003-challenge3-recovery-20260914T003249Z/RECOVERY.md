# D003 Challenge3 Recovery

## Job identity
- Exact durable job_id: `ddff8ce67f42489cb457a96b22b1828b`
- len(job_id): 32
- Raw POST artifacts: NOT FOUND. Searched `/tmp/keystone-d003*`, `/tmp`, `/home/runner/workspace`, and available shell/history evidence. The durable key is the exact recovered ID, but raw `post.out` cannot be independently verified.
- Challenge POST count during recovery: 0. No retry or second POST was issued.

## Durable record
- Store: `/home/runner/workspace/artifacts/api-server/data/export_jobs/jobs.json`
- Exact key: PRESENT
- nickname: Challenge
- created_at: `2026-09-14T00:12:58.572959+00:00`
- completed_at: `2026-09-14T00:13:00.001118+00:00`
- updated_at: `2026-09-14T00:13:00.001125+00:00`
- durable state: FAILED
- error: `_quote_stats` unbound
- result_path: None; no READY result or timing payload exists.
- lifecycle evidence: job_creation_to_task_start_ms `351.67`; async_schedule_wait_ms `351.67`; export failed about 1.428 seconds after creation.

## Newest durable jobs by created_at
- `2026-09-14T00:12:58.572959+00:00` | `ddff8ce67f42489cb457a96b22b1828b` | FAILED | `_quote_stats` unbound
- `2026-09-13T19:59:45.559293+00:00` | `797cad5e5824800983644b02751548a8` | READY
- `2026-09-13T19:49:07.439464+00:00` | `1fb7934d71414e95b901ef1c30f3f741` | FAILED | `job_payload` undefined
- `2026-09-13T15:46:22.197139+00:00` | `f6bd5b60cf2440738ad125d57bc3806` | FAILED | account external ID
- `2026-09-12T16:09:39.540612+00:00` | `5130f4174ead4f1ea0a2df99e93c73e2` | READY

## 404 diagnosis
- Exact durable ID GET after the run: HTTP 200 and returned the persisted FAILED record.
- Same ID with UUID hyphens, length 36: HTTP 404, `AI Scan export job not found.`
- Truncated ID, length 30: HTTP 404, same detail.
- Source evidence: the GET/download route calls `_load_export_job(job_id)`, which calls `export_job_store.get_job(job_id, include_content=...)`; `get_job` performs an exact key lookup in the durable `jobs.json` index.
- Conclusion: the 200-second 404 polling was caused by a wrong, malformed, or truncated poll ID, not by a durable-load failure. The exact malformed value used by the poller cannot be proven because its raw `post.out` and JOB_ID file were not retained.
- A uvicorn reload loss is not supported: the exact record is durable, and exact-ID lookup works now. A GET endpoint bug is not supported by the source and live exact-ID 200. A brief write/read race cannot explain 404s for about 200 seconds; the durable record was created and failed within about 1.4 seconds.

## Fix
- Fix applied: NO. No source files changed; no restart; no Challenge POST.

## Evidence backup
- `/home/runner/workspace/artifacts/api-server/.keystone-backups/d003-challenge3-recovery-20260914T003249Z/`
- Includes `jobs.json`, `DURABLE_RECORD.txt`, and `GET_CHECK.txt`.
- Full durable error text: cannot access local variable "_quote_stats" where it is not associated with a value
