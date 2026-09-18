# Keystone D003 — Persist instrumentation

Status: COMPLETE
Challenge=0

## LIVE_OK and checkpoint
- Proved the live Replit workspace with `LIVE_OK` and `pwd` (`/workspace`).
- Pre-edit checkpoint created at:
  `artifacts/api-server/.keystone-backups/patch002do-persist-20260913T151714Z/`
- SHA256 manifest: `/tmp/keystone-d003/PERSIST_CHECKPOINT_SHA256.txt`
- Original hashes:
  - `exports.py`: `1c41a253e4c898f240e69e9560cc9bd80cd134854d4e23b0efbe4083c43132c6`
  - `export_timings.py`: `9bcde1e76e4fa1d460faa8d9718abb82a1201311fd8493d70b71ad70cf5d147`

## Before/after path
Before, finalization serialized the payload and saved the job without recording a direct serialization/save span, and `ready_visible` was stamped before the durable save path.

After, `artifacts/api-server/app/routes/exports.py` records `payload_assembly_serialization_ms` around payload JSON serialization, records `durable_result_write_ms` around `export_job_store.save_job(job)`, and stamps `ready_visible` after the durable save. The existing `build_patch002dj` call then receives the completed job timing data.

`artifacts/api-server/app/services/export_timings.py` maps those job timings into the existing 002D-J buckets:
- `payload_assembly_serialization`
- `durable_result_write`
- `durable_ready_transition`
- `logical_complete_to_visible_ready`

No new top-level persist bucket and no broker/Challenge logic were added.

## Files changed
- `artifacts/api-server/app/routes/exports.py`
- `artifacts/api-server/app/services/export_timings.py`

## Validation
- `python -m py_compile artifacts/api-server/app/routes/exports.py artifacts/api-server/app/services/export_timings.py` — PASS.
- Import via `PYTHONPATH=artifacts/api-server` — PASS.
- Synthetic `build_patch002dj` fixture with job timings `1.25 ms`, `2.5 ms` and clock delta `0.004 ms` produced:
  - `payload_assembly_serialization`: `1.25 ms`
  - `durable_result_write`: `2.5 ms`
  - `durable_ready_transition`: `0.004 ms`
  - `logical_complete_to_visible_ready`: `0.004 ms`
- `RESIDUAL_GAP.md` was checked; no applicable file was present at the target path.

## Backup
This report is also copied into the pre-edit backup directory alongside the checkpointed source files.

## Recommendation
Do not run a Challenge. The next step is one normal controlled export and inspection of the emitted 002D-J diagnostics to confirm the live path reports these non-zero buckets.
