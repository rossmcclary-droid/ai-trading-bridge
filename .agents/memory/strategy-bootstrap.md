---
name: Strategy bootstrap handling
description: Rules for versioned Trading Brain strategy configuration.
---

Keep strategy bootstrap metadata and grading policy separate from the full strategy rules; do not invent, summarize, reinterpret, or replace rules before the approved version is loaded.

**Why:** The Trading Brain configuration is being staged for a later Bootstrap v2 insertion, and premature rule content could change execution decisions.

**How to apply:** Expose only the active bootstrap identity, lineage, grading scale, minimum executable grade, and loaded-state flag until the full rules are explicitly provided.