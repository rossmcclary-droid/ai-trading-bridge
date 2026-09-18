# DIRECTIVE 003 — JOB_PAYLOAD_FIX

## Outcome
Fixed the finalize/READY-path NameError without changing scan, quote, concurrency, or API semantics.
Challenge=0 this run. No broker POST. No optimization.

## Checkpoint
Backup directory: artifacts/api-server/.keystone-backups/patch002ds-job-payload-20260913T195400Z
Checkpoint exports.py SHA256: 86be1c2eddafe1c9254d0cc34bd651a9afcaf421b6ac5ff5690ce3789e3bb2e0
Checkpoint file: /tmp/keystone-d003-challenge/JOB_PAYLOAD_CHECKPOINT_SHA256.txt

## Diagnosis
Durable job 1fb7934d71414e95b901ef1c30f3f741 in artifacts/api-server/data/export_jobs/jobs.json is FAILED with error: name job_payload is not defined.
In exports.py, _job_payload is initialized/loaded at lines 4002/4004 and _job_diag is derived from it at line 4005. The finalize block incorrectly referenced bare job_payload at lines 4033 and 4052.

## Minimal fix
Line 4033 now uses _job_payload.setdefault("diagnostics", {}).
Line 4052 now guards with if _job_payload is not None:.
Only source file edited: artifacts/api-server/app/routes/exports.py.

## Validation
PASS: python -m py_compile artifacts/api-server/app/routes/exports.py
PASS: PYTHONPATH=artifacts/api-server python import app.routes.exports
PASS: bare-symbol scan rg -n "\\bjob_payload\\b" exports.py returned no matches.
PASS: adjacent finalize-path review of lines 3988-4062 found no other concrete, unambiguous undefined name.
Note: pyflakes is unavailable in the Replit environment; no broker or synthetic finalize call was run.

## Hashes
Final exports.py SHA256: 6a7ebe352748f61a3f8c8770e150b28d4f10283e552fb315cab3b8458f845878

## Challenge safety
No new Challenge measurement was run. One new Challenge measurement is conditionally safe only after this source is deployed/restarted and the live health/runtime path is confirmed; source-only validation does not establish live safety.
