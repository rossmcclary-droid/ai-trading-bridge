# DIRECTIVE 003 — Challenge measurement

- Job ID: `797cafd5e5824800983644b0275154a8`
- Status: `READY`
- Created: `2026-09-13T19:59:45.559293+00:00`
- READY/completed: `2026-09-13T20:01:39.406347+00:00`
- Created→READY: `113.847 s`
- Challenge count: **1**

## Complete export payload

```json
{
  "account": {
    "environment": "Demo",
    "nickname": "Challenge",
    "platform": "TradeLocker"
  },
  "account_risk_snapshot": {
    "available": true,
    "balance": 9333.76,
    "daily_fees": 0,
    "daily_gross_pl": 0,
    "daily_net_pl": 0,
    "daily_trade_count": 0,
    "daily_volume": 0.0,
    "equity": null,
    "error": null,
    "floating_gross_pl": 0,
    "floating_net_pl": 0.0,
    "free_margin": 9333.76,
    "initial_margin_requirement": 0,
    "leverage": null,
    "maintenance_margin_requirement": 0,
    "margin_warning_level": 100.0,
    "maximum_permitted_risk_percent": 1.0,
    "orders_count": 0,
    "positions_count": 0,
    "raw_tradelocker_state": {
      "availableFunds": 9333.76,
      "balance": 9333.76,
      "blockedBalance": 0,
      "blockedForStocks": 0,
      "cashBalance": 9333.76,
      "initialMarginReq": 0,
      "maintMarginReq": 0,
      "marginBeforeWarning": 9333.76,
      "marginWarningLevel": 100.0,
      "openGrossPnL": 0,
      "openNetPnL": 0.0,
      "optionValue": 0,
      "ordersCount": 0,
      "positionsCount": 0,
      "projectedBalance": 9333.76,
      "stockOrdersReq": 0,
      "stocksValue": 0,
      "stopOutLevel": 144.0,
      "todayFees": 0,
      "todayGross": 0,
      "todayNet": 0,
      "todayTradesCount": 0,
      "todayVolume": 0.0,
      "unsettledCash": 0,
      "warningMarginReq": 0,
      "withdrawalAvailable": 9333.76
    },
    "stop_out_level": 144.0,
    "unavailable_fields": [
      "equity",
      "used_margin",
      "leverage"
    ],
    "used_margin": null
  },
  "atlas_context": {
    "bootstrap": {
      "modified_at": "2026-08-26T10:57:37.697127+00:00",
      "path": "/home/runner/workspace/artifacts/api-server/app/brain/bootstrap_v2.md",
      "previous_available": true,
      "previous_filename": "bootstrap_20260826T105737Z_f309b008cfe1_pre_rollback.md",
      "restart_required": true,
      "sha256": "84a467e807998069de9dab42584a7c2294e03ec7e7eee12d4b85e8bffa86bc9a",
      "size_bytes": 37917
    },
    "monitor": {
      "actionable_instrument": null,
      "actionable_trade_found": false,
      "candidate_instrument": null,
      "candidate_ready_for_review": false,
      "external_ai_review_status": null,
      "interval_seconds": 60,
      "last_error": null,
      "last_scan_at": null,
      "nickname": null,
      "running": false,
      "scan_count": 0,
      "started_at": null,
      "stop_reason": null,
      "symbols": null,
      "workflow_state": "IDLE"
    }
  },
  "bootstrap_runtime_status": "LOADED_CURRENT",
  "bootstrap_runtime_verification": {
    "bootstrap_runtime_status": "LOADED_CURRENT",
    "configured_bootstrap_path": "/home/runner/workspace/artifacts/api-server/app/brain/bootstrap_v2.md",
    "configured_bootstrap_sha256": "84a467e807998069de9dab42584a7c2294e03ec7e7eee12d4b85e8bffa86bc9a",
    "current_disk_bootstrap_sha256": "84a467e807998069de9dab42584a7c2294e03ec7e7eee12d4b85e8bffa86bc9a",
    "legacy_restart_required": true,
    "runtime_loaded_bootstrap_sha256": "84a467e807998069de9dab42584a7c2294e03ec7e7eee12d4b85e8bffa86bc9a",
    "verification_basis": "Configured bootstrap SHA-256, bootstrap module startup SHA-256, and current on-disk SHA-256 are identical."
  },
  "configured_bootstrap_sha256": "84a467e807998069de9dab42584a7c2294e03ec7e7eee12d4b85e8bffa86bc9a",
  "current_exposure": {
    "available": true,
    "error": null,
    "normalization_note": "Broker records are preserved verbatim. Normalized symbol/direction/size/entry/SL/TP/P&L fields will be added after a non-empty TradeLocker response is observed.",
    "open_position_count": 0,
    "open_positions": [],
    "pending_order_count": 0,
    "pending_orders": [],
    "raw_orders_response": {
      "d": {
        "orders": []
      },
      "s": "ok"
    },
    "raw_positions_response": {
      "d": {
        "positions": []
      },
      "s": "ok"
    }
  },
  "data_source": "TradeLocker",
  "diagnostics": {
    "patch002_timings_ms": {
      "stage_1_account_and_connector": 1289.419,
      "stage_2_market_discovery": 11124.847,
      "stage_3_scanner": 1544.812,
      "stage_4_analysis": 2689.374,
      "stage_5_payload_assembly": 0.056,
      "stage_6_truth_layer": 0.04,
      "stage_7_bootstrap_and_response": 0.236
    },
    "patch002b_timings": {
      "async_schedule_wait_ms": 95.553,
      "duplicate_processing": {},
      "duplicate_symbols": [],
      "export_ai_scan_total_ms": 113738.113,
      "job_creation_to_task_start_ms": 95.553,
      "job_state_finalization_ms": 0.09,
      "market_discovery_parent_total_ms": 11124.822,
      "market_discovery_substages_ms": {
        "account_instrument_resolution_ms": 1289.419,
        "filtering_normalization_ms": 0.0,
        "other_discovery_ms": 0.0,
        "quote_retrieval_gather_ms": 11068.417,
        "resolver_spec_details_ms": 0.0,
        "shortlist_construction_ms": 55.532,
        "universe_instrument_acquisition_ms": 1289.192,
        "waits_retries_delays_ms": 0.0
      },
      "per_symbol_aggregate": {
        "execution_mode": "serial",
        "max_ms": 2689.365,
        "slowest_symbol": "DASHUSD",
        "sum_ms": 8600.484
      },
      "per_symbol_timings": [
        {
          "analysis_ms": 1.04,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 1.04,
          "retry_count": 0,
          "symbol": "BTCUSD",
          "timeframe_request_count": 4,
          "total_ms": 1463.182
        },
        {
          "analysis_ms": 1.29,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 1.29,
          "retry_count": 0,
          "symbol": "ETHUSD",
          "timeframe_request_count": 4,
          "total_ms": 1448.858
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "SOLUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.002
        },
        {
          "analysis_ms": 1.096,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 1.096,
          "retry_count": 0,
          "symbol": "BNBUSD",
          "timeframe_request_count": 4,
          "total_ms": 1454.273
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "XRPUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.001
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "XMRUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.0
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "XLMUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.0
        },
        {
          "analysis_ms": 0.837,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 0.837,
          "retry_count": 0,
          "symbol": "DOGEUSD",
          "timeframe_request_count": 4,
          "total_ms": 1544.802
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "ZECUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.001
        },
        {
          "analysis_ms": 1.324,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 1.324,
          "retry_count": 0,
          "symbol": "DASHUSD",
          "timeframe_request_count": 4,
          "total_ms": 2689.365
        }
      ],
      "post_export_write_prepare_ms": 13.155,
      "shortlist_raw_count": 10,
      "shortlist_unique_count": 10,
      "total_created_to_ready_ms": 113847.082,
      "wrapper_pre_export_ms": 0.011
    },
    "patch002c_timings": {
      "aggregates": {
        "execution_mode": "sequential scan loop",
        "max_ms": 2689.365,
        "slowest_ms": 2689.365,
        "sum_ms": 8600.484
      },
      "attributed_pct_of_created_to_ready": 100.0,
      "discovery_substages": [
        {
          "ms": 1289.192,
          "name": "universe_instrument_acquisition_ms"
        },
        {
          "ms": 11068.417,
          "name": "quote_retrieval_gather_ms"
        },
        {
          "ms": 55.532,
          "name": "shortlist_construction_ms"
        },
        {
          "ms": 0.0,
          "name": "filtering_normalization_ms"
        },
        {
          "ms": 0.0,
          "name": "resolver_spec_details_ms"
        },
        {
          "ms": 0.0,
          "name": "waits_retries_delays_ms"
        },
        {
          "ms": 0.0,
          "name": "other_discovery_ms"
        },
        {
          "ms": 1289.419,
          "name": "account_instrument_resolution_ms"
        }
      ],
      "duplicates": {
        "dups": [],
        "list_build": "requested_symbols/market_discovery shortlist",
        "raw": 10,
        "unique": 10
      },
      "measurement_only": true,
      "non_overlapping_export_buckets": [
        {
          "ms": 13702.56,
          "name": "market_discovery"
        },
        {
          "ms": 1544.812,
          "name": "scanner_per_symbol"
        },
        {
          "ms": 98481.108,
          "name": "analysis_enrichment_sizing_truth_bootstrap_serialize"
        }
      ],
      "per_symbol": [
        {
          "analysis_ms": 1.04,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 1.04,
          "retry_count": 0,
          "symbol": "BTCUSD",
          "timeframe_request_count": 4,
          "total_ms": 1463.182
        },
        {
          "analysis_ms": 1.29,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 1.29,
          "retry_count": 0,
          "symbol": "ETHUSD",
          "timeframe_request_count": 4,
          "total_ms": 1448.858
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "SOLUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.002
        },
        {
          "analysis_ms": 1.096,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 1.096,
          "retry_count": 0,
          "symbol": "BNBUSD",
          "timeframe_request_count": 4,
          "total_ms": 1454.273
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "XRPUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.001
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "XMRUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.0
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "XLMUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.0
        },
        {
          "analysis_ms": 0.837,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 0.837,
          "retry_count": 0,
          "symbol": "DOGEUSD",
          "timeframe_request_count": 4,
          "total_ms": 1544.802
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "ZECUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.001
        },
        {
          "analysis_ms": 1.324,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 1.324,
          "retry_count": 0,
          "symbol": "DASHUSD",
          "timeframe_request_count": 4,
          "total_ms": 2689.365
        }
      ],
      "quote_gather": {
        "failures": 0,
        "gather_wall_ms": 11068.417,
        "n_tasks": 19
      },
      "residual_ms": 100025.92,
      "residual_pct": 87.952,
      "wall": {
        "created_to_ready_ms": 113728.48,
        "export_ai_scan_ms": 113728.48,
        "queue_ms": 0.0,
        "scope": "in-process export; READY boundary unavailable"
      }
    },
    "patch002d_timings": {
      "duplicates": [],
      "events": [],
      "history": {
        "history_delay_sleep_ms": 0.0,
        "history_network_ms": 0.0,
        "history_processing_ms": 0.0,
        "total_ms": 0.0
      },
      "history_aggregates": {
        "delay_sleep_ms": 0.0,
        "network_ms": 0.0,
        "processing_ms": 0.0,
        "total_ms": 0.0
      },
      "largest_atomic": {
        "ms": 11124.847,
        "name": "other_discovery"
      },
      "measurement_only": true,
      "mega_bucket_split": [
        {
          "ms": 1289.419,
          "name": "account_instrument_detail_lookup",
          "nested": true
        },
        {
          "ms": 11124.847,
          "name": "other_discovery",
          "nested": true
        },
        {
          "ms": 2689.374,
          "name": "candidate_analysis",
          "nested": true
        },
        {
          "ms": 0.056,
          "name": "payload_assembly",
          "nested": true
        },
        {
          "ms": 0.04,
          "name": "truth_layer",
          "nested": true
        },
        {
          "ms": 0.236,
          "name": "bootstrap_status",
          "nested": true
        }
      ],
      "nested_spans_are_not_in_top_level": true,
      "other_discovery_split": [
        {
          "ms": 1289.192,
          "name": "universe_instrument_acquisition_ms",
          "nested": true
        },
        {
          "ms": 11068.417,
          "name": "quote_retrieval_gather_ms",
          "nested": true
        },
        {
          "ms": 55.532,
          "name": "shortlist_construction_ms",
          "nested": true
        },
        {
          "ms": 0.0,
          "name": "filtering_normalization_ms",
          "nested": true
        },
        {
          "ms": 0.0,
          "name": "resolver_spec_details_ms",
          "nested": true
        },
        {
          "ms": 0.0,
          "name": "waits_retries_delays_ms",
          "nested": true
        },
        {
          "ms": 0.0,
          "name": "other_discovery_ms",
          "nested": true
        },
        {
          "ms": 1289.419,
          "name": "account_instrument_resolution_ms",
          "nested": true
        }
      ],
      "per_symbol": [
        {
          "analysis_ms": 1.04,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 1.04,
          "retry_count": 0,
          "symbol": "BTCUSD",
          "timeframe_request_count": 4,
          "total_ms": 1463.182
        },
        {
          "analysis_ms": 1.29,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 1.29,
          "retry_count": 0,
          "symbol": "ETHUSD",
          "timeframe_request_count": 4,
          "total_ms": 1448.858
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "SOLUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.002
        },
        {
          "analysis_ms": 1.096,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 1.096,
          "retry_count": 0,
          "symbol": "BNBUSD",
          "timeframe_request_count": 4,
          "total_ms": 1454.273
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "XRPUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.001
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "XMRUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.0
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "XLMUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.0
        },
        {
          "analysis_ms": 0.837,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 0.837,
          "retry_count": 0,
          "symbol": "DOGEUSD",
          "timeframe_request_count": 4,
          "total_ms": 1544.802
        },
        {
          "analysis_ms": 0.0,
          "history_ms": null,
          "retry_count": 0,
          "symbol": "ZECUSD",
          "timeframe_request_count": 4,
          "total_ms": 0.001
        },
        {
          "analysis_ms": 1.324,
          "history_delay_sleep_ms": 0.0,
          "history_ms": null,
          "history_network_ms": 0.0,
          "history_or_analysis_cpu_ms": 1.324,
          "retry_count": 0,
          "symbol": "DASHUSD",
          "timeframe_request_count": 4,
          "total_ms": 2689.365
        }
      ],
      "quote": {
        "consistency_note": "gather_wall_ms is true asyncio.gather elapsed; max(task_elapsed_ms) is the slowest individual task; Semaphore(6) is the concurrency limit; these are different quantities.",
        "gather_wall_ms": 11068.417,
        "max_task_elapsed_ms": 11066.522,
        "n_tasks": 24,
        "slowest_ms_invalid_legacy": null,
        "task_elapsed_ms": [
          1433.134,
          1438.243,
          1445.956,
          1450.877,
          1458.563,
          1462.407,
          2879.9,
          2881.988,
          2897.874,
          2906.567,
          2943.172,
          3575.49,
          9599.579,
          9618.187,
          9649.396,
          9658.108,
          9676.82,
          10322.507,
          11066.522
        ]
      },
      "residual_ms": 97079.914,
      "schema": "patch002d",
      "second_largest_atomic": {
        "ms": 11124.847,
        "name": "stage_2_market_discovery"
      },
      "top_level": [
        {
          "ms": 1289.419,
          "name": "stage_1_account_and_connector",
          "nested": false
        },
        {
          "ms": 11124.847,
          "name": "stage_2_market_discovery",
          "nested": false
        },
        {
          "ms": 1544.812,
          "name": "stage_3_scanner",
          "nested": false
        },
        {
          "ms": 2689.374,
          "name": "stage_4_analysis",
          "nested": false
        },
        {
          "ms": 0.056,
          "name": "stage_5_payload_assembly",
          "nested": false
        },
        {
          "ms": 0.04,
          "name": "stage_6_truth_layer",
          "nested": false
        },
        {
          "ms": 0.236,
          "name": "stage_7_bootstrap_and_response",
          "nested": false
        }
      ],
      "top_level_coverage_pct": 14.639,
      "top_level_non_overlapping": true,
      "top_level_sum_ms": 16648.784,
      "wall_created_to_ready_ms": 113728.698
    },
    "patch002dj_timings": {
      "clock": {
        "created_to_ready_ms": null,
        "time_source": "perf_counter"
      },
      "coverage_pct": 0.0,
      "nested_spans_are_not_in_top_level": true,
      "nested_timings": {
        "stage_1_account_and_connector": {
          "ms": 1289.419,
          "nested": true
        },
        "stage_2_market_discovery": {
          "ms": 11124.847,
          "nested": true
        },
        "stage_3_scanner": {
          "ms": 1544.812,
          "nested": true
        },
        "stage_4_analysis": {
          "ms": 2689.374,
          "nested": true
        },
        "stage_5_payload_assembly": {
          "ms": 0.056,
          "nested": true
        },
        "stage_6_truth_layer": {
          "ms": 0.04,
          "nested": true
        },
        "stage_7_bootstrap_and_response": {
          "ms": 0.236,
          "nested": true
        }
      },
      "non_overlapping": true,
      "patch": "002D-J",
      "residual_ms": null,
      "residual_pct": 0.0,
      "source_timing_key": "patch002dj_timings_ms",
      "top_level": {
        "accepted_queued": {
          "ms": 0.096,
          "source": "clock.queued_to_task_start"
        },
        "account_and_connector": {
          "ms": 1289.419,
          "source": "stage_1_account_and_connector"
        },
        "bootstrap_verification": {
          "ms": 0.236,
          "source": "stage_7_bootstrap_and_response"
        },
        "deep_analysis": {
          "ms": 2689.374,
          "source": "stage_4_analysis"
        },
        "discovery": {
          "ms": 11124.847,
          "source": "stage_2_market_discovery"
        },
        "durable_ready_transition": {
          "ms": null,
          "source": "clock.logical_complete_to_ready_visible"
        },
        "durable_result_write": {
          "ms": 13.155,
          "source": "job.post_export_write_prepare_ms"
        },
        "enrichment": {
          "ms": null,
          "source": null
        },
        "export_function_start": {
          "ms": 0.0,
          "source": "clock.task_start_to_export_start"
        },
        "job_creation": {
          "ms": 0.0,
          "source": "clock.created_to_queued"
        },
        "logical_complete_to_visible_ready": {
          "ms": null,
          "source": "clock.logical_complete_to_ready_visible"
        },
        "payload_assembly_serialization": {
          "ms": 8.559,
          "source": "job.payload_assembly_serialization_ms"
        },
        "per_symbol_history_timeframe_fetches": {
          "ms": null,
          "source": null
        },
        "quote_gather": {
          "ms": null,
          "source": null
        },
        "shortlist_selection": {
          "ms": null,
          "source": null
        },
        "truth_layer": {
          "ms": 0.04,
          "source": "stage_6_truth_layer"
        }
      },
      "top_level_sum_ms": 15125.726,
      "unmapped_top_level_buckets": [
        "quote_gather",
        "shortlist_selection",
        "per_symbol_history_timeframe_fetches",
        "enrichment",
        "durable_ready_transition",
        "logical_complete_to_visible_ready"
      ]
    },
    "timing_clock": "perf_counter"
  },
  "export_completeness": {
    "account_state_available": true,
    "candles_complete": true,
    "data_age_seconds": 14496,
    "external_ai_decision_ready": true,
    "instrument_specs_available": true,
    "positions_available": true,
    "quotes_available": true
  },
  "external_ai_workflow": {
    "allowed_external_ai_decisions": [
      "APPROVE",
      "WATCH",
      "REJECT"
    ],
    "bridge_role": "READ_ONLY_MARKET_INTELLIGENCE",
    "candidate_status_meaning": "AWAITING_EXTERNAL_AI_REVIEW means the Bridge found and froze a setup worthy of independent Atlas review. It is not trade authorization.",
    "decision_meanings": {
      "APPROVE": "Recommend the frozen setup to the user for manual placement. This does not authorize Bridge execution.",
      "REJECT": "Discard the frozen candidate as unsuitable.",
      "WATCH": "Do not recommend the trade yet. Return monitoring conditions so the Bridge can continue observing it."
    },
    "execution_allowed": false,
    "execution_instruction": "The Bridge cannot execute trades. If APPROVE is returned, present the final trade plan to the user for manual placement through their permitted copy-trading workflow.",
    "review_protocol": [
      "Reassess the frozen candidate using the freshest market data.",
      "Check account state, exposure, spreads, candles, and data freshness.",
      "Do not treat the frozen trade plan as authorization.",
      "Return exactly one decision: APPROVE, WATCH, or REJECT.",
      "If WATCH is selected, provide explicit monitoring conditions.",
      "If APPROVE is selected, present the final setup to the user."
    ],
    "user_execution_required": true
  },
  "external_review_requirements": {
    "bridge_analysis_is_trade_authorization": false,
    "fresh_economic_calendar_check_required": true,
    "fresh_macro_context_required": true,
    "fresh_market_reassessment_required": true,
    "fresh_web_news_check_required": true,
    "instruction": "Before APPROVE, independently reassess the current market, relevant breaking news, macro conditions, and economic-calendar risk. Treat all Bridge plans and historical monitor state as decision context, never authorization.",
    "pending_entries_must_be_reassessed": true,
    "use_live_ask_for_long_market_entry": true,
    "use_live_bid_for_short_market_entry": true
  },
  "generated_at": "2026-09-13T20:01:39.382930+00:00",
  "instruments": [
    {
      "bridge_analysis": {
        "decision": "WATCH",
        "directional_bias": "bullish",
        "execution_5m": {
          "candle_confirmed": true,
          "confirmed": false,
          "reason": "5M structure shifted, but momentum/candle confirmation is incomplete.",
          "rsi_14": 49.73,
          "rsi_confirmed": false,
          "structure_shift": true
        },
        "execution_context": {
          "atr_14": 95.275307,
          "distance_to_high": 132.79999999998836,
          "distance_to_low": 273.0,
          "extension": "normal",
          "range_position": 0.6727,
          "recent_high": 77386.4,
          "recent_low": 76980.6
        },
        "geometry": {
          "entry_quality": "late",
          "invalidation": 76980.6,
          "reward_to_risk": 0.49,
          "risk_distance": 273.0,
          "room_to_target": 132.79999999998836,
          "target_reference": 77386.4
        },
        "multi_horizon_state": "transitioning",
        "reason": "The setup has not earned approval under current multi-horizon evidence.",
        "setup_grade": "WATCH",
        "symbol": "BTCUSD",
        "timeframes": {
          "15M": {
            "candle_count": 192,
            "last_price": 77253.6,
            "momentum": "neutral",
            "rsi_14": 56.39,
            "structure": "bullish"
          },
          "1H": {
            "candle_count": 168,
            "last_price": 77253.6,
            "momentum": "neutral",
            "rsi_14": 55.29,
            "structure": "bullish"
          },
          "4H": {
            "candle_count": 84,
            "last_price": 77253.6,
            "momentum": "neutral",
            "rsi_14": 45.71,
            "structure": "neutral"
          },
          "5M": {
            "candle_count": 144,
            "last_price": 77253.6,
            "momentum": "neutral",
            "rsi_14": 49.73,
            "structure": "bearish"
          }
        },
        "trade_plan": {
          "distinct_targets": [
            77386.4
          ],
          "entry_reference": 77253.6,
          "final_safe_loss": 76980.6,
          "geometry_policy": "structural_invalidation_no_synthetic_buffer",
          "live_market_entry_reference": null,
          "live_market_entry_reference_is_authorization": false,
          "live_market_entry_reference_side": null,
          "reason": "Structural trade geometry is viable.",
          "reward_to_tp1": 132.79999999998836,
          "reward_to_tp2": null,
          "reward_to_tp3": null,
          "risk_distance": 273.0,
          "rr_tp1": 0.49,
          "rr_tp2": null,
          "rr_tp3": null,
          "safe_loss": 76980.6,
          "stop_buffer": 0.0,
          "stop_buffer_basis": "No synthetic buffer applied. Structural invalidation is the authoritative Bridge stop until Atlas defines an explicit buffer rule.",
          "structure_invalidation": 76980.6,
          "target_count": 1,
          "tp1": 77386.4,
          "tp2": null,
          "tp3": null,
          "valid": true
        }
      },
      "broker": {
        "route_id": 452,
        "tradable_instrument_id": 206
      },
      "instrument_specs": {
        "available": true,
        "bar_source": "BID",
        "base_currency": "BTC",
        "cache": {
          "age_seconds": 1487313.865,
          "captured_at": "2026-08-27T14:53:05.516347+00:00",
          "source": "stale_cache",
          "stale": true
        },
        "contract_size": 1,
        "error": null,
        "leverage": "3.00",
        "lot_step": 0.01,
        "margin_hedging_type": "fx_cfd",
        "maximum_lot": null,
        "minimum_lot": 0.01,
        "minimum_stop_distance": null,
        "quote_currency": "USD",
        "raw_details": {
          "d": {
            "barSource": "BID",
            "baseCurrency": "BTC",
            "betSize": null,
            "betStep": null,
            "bettingCurrency": null,
            "contractMonth": null,
            "country": null,
            "deliveryStatus": null,
            "description": "Bitcoin vs US Dollar",
            "exerciseStyle": null,
            "firstTradeDate": null,
            "hasDaily": true,
            "hasIntraday": true,
            "industry": null,
            "isin": "",
            "lastTradeDate": null,
            "leverage": "3.00",
            "localizedName": "BTCUSD",
            "logoUrl": null,
            "lotSize": 1,
            "lotStep": 0.01,
            "margin_hedging_type": "fx_cfd",
            "marketCap": null,
            "marketDataExchange": "Cryptos",
            "maxLot": null,
            "minLot": 0.01,
            "name": "BTCUSD",
            "noticeDate": null,
            "quotingCurrency": "USD",
            "sector": null,
            "settlementDate": null,
            "settlementSystem": "Immediate",
            "strikePrice": null,
            "strikeType": null,
            "symbolStatus": "FULLY_OPEN",
            "tickCost": [
              {
                "leftRangeLimit": null,
                "tickCost": 0.0
              }
            ],
            "tickSize": [
              {
                "leftRangeLimit": null,
                "tickSize": 0.01
              }
            ],
            "tradeSessionId": 1547,
            "tradeSessionStatusId": 20,
            "tradingExchange": "Crypto",
            "type": "CRYPTO"
          },
          "s": "ok"
        },
        "route_id": 9912,
        "symbol_status": "FULLY_OPEN",
        "tick_cost_raw": 0.0,
        "tick_size": 0.01,
        "tick_value": null,
        "tradable_instrument_id": 206,
        "trading_session_id": 1547,
        "trading_session_status_id": 20
      },
      "market_snapshot": {
        "analysis_price": 77253.6,
        "analysis_price_source": "latest_5m_bar",
        "ask": 77261.7,
        "ask_size": 1.0,
        "atlas_received_at": "2026-09-13T20:01:32.245578+00:00",
        "bid": 77260.5,
        "bid_size": 1.0,
        "broker_staleness_known": false,
        "cache": {
          "age_seconds": 0,
          "captured_at": "2026-09-13T20:01:32.245558+00:00",
          "source": "live",
          "stale": false
        },
        "live_ask": 77261.7,
        "live_bid": 77260.5,
        "live_executable_market_entry": null,
        "live_executable_market_entry_is_authorization": false,
        "live_executable_market_entry_side": null,
        "live_mid": 77261.1,
        "market_entry_price_policy": "LONG market execution evaluates live ask; SHORT market execution evaluates live bid. Structural or pending entry_reference remains context and must be reassessed before approval.",
        "price_semantics": "analysis_price is the latest 5M bar/reference price, not an executable quote. live_bid and live_ask are current TradeLocker quote values; live_mid is their midpoint. For market-entry evaluation use live_ask for LONG and live_bid for SHORT.",
        "quote_age_seconds": null,
        "quote_error": null,
        "quote_note": "Bid/ask values are live TradeLocker quote values. The broker response does not currently expose a quote timestamp, so broker quote age/staleness is left null rather than estimated.",
        "quote_timestamp": null,
        "quotes_available": true,
        "raw_quote": {
          "d": {
            "ap": 77261.7,
            "as": 1.0,
            "bp": 77260.5,
            "bs": 1.0
          },
          "s": "ok"
        },
        "spread": 1.1999999999970896
      },
      "symbol": "BTCUSD",
      "timeframes": {
        "15M": {
          "candle_count": 192,
          "candle_status": {
            "data_age_seconds": 990,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789328700000,
            "latest_timestamp_utc": "2026-09-13T19:45:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 900
          },
          "candles": [
            {
              "close": 77420.56,
              "high": 77460.0,
              "low": 77240.05,
              "open": 77250.02,
              "timestamp": 1789156800000,
              "volume": 4470.0
            },
            {
              "close": 77354.13,
              "high": 77420.38,
              "low": 77335.14,
              "open": 77420.37,
              "timestamp": 1789157700000,
              "volume": 4479.0
            },
            {
              "close": 77377.46,
              "high": 77429.0,
              "low": 77239.82,
              "open": 77354.13,
              "timestamp": 1789158600000,
              "volume": 4489.0
            },
            {
              "close": 77295.04,
              "high": 77386.16,
              "low": 77161.55,
              "open": 77377.46,
              "timestamp": 1789159500000,
              "volume": 4488.0
            },
            {
              "close": 77335.99,
              "high": 77396.24,
              "low": 77281.1,
              "open": 77295.04,
              "timestamp": 1789160400000,
              "volume": 3321.0
            },
            {
              "close": 77330.81,
              "high": 77396.4,
              "low": 77315.25,
              "open": 77335.72,
              "timestamp": 1789161300000,
              "volume": 4476.0
            },
            {
              "close": 77309.21,
              "high": 77365.83,
              "low": 77293.21,
              "open": 77330.81,
              "timestamp": 1789162200000,
              "volume": 4489.0
            },
            {
              "close": 77079.7,
              "high": 77321.13,
              "low": 77037.93,
              "open": 77309.21,
              "timestamp": 1789163100000,
              "volume": 4488.0
            },
            {
              "close": 77148.4,
              "high": 77148.4,
              "low": 76941.98,
              "open": 77079.7,
              "timestamp": 1789164000000,
              "volume": 3877.0
            },
            {
              "close": 77094.41,
              "high": 77203.1,
              "low": 77069.01,
              "open": 77148.4,
              "timestamp": 1789164900000,
              "volume": 4475.0
            },
            {
              "close": 77087.7,
              "high": 77174.8,
              "low": 76959.5,
              "open": 77087.52,
              "timestamp": 1789165800000,
              "volume": 4479.0
            },
            {
              "close": 77108.47,
              "high": 77129.9,
              "low": 76960.1,
              "open": 77087.7,
              "timestamp": 1789166700000,
              "volume": 4480.0
            },
            {
              "close": 77096.9,
              "high": 77189.1,
              "low": 77084.65,
              "open": 77108.47,
              "timestamp": 1789167600000,
              "volume": 4477.0
            },
            {
              "close": 77159.39,
              "high": 77162.6,
              "low": 77096.9,
              "open": 77096.9,
              "timestamp": 1789168500000,
              "volume": 4480.0
            },
            {
              "close": 77143.59,
              "high": 77189.6,
              "low": 77110.93,
              "open": 77159.39,
              "timestamp": 1789169400000,
              "volume": 4476.0
            },
            {
              "close": 77190.5,
              "high": 77190.64,
              "low": 77130.93,
              "open": 77143.59,
              "timestamp": 1789170300000,
              "volume": 4477.0
            },
            {
              "close": 77257.6,
              "high": 77271.4,
              "low": 77169.8,
              "open": 77190.5,
              "timestamp": 1789171200000,
              "volume": 4471.0
            },
            {
              "close": 77239.8,
              "high": 77274.2,
              "low": 77239.52,
              "open": 77257.6,
              "timestamp": 1789172100000,
              "volume": 4473.0
            },
            {
              "close": 77248.1,
              "high": 77258.5,
              "low": 77204.81,
              "open": 77239.8,
              "timestamp": 1789173000000,
              "volume": 4476.0
            },
            {
              "close": 77250.38,
              "high": 77286.9,
              "low": 77235.87,
              "open": 77248.1,
              "timestamp": 1789173900000,
              "volume": 4478.0
            },
            {
              "close": 77336.04,
              "high": 77336.1,
              "low": 77218.7,
              "open": 77250.4,
              "timestamp": 1789174800000,
              "volume": 4479.0
            },
            {
              "close": 77286.8,
              "high": 77346.2,
              "low": 77257.66,
              "open": 77336.04,
              "timestamp": 1789175700000,
              "volume": 4486.0
            },
            {
              "close": 77241.4,
              "high": 77287.5,
              "low": 77221.8,
              "open": 77286.8,
              "timestamp": 1789176600000,
              "volume": 4481.0
            },
            {
              "close": 77235.42,
              "high": 77299.4,
              "low": 77225.12,
              "open": 77241.4,
              "timestamp": 1789177500000,
              "volume": 4478.0
            },
            {
              "close": 77265.01,
              "high": 77290.2,
              "low": 77229.91,
              "open": 77235.42,
              "timestamp": 1789178400000,
              "volume": 4479.0
            },
            {
              "close": 77249.9,
              "high": 77292.53,
              "low": 77239.4,
              "open": 77265.01,
              "timestamp": 1789179300000,
              "volume": 4484.0
            },
            {
              "close": 77193.63,
              "high": 77257.1,
              "low": 77176.08,
              "open": 77249.9,
              "timestamp": 1789180200000,
              "volume": 4486.0
            },
            {
              "close": 77253.22,
              "high": 77284.2,
              "low": 77178.86,
              "open": 77193.81,
              "timestamp": 1789181100000,
              "volume": 4486.0
            },
            {
              "close": 77243.45,
              "high": 77313.97,
              "low": 77212.89,
              "open": 77248.37,
              "timestamp": 1789182000000,
              "volume": 4485.0
            },
            {
              "close": 77248.84,
              "high": 77279.4,
              "low": 77194.0,
              "open": 77243.45,
              "timestamp": 1789182900000,
              "volume": 4480.0
            },
            {
              "close": 77214.03,
              "high": 77248.84,
              "low": 77200.1,
              "open": 77247.91,
              "timestamp": 1789183800000,
              "volume": 4479.0
            },
            {
              "close": 77236.3,
              "high": 77241.73,
              "low": 77201.29,
              "open": 77214.03,
              "timestamp": 1789184700000,
              "volume": 4476.0
            },
            {
              "close": 77256.79,
              "high": 77288.2,
              "low": 77236.24,
              "open": 77236.3,
              "timestamp": 1789185600000,
              "volume": 4478.0
            },
            {
              "close": 77220.4,
              "high": 77260.5,
              "low": 77183.96,
              "open": 77256.79,
              "timestamp": 1789186500000,
              "volume": 4477.0
            },
            {
              "close": 77212.6,
              "high": 77261.1,
              "low": 77206.02,
              "open": 77220.4,
              "timestamp": 1789187400000,
              "volume": 4476.0
            },
            {
              "close": 77185.73,
              "high": 77232.5,
              "low": 77185.53,
              "open": 77212.6,
              "timestamp": 1789188300000,
              "volume": 4486.0
            },
            {
              "close": 77186.73,
              "high": 77206.3,
              "low": 77128.18,
              "open": 77185.73,
              "timestamp": 1789189200000,
              "volume": 4479.0
            },
            {
              "close": 77155.57,
              "high": 77205.9,
              "low": 77152.53,
              "open": 77186.73,
              "timestamp": 1789190100000,
              "volume": 4477.0
            },
            {
              "close": 77199.4,
              "high": 77225.6,
              "low": 77151.6,
              "open": 77155.57,
              "timestamp": 1789191000000,
              "volume": 4479.0
            },
            {
              "close": 77177.11,
              "high": 77222.1,
              "low": 77175.96,
              "open": 77199.4,
              "timestamp": 1789191900000,
              "volume": 4475.0
            },
            {
              "close": 77177.6,
              "high": 77198.9,
              "low": 77172.64,
              "open": 77177.11,
              "timestamp": 1789192800000,
              "volume": 4477.0
            },
            {
              "close": 77205.16,
              "high": 77205.3,
              "low": 77177.56,
              "open": 77177.6,
              "timestamp": 1789193700000,
              "volume": 4475.0
            },
            {
              "close": 77285.5,
              "high": 77289.76,
              "low": 77205.16,
              "open": 77205.16,
              "timestamp": 1789194600000,
              "volume": 4475.0
            },
            {
              "close": 77259.48,
              "high": 77326.5,
              "low": 77256.2,
              "open": 77285.5,
              "timestamp": 1789195500000,
              "volume": 4483.0
            },
            {
              "close": 77303.8,
              "high": 77309.4,
              "low": 77259.0,
              "open": 77259.48,
              "timestamp": 1789196400000,
              "volume": 4478.0
            },
            {
              "close": 77270.82,
              "high": 77303.8,
              "low": 77267.95,
              "open": 77303.8,
              "timestamp": 1789197300000,
              "volume": 4471.0
            },
            {
              "close": 77243.4,
              "high": 77270.96,
              "low": 77240.86,
              "open": 77270.82,
              "timestamp": 1789198200000,
              "volume": 4478.0
            },
            {
              "close": 77236.3,
              "high": 77272.3,
              "low": 77221.74,
              "open": 77243.4,
              "timestamp": 1789199100000,
              "volume": 4471.0
            },
            {
              "close": 77263.6,
              "high": 77310.4,
              "low": 77220.24,
              "open": 77236.3,
              "timestamp": 1789200000000,
              "volume": 4474.0
            },
            {
              "close": 77266.8,
              "high": 77307.63,
              "low": 77254.7,
              "open": 77263.6,
              "timestamp": 1789200900000,
              "volume": 4474.0
            },
            {
              "close": 77310.0,
              "high": 77310.65,
              "low": 77266.8,
              "open": 77266.8,
              "timestamp": 1789201800000,
              "volume": 4475.0
            },
            {
              "close": 77324.45,
              "high": 77339.3,
              "low": 77290.0,
              "open": 77310.0,
              "timestamp": 1789202700000,
              "volume": 4481.0
            },
            {
              "close": 77336.21,
              "high": 77349.4,
              "low": 77301.77,
              "open": 77324.45,
              "timestamp": 1789203600000,
              "volume": 4475.0
            },
            {
              "close": 77336.5,
              "high": 77349.4,
              "low": 77309.71,
              "open": 77336.21,
              "timestamp": 1789204500000,
              "volume": 4475.0
            },
            {
              "close": 77305.7,
              "high": 77347.3,
              "low": 77290.57,
              "open": 77336.5,
              "timestamp": 1789205400000,
              "volume": 4478.0
            },
            {
              "close": 77319.4,
              "high": 77330.83,
              "low": 77295.08,
              "open": 77305.7,
              "timestamp": 1789206300000,
              "volume": 4474.0
            },
            {
              "close": 77364.97,
              "high": 77366.1,
              "low": 77319.4,
              "open": 77319.4,
              "timestamp": 1789207200000,
              "volume": 4474.0
            },
            {
              "close": 77341.41,
              "high": 77364.97,
              "low": 77337.8,
              "open": 77364.97,
              "timestamp": 1789208100000,
              "volume": 4476.0
            },
            {
              "close": 77331.4,
              "high": 77341.5,
              "low": 77313.4,
              "open": 77341.41,
              "timestamp": 1789209000000,
              "volume": 4480.0
            },
            {
              "close": 77298.03,
              "high": 77349.2,
              "low": 77274.18,
              "open": 77331.4,
              "timestamp": 1789209900000,
              "volume": 4481.0
            },
            {
              "close": 77296.23,
              "high": 77316.4,
              "low": 77276.21,
              "open": 77298.03,
              "timestamp": 1789210800000,
              "volume": 4474.0
            },
            {
              "close": 77263.9,
              "high": 77296.69,
              "low": 77259.17,
              "open": 77296.23,
              "timestamp": 1789211700000,
              "volume": 4475.0
            },
            {
              "close": 77312.9,
              "high": 77318.6,
              "low": 77259.64,
              "open": 77263.9,
              "timestamp": 1789212600000,
              "volume": 4476.0
            },
            {
              "close": 77325.2,
              "high": 77331.2,
              "low": 77312.9,
              "open": 77312.9,
              "timestamp": 1789213500000,
              "volume": 4475.0
            },
            {
              "close": 77292.81,
              "high": 77332.87,
              "low": 77279.03,
              "open": 77325.2,
              "timestamp": 1789214400000,
              "volume": 4478.0
            },
            {
              "close": 77293.8,
              "high": 77314.7,
              "low": 77272.42,
              "open": 77292.81,
              "timestamp": 1789215300000,
              "volume": 4473.0
            },
            {
              "close": 77291.15,
              "high": 77313.0,
              "low": 77290.5,
              "open": 77293.8,
              "timestamp": 1789216200000,
              "volume": 4472.0
            },
            {
              "close": 77294.3,
              "high": 77307.92,
              "low": 77249.61,
              "open": 77291.07,
              "timestamp": 1789217100000,
              "volume": 4478.0
            },
            {
              "close": 77282.79,
              "high": 77363.9,
              "low": 77265.97,
              "open": 77294.3,
              "timestamp": 1789218000000,
              "volume": 4480.0
            },
            {
              "close": 77268.22,
              "high": 77285.8,
              "low": 77214.7,
              "open": 77282.8,
              "timestamp": 1789218900000,
              "volume": 4480.0
            },
            {
              "close": 77264.92,
              "high": 77295.5,
              "low": 77227.35,
              "open": 77268.22,
              "timestamp": 1789219800000,
              "volume": 4473.0
            },
            {
              "close": 77328.6,
              "high": 77328.8,
              "low": 77234.4,
              "open": 77264.92,
              "timestamp": 1789220700000,
              "volume": 4474.0
            },
            {
              "close": 77333.31,
              "high": 77349.4,
              "low": 77328.6,
              "open": 77328.6,
              "timestamp": 1789221600000,
              "volume": 4476.0
            },
            {
              "close": 77393.5,
              "high": 77394.9,
              "low": 77333.31,
              "open": 77333.31,
              "timestamp": 1789222500000,
              "volume": 4477.0
            },
            {
              "close": 77412.47,
              "high": 77449.2,
              "low": 77392.7,
              "open": 77393.5,
              "timestamp": 1789223400000,
              "volume": 4487.0
            },
            {
              "close": 77425.8,
              "high": 77476.8,
              "low": 77412.38,
              "open": 77412.47,
              "timestamp": 1789224300000,
              "volume": 4496.0
            },
            {
              "close": 77395.52,
              "high": 77433.2,
              "low": 77376.52,
              "open": 77429.9,
              "timestamp": 1789225200000,
              "volume": 4477.0
            },
            {
              "close": 77418.45,
              "high": 77448.6,
              "low": 77390.66,
              "open": 77395.52,
              "timestamp": 1789226100000,
              "volume": 4475.0
            },
            {
              "close": 77365.96,
              "high": 77419.6,
              "low": 77335.39,
              "open": 77418.45,
              "timestamp": 1789227000000,
              "volume": 4479.0
            },
            {
              "close": 77343.2,
              "high": 77408.5,
              "low": 77338.8,
              "open": 77365.96,
              "timestamp": 1789227900000,
              "volume": 4475.0
            },
            {
              "close": 77333.24,
              "high": 77384.3,
              "low": 77301.6,
              "open": 77343.2,
              "timestamp": 1789228800000,
              "volume": 4478.0
            },
            {
              "close": 77349.0,
              "high": 77349.0,
              "low": 77333.24,
              "open": 77333.24,
              "timestamp": 1789229700000,
              "volume": 4475.0
            },
            {
              "close": 77326.66,
              "high": 77353.2,
              "low": 77320.52,
              "open": 77349.0,
              "timestamp": 1789230600000,
              "volume": 4476.0
            },
            {
              "close": 77325.26,
              "high": 77349.0,
              "low": 77299.93,
              "open": 77326.66,
              "timestamp": 1789231500000,
              "volume": 4484.0
            },
            {
              "close": 77323.7,
              "high": 77365.0,
              "low": 77308.64,
              "open": 77325.26,
              "timestamp": 1789232400000,
              "volume": 4478.0
            },
            {
              "close": 77262.3,
              "high": 77329.3,
              "low": 77235.5,
              "open": 77323.7,
              "timestamp": 1789233300000,
              "volume": 4479.0
            },
            {
              "close": 77201.5,
              "high": 77262.3,
              "low": 77173.3,
              "open": 77262.3,
              "timestamp": 1789234200000,
              "volume": 4490.0
            },
            {
              "close": 77173.0,
              "high": 77201.5,
              "low": 77139.81,
              "open": 77201.5,
              "timestamp": 1789235100000,
              "volume": 4479.0
            },
            {
              "close": 77132.35,
              "high": 77189.5,
              "low": 77132.25,
              "open": 77173.0,
              "timestamp": 1789236000000,
              "volume": 4475.0
            },
            {
              "close": 77167.8,
              "high": 77173.9,
              "low": 77088.2,
              "open": 77132.35,
              "timestamp": 1789236900000,
              "volume": 4492.0
            },
            {
              "close": 77152.38,
              "high": 77167.83,
              "low": 77084.68,
              "open": 77167.8,
              "timestamp": 1789237800000,
              "volume": 4481.0
            },
            {
              "close": 77105.1,
              "high": 77152.49,
              "low": 77095.3,
              "open": 77152.38,
              "timestamp": 1789238700000,
              "volume": 4477.0
            },
            {
              "close": 77141.01,
              "high": 77152.22,
              "low": 77091.0,
              "open": 77105.1,
              "timestamp": 1789239600000,
              "volume": 4475.0
            },
            {
              "close": 77092.65,
              "high": 77156.43,
              "low": 77088.67,
              "open": 77141.01,
              "timestamp": 1789240500000,
              "volume": 4476.0
            },
            {
              "close": 77040.1,
              "high": 77114.1,
              "low": 77024.51,
              "open": 77092.65,
              "timestamp": 1789241400000,
              "volume": 4486.0
            },
            {
              "close": 77083.5,
              "high": 77127.0,
              "low": 77040.01,
              "open": 77040.1,
              "timestamp": 1789242300000,
              "volume": 4479.0
            },
            {
              "close": 77143.21,
              "high": 77145.7,
              "low": 77083.5,
              "open": 77083.5,
              "timestamp": 1789243200000,
              "volume": 4485.0
            },
            {
              "close": 77157.31,
              "high": 77168.6,
              "low": 77124.69,
              "open": 77143.21,
              "timestamp": 1789244100000,
              "volume": 4472.0
            },
            {
              "close": 77141.6,
              "high": 77178.42,
              "low": 77118.44,
              "open": 77157.31,
              "timestamp": 1789245000000,
              "volume": 4484.0
            },
            {
              "close": 77128.63,
              "high": 77187.3,
              "low": 77118.45,
              "open": 77141.6,
              "timestamp": 1789245900000,
              "volume": 4487.0
            },
            {
              "close": 77127.8,
              "high": 77203.2,
              "low": 77104.6,
              "open": 77128.63,
              "timestamp": 1789246800000,
              "volume": 3479.0
            },
            {
              "close": 77172.1,
              "high": 77172.11,
              "low": 77127.7,
              "open": 77127.8,
              "timestamp": 1789247700000,
              "volume": 4473.0
            },
            {
              "close": 77198.39,
              "high": 77228.4,
              "low": 77172.1,
              "open": 77172.1,
              "timestamp": 1789248600000,
              "volume": 4475.0
            },
            {
              "close": 77217.8,
              "high": 77237.8,
              "low": 77166.03,
              "open": 77198.38,
              "timestamp": 1789249500000,
              "volume": 4485.0
            },
            {
              "close": 77224.9,
              "high": 77255.32,
              "low": 77168.94,
              "open": 77217.8,
              "timestamp": 1789250400000,
              "volume": 4488.0
            },
            {
              "close": 77164.53,
              "high": 77265.95,
              "low": 77143.91,
              "open": 77224.94,
              "timestamp": 1789251300000,
              "volume": 4482.0
            },
            {
              "close": 77156.2,
              "high": 77201.6,
              "low": 77146.24,
              "open": 77164.54,
              "timestamp": 1789252200000,
              "volume": 4476.0
            },
            {
              "close": 77194.7,
              "high": 77208.1,
              "low": 77156.2,
              "open": 77156.2,
              "timestamp": 1789253100000,
              "volume": 4477.0
            },
            {
              "close": 77241.09,
              "high": 77243.52,
              "low": 77194.62,
              "open": 77194.7,
              "timestamp": 1789254000000,
              "volume": 4473.0
            },
            {
              "close": 77219.57,
              "high": 77251.4,
              "low": 77201.83,
              "open": 77241.09,
              "timestamp": 1789254900000,
              "volume": 4475.0
            },
            {
              "close": 77218.17,
              "high": 77229.9,
              "low": 77190.98,
              "open": 77219.57,
              "timestamp": 1789255800000,
              "volume": 4478.0
            },
            {
              "close": 77242.21,
              "high": 77258.5,
              "low": 77218.14,
              "open": 77218.22,
              "timestamp": 1789256700000,
              "volume": 4477.0
            },
            {
              "close": 77238.09,
              "high": 77274.8,
              "low": 77223.5,
              "open": 77234.52,
              "timestamp": 1789257600000,
              "volume": 4174.0
            },
            {
              "close": 77231.51,
              "high": 77251.3,
              "low": 77227.05,
              "open": 77238.09,
              "timestamp": 1789258500000,
              "volume": 4476.0
            },
            {
              "close": 77181.61,
              "high": 77231.6,
              "low": 77117.01,
              "open": 77231.51,
              "timestamp": 1789259400000,
              "volume": 4479.0
            },
            {
              "close": 77238.94,
              "high": 77254.6,
              "low": 77181.61,
              "open": 77181.61,
              "timestamp": 1789260300000,
              "volume": 4479.0
            },
            {
              "close": 77248.23,
              "high": 77269.3,
              "low": 77216.27,
              "open": 77238.94,
              "timestamp": 1789261200000,
              "volume": 4477.0
            },
            {
              "close": 77220.7,
              "high": 77308.32,
              "low": 77219.1,
              "open": 77248.23,
              "timestamp": 1789262100000,
              "volume": 4482.0
            },
            {
              "close": 77260.66,
              "high": 77270.59,
              "low": 77206.59,
              "open": 77220.7,
              "timestamp": 1789263000000,
              "volume": 4480.0
            },
            {
              "close": 77285.0,
              "high": 77289.4,
              "low": 77244.17,
              "open": 77260.66,
              "timestamp": 1789263900000,
              "volume": 4477.0
            },
            {
              "close": 77255.3,
              "high": 77285.0,
              "low": 77234.48,
              "open": 77285.0,
              "timestamp": 1789264800000,
              "volume": 4472.0
            },
            {
              "close": 77232.9,
              "high": 77269.48,
              "low": 77216.3,
              "open": 77255.3,
              "timestamp": 1789265700000,
              "volume": 4475.0
            },
            {
              "close": 77267.75,
              "high": 77273.8,
              "low": 77207.81,
              "open": 77232.9,
              "timestamp": 1789266600000,
              "volume": 4485.0
            },
            {
              "close": 77262.24,
              "high": 77286.4,
              "low": 77250.13,
              "open": 77267.75,
              "timestamp": 1789267500000,
              "volume": 4482.0
            },
            {
              "close": 77251.4,
              "high": 77287.3,
              "low": 77236.5,
              "open": 77262.24,
              "timestamp": 1789268400000,
              "volume": 4475.0
            },
            {
              "close": 77225.63,
              "high": 77252.1,
              "low": 77208.54,
              "open": 77251.4,
              "timestamp": 1789269300000,
              "volume": 4471.0
            },
            {
              "close": 77187.7,
              "high": 77225.63,
              "low": 77165.28,
              "open": 77225.63,
              "timestamp": 1789270200000,
              "volume": 4477.0
            },
            {
              "close": 77161.67,
              "high": 77193.3,
              "low": 77149.65,
              "open": 77187.7,
              "timestamp": 1789271100000,
              "volume": 4474.0
            },
            {
              "close": 77175.7,
              "high": 77227.1,
              "low": 77154.76,
              "open": 77161.67,
              "timestamp": 1789272000000,
              "volume": 4480.0
            },
            {
              "close": 77191.86,
              "high": 77225.5,
              "low": 77175.65,
              "open": 77175.7,
              "timestamp": 1789272900000,
              "volume": 4475.0
            },
            {
              "close": 77181.85,
              "high": 77202.97,
              "low": 77175.94,
              "open": 77191.24,
              "timestamp": 1789273800000,
              "volume": 4478.0
            },
            {
              "close": 77177.62,
              "high": 77193.7,
              "low": 77164.77,
              "open": 77181.85,
              "timestamp": 1789274700000,
              "volume": 4476.0
            },
            {
              "close": 77209.74,
              "high": 77210.5,
              "low": 77177.6,
              "open": 77177.66,
              "timestamp": 1789275600000,
              "volume": 4475.0
            },
            {
              "close": 77249.4,
              "high": 77249.4,
              "low": 77207.66,
              "open": 77209.74,
              "timestamp": 1789276500000,
              "volume": 4476.0
            },
            {
              "close": 77271.7,
              "high": 77271.7,
              "low": 77249.36,
              "open": 77249.4,
              "timestamp": 1789277400000,
              "volume": 4478.0
            },
            {
              "close": 77280.03,
              "high": 77289.4,
              "low": 77271.7,
              "open": 77271.7,
              "timestamp": 1789278300000,
              "volume": 4479.0
            },
            {
              "close": 77264.8,
              "high": 77290.5,
              "low": 77263.72,
              "open": 77280.03,
              "timestamp": 1789279200000,
              "volume": 4474.0
            },
            {
              "close": 77261.7,
              "high": 77273.1,
              "low": 77249.35,
              "open": 77264.8,
              "timestamp": 1789280100000,
              "volume": 4472.0
            },
            {
              "close": 77258.9,
              "high": 77267.6,
              "low": 77229.1,
              "open": 77261.7,
              "timestamp": 1789281000000,
              "volume": 4478.0
            },
            {
              "close": 77081.5,
              "high": 77258.9,
              "low": 77011.88,
              "open": 77258.9,
              "timestamp": 1789281900000,
              "volume": 4489.0
            },
            {
              "close": 77129.04,
              "high": 77130.2,
              "low": 77055.36,
              "open": 77081.5,
              "timestamp": 1789282800000,
              "volume": 4479.0
            },
            {
              "close": 77105.0,
              "high": 77135.8,
              "low": 77082.64,
              "open": 77129.25,
              "timestamp": 1789283700000,
              "volume": 4477.0
            },
            {
              "close": 77124.25,
              "high": 77133.1,
              "low": 77049.8,
              "open": 77105.01,
              "timestamp": 1789284600000,
              "volume": 4477.0
            },
            {
              "close": 77086.33,
              "high": 77132.0,
              "low": 77053.6,
              "open": 77124.23,
              "timestamp": 1789285500000,
              "volume": 4472.0
            },
            {
              "close": 77028.91,
              "high": 77144.87,
              "low": 76999.3,
              "open": 77086.24,
              "timestamp": 1789286400000,
              "volume": 4477.0
            },
            {
              "close": 76987.46,
              "high": 77028.91,
              "low": 76965.5,
              "open": 77028.91,
              "timestamp": 1789287300000,
              "volume": 4490.0
            },
            {
              "close": 76792.32,
              "high": 76987.46,
              "low": 76711.55,
              "open": 76987.46,
              "timestamp": 1789288200000,
              "volume": 4492.0
            },
            {
              "close": 76767.07,
              "high": 76840.4,
              "low": 76720.12,
              "open": 76792.32,
              "timestamp": 1789289100000,
              "volume": 4477.0
            },
            {
              "close": 76779.5,
              "high": 76868.7,
              "low": 76747.22,
              "open": 76766.74,
              "timestamp": 1789290000000,
              "volume": 4479.0
            },
            {
              "close": 76603.88,
              "high": 76790.88,
              "low": 76558.91,
              "open": 76779.5,
              "timestamp": 1789290900000,
              "volume": 4489.0
            },
            {
              "close": 76685.12,
              "high": 76742.4,
              "low": 76531.65,
              "open": 76603.86,
              "timestamp": 1789291800000,
              "volume": 4478.0
            },
            {
              "close": 76765.29,
              "high": 76791.23,
              "low": 76682.81,
              "open": 76685.12,
              "timestamp": 1789292700000,
              "volume": 4479.0
            },
            {
              "close": 76764.61,
              "high": 76781.4,
              "low": 76719.2,
              "open": 76765.29,
              "timestamp": 1789293600000,
              "volume": 4472.0
            },
            {
              "close": 76729.39,
              "high": 76777.6,
              "low": 76711.07,
              "open": 76764.61,
              "timestamp": 1789294500000,
              "volume": 4479.0
            },
            {
              "close": 76664.24,
              "high": 76784.8,
              "low": 76662.89,
              "open": 76729.39,
              "timestamp": 1789295400000,
              "volume": 4478.0
            },
            {
              "close": 76643.0,
              "high": 76720.1,
              "low": 76594.02,
              "open": 76664.24,
              "timestamp": 1789296300000,
              "volume": 4500.0
            },
            {
              "close": 76492.01,
              "high": 76681.5,
              "low": 76464.5,
              "open": 76643.0,
              "timestamp": 1789297200000,
              "volume": 4546.0
            },
            {
              "close": 76633.1,
              "high": 76637.73,
              "low": 76492.0,
              "open": 76492.01,
              "timestamp": 1789298100000,
              "volume": 4509.0
            },
            {
              "close": 76745.13,
              "high": 76765.75,
              "low": 76615.86,
              "open": 76633.07,
              "timestamp": 1789299000000,
              "volume": 4555.0
            },
            {
              "close": 76752.3,
              "high": 76769.4,
              "low": 76713.17,
              "open": 76745.12,
              "timestamp": 1789299900000,
              "volume": 4489.0
            },
            {
              "close": 76765.82,
              "high": 76773.4,
              "low": 76720.8,
              "open": 76752.3,
              "timestamp": 1789300800000,
              "volume": 4474.0
            },
            {
              "close": 76799.51,
              "high": 76826.62,
              "low": 76763.22,
              "open": 76765.82,
              "timestamp": 1789301700000,
              "volume": 4486.0
            },
            {
              "close": 76695.06,
              "high": 76830.4,
              "low": 76671.71,
              "open": 76799.51,
              "timestamp": 1789302600000,
              "volume": 4484.0
            },
            {
              "close": 76724.97,
              "high": 76755.5,
              "low": 76653.87,
              "open": 76695.05,
              "timestamp": 1789303500000,
              "volume": 4480.0
            },
            {
              "close": 76729.4,
              "high": 76736.1,
              "low": 76641.02,
              "open": 76724.83,
              "timestamp": 1789304400000,
              "volume": 4481.0
            },
            {
              "close": 76545.1,
              "high": 76743.61,
              "low": 76513.77,
              "open": 76729.4,
              "timestamp": 1789305300000,
              "volume": 4488.0
            },
            {
              "close": 76734.84,
              "high": 76739.3,
              "low": 76544.42,
              "open": 76545.02,
              "timestamp": 1789306200000,
              "volume": 4485.0
            },
            {
              "close": 76813.11,
              "high": 76891.5,
              "low": 76734.84,
              "open": 76735.26,
              "timestamp": 1789307100000,
              "volume": 4483.0
            },
            {
              "close": 76973.4,
              "high": 76979.4,
              "low": 76810.01,
              "open": 76813.11,
              "timestamp": 1789308000000,
              "volume": 4482.0
            },
            {
              "close": 77067.05,
              "high": 77090.8,
              "low": 76973.4,
              "open": 76973.4,
              "timestamp": 1789308900000,
              "volume": 4486.0
            },
            {
              "close": 77150.3,
              "high": 77231.1,
              "low": 77047.42,
              "open": 77067.05,
              "timestamp": 1789309800000,
              "volume": 4486.0
            },
            {
              "close": 77174.6,
              "high": 77221.36,
              "low": 77123.94,
              "open": 77150.3,
              "timestamp": 1789310700000,
              "volume": 4484.0
            },
            {
              "close": 77087.33,
              "high": 77178.2,
              "low": 77071.61,
              "open": 77174.6,
              "timestamp": 1789311600000,
              "volume": 4486.0
            },
            {
              "close": 77006.4,
              "high": 77174.4,
              "low": 76980.6,
              "open": 77087.33,
              "timestamp": 1789312500000,
              "volume": 4484.0
            },
            {
              "close": 77129.54,
              "high": 77148.01,
              "low": 77006.4,
              "open": 77006.4,
              "timestamp": 1789313400000,
              "volume": 4474.0
            },
            {
              "close": 77097.34,
              "high": 77130.18,
              "low": 77080.68,
              "open": 77129.54,
              "timestamp": 1789314300000,
              "volume": 4474.0
            },
            {
              "close": 77165.03,
              "high": 77226.13,
              "low": 77086.8,
              "open": 77097.34,
              "timestamp": 1789315200000,
              "volume": 4487.0
            },
            {
              "close": 77208.71,
              "high": 77266.42,
              "low": 77150.16,
              "open": 77165.03,
              "timestamp": 1789316100000,
              "volume": 4483.0
            },
            {
              "close": 77281.78,
              "high": 77332.3,
              "low": 77191.3,
              "open": 77208.71,
              "timestamp": 1789317000000,
              "volume": 4483.0
            },
            {
              "close": 77252.0,
              "high": 77297.65,
              "low": 77200.47,
              "open": 77281.68,
              "timestamp": 1789317900000,
              "volume": 4483.0
            },
            {
              "close": 77340.71,
              "high": 77386.4,
              "low": 77252.0,
              "open": 77252.0,
              "timestamp": 1789318800000,
              "volume": 4485.0
            },
            {
              "close": 77264.15,
              "high": 77369.04,
              "low": 77263.93,
              "open": 77340.71,
              "timestamp": 1789319700000,
              "volume": 4488.0
            },
            {
              "close": 77238.61,
              "high": 77264.5,
              "low": 77212.11,
              "open": 77264.15,
              "timestamp": 1789320600000,
              "volume": 4488.0
            },
            {
              "close": 77295.02,
              "high": 77333.7,
              "low": 77238.61,
              "open": 77238.61,
              "timestamp": 1789321500000,
              "volume": 4483.0
            },
            {
              "close": 77333.12,
              "high": 77334.4,
              "low": 77272.54,
              "open": 77295.02,
              "timestamp": 1789322400000,
              "volume": 4480.0
            },
            {
              "close": 77294.84,
              "high": 77354.4,
              "low": 77293.32,
              "open": 77333.05,
              "timestamp": 1789323300000,
              "volume": 4482.0
            },
            {
              "close": 77338.6,
              "high": 77344.8,
              "low": 77278.7,
              "open": 77294.81,
              "timestamp": 1789324200000,
              "volume": 4478.0
            },
            {
              "close": 77313.2,
              "high": 77349.4,
              "low": 77301.41,
              "open": 77338.6,
              "timestamp": 1789325100000,
              "volume": 4483.0
            },
            {
              "close": 77244.11,
              "high": 77380.9,
              "low": 77244.0,
              "open": 77313.22,
              "timestamp": 1789326000000,
              "volume": 4481.0
            },
            {
              "close": 77242.3,
              "high": 77250.6,
              "low": 77190.33,
              "open": 77244.11,
              "timestamp": 1789326900000,
              "volume": 4480.0
            },
            {
              "close": 77213.9,
              "high": 77246.4,
              "low": 77188.38,
              "open": 77242.3,
              "timestamp": 1789327800000,
              "volume": 4481.0
            },
            {
              "close": 77253.6,
              "high": 77253.6,
              "low": 77203.16,
              "open": 77213.9,
              "timestamp": 1789328700000,
              "volume": 4480.0
            }
          ],
          "last_price": 77253.6,
          "momentum": "neutral",
          "rsi_14": 56.39,
          "structure": "bullish"
        },
        "1H": {
          "candle_count": 168,
          "candle_status": {
            "data_age_seconds": 3690,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789326000000,
            "latest_timestamp_utc": "2026-09-13T19:00:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 3600
          },
          "candles": [
            {
              "close": 79872.6,
              "high": 79935.5,
              "low": 79740.14,
              "open": 79804.2,
              "timestamp": 1788724800000,
              "volume": 17058.0
            },
            {
              "close": 79902.02,
              "high": 79996.4,
              "low": 79830.23,
              "open": 79872.6,
              "timestamp": 1788728400000,
              "volume": 17942.0
            },
            {
              "close": 80004.8,
              "high": 80057.4,
              "low": 79599.14,
              "open": 79902.02,
              "timestamp": 1788732000000,
              "volume": 17941.0
            },
            {
              "close": 80299.55,
              "high": 80521.62,
              "low": 79963.61,
              "open": 80004.8,
              "timestamp": 1788735600000,
              "volume": 17952.0
            },
            {
              "close": 80121.34,
              "high": 80404.4,
              "low": 80019.87,
              "open": 80300.11,
              "timestamp": 1788739200000,
              "volume": 17943.0
            },
            {
              "close": 79885.7,
              "high": 80205.2,
              "low": 79787.27,
              "open": 80121.34,
              "timestamp": 1788742800000,
              "volume": 17936.0
            },
            {
              "close": 79842.24,
              "high": 80407.72,
              "low": 79754.51,
              "open": 79885.73,
              "timestamp": 1788746400000,
              "volume": 17942.0
            },
            {
              "close": 79558.76,
              "high": 79952.8,
              "low": 79534.6,
              "open": 79842.24,
              "timestamp": 1788750000000,
              "volume": 17937.0
            },
            {
              "close": 79685.11,
              "high": 79694.3,
              "low": 79500.1,
              "open": 79558.76,
              "timestamp": 1788753600000,
              "volume": 17924.0
            },
            {
              "close": 79717.69,
              "high": 79892.24,
              "low": 79620.12,
              "open": 79685.11,
              "timestamp": 1788757200000,
              "volume": 17927.0
            },
            {
              "close": 79615.81,
              "high": 79786.2,
              "low": 79608.52,
              "open": 79715.78,
              "timestamp": 1788760800000,
              "volume": 17948.0
            },
            {
              "close": 79354.7,
              "high": 79654.5,
              "low": 78956.37,
              "open": 79616.24,
              "timestamp": 1788764400000,
              "volume": 17963.0
            },
            {
              "close": 79394.24,
              "high": 79493.9,
              "low": 79354.8,
              "open": 79357.2,
              "timestamp": 1788768000000,
              "volume": 17946.0
            },
            {
              "close": 79278.0,
              "high": 79516.8,
              "low": 79257.75,
              "open": 79394.24,
              "timestamp": 1788771600000,
              "volume": 17945.0
            },
            {
              "close": 79325.02,
              "high": 79418.21,
              "low": 79278.0,
              "open": 79278.0,
              "timestamp": 1788775200000,
              "volume": 17932.0
            },
            {
              "close": 79376.18,
              "high": 79449.4,
              "low": 79237.81,
              "open": 79325.02,
              "timestamp": 1788778800000,
              "volume": 17954.0
            },
            {
              "close": 79566.88,
              "high": 79599.36,
              "low": 79364.06,
              "open": 79376.18,
              "timestamp": 1788782400000,
              "volume": 17968.0
            },
            {
              "close": 79313.87,
              "high": 79612.97,
              "low": 79267.41,
              "open": 79566.88,
              "timestamp": 1788786000000,
              "volume": 17970.0
            },
            {
              "close": 79151.39,
              "high": 79358.9,
              "low": 78912.51,
              "open": 79313.87,
              "timestamp": 1788789600000,
              "volume": 17994.0
            },
            {
              "close": 78781.6,
              "high": 79151.41,
              "low": 78644.74,
              "open": 79151.39,
              "timestamp": 1788793200000,
              "volume": 17951.0
            },
            {
              "close": 78988.75,
              "high": 78996.2,
              "low": 78765.5,
              "open": 78785.6,
              "timestamp": 1788796800000,
              "volume": 17948.0
            },
            {
              "close": 79152.9,
              "high": 79184.4,
              "low": 78971.73,
              "open": 78988.75,
              "timestamp": 1788800400000,
              "volume": 17956.0
            },
            {
              "close": 79157.87,
              "high": 79209.1,
              "low": 79053.71,
              "open": 79152.9,
              "timestamp": 1788804000000,
              "volume": 17955.0
            },
            {
              "close": 79324.8,
              "high": 79375.18,
              "low": 79108.77,
              "open": 79157.87,
              "timestamp": 1788807600000,
              "volume": 17952.0
            },
            {
              "close": 79206.4,
              "high": 79364.4,
              "low": 79130.13,
              "open": 79324.8,
              "timestamp": 1788811200000,
              "volume": 17958.0
            },
            {
              "close": 79128.69,
              "high": 79245.8,
              "low": 79128.69,
              "open": 79206.4,
              "timestamp": 1788814800000,
              "volume": 16711.0
            },
            {
              "close": 78912.44,
              "high": 79181.4,
              "low": 78753.01,
              "open": 79128.69,
              "timestamp": 1788818400000,
              "volume": 17346.0
            },
            {
              "close": 79074.65,
              "high": 79178.8,
              "low": 78894.14,
              "open": 78912.44,
              "timestamp": 1788822000000,
              "volume": 17950.0
            },
            {
              "close": 79286.4,
              "high": 79286.4,
              "low": 78936.64,
              "open": 79074.79,
              "timestamp": 1788825600000,
              "volume": 17949.0
            },
            {
              "close": 79408.5,
              "high": 79435.54,
              "low": 79229.07,
              "open": 79286.4,
              "timestamp": 1788829200000,
              "volume": 17949.0
            },
            {
              "close": 78897.02,
              "high": 79458.1,
              "low": 78897.02,
              "open": 79408.5,
              "timestamp": 1788832800000,
              "volume": 17964.0
            },
            {
              "close": 78879.38,
              "high": 78976.0,
              "low": 78689.54,
              "open": 78897.02,
              "timestamp": 1788836400000,
              "volume": 17957.0
            },
            {
              "close": 78649.5,
              "high": 78904.02,
              "low": 78649.5,
              "open": 78879.38,
              "timestamp": 1788840000000,
              "volume": 17952.0
            },
            {
              "close": 78550.69,
              "high": 78849.4,
              "low": 78510.74,
              "open": 78649.5,
              "timestamp": 1788843600000,
              "volume": 17958.0
            },
            {
              "close": 78288.9,
              "high": 78596.1,
              "low": 78225.16,
              "open": 78550.7,
              "timestamp": 1788847200000,
              "volume": 17902.0
            },
            {
              "close": 78444.5,
              "high": 78564.4,
              "low": 78141.1,
              "open": 78288.9,
              "timestamp": 1788850800000,
              "volume": 17939.0
            },
            {
              "close": 78395.3,
              "high": 78556.8,
              "low": 78252.51,
              "open": 78444.5,
              "timestamp": 1788854400000,
              "volume": 17950.0
            },
            {
              "close": 78727.51,
              "high": 78771.8,
              "low": 78309.69,
              "open": 78395.3,
              "timestamp": 1788858000000,
              "volume": 17948.0
            },
            {
              "close": 78528.81,
              "high": 78967.36,
              "low": 78528.03,
              "open": 78727.49,
              "timestamp": 1788861600000,
              "volume": 17869.0
            },
            {
              "close": 78399.5,
              "high": 78543.9,
              "low": 78254.5,
              "open": 78528.82,
              "timestamp": 1788865200000,
              "volume": 18010.0
            },
            {
              "close": 78416.3,
              "high": 78452.7,
              "low": 78186.7,
              "open": 78399.5,
              "timestamp": 1788868800000,
              "volume": 17980.0
            },
            {
              "close": 77935.86,
              "high": 78511.4,
              "low": 77599.5,
              "open": 78419.4,
              "timestamp": 1788872400000,
              "volume": 17997.0
            },
            {
              "close": 78524.3,
              "high": 78590.8,
              "low": 77828.0,
              "open": 77935.55,
              "timestamp": 1788876000000,
              "volume": 18008.0
            },
            {
              "close": 78868.08,
              "high": 78870.6,
              "low": 78414.41,
              "open": 78524.3,
              "timestamp": 1788879600000,
              "volume": 17976.0
            },
            {
              "close": 78699.11,
              "high": 78935.3,
              "low": 78537.81,
              "open": 78867.51,
              "timestamp": 1788883200000,
              "volume": 17986.0
            },
            {
              "close": 78466.2,
              "high": 78856.4,
              "low": 78458.32,
              "open": 78699.11,
              "timestamp": 1788886800000,
              "volume": 17980.0
            },
            {
              "close": 78398.5,
              "high": 78782.4,
              "low": 78230.01,
              "open": 78466.18,
              "timestamp": 1788890400000,
              "volume": 17849.0
            },
            {
              "close": 78406.34,
              "high": 78495.0,
              "low": 78283.29,
              "open": 78398.5,
              "timestamp": 1788894000000,
              "volume": 17972.0
            },
            {
              "close": 78447.3,
              "high": 78586.69,
              "low": 78366.27,
              "open": 78404.85,
              "timestamp": 1788897600000,
              "volume": 17972.0
            },
            {
              "close": 78457.6,
              "high": 78586.0,
              "low": 78359.41,
              "open": 78447.3,
              "timestamp": 1788901200000,
              "volume": 16735.0
            },
            {
              "close": 78525.58,
              "high": 78618.7,
              "low": 78419.23,
              "open": 78457.6,
              "timestamp": 1788904800000,
              "volume": 17325.0
            },
            {
              "close": 78425.05,
              "high": 78542.9,
              "low": 78374.0,
              "open": 78525.58,
              "timestamp": 1788908400000,
              "volume": 17937.0
            },
            {
              "close": 78745.26,
              "high": 78758.5,
              "low": 78423.44,
              "open": 78425.05,
              "timestamp": 1788912000000,
              "volume": 17966.0
            },
            {
              "close": 78847.68,
              "high": 78859.35,
              "low": 78591.25,
              "open": 78745.26,
              "timestamp": 1788915600000,
              "volume": 17969.0
            },
            {
              "close": 78687.7,
              "high": 78895.57,
              "low": 78644.31,
              "open": 78847.68,
              "timestamp": 1788919200000,
              "volume": 17954.0
            },
            {
              "close": 78593.2,
              "high": 78687.74,
              "low": 78507.01,
              "open": 78687.74,
              "timestamp": 1788922800000,
              "volume": 17939.0
            },
            {
              "close": 79135.34,
              "high": 79185.31,
              "low": 78593.2,
              "open": 78593.2,
              "timestamp": 1788926400000,
              "volume": 17965.0
            },
            {
              "close": 78904.3,
              "high": 79342.01,
              "low": 78800.58,
              "open": 79135.34,
              "timestamp": 1788930000000,
              "volume": 17948.0
            },
            {
              "close": 79124.8,
              "high": 79259.3,
              "low": 78821.29,
              "open": 78905.36,
              "timestamp": 1788933600000,
              "volume": 17933.0
            },
            {
              "close": 79244.87,
              "high": 79375.76,
              "low": 79118.49,
              "open": 79124.8,
              "timestamp": 1788937200000,
              "volume": 17959.0
            },
            {
              "close": 79659.99,
              "high": 79734.3,
              "low": 79230.63,
              "open": 79244.87,
              "timestamp": 1788940800000,
              "volume": 17965.0
            },
            {
              "close": 78912.42,
              "high": 79679.7,
              "low": 78855.71,
              "open": 79659.99,
              "timestamp": 1788944400000,
              "volume": 17948.0
            },
            {
              "close": 78881.57,
              "high": 79147.8,
              "low": 78836.5,
              "open": 78912.42,
              "timestamp": 1788948000000,
              "volume": 17956.0
            },
            {
              "close": 79280.94,
              "high": 79346.2,
              "low": 78697.5,
              "open": 78881.58,
              "timestamp": 1788951600000,
              "volume": 18001.0
            },
            {
              "close": 79565.8,
              "high": 79629.7,
              "low": 79236.6,
              "open": 79280.95,
              "timestamp": 1788955200000,
              "volume": 17976.0
            },
            {
              "close": 79112.06,
              "high": 79647.5,
              "low": 79068.43,
              "open": 79565.8,
              "timestamp": 1788958800000,
              "volume": 17993.0
            },
            {
              "close": 78930.67,
              "high": 79379.4,
              "low": 78843.54,
              "open": 79112.06,
              "timestamp": 1788962400000,
              "volume": 18005.0
            },
            {
              "close": 78566.97,
              "high": 79363.11,
              "low": 78019.5,
              "open": 78930.67,
              "timestamp": 1788966000000,
              "volume": 17357.0
            },
            {
              "close": 78768.75,
              "high": 78921.25,
              "low": 78418.7,
              "open": 78566.99,
              "timestamp": 1788969600000,
              "volume": 17981.0
            },
            {
              "close": 78737.31,
              "high": 78901.7,
              "low": 78624.18,
              "open": 78768.75,
              "timestamp": 1788973200000,
              "volume": 17976.0
            },
            {
              "close": 78383.4,
              "high": 78759.6,
              "low": 78370.1,
              "open": 78737.31,
              "timestamp": 1788976800000,
              "volume": 17962.0
            },
            {
              "close": 78199.37,
              "high": 78548.77,
              "low": 78111.4,
              "open": 78383.4,
              "timestamp": 1788980400000,
              "volume": 17962.0
            },
            {
              "close": 78281.07,
              "high": 78302.2,
              "low": 77886.85,
              "open": 78192.35,
              "timestamp": 1788984000000,
              "volume": 17960.0
            },
            {
              "close": 78105.25,
              "high": 78281.4,
              "low": 77949.05,
              "open": 78281.2,
              "timestamp": 1788987600000,
              "volume": 16653.0
            },
            {
              "close": 77884.31,
              "high": 78159.4,
              "low": 77720.9,
              "open": 78105.25,
              "timestamp": 1788991200000,
              "volume": 17353.0
            },
            {
              "close": 78262.94,
              "high": 78281.69,
              "low": 77878.26,
              "open": 77883.31,
              "timestamp": 1788994800000,
              "volume": 17958.0
            },
            {
              "close": 78136.82,
              "high": 78345.12,
              "low": 78061.8,
              "open": 78262.94,
              "timestamp": 1788998400000,
              "volume": 17951.0
            },
            {
              "close": 78060.37,
              "high": 78482.0,
              "low": 77911.6,
              "open": 78136.81,
              "timestamp": 1789002000000,
              "volume": 17967.0
            },
            {
              "close": 78322.29,
              "high": 78339.4,
              "low": 77950.68,
              "open": 78060.37,
              "timestamp": 1789005600000,
              "volume": 17959.0
            },
            {
              "close": 78296.6,
              "high": 78530.73,
              "low": 78240.49,
              "open": 78321.89,
              "timestamp": 1789009200000,
              "volume": 17946.0
            },
            {
              "close": 78375.09,
              "high": 78410.2,
              "low": 78268.44,
              "open": 78296.6,
              "timestamp": 1789012800000,
              "volume": 17936.0
            },
            {
              "close": 78502.9,
              "high": 78532.7,
              "low": 78243.79,
              "open": 78375.09,
              "timestamp": 1789016400000,
              "volume": 17956.0
            },
            {
              "close": 78388.2,
              "high": 78509.4,
              "low": 78121.5,
              "open": 78502.9,
              "timestamp": 1789020000000,
              "volume": 17938.0
            },
            {
              "close": 78069.73,
              "high": 78393.3,
              "low": 77866.61,
              "open": 78388.2,
              "timestamp": 1789023600000,
              "volume": 17964.0
            },
            {
              "close": 78072.16,
              "high": 78135.6,
              "low": 77990.49,
              "open": 78069.73,
              "timestamp": 1789027200000,
              "volume": 17948.0
            },
            {
              "close": 77968.2,
              "high": 78194.57,
              "low": 77892.95,
              "open": 78072.16,
              "timestamp": 1789030800000,
              "volume": 17943.0
            },
            {
              "close": 77836.32,
              "high": 78017.2,
              "low": 77789.6,
              "open": 77963.34,
              "timestamp": 1789034400000,
              "volume": 17961.0
            },
            {
              "close": 77816.9,
              "high": 78028.2,
              "low": 77668.11,
              "open": 77836.31,
              "timestamp": 1789038000000,
              "volume": 17968.0
            },
            {
              "close": 76859.3,
              "high": 77935.0,
              "low": 76633.8,
              "open": 77816.9,
              "timestamp": 1789041600000,
              "volume": 18015.0
            },
            {
              "close": 77136.85,
              "high": 77206.8,
              "low": 76691.72,
              "open": 76859.22,
              "timestamp": 1789045200000,
              "volume": 18016.0
            },
            {
              "close": 77375.74,
              "high": 77393.3,
              "low": 76921.84,
              "open": 77136.85,
              "timestamp": 1789048800000,
              "volume": 17763.0
            },
            {
              "close": 77218.0,
              "high": 77380.5,
              "low": 77058.32,
              "open": 77375.74,
              "timestamp": 1789052400000,
              "volume": 17968.0
            },
            {
              "close": 77171.14,
              "high": 77279.4,
              "low": 76762.5,
              "open": 77218.0,
              "timestamp": 1789056000000,
              "volume": 17983.0
            },
            {
              "close": 77295.91,
              "high": 77514.29,
              "low": 77091.09,
              "open": 77171.19,
              "timestamp": 1789059600000,
              "volume": 17985.0
            },
            {
              "close": 77222.01,
              "high": 77311.6,
              "low": 76944.23,
              "open": 77295.91,
              "timestamp": 1789063200000,
              "volume": 17964.0
            },
            {
              "close": 77133.1,
              "high": 77269.5,
              "low": 77042.99,
              "open": 77222.01,
              "timestamp": 1789066800000,
              "volume": 17962.0
            },
            {
              "close": 77232.61,
              "high": 77315.4,
              "low": 77069.97,
              "open": 77128.43,
              "timestamp": 1789070400000,
              "volume": 17945.0
            },
            {
              "close": 77113.0,
              "high": 77269.0,
              "low": 77069.61,
              "open": 77232.61,
              "timestamp": 1789074000000,
              "volume": 16761.0
            },
            {
              "close": 76793.42,
              "high": 77181.9,
              "low": 76772.62,
              "open": 77113.0,
              "timestamp": 1789077600000,
              "volume": 17347.0
            },
            {
              "close": 76535.05,
              "high": 76839.4,
              "low": 76417.95,
              "open": 76793.42,
              "timestamp": 1789081200000,
              "volume": 17959.0
            },
            {
              "close": 76879.91,
              "high": 76903.64,
              "low": 76522.04,
              "open": 76535.05,
              "timestamp": 1789084800000,
              "volume": 17953.0
            },
            {
              "close": 76945.89,
              "high": 76978.37,
              "low": 76636.8,
              "open": 76879.92,
              "timestamp": 1789088400000,
              "volume": 17947.0
            },
            {
              "close": 76811.96,
              "high": 76987.4,
              "low": 76736.83,
              "open": 76946.01,
              "timestamp": 1789092000000,
              "volume": 17916.0
            },
            {
              "close": 76860.3,
              "high": 76863.4,
              "low": 76666.15,
              "open": 76811.96,
              "timestamp": 1789095600000,
              "volume": 17958.0
            },
            {
              "close": 77074.18,
              "high": 77166.0,
              "low": 76848.75,
              "open": 76860.3,
              "timestamp": 1789099200000,
              "volume": 17949.0
            },
            {
              "close": 77219.52,
              "high": 77226.71,
              "low": 77028.2,
              "open": 77074.18,
              "timestamp": 1789102800000,
              "volume": 17947.0
            },
            {
              "close": 77263.4,
              "high": 77399.0,
              "low": 77139.51,
              "open": 77219.52,
              "timestamp": 1789106400000,
              "volume": 17959.0
            },
            {
              "close": 77187.51,
              "high": 77373.0,
              "low": 77159.33,
              "open": 77262.47,
              "timestamp": 1789110000000,
              "volume": 17953.0
            },
            {
              "close": 77323.52,
              "high": 77468.36,
              "low": 77100.0,
              "open": 77187.5,
              "timestamp": 1789113600000,
              "volume": 17943.0
            },
            {
              "close": 77000.3,
              "high": 77332.1,
              "low": 76820.47,
              "open": 77323.52,
              "timestamp": 1789117200000,
              "volume": 17948.0
            },
            {
              "close": 76959.5,
              "high": 77129.1,
              "low": 76923.23,
              "open": 77000.3,
              "timestamp": 1789120800000,
              "volume": 17956.0
            },
            {
              "close": 77000.02,
              "high": 77013.3,
              "low": 76705.22,
              "open": 76959.5,
              "timestamp": 1789124400000,
              "volume": 17962.0
            },
            {
              "close": 77990.57,
              "high": 78113.5,
              "low": 75998.84,
              "open": 76999.44,
              "timestamp": 1789128000000,
              "volume": 18035.0
            },
            {
              "close": 79211.31,
              "high": 79293.81,
              "low": 77210.81,
              "open": 77992.01,
              "timestamp": 1789131600000,
              "volume": 17862.0
            },
            {
              "close": 78756.81,
              "high": 79853.68,
              "low": 78469.29,
              "open": 79211.31,
              "timestamp": 1789135200000,
              "volume": 17926.0
            },
            {
              "close": 77681.73,
              "high": 78793.2,
              "low": 77268.23,
              "open": 78756.71,
              "timestamp": 1789138800000,
              "volume": 17973.0
            },
            {
              "close": 77872.02,
              "high": 78028.65,
              "low": 77338.2,
              "open": 77679.79,
              "timestamp": 1789142400000,
              "volume": 17973.0
            },
            {
              "close": 77492.85,
              "high": 77923.5,
              "low": 77449.5,
              "open": 77872.03,
              "timestamp": 1789146000000,
              "volume": 17959.0
            },
            {
              "close": 77018.08,
              "high": 77508.5,
              "low": 76837.3,
              "open": 77492.87,
              "timestamp": 1789149600000,
              "volume": 17969.0
            },
            {
              "close": 77242.5,
              "high": 77338.49,
              "low": 76964.85,
              "open": 77018.47,
              "timestamp": 1789153200000,
              "volume": 17966.0
            },
            {
              "close": 77295.04,
              "high": 77460.0,
              "low": 77161.55,
              "open": 77250.02,
              "timestamp": 1789156800000,
              "volume": 17926.0
            },
            {
              "close": 77079.7,
              "high": 77396.4,
              "low": 77037.93,
              "open": 77295.04,
              "timestamp": 1789160400000,
              "volume": 16774.0
            },
            {
              "close": 77108.47,
              "high": 77203.1,
              "low": 76941.98,
              "open": 77079.7,
              "timestamp": 1789164000000,
              "volume": 17311.0
            },
            {
              "close": 77190.5,
              "high": 77190.64,
              "low": 77084.65,
              "open": 77108.47,
              "timestamp": 1789167600000,
              "volume": 17910.0
            },
            {
              "close": 77250.38,
              "high": 77286.9,
              "low": 77169.8,
              "open": 77190.5,
              "timestamp": 1789171200000,
              "volume": 17898.0
            },
            {
              "close": 77235.42,
              "high": 77346.2,
              "low": 77218.7,
              "open": 77250.4,
              "timestamp": 1789174800000,
              "volume": 17924.0
            },
            {
              "close": 77253.22,
              "high": 77292.53,
              "low": 77176.08,
              "open": 77235.42,
              "timestamp": 1789178400000,
              "volume": 17935.0
            },
            {
              "close": 77236.3,
              "high": 77313.97,
              "low": 77194.0,
              "open": 77248.37,
              "timestamp": 1789182000000,
              "volume": 17920.0
            },
            {
              "close": 77185.73,
              "high": 77288.2,
              "low": 77183.96,
              "open": 77236.3,
              "timestamp": 1789185600000,
              "volume": 17917.0
            },
            {
              "close": 77177.11,
              "high": 77225.6,
              "low": 77128.18,
              "open": 77185.73,
              "timestamp": 1789189200000,
              "volume": 17910.0
            },
            {
              "close": 77259.48,
              "high": 77326.5,
              "low": 77172.64,
              "open": 77177.11,
              "timestamp": 1789192800000,
              "volume": 17910.0
            },
            {
              "close": 77236.3,
              "high": 77309.4,
              "low": 77221.74,
              "open": 77259.48,
              "timestamp": 1789196400000,
              "volume": 17898.0
            },
            {
              "close": 77324.45,
              "high": 77339.3,
              "low": 77220.24,
              "open": 77236.3,
              "timestamp": 1789200000000,
              "volume": 17904.0
            },
            {
              "close": 77319.4,
              "high": 77349.4,
              "low": 77290.57,
              "open": 77324.45,
              "timestamp": 1789203600000,
              "volume": 17902.0
            },
            {
              "close": 77298.03,
              "high": 77366.1,
              "low": 77274.18,
              "open": 77319.4,
              "timestamp": 1789207200000,
              "volume": 17911.0
            },
            {
              "close": 77325.2,
              "high": 77331.2,
              "low": 77259.17,
              "open": 77298.03,
              "timestamp": 1789210800000,
              "volume": 17900.0
            },
            {
              "close": 77294.3,
              "high": 77332.87,
              "low": 77249.61,
              "open": 77325.2,
              "timestamp": 1789214400000,
              "volume": 17901.0
            },
            {
              "close": 77328.6,
              "high": 77363.9,
              "low": 77214.7,
              "open": 77294.3,
              "timestamp": 1789218000000,
              "volume": 17907.0
            },
            {
              "close": 77425.8,
              "high": 77476.8,
              "low": 77328.6,
              "open": 77328.6,
              "timestamp": 1789221600000,
              "volume": 17936.0
            },
            {
              "close": 77343.2,
              "high": 77448.6,
              "low": 77335.39,
              "open": 77429.9,
              "timestamp": 1789225200000,
              "volume": 17906.0
            },
            {
              "close": 77325.26,
              "high": 77384.3,
              "low": 77299.93,
              "open": 77343.2,
              "timestamp": 1789228800000,
              "volume": 17913.0
            },
            {
              "close": 77173.0,
              "high": 77365.0,
              "low": 77139.81,
              "open": 77325.26,
              "timestamp": 1789232400000,
              "volume": 17926.0
            },
            {
              "close": 77105.1,
              "high": 77189.5,
              "low": 77084.68,
              "open": 77173.0,
              "timestamp": 1789236000000,
              "volume": 17925.0
            },
            {
              "close": 77083.5,
              "high": 77156.43,
              "low": 77024.51,
              "open": 77105.1,
              "timestamp": 1789239600000,
              "volume": 17916.0
            },
            {
              "close": 77128.63,
              "high": 77187.3,
              "low": 77083.5,
              "open": 77083.5,
              "timestamp": 1789243200000,
              "volume": 17928.0
            },
            {
              "close": 77217.8,
              "high": 77237.8,
              "low": 77104.6,
              "open": 77128.63,
              "timestamp": 1789246800000,
              "volume": 16912.0
            },
            {
              "close": 77194.7,
              "high": 77265.95,
              "low": 77143.91,
              "open": 77217.8,
              "timestamp": 1789250400000,
              "volume": 17923.0
            },
            {
              "close": 77242.21,
              "high": 77258.5,
              "low": 77190.98,
              "open": 77194.7,
              "timestamp": 1789254000000,
              "volume": 17903.0
            },
            {
              "close": 77238.94,
              "high": 77274.8,
              "low": 77117.01,
              "open": 77234.52,
              "timestamp": 1789257600000,
              "volume": 17608.0
            },
            {
              "close": 77285.0,
              "high": 77308.32,
              "low": 77206.59,
              "open": 77238.94,
              "timestamp": 1789261200000,
              "volume": 17916.0
            },
            {
              "close": 77262.24,
              "high": 77286.4,
              "low": 77207.81,
              "open": 77285.0,
              "timestamp": 1789264800000,
              "volume": 17914.0
            },
            {
              "close": 77161.67,
              "high": 77287.3,
              "low": 77149.65,
              "open": 77262.24,
              "timestamp": 1789268400000,
              "volume": 17897.0
            },
            {
              "close": 77177.62,
              "high": 77227.1,
              "low": 77154.76,
              "open": 77161.67,
              "timestamp": 1789272000000,
              "volume": 17909.0
            },
            {
              "close": 77280.03,
              "high": 77289.4,
              "low": 77177.6,
              "open": 77177.66,
              "timestamp": 1789275600000,
              "volume": 17908.0
            },
            {
              "close": 77081.5,
              "high": 77290.5,
              "low": 77011.88,
              "open": 77280.03,
              "timestamp": 1789279200000,
              "volume": 17913.0
            },
            {
              "close": 77086.33,
              "high": 77135.8,
              "low": 77049.8,
              "open": 77081.5,
              "timestamp": 1789282800000,
              "volume": 17905.0
            },
            {
              "close": 76767.07,
              "high": 77144.87,
              "low": 76711.55,
              "open": 77086.24,
              "timestamp": 1789286400000,
              "volume": 17936.0
            },
            {
              "close": 76765.29,
              "high": 76868.7,
              "low": 76531.65,
              "open": 76766.74,
              "timestamp": 1789290000000,
              "volume": 17925.0
            },
            {
              "close": 76643.0,
              "high": 76784.8,
              "low": 76594.02,
              "open": 76765.29,
              "timestamp": 1789293600000,
              "volume": 17929.0
            },
            {
              "close": 76752.3,
              "high": 76769.4,
              "low": 76464.5,
              "open": 76643.0,
              "timestamp": 1789297200000,
              "volume": 18099.0
            },
            {
              "close": 76724.97,
              "high": 76830.4,
              "low": 76653.87,
              "open": 76752.3,
              "timestamp": 1789300800000,
              "volume": 17924.0
            },
            {
              "close": 76813.11,
              "high": 76891.5,
              "low": 76513.77,
              "open": 76724.83,
              "timestamp": 1789304400000,
              "volume": 17937.0
            },
            {
              "close": 77174.6,
              "high": 77231.1,
              "low": 76810.01,
              "open": 76813.11,
              "timestamp": 1789308000000,
              "volume": 17938.0
            },
            {
              "close": 77097.34,
              "high": 77178.2,
              "low": 76980.6,
              "open": 77174.6,
              "timestamp": 1789311600000,
              "volume": 17918.0
            },
            {
              "close": 77252.0,
              "high": 77332.3,
              "low": 77086.8,
              "open": 77097.34,
              "timestamp": 1789315200000,
              "volume": 17936.0
            },
            {
              "close": 77295.02,
              "high": 77386.4,
              "low": 77212.11,
              "open": 77252.0,
              "timestamp": 1789318800000,
              "volume": 17944.0
            },
            {
              "close": 77313.2,
              "high": 77354.4,
              "low": 77272.54,
              "open": 77295.02,
              "timestamp": 1789322400000,
              "volume": 17923.0
            },
            {
              "close": 77253.6,
              "high": 77380.9,
              "low": 77188.38,
              "open": 77313.22,
              "timestamp": 1789326000000,
              "volume": 17922.0
            }
          ],
          "last_price": 77253.6,
          "momentum": "neutral",
          "rsi_14": 55.29,
          "structure": "bullish"
        },
        "4H": {
          "candle_count": 84,
          "candle_status": {
            "data_age_seconds": 14490,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789315200000,
            "latest_timestamp_utc": "2026-09-13T16:00:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 14400
          },
          "candles": [
            {
              "close": 77638.29,
              "high": 78899.19,
              "low": 76953.21,
              "open": 78827.59,
              "timestamp": 1788120000000,
              "volume": 71099.0
            },
            {
              "close": 77726.61,
              "high": 78152.41,
              "low": 77349.5,
              "open": 77638.26,
              "timestamp": 1788134400000,
              "volume": 71840.0
            },
            {
              "close": 78167.54,
              "high": 78286.1,
              "low": 77425.41,
              "open": 77726.61,
              "timestamp": 1788148800000,
              "volume": 71853.0
            },
            {
              "close": 78283.84,
              "high": 78768.9,
              "low": 77949.26,
              "open": 78167.62,
              "timestamp": 1788163200000,
              "volume": 71973.0
            },
            {
              "close": 78541.47,
              "high": 78742.23,
              "low": 77667.63,
              "open": 78283.83,
              "timestamp": 1788177600000,
              "volume": 72037.0
            },
            {
              "close": 78864.05,
              "high": 79222.53,
              "low": 78449.5,
              "open": 78541.47,
              "timestamp": 1788192000000,
              "volume": 72128.0
            },
            {
              "close": 78548.9,
              "high": 79153.3,
              "low": 78361.82,
              "open": 78868.05,
              "timestamp": 1788206400000,
              "volume": 70073.0
            },
            {
              "close": 78652.45,
              "high": 78868.02,
              "low": 78149.5,
              "open": 78548.9,
              "timestamp": 1788220800000,
              "volume": 71799.0
            },
            {
              "close": 78599.7,
              "high": 79194.69,
              "low": 78467.16,
              "open": 78652.45,
              "timestamp": 1788235200000,
              "volume": 71906.0
            },
            {
              "close": 78055.71,
              "high": 78626.8,
              "low": 77718.57,
              "open": 78599.7,
              "timestamp": 1788249600000,
              "volume": 71818.0
            },
            {
              "close": 77876.8,
              "high": 78394.5,
              "low": 77393.85,
              "open": 78055.71,
              "timestamp": 1788264000000,
              "volume": 71928.0
            },
            {
              "close": 77281.75,
              "high": 77942.2,
              "low": 76367.3,
              "open": 77876.8,
              "timestamp": 1788278400000,
              "volume": 71793.0
            },
            {
              "close": 77399.51,
              "high": 77599.3,
              "low": 76882.53,
              "open": 77285.16,
              "timestamp": 1788292800000,
              "volume": 69706.0
            },
            {
              "close": 77533.54,
              "high": 77762.6,
              "low": 76681.61,
              "open": 77399.51,
              "timestamp": 1788307200000,
              "volume": 71789.0
            },
            {
              "close": 77444.2,
              "high": 77731.21,
              "low": 77264.02,
              "open": 77533.54,
              "timestamp": 1788321600000,
              "volume": 71732.0
            },
            {
              "close": 76787.86,
              "high": 77517.6,
              "low": 76189.26,
              "open": 77444.2,
              "timestamp": 1788336000000,
              "volume": 71881.0
            },
            {
              "close": 77249.4,
              "high": 77458.69,
              "low": 76571.98,
              "open": 76787.86,
              "timestamp": 1788350400000,
              "volume": 62017.0
            },
            {
              "close": 77296.03,
              "high": 77546.0,
              "low": 76913.8,
              "open": 77249.4,
              "timestamp": 1788364800000,
              "volume": 71626.0
            },
            {
              "close": 77298.38,
              "high": 77489.3,
              "low": 76972.38,
              "open": 77300.31,
              "timestamp": 1788379200000,
              "volume": 69912.0
            },
            {
              "close": 77664.55,
              "high": 77875.35,
              "low": 76926.7,
              "open": 77298.05,
              "timestamp": 1788393600000,
              "volume": 71769.0
            },
            {
              "close": 77620.88,
              "high": 78144.09,
              "low": 77055.1,
              "open": 77664.54,
              "timestamp": 1788408000000,
              "volume": 71772.0
            },
            {
              "close": 77908.62,
              "high": 78031.4,
              "low": 77435.29,
              "open": 77626.8,
              "timestamp": 1788422400000,
              "volume": 71054.0
            },
            {
              "close": 81314.88,
              "high": 81332.8,
              "low": 77852.31,
              "open": 77908.62,
              "timestamp": 1788436800000,
              "volume": 62709.0
            },
            {
              "close": 81709.13,
              "high": 81759.43,
              "low": 80585.6,
              "open": 81314.85,
              "timestamp": 1788451200000,
              "volume": 71936.0
            },
            {
              "close": 81229.06,
              "high": 82266.79,
              "low": 80861.54,
              "open": 81723.81,
              "timestamp": 1788465600000,
              "volume": 69988.0
            },
            {
              "close": 80806.17,
              "high": 81393.2,
              "low": 80625.61,
              "open": 81229.06,
              "timestamp": 1788480000000,
              "volume": 71805.0
            },
            {
              "close": 80627.31,
              "high": 81259.47,
              "low": 80538.01,
              "open": 80806.31,
              "timestamp": 1788494400000,
              "volume": 71768.0
            },
            {
              "close": 81183.63,
              "high": 81377.1,
              "low": 80465.59,
              "open": 80627.31,
              "timestamp": 1788508800000,
              "volume": 71874.0
            },
            {
              "close": 79384.3,
              "high": 81322.08,
              "low": 78617.51,
              "open": 81184.65,
              "timestamp": 1788523200000,
              "volume": 61171.0
            },
            {
              "close": 79754.1,
              "high": 79837.5,
              "low": 79333.38,
              "open": 79384.3,
              "timestamp": 1788537600000,
              "volume": 71889.0
            },
            {
              "close": 79615.6,
              "high": 79824.9,
              "low": 79469.76,
              "open": 79754.1,
              "timestamp": 1788552000000,
              "volume": 69800.0
            },
            {
              "close": 79543.21,
              "high": 79675.2,
              "low": 79434.02,
              "open": 79615.6,
              "timestamp": 1788566400000,
              "volume": 71615.0
            },
            {
              "close": 79649.4,
              "high": 79676.3,
              "low": 79404.43,
              "open": 79543.21,
              "timestamp": 1788580800000,
              "volume": 55486.0
            },
            {
              "close": 79576.9,
              "high": 79697.5,
              "low": 79529.4,
              "open": 79653.46,
              "timestamp": 1788595200000,
              "volume": 66342.0
            },
            {
              "close": 79759.5,
              "high": 79780.88,
              "low": 79504.1,
              "open": 79576.9,
              "timestamp": 1788609600000,
              "volume": 71642.0
            },
            {
              "close": 79719.21,
              "high": 80166.4,
              "low": 79673.8,
              "open": 79759.5,
              "timestamp": 1788624000000,
              "volume": 71749.0
            },
            {
              "close": 79795.87,
              "high": 79909.28,
              "low": 79651.93,
              "open": 79719.21,
              "timestamp": 1788638400000,
              "volume": 70599.0
            },
            {
              "close": 79990.15,
              "high": 80079.8,
              "low": 79786.84,
              "open": 79786.84,
              "timestamp": 1788652800000,
              "volume": 71327.0
            },
            {
              "close": 79764.89,
              "high": 80084.6,
              "low": 79538.51,
              "open": 79990.15,
              "timestamp": 1788667200000,
              "volume": 71306.0
            },
            {
              "close": 79877.8,
              "high": 79997.3,
              "low": 79715.35,
              "open": 79764.87,
              "timestamp": 1788681600000,
              "volume": 71596.0
            },
            {
              "close": 79676.34,
              "high": 79973.0,
              "low": 79165.16,
              "open": 79877.8,
              "timestamp": 1788696000000,
              "volume": 71658.0
            },
            {
              "close": 79804.2,
              "high": 79939.4,
              "low": 79542.04,
              "open": 79676.35,
              "timestamp": 1788710400000,
              "volume": 71647.0
            },
            {
              "close": 80299.55,
              "high": 80521.62,
              "low": 79599.14,
              "open": 79804.2,
              "timestamp": 1788724800000,
              "volume": 70893.0
            },
            {
              "close": 79558.76,
              "high": 80407.72,
              "low": 79534.6,
              "open": 80300.11,
              "timestamp": 1788739200000,
              "volume": 71758.0
            },
            {
              "close": 79354.7,
              "high": 79892.24,
              "low": 78956.37,
              "open": 79558.76,
              "timestamp": 1788753600000,
              "volume": 71762.0
            },
            {
              "close": 79376.18,
              "high": 79516.8,
              "low": 79237.81,
              "open": 79357.2,
              "timestamp": 1788768000000,
              "volume": 71777.0
            },
            {
              "close": 78781.6,
              "high": 79612.97,
              "low": 78644.74,
              "open": 79376.18,
              "timestamp": 1788782400000,
              "volume": 71883.0
            },
            {
              "close": 79324.8,
              "high": 79375.18,
              "low": 78765.5,
              "open": 78785.6,
              "timestamp": 1788796800000,
              "volume": 71811.0
            },
            {
              "close": 79074.65,
              "high": 79364.4,
              "low": 78753.01,
              "open": 79324.8,
              "timestamp": 1788811200000,
              "volume": 69965.0
            },
            {
              "close": 78879.38,
              "high": 79458.1,
              "low": 78689.54,
              "open": 79074.79,
              "timestamp": 1788825600000,
              "volume": 71819.0
            },
            {
              "close": 78444.5,
              "high": 78904.02,
              "low": 78141.1,
              "open": 78879.38,
              "timestamp": 1788840000000,
              "volume": 71751.0
            },
            {
              "close": 78399.5,
              "high": 78967.36,
              "low": 78252.51,
              "open": 78444.5,
              "timestamp": 1788854400000,
              "volume": 71777.0
            },
            {
              "close": 78868.08,
              "high": 78870.6,
              "low": 77599.5,
              "open": 78399.5,
              "timestamp": 1788868800000,
              "volume": 71961.0
            },
            {
              "close": 78406.34,
              "high": 78935.3,
              "low": 78230.01,
              "open": 78867.51,
              "timestamp": 1788883200000,
              "volume": 71787.0
            },
            {
              "close": 78425.05,
              "high": 78618.7,
              "low": 78359.41,
              "open": 78404.85,
              "timestamp": 1788897600000,
              "volume": 69969.0
            },
            {
              "close": 78593.2,
              "high": 78895.57,
              "low": 78423.44,
              "open": 78425.05,
              "timestamp": 1788912000000,
              "volume": 71828.0
            },
            {
              "close": 79244.87,
              "high": 79375.76,
              "low": 78593.2,
              "open": 78593.2,
              "timestamp": 1788926400000,
              "volume": 71805.0
            },
            {
              "close": 79280.94,
              "high": 79734.3,
              "low": 78697.5,
              "open": 79244.87,
              "timestamp": 1788940800000,
              "volume": 71870.0
            },
            {
              "close": 78566.97,
              "high": 79647.5,
              "low": 78019.5,
              "open": 79280.95,
              "timestamp": 1788955200000,
              "volume": 71331.0
            },
            {
              "close": 78199.37,
              "high": 78921.25,
              "low": 78111.4,
              "open": 78566.99,
              "timestamp": 1788969600000,
              "volume": 71881.0
            },
            {
              "close": 78262.94,
              "high": 78302.2,
              "low": 77720.9,
              "open": 78192.35,
              "timestamp": 1788984000000,
              "volume": 69924.0
            },
            {
              "close": 78296.6,
              "high": 78530.73,
              "low": 77911.6,
              "open": 78262.94,
              "timestamp": 1788998400000,
              "volume": 71823.0
            },
            {
              "close": 78069.73,
              "high": 78532.7,
              "low": 77866.61,
              "open": 78296.6,
              "timestamp": 1789012800000,
              "volume": 71794.0
            },
            {
              "close": 77816.9,
              "high": 78194.57,
              "low": 77668.11,
              "open": 78069.73,
              "timestamp": 1789027200000,
              "volume": 71820.0
            },
            {
              "close": 77218.0,
              "high": 77935.0,
              "low": 76633.8,
              "open": 77816.9,
              "timestamp": 1789041600000,
              "volume": 71762.0
            },
            {
              "close": 77133.1,
              "high": 77514.29,
              "low": 76762.5,
              "open": 77218.0,
              "timestamp": 1789056000000,
              "volume": 71894.0
            },
            {
              "close": 76535.05,
              "high": 77315.4,
              "low": 76417.95,
              "open": 77128.43,
              "timestamp": 1789070400000,
              "volume": 70012.0
            },
            {
              "close": 76860.3,
              "high": 76987.4,
              "low": 76522.04,
              "open": 76535.05,
              "timestamp": 1789084800000,
              "volume": 71774.0
            },
            {
              "close": 77187.51,
              "high": 77399.0,
              "low": 76848.75,
              "open": 76860.3,
              "timestamp": 1789099200000,
              "volume": 71808.0
            },
            {
              "close": 77000.02,
              "high": 77468.36,
              "low": 76705.22,
              "open": 77187.5,
              "timestamp": 1789113600000,
              "volume": 71809.0
            },
            {
              "close": 77681.73,
              "high": 79853.68,
              "low": 75998.84,
              "open": 76999.44,
              "timestamp": 1789128000000,
              "volume": 71796.0
            },
            {
              "close": 77242.5,
              "high": 78028.65,
              "low": 76837.3,
              "open": 77679.79,
              "timestamp": 1789142400000,
              "volume": 71867.0
            },
            {
              "close": 77190.5,
              "high": 77460.0,
              "low": 76941.98,
              "open": 77250.02,
              "timestamp": 1789156800000,
              "volume": 69921.0
            },
            {
              "close": 77236.3,
              "high": 77346.2,
              "low": 77169.8,
              "open": 77190.5,
              "timestamp": 1789171200000,
              "volume": 71677.0
            },
            {
              "close": 77236.3,
              "high": 77326.5,
              "low": 77128.18,
              "open": 77236.3,
              "timestamp": 1789185600000,
              "volume": 71635.0
            },
            {
              "close": 77325.2,
              "high": 77366.1,
              "low": 77220.24,
              "open": 77236.3,
              "timestamp": 1789200000000,
              "volume": 71617.0
            },
            {
              "close": 77343.2,
              "high": 77476.8,
              "low": 77214.7,
              "open": 77325.2,
              "timestamp": 1789214400000,
              "volume": 71650.0
            },
            {
              "close": 77083.5,
              "high": 77384.3,
              "low": 77024.51,
              "open": 77343.2,
              "timestamp": 1789228800000,
              "volume": 71680.0
            },
            {
              "close": 77242.21,
              "high": 77265.95,
              "low": 77083.5,
              "open": 77083.5,
              "timestamp": 1789243200000,
              "volume": 70666.0
            },
            {
              "close": 77161.67,
              "high": 77308.32,
              "low": 77117.01,
              "open": 77234.52,
              "timestamp": 1789257600000,
              "volume": 71335.0
            },
            {
              "close": 77086.33,
              "high": 77290.5,
              "low": 77011.88,
              "open": 77161.67,
              "timestamp": 1789272000000,
              "volume": 71635.0
            },
            {
              "close": 76752.3,
              "high": 77144.87,
              "low": 76464.5,
              "open": 77086.24,
              "timestamp": 1789286400000,
              "volume": 71889.0
            },
            {
              "close": 77097.34,
              "high": 77231.1,
              "low": 76513.77,
              "open": 76752.3,
              "timestamp": 1789300800000,
              "volume": 71717.0
            },
            {
              "close": 77253.6,
              "high": 77386.4,
              "low": 77086.8,
              "open": 77097.34,
              "timestamp": 1789315200000,
              "volume": 71725.0
            }
          ],
          "last_price": 77253.6,
          "momentum": "neutral",
          "rsi_14": 45.71,
          "structure": "neutral"
        },
        "5M": {
          "candle_count": 144,
          "candle_status": {
            "data_age_seconds": 390,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789329300000,
            "latest_timestamp_utc": "2026-09-13T19:55:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 300
          },
          "candles": [
            {
              "close": 77123.86,
              "high": 77144.87,
              "low": 77078.21,
              "open": 77086.24,
              "timestamp": 1789286400000,
              "volume": 1492.0
            },
            {
              "close": 77081.54,
              "high": 77123.93,
              "low": 77066.15,
              "open": 77123.86,
              "timestamp": 1789286700000,
              "volume": 1491.0
            },
            {
              "close": 77028.91,
              "high": 77081.54,
              "low": 76999.3,
              "open": 77081.54,
              "timestamp": 1789287000000,
              "volume": 1494.0
            },
            {
              "close": 76968.67,
              "high": 77028.91,
              "low": 76965.5,
              "open": 77028.91,
              "timestamp": 1789287300000,
              "volume": 1498.0
            },
            {
              "close": 76993.71,
              "high": 77005.06,
              "low": 76968.82,
              "open": 76968.82,
              "timestamp": 1789287600000,
              "volume": 1497.0
            },
            {
              "close": 76987.46,
              "high": 76994.2,
              "low": 76986.32,
              "open": 76993.71,
              "timestamp": 1789287900000,
              "volume": 1495.0
            },
            {
              "close": 76863.44,
              "high": 76987.46,
              "low": 76810.0,
              "open": 76987.46,
              "timestamp": 1789288200000,
              "volume": 1497.0
            },
            {
              "close": 76748.29,
              "high": 76876.7,
              "low": 76732.61,
              "open": 76863.44,
              "timestamp": 1789288500000,
              "volume": 1501.0
            },
            {
              "close": 76792.32,
              "high": 76835.7,
              "low": 76711.55,
              "open": 76748.23,
              "timestamp": 1789288800000,
              "volume": 1494.0
            },
            {
              "close": 76830.77,
              "high": 76840.4,
              "low": 76753.57,
              "open": 76792.32,
              "timestamp": 1789289100000,
              "volume": 1492.0
            },
            {
              "close": 76781.32,
              "high": 76840.4,
              "low": 76767.95,
              "open": 76830.77,
              "timestamp": 1789289400000,
              "volume": 1492.0
            },
            {
              "close": 76767.07,
              "high": 76796.07,
              "low": 76720.12,
              "open": 76781.32,
              "timestamp": 1789289700000,
              "volume": 1493.0
            },
            {
              "close": 76815.84,
              "high": 76815.9,
              "low": 76763.97,
              "open": 76766.74,
              "timestamp": 1789290000000,
              "volume": 1494.0
            },
            {
              "close": 76808.47,
              "high": 76868.7,
              "low": 76808.47,
              "open": 76815.85,
              "timestamp": 1789290300000,
              "volume": 1493.0
            },
            {
              "close": 76779.5,
              "high": 76808.63,
              "low": 76747.22,
              "open": 76808.2,
              "timestamp": 1789290600000,
              "volume": 1492.0
            },
            {
              "close": 76730.8,
              "high": 76779.5,
              "low": 76717.98,
              "open": 76779.5,
              "timestamp": 1789290900000,
              "volume": 1493.0
            },
            {
              "close": 76677.0,
              "high": 76790.88,
              "low": 76624.3,
              "open": 76730.8,
              "timestamp": 1789291200000,
              "volume": 1497.0
            },
            {
              "close": 76603.88,
              "high": 76696.0,
              "low": 76558.91,
              "open": 76677.0,
              "timestamp": 1789291500000,
              "volume": 1499.0
            },
            {
              "close": 76566.7,
              "high": 76649.4,
              "low": 76531.65,
              "open": 76603.86,
              "timestamp": 1789291800000,
              "volume": 1491.0
            },
            {
              "close": 76688.86,
              "high": 76742.4,
              "low": 76566.7,
              "open": 76566.7,
              "timestamp": 1789292100000,
              "volume": 1494.0
            },
            {
              "close": 76685.12,
              "high": 76721.5,
              "low": 76680.86,
              "open": 76688.86,
              "timestamp": 1789292400000,
              "volume": 1493.0
            },
            {
              "close": 76736.54,
              "high": 76743.63,
              "low": 76682.81,
              "open": 76685.12,
              "timestamp": 1789292700000,
              "volume": 1492.0
            },
            {
              "close": 76762.14,
              "high": 76769.8,
              "low": 76715.29,
              "open": 76736.54,
              "timestamp": 1789293000000,
              "volume": 1492.0
            },
            {
              "close": 76765.29,
              "high": 76791.23,
              "low": 76691.8,
              "open": 76762.14,
              "timestamp": 1789293300000,
              "volume": 1495.0
            },
            {
              "close": 76754.8,
              "high": 76781.4,
              "low": 76754.51,
              "open": 76765.29,
              "timestamp": 1789293600000,
              "volume": 1490.0
            },
            {
              "close": 76764.31,
              "high": 76774.3,
              "low": 76737.06,
              "open": 76754.8,
              "timestamp": 1789293900000,
              "volume": 1492.0
            },
            {
              "close": 76764.61,
              "high": 76772.2,
              "low": 76719.2,
              "open": 76764.31,
              "timestamp": 1789294200000,
              "volume": 1490.0
            },
            {
              "close": 76737.9,
              "high": 76777.6,
              "low": 76737.47,
              "open": 76764.61,
              "timestamp": 1789294500000,
              "volume": 1492.0
            },
            {
              "close": 76715.41,
              "high": 76739.47,
              "low": 76711.07,
              "open": 76737.86,
              "timestamp": 1789294800000,
              "volume": 1493.0
            },
            {
              "close": 76729.39,
              "high": 76729.4,
              "low": 76714.22,
              "open": 76715.41,
              "timestamp": 1789295100000,
              "volume": 1494.0
            },
            {
              "close": 76778.15,
              "high": 76784.8,
              "low": 76728.82,
              "open": 76729.39,
              "timestamp": 1789295400000,
              "volume": 1493.0
            },
            {
              "close": 76752.81,
              "high": 76778.5,
              "low": 76746.06,
              "open": 76778.17,
              "timestamp": 1789295700000,
              "volume": 1493.0
            },
            {
              "close": 76664.24,
              "high": 76752.81,
              "low": 76662.89,
              "open": 76752.81,
              "timestamp": 1789296000000,
              "volume": 1492.0
            },
            {
              "close": 76716.29,
              "high": 76720.1,
              "low": 76664.23,
              "open": 76664.24,
              "timestamp": 1789296300000,
              "volume": 1495.0
            },
            {
              "close": 76646.67,
              "high": 76716.29,
              "low": 76625.4,
              "open": 76716.29,
              "timestamp": 1789296600000,
              "volume": 1499.0
            },
            {
              "close": 76643.0,
              "high": 76676.5,
              "low": 76594.02,
              "open": 76646.67,
              "timestamp": 1789296900000,
              "volume": 1506.0
            },
            {
              "close": 76669.4,
              "high": 76681.5,
              "low": 76464.5,
              "open": 76643.0,
              "timestamp": 1789297200000,
              "volume": 1519.0
            },
            {
              "close": 76571.6,
              "high": 76674.76,
              "low": 76555.55,
              "open": 76668.98,
              "timestamp": 1789297500000,
              "volume": 1523.0
            },
            {
              "close": 76492.01,
              "high": 76603.0,
              "low": 76483.11,
              "open": 76571.6,
              "timestamp": 1789297800000,
              "volume": 1504.0
            },
            {
              "close": 76570.79,
              "high": 76606.97,
              "low": 76492.0,
              "open": 76492.01,
              "timestamp": 1789298100000,
              "volume": 1500.0
            },
            {
              "close": 76628.65,
              "high": 76630.0,
              "low": 76565.48,
              "open": 76570.79,
              "timestamp": 1789298400000,
              "volume": 1505.0
            },
            {
              "close": 76633.1,
              "high": 76637.73,
              "low": 76612.63,
              "open": 76628.9,
              "timestamp": 1789298700000,
              "volume": 1504.0
            },
            {
              "close": 76661.35,
              "high": 76661.4,
              "low": 76615.86,
              "open": 76633.07,
              "timestamp": 1789299000000,
              "volume": 1513.0
            },
            {
              "close": 76722.58,
              "high": 76731.3,
              "low": 76660.58,
              "open": 76661.35,
              "timestamp": 1789299300000,
              "volume": 1533.0
            },
            {
              "close": 76745.13,
              "high": 76765.75,
              "low": 76722.57,
              "open": 76722.58,
              "timestamp": 1789299600000,
              "volume": 1509.0
            },
            {
              "close": 76736.85,
              "high": 76757.0,
              "low": 76713.17,
              "open": 76745.12,
              "timestamp": 1789299900000,
              "volume": 1503.0
            },
            {
              "close": 76746.6,
              "high": 76769.4,
              "low": 76736.85,
              "open": 76736.85,
              "timestamp": 1789300200000,
              "volume": 1492.0
            },
            {
              "close": 76752.3,
              "high": 76759.3,
              "low": 76719.61,
              "open": 76746.6,
              "timestamp": 1789300500000,
              "volume": 1494.0
            },
            {
              "close": 76720.81,
              "high": 76752.7,
              "low": 76720.8,
              "open": 76752.3,
              "timestamp": 1789300800000,
              "volume": 1491.0
            },
            {
              "close": 76739.48,
              "high": 76748.7,
              "low": 76720.81,
              "open": 76720.81,
              "timestamp": 1789301100000,
              "volume": 1492.0
            },
            {
              "close": 76765.82,
              "high": 76773.4,
              "low": 76739.48,
              "open": 76739.48,
              "timestamp": 1789301400000,
              "volume": 1491.0
            },
            {
              "close": 76806.77,
              "high": 76826.62,
              "low": 76763.22,
              "open": 76765.82,
              "timestamp": 1789301700000,
              "volume": 1500.0
            },
            {
              "close": 76809.57,
              "high": 76815.5,
              "low": 76784.22,
              "open": 76806.77,
              "timestamp": 1789302000000,
              "volume": 1495.0
            },
            {
              "close": 76799.51,
              "high": 76818.0,
              "low": 76799.5,
              "open": 76809.57,
              "timestamp": 1789302300000,
              "volume": 1491.0
            },
            {
              "close": 76760.9,
              "high": 76830.4,
              "low": 76750.6,
              "open": 76799.51,
              "timestamp": 1789302600000,
              "volume": 1495.0
            },
            {
              "close": 76755.2,
              "high": 76768.0,
              "low": 76717.11,
              "open": 76760.9,
              "timestamp": 1789302900000,
              "volume": 1493.0
            },
            {
              "close": 76695.06,
              "high": 76759.4,
              "low": 76671.71,
              "open": 76755.2,
              "timestamp": 1789303200000,
              "volume": 1496.0
            },
            {
              "close": 76668.03,
              "high": 76698.4,
              "low": 76667.35,
              "open": 76695.05,
              "timestamp": 1789303500000,
              "volume": 1494.0
            },
            {
              "close": 76706.51,
              "high": 76724.55,
              "low": 76653.87,
              "open": 76668.03,
              "timestamp": 1789303800000,
              "volume": 1493.0
            },
            {
              "close": 76724.97,
              "high": 76755.5,
              "low": 76684.96,
              "open": 76706.51,
              "timestamp": 1789304100000,
              "volume": 1493.0
            },
            {
              "close": 76664.41,
              "high": 76724.97,
              "low": 76664.39,
              "open": 76724.83,
              "timestamp": 1789304400000,
              "volume": 1495.0
            },
            {
              "close": 76703.86,
              "high": 76703.86,
              "low": 76641.02,
              "open": 76664.58,
              "timestamp": 1789304700000,
              "volume": 1495.0
            },
            {
              "close": 76729.4,
              "high": 76736.1,
              "low": 76700.01,
              "open": 76703.86,
              "timestamp": 1789305000000,
              "volume": 1491.0
            },
            {
              "close": 76662.19,
              "high": 76743.61,
              "low": 76660.59,
              "open": 76729.4,
              "timestamp": 1789305300000,
              "volume": 1492.0
            },
            {
              "close": 76629.0,
              "high": 76670.3,
              "low": 76569.59,
              "open": 76662.51,
              "timestamp": 1789305600000,
              "volume": 1499.0
            },
            {
              "close": 76545.1,
              "high": 76632.2,
              "low": 76513.77,
              "open": 76629.0,
              "timestamp": 1789305900000,
              "volume": 1497.0
            },
            {
              "close": 76633.3,
              "high": 76656.1,
              "low": 76544.42,
              "open": 76545.02,
              "timestamp": 1789306200000,
              "volume": 1496.0
            },
            {
              "close": 76676.3,
              "high": 76676.3,
              "low": 76633.3,
              "open": 76633.3,
              "timestamp": 1789306500000,
              "volume": 1497.0
            },
            {
              "close": 76734.84,
              "high": 76739.3,
              "low": 76667.43,
              "open": 76676.3,
              "timestamp": 1789306800000,
              "volume": 1492.0
            },
            {
              "close": 76811.0,
              "high": 76811.0,
              "low": 76734.84,
              "open": 76735.26,
              "timestamp": 1789307100000,
              "volume": 1493.0
            },
            {
              "close": 76829.83,
              "high": 76891.5,
              "low": 76793.89,
              "open": 76811.0,
              "timestamp": 1789307400000,
              "volume": 1495.0
            },
            {
              "close": 76813.11,
              "high": 76837.4,
              "low": 76805.99,
              "open": 76829.83,
              "timestamp": 1789307700000,
              "volume": 1495.0
            },
            {
              "close": 76831.3,
              "high": 76842.9,
              "low": 76810.01,
              "open": 76813.11,
              "timestamp": 1789308000000,
              "volume": 1491.0
            },
            {
              "close": 76936.41,
              "high": 76936.5,
              "low": 76831.25,
              "open": 76831.3,
              "timestamp": 1789308300000,
              "volume": 1497.0
            },
            {
              "close": 76973.4,
              "high": 76979.4,
              "low": 76916.28,
              "open": 76936.41,
              "timestamp": 1789308600000,
              "volume": 1494.0
            },
            {
              "close": 77017.61,
              "high": 77079.2,
              "low": 76973.4,
              "open": 76973.4,
              "timestamp": 1789308900000,
              "volume": 1492.0
            },
            {
              "close": 77039.33,
              "high": 77065.0,
              "low": 77017.61,
              "open": 77017.61,
              "timestamp": 1789309200000,
              "volume": 1497.0
            },
            {
              "close": 77067.05,
              "high": 77090.8,
              "low": 77020.15,
              "open": 77039.33,
              "timestamp": 1789309500000,
              "volume": 1497.0
            },
            {
              "close": 77076.2,
              "high": 77086.7,
              "low": 77047.42,
              "open": 77067.05,
              "timestamp": 1789309800000,
              "volume": 1493.0
            },
            {
              "close": 77165.74,
              "high": 77231.1,
              "low": 77075.05,
              "open": 77076.2,
              "timestamp": 1789310100000,
              "volume": 1498.0
            },
            {
              "close": 77150.3,
              "high": 77174.8,
              "low": 77115.26,
              "open": 77165.74,
              "timestamp": 1789310400000,
              "volume": 1495.0
            },
            {
              "close": 77167.21,
              "high": 77221.36,
              "low": 77150.3,
              "open": 77150.3,
              "timestamp": 1789310700000,
              "volume": 1491.0
            },
            {
              "close": 77168.81,
              "high": 77179.4,
              "low": 77123.94,
              "open": 77167.21,
              "timestamp": 1789311000000,
              "volume": 1494.0
            },
            {
              "close": 77174.6,
              "high": 77194.5,
              "low": 77130.84,
              "open": 77168.81,
              "timestamp": 1789311300000,
              "volume": 1499.0
            },
            {
              "close": 77099.4,
              "high": 77178.2,
              "low": 77086.8,
              "open": 77174.6,
              "timestamp": 1789311600000,
              "volume": 1499.0
            },
            {
              "close": 77099.4,
              "high": 77106.3,
              "low": 77076.6,
              "open": 77099.4,
              "timestamp": 1789311900000,
              "volume": 1495.0
            },
            {
              "close": 77087.33,
              "high": 77099.4,
              "low": 77071.61,
              "open": 77099.4,
              "timestamp": 1789312200000,
              "volume": 1492.0
            },
            {
              "close": 76982.6,
              "high": 77087.44,
              "low": 76980.6,
              "open": 77087.33,
              "timestamp": 1789312500000,
              "volume": 1497.0
            },
            {
              "close": 77157.82,
              "high": 77174.4,
              "low": 76982.6,
              "open": 76982.6,
              "timestamp": 1789312800000,
              "volume": 1493.0
            },
            {
              "close": 77006.4,
              "high": 77157.82,
              "low": 76987.2,
              "open": 77157.82,
              "timestamp": 1789313100000,
              "volume": 1494.0
            },
            {
              "close": 77084.5,
              "high": 77084.5,
              "low": 77006.4,
              "open": 77006.4,
              "timestamp": 1789313400000,
              "volume": 1490.0
            },
            {
              "close": 77048.5,
              "high": 77084.5,
              "low": 77042.0,
              "open": 77084.5,
              "timestamp": 1789313700000,
              "volume": 1490.0
            },
            {
              "close": 77129.54,
              "high": 77148.01,
              "low": 77039.5,
              "open": 77044.51,
              "timestamp": 1789314000000,
              "volume": 1494.0
            },
            {
              "close": 77124.4,
              "high": 77130.18,
              "low": 77097.9,
              "open": 77129.54,
              "timestamp": 1789314300000,
              "volume": 1491.0
            },
            {
              "close": 77120.5,
              "high": 77128.0,
              "low": 77099.54,
              "open": 77124.4,
              "timestamp": 1789314600000,
              "volume": 1491.0
            },
            {
              "close": 77097.34,
              "high": 77120.49,
              "low": 77080.68,
              "open": 77120.49,
              "timestamp": 1789314900000,
              "volume": 1492.0
            },
            {
              "close": 77122.65,
              "high": 77155.3,
              "low": 77097.33,
              "open": 77097.34,
              "timestamp": 1789315200000,
              "volume": 1494.0
            },
            {
              "close": 77115.01,
              "high": 77165.7,
              "low": 77089.3,
              "open": 77122.65,
              "timestamp": 1789315500000,
              "volume": 1492.0
            },
            {
              "close": 77165.03,
              "high": 77226.13,
              "low": 77086.8,
              "open": 77115.01,
              "timestamp": 1789315800000,
              "volume": 1501.0
            },
            {
              "close": 77183.0,
              "high": 77193.12,
              "low": 77150.16,
              "open": 77165.03,
              "timestamp": 1789316100000,
              "volume": 1495.0
            },
            {
              "close": 77226.8,
              "high": 77239.33,
              "low": 77183.0,
              "open": 77183.0,
              "timestamp": 1789316400000,
              "volume": 1495.0
            },
            {
              "close": 77208.71,
              "high": 77266.42,
              "low": 77204.5,
              "open": 77226.8,
              "timestamp": 1789316700000,
              "volume": 1493.0
            },
            {
              "close": 77201.54,
              "high": 77249.4,
              "low": 77201.53,
              "open": 77208.71,
              "timestamp": 1789317000000,
              "volume": 1493.0
            },
            {
              "close": 77228.3,
              "high": 77228.4,
              "low": 77191.3,
              "open": 77201.54,
              "timestamp": 1789317300000,
              "volume": 1493.0
            },
            {
              "close": 77281.78,
              "high": 77332.3,
              "low": 77228.3,
              "open": 77228.3,
              "timestamp": 1789317600000,
              "volume": 1497.0
            },
            {
              "close": 77211.67,
              "high": 77288.9,
              "low": 77200.47,
              "open": 77281.68,
              "timestamp": 1789317900000,
              "volume": 1494.0
            },
            {
              "close": 77259.45,
              "high": 77260.6,
              "low": 77209.25,
              "open": 77211.67,
              "timestamp": 1789318200000,
              "volume": 1495.0
            },
            {
              "close": 77252.0,
              "high": 77297.65,
              "low": 77248.68,
              "open": 77259.46,
              "timestamp": 1789318500000,
              "volume": 1494.0
            },
            {
              "close": 77295.57,
              "high": 77296.5,
              "low": 77252.0,
              "open": 77252.0,
              "timestamp": 1789318800000,
              "volume": 1492.0
            },
            {
              "close": 77309.34,
              "high": 77332.4,
              "low": 77287.43,
              "open": 77295.57,
              "timestamp": 1789319100000,
              "volume": 1496.0
            },
            {
              "close": 77340.71,
              "high": 77386.4,
              "low": 77309.34,
              "open": 77309.34,
              "timestamp": 1789319400000,
              "volume": 1497.0
            },
            {
              "close": 77322.5,
              "high": 77369.04,
              "low": 77304.43,
              "open": 77340.71,
              "timestamp": 1789319700000,
              "volume": 1496.0
            },
            {
              "close": 77280.44,
              "high": 77328.3,
              "low": 77279.64,
              "open": 77326.2,
              "timestamp": 1789320000000,
              "volume": 1494.0
            },
            {
              "close": 77264.15,
              "high": 77292.3,
              "low": 77263.93,
              "open": 77280.42,
              "timestamp": 1789320300000,
              "volume": 1498.0
            },
            {
              "close": 77215.45,
              "high": 77264.5,
              "low": 77212.11,
              "open": 77264.15,
              "timestamp": 1789320600000,
              "volume": 1493.0
            },
            {
              "close": 77243.37,
              "high": 77255.3,
              "low": 77215.4,
              "open": 77215.45,
              "timestamp": 1789320900000,
              "volume": 1501.0
            },
            {
              "close": 77238.61,
              "high": 77246.49,
              "low": 77233.86,
              "open": 77243.37,
              "timestamp": 1789321200000,
              "volume": 1494.0
            },
            {
              "close": 77299.4,
              "high": 77299.4,
              "low": 77238.61,
              "open": 77238.61,
              "timestamp": 1789321500000,
              "volume": 1496.0
            },
            {
              "close": 77299.71,
              "high": 77333.7,
              "low": 77290.77,
              "open": 77299.4,
              "timestamp": 1789321800000,
              "volume": 1494.0
            },
            {
              "close": 77295.02,
              "high": 77309.4,
              "low": 77295.0,
              "open": 77299.72,
              "timestamp": 1789322100000,
              "volume": 1493.0
            },
            {
              "close": 77283.02,
              "high": 77299.3,
              "low": 77276.06,
              "open": 77295.02,
              "timestamp": 1789322400000,
              "volume": 1490.0
            },
            {
              "close": 77280.69,
              "high": 77292.2,
              "low": 77272.54,
              "open": 77283.02,
              "timestamp": 1789322700000,
              "volume": 1494.0
            },
            {
              "close": 77333.12,
              "high": 77334.4,
              "low": 77274.25,
              "open": 77280.69,
              "timestamp": 1789323000000,
              "volume": 1496.0
            },
            {
              "close": 77314.7,
              "high": 77354.4,
              "low": 77310.7,
              "open": 77333.05,
              "timestamp": 1789323300000,
              "volume": 1492.0
            },
            {
              "close": 77331.3,
              "high": 77341.8,
              "low": 77314.7,
              "open": 77314.7,
              "timestamp": 1789323600000,
              "volume": 1497.0
            },
            {
              "close": 77294.84,
              "high": 77337.2,
              "low": 77293.32,
              "open": 77331.3,
              "timestamp": 1789323900000,
              "volume": 1493.0
            },
            {
              "close": 77321.9,
              "high": 77324.0,
              "low": 77278.7,
              "open": 77294.81,
              "timestamp": 1789324200000,
              "volume": 1493.0
            },
            {
              "close": 77338.56,
              "high": 77344.8,
              "low": 77321.9,
              "open": 77321.9,
              "timestamp": 1789324500000,
              "volume": 1493.0
            },
            {
              "close": 77338.6,
              "high": 77338.6,
              "low": 77312.1,
              "open": 77338.54,
              "timestamp": 1789324800000,
              "volume": 1492.0
            },
            {
              "close": 77335.45,
              "high": 77349.4,
              "low": 77335.11,
              "open": 77338.6,
              "timestamp": 1789325100000,
              "volume": 1492.0
            },
            {
              "close": 77337.52,
              "high": 77337.6,
              "low": 77335.93,
              "open": 77336.5,
              "timestamp": 1789325400000,
              "volume": 1495.0
            },
            {
              "close": 77313.2,
              "high": 77337.53,
              "low": 77301.41,
              "open": 77337.52,
              "timestamp": 1789325700000,
              "volume": 1496.0
            },
            {
              "close": 77346.81,
              "high": 77347.23,
              "low": 77313.22,
              "open": 77313.22,
              "timestamp": 1789326000000,
              "volume": 1493.0
            },
            {
              "close": 77285.4,
              "high": 77380.9,
              "low": 77281.6,
              "open": 77346.81,
              "timestamp": 1789326300000,
              "volume": 1496.0
            },
            {
              "close": 77244.11,
              "high": 77292.9,
              "low": 77244.0,
              "open": 77285.4,
              "timestamp": 1789326600000,
              "volume": 1492.0
            },
            {
              "close": 77213.08,
              "high": 77250.6,
              "low": 77212.01,
              "open": 77244.11,
              "timestamp": 1789326900000,
              "volume": 1496.0
            },
            {
              "close": 77234.53,
              "high": 77234.6,
              "low": 77190.33,
              "open": 77213.07,
              "timestamp": 1789327200000,
              "volume": 1493.0
            },
            {
              "close": 77242.3,
              "high": 77242.3,
              "low": 77224.9,
              "open": 77234.53,
              "timestamp": 1789327500000,
              "volume": 1491.0
            },
            {
              "close": 77209.46,
              "high": 77246.4,
              "low": 77196.28,
              "open": 77242.3,
              "timestamp": 1789327800000,
              "volume": 1494.0
            },
            {
              "close": 77197.73,
              "high": 77218.7,
              "low": 77188.38,
              "open": 77209.46,
              "timestamp": 1789328100000,
              "volume": 1495.0
            },
            {
              "close": 77213.9,
              "high": 77213.9,
              "low": 77197.37,
              "open": 77197.73,
              "timestamp": 1789328400000,
              "volume": 1492.0
            },
            {
              "close": 77214.24,
              "high": 77221.0,
              "low": 77206.24,
              "open": 77213.9,
              "timestamp": 1789328700000,
              "volume": 1493.0
            },
            {
              "close": 77245.65,
              "high": 77245.67,
              "low": 77203.16,
              "open": 77214.24,
              "timestamp": 1789329000000,
              "volume": 1495.0
            },
            {
              "close": 77253.6,
              "high": 77253.6,
              "low": 77245.64,
              "open": 77245.65,
              "timestamp": 1789329300000,
              "volume": 1492.0
            }
          ],
          "last_price": 77253.6,
          "momentum": "neutral",
          "rsi_14": 49.73,
          "structure": "bearish"
        }
      }
    },
    {
      "bridge_analysis": {
        "decision": "REJECT",
        "directional_bias": "neutral",
        "execution_5m": {
          "candle_confirmed": false,
          "confirmed": false,
          "reason": "No directional bias is established.",
          "rsi_confirmed": false,
          "structure_shift": false
        },
        "execution_context": {
          "atr_14": 4.976935,
          "distance_to_high": 9.83999999999969,
          "distance_to_low": 23.390000000000327,
          "extension": "normal",
          "range_position": 0.7039,
          "recent_high": 2514.6,
          "recent_low": 2481.37
        },
        "geometry": {
          "entry_quality": "unknown",
          "invalidation": null,
          "reward_to_risk": null,
          "risk_distance": null,
          "room_to_target": null,
          "target_reference": null
        },
        "multi_horizon_state": "conflicted",
        "reason": "Directional evidence is materially conflicted and lacks sufficient edge.",
        "setup_grade": "REJECT",
        "symbol": "ETHUSD",
        "timeframes": {
          "15M": {
            "candle_count": 192,
            "last_price": 2504.76,
            "momentum": "neutral",
            "rsi_14": 59.45,
            "structure": "bullish"
          },
          "1H": {
            "candle_count": 168,
            "last_price": 2504.76,
            "momentum": "neutral",
            "rsi_14": 50.44,
            "structure": "neutral"
          },
          "4H": {
            "candle_count": 84,
            "last_price": 2504.76,
            "momentum": "neutral",
            "rsi_14": 51.6,
            "structure": "neutral"
          },
          "5M": {
            "candle_count": 144,
            "last_price": 2504.76,
            "momentum": "neutral",
            "rsi_14": 50.08,
            "structure": "bearish"
          }
        },
        "trade_plan": {
          "entry_reference": null,
          "live_market_entry_reference": null,
          "live_market_entry_reference_is_authorization": false,
          "live_market_entry_reference_side": null,
          "reason": "No directional bias is established.",
          "reward_to_tp1": null,
          "reward_to_tp2": null,
          "reward_to_tp3": null,
          "risk_distance": null,
          "rr_tp1": null,
          "rr_tp2": null,
          "rr_tp3": null,
          "safe_loss": null,
          "tp1": null,
          "tp2": null,
          "tp3": null,
          "valid": false
        }
      },
      "broker": {
        "route_id": 452,
        "tradable_instrument_id": 214
      },
      "instrument_specs": {
        "available": true,
        "bar_source": "BID",
        "base_currency": "ETH",
        "cache": {
          "age_seconds": 637607.319,
          "captured_at": "2026-09-06T10:54:52.063331+00:00",
          "source": "stale_cache",
          "stale": true
        },
        "contract_size": 10,
        "error": null,
        "leverage": "3.00",
        "lot_step": 0.01,
        "margin_hedging_type": "fx_cfd",
        "maximum_lot": null,
        "minimum_lot": 0.01,
        "minimum_stop_distance": null,
        "quote_currency": "USD",
        "raw_details": {
          "d": {
            "barSource": "BID",
            "baseCurrency": "ETH",
            "betSize": null,
            "betStep": null,
            "bettingCurrency": null,
            "contractMonth": null,
            "country": null,
            "deliveryStatus": null,
            "description": "Ethereum vs US Dollar",
            "exerciseStyle": null,
            "firstTradeDate": null,
            "hasDaily": true,
            "hasIntraday": true,
            "industry": null,
            "isin": "",
            "lastTradeDate": null,
            "leverage": "3.00",
            "localizedName": "ETHUSD",
            "logoUrl": null,
            "lotSize": 10,
            "lotStep": 0.01,
            "margin_hedging_type": "fx_cfd",
            "marketCap": null,
            "marketDataExchange": "Cryptos",
            "maxLot": null,
            "minLot": 0.01,
            "name": "ETHUSD",
            "noticeDate": null,
            "quotingCurrency": "USD",
            "sector": null,
            "settlementDate": null,
            "settlementSystem": "Immediate",
            "strikePrice": null,
            "strikeType": null,
            "symbolStatus": "FULLY_OPEN",
            "tickCost": [
              {
                "leftRangeLimit": null,
                "tickCost": 0.0
              }
            ],
            "tickSize": [
              {
                "leftRangeLimit": null,
                "tickSize": 0.01
              }
            ],
            "tradeSessionId": 1547,
            "tradeSessionStatusId": 20,
            "tradingExchange": "Crypto",
            "type": "CRYPTO"
          },
          "s": "ok"
        },
        "route_id": 9912,
        "symbol_status": "FULLY_OPEN",
        "tick_cost_raw": 0.0,
        "tick_size": 0.01,
        "tick_value": null,
        "tradable_instrument_id": 214,
        "trading_session_id": 1547,
        "trading_session_status_id": 20
      },
      "market_snapshot": {
        "analysis_price": 2504.76,
        "analysis_price_source": "latest_5m_bar",
        "ask": 2505.98,
        "ask_size": 20.0,
        "atlas_received_at": "2026-09-13T20:01:33.694462+00:00",
        "bid": 2505.3,
        "bid_size": 20.0,
        "broker_staleness_known": false,
        "cache": {
          "age_seconds": 0,
          "captured_at": "2026-09-13T20:01:33.694443+00:00",
          "source": "live",
          "stale": false
        },
        "live_ask": 2505.98,
        "live_bid": 2505.3,
        "live_executable_market_entry": null,
        "live_executable_market_entry_is_authorization": false,
        "live_executable_market_entry_side": null,
        "live_mid": 2505.6400000000003,
        "market_entry_price_policy": "LONG market execution evaluates live ask; SHORT market execution evaluates live bid. Structural or pending entry_reference remains context and must be reassessed before approval.",
        "price_semantics": "analysis_price is the latest 5M bar/reference price, not an executable quote. live_bid and live_ask are current TradeLocker quote values; live_mid is their midpoint. For market-entry evaluation use live_ask for LONG and live_bid for SHORT.",
        "quote_age_seconds": null,
        "quote_error": null,
        "quote_note": "Bid/ask values are live TradeLocker quote values. The broker response does not currently expose a quote timestamp, so broker quote age/staleness is left null rather than estimated.",
        "quote_timestamp": null,
        "quotes_available": true,
        "raw_quote": {
          "d": {
            "ap": 2505.98,
            "as": 20.0,
            "bp": 2505.3,
            "bs": 20.0
          },
          "s": "ok"
        },
        "spread": 0.6799999999998363
      },
      "symbol": "ETHUSD",
      "timeframes": {
        "15M": {
          "candle_count": 192,
          "candle_status": {
            "data_age_seconds": 992,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789328700000,
            "latest_timestamp_utc": "2026-09-13T19:45:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 900
          },
          "candles": [
            {
              "close": 2543.13,
              "high": 2545.95,
              "low": 2536.27,
              "open": 2537.96,
              "timestamp": 1789156800000,
              "volume": 4472.0
            },
            {
              "close": 2535.05,
              "high": 2543.13,
              "low": 2534.06,
              "open": 2543.13,
              "timestamp": 1789157700000,
              "volume": 4482.0
            },
            {
              "close": 2535.85,
              "high": 2540.25,
              "low": 2524.35,
              "open": 2535.05,
              "timestamp": 1789158600000,
              "volume": 4490.0
            },
            {
              "close": 2529.07,
              "high": 2536.43,
              "low": 2521.25,
              "open": 2535.85,
              "timestamp": 1789159500000,
              "volume": 4489.0
            },
            {
              "close": 2537.76,
              "high": 2539.17,
              "low": 2528.83,
              "open": 2529.07,
              "timestamp": 1789160400000,
              "volume": 3305.0
            },
            {
              "close": 2534.43,
              "high": 2539.1,
              "low": 2534.39,
              "open": 2537.76,
              "timestamp": 1789161300000,
              "volume": 4473.0
            },
            {
              "close": 2533.43,
              "high": 2537.12,
              "low": 2532.6,
              "open": 2534.43,
              "timestamp": 1789162200000,
              "volume": 4476.0
            },
            {
              "close": 2514.74,
              "high": 2534.3,
              "low": 2511.79,
              "open": 2533.43,
              "timestamp": 1789163100000,
              "volume": 4479.0
            },
            {
              "close": 2518.55,
              "high": 2518.74,
              "low": 2504.35,
              "open": 2514.74,
              "timestamp": 1789164000000,
              "volume": 3875.0
            },
            {
              "close": 2516.69,
              "high": 2522.15,
              "low": 2515.2,
              "open": 2518.55,
              "timestamp": 1789164900000,
              "volume": 4477.0
            },
            {
              "close": 2515.91,
              "high": 2521.37,
              "low": 2508.41,
              "open": 2516.39,
              "timestamp": 1789165800000,
              "volume": 4478.0
            },
            {
              "close": 2510.31,
              "high": 2515.91,
              "low": 2505.43,
              "open": 2515.91,
              "timestamp": 1789166700000,
              "volume": 4471.0
            },
            {
              "close": 2511.66,
              "high": 2513.47,
              "low": 2507.67,
              "open": 2510.31,
              "timestamp": 1789167600000,
              "volume": 4473.0
            },
            {
              "close": 2510.61,
              "high": 2513.83,
              "low": 2508.05,
              "open": 2511.66,
              "timestamp": 1789168500000,
              "volume": 4472.0
            },
            {
              "close": 2509.68,
              "high": 2512.85,
              "low": 2509.45,
              "open": 2510.61,
              "timestamp": 1789169400000,
              "volume": 4474.0
            },
            {
              "close": 2515.13,
              "high": 2515.26,
              "low": 2509.67,
              "open": 2509.68,
              "timestamp": 1789170300000,
              "volume": 4478.0
            },
            {
              "close": 2515.66,
              "high": 2516.39,
              "low": 2509.93,
              "open": 2515.13,
              "timestamp": 1789171200000,
              "volume": 4474.0
            },
            {
              "close": 2513.82,
              "high": 2516.32,
              "low": 2513.59,
              "open": 2515.66,
              "timestamp": 1789172100000,
              "volume": 4473.0
            },
            {
              "close": 2511.93,
              "high": 2513.82,
              "low": 2511.23,
              "open": 2513.82,
              "timestamp": 1789173000000,
              "volume": 4476.0
            },
            {
              "close": 2509.16,
              "high": 2512.25,
              "low": 2509.14,
              "open": 2511.93,
              "timestamp": 1789173900000,
              "volume": 4475.0
            },
            {
              "close": 2514.63,
              "high": 2514.66,
              "low": 2507.97,
              "open": 2509.16,
              "timestamp": 1789174800000,
              "volume": 4473.0
            },
            {
              "close": 2512.78,
              "high": 2515.79,
              "low": 2510.71,
              "open": 2514.63,
              "timestamp": 1789175700000,
              "volume": 4476.0
            },
            {
              "close": 2512.16,
              "high": 2514.14,
              "low": 2510.15,
              "open": 2512.78,
              "timestamp": 1789176600000,
              "volume": 4481.0
            },
            {
              "close": 2512.13,
              "high": 2515.29,
              "low": 2511.18,
              "open": 2512.16,
              "timestamp": 1789177500000,
              "volume": 4486.0
            },
            {
              "close": 2511.79,
              "high": 2514.39,
              "low": 2511.27,
              "open": 2512.13,
              "timestamp": 1789178400000,
              "volume": 4482.0
            },
            {
              "close": 2512.78,
              "high": 2513.92,
              "low": 2511.36,
              "open": 2511.79,
              "timestamp": 1789179300000,
              "volume": 4475.0
            },
            {
              "close": 2512.28,
              "high": 2514.31,
              "low": 2511.13,
              "open": 2512.78,
              "timestamp": 1789180200000,
              "volume": 4477.0
            },
            {
              "close": 2512.83,
              "high": 2513.77,
              "low": 2510.85,
              "open": 2512.28,
              "timestamp": 1789181100000,
              "volume": 4482.0
            },
            {
              "close": 2512.05,
              "high": 2514.56,
              "low": 2510.21,
              "open": 2512.77,
              "timestamp": 1789182000000,
              "volume": 4483.0
            },
            {
              "close": 2511.86,
              "high": 2514.33,
              "low": 2507.77,
              "open": 2512.05,
              "timestamp": 1789182900000,
              "volume": 4482.0
            },
            {
              "close": 2511.41,
              "high": 2512.12,
              "low": 2510.22,
              "open": 2511.86,
              "timestamp": 1789183800000,
              "volume": 4472.0
            },
            {
              "close": 2511.65,
              "high": 2512.3,
              "low": 2509.97,
              "open": 2511.41,
              "timestamp": 1789184700000,
              "volume": 4474.0
            },
            {
              "close": 2511.33,
              "high": 2512.25,
              "low": 2511.01,
              "open": 2511.65,
              "timestamp": 1789185600000,
              "volume": 4481.0
            },
            {
              "close": 2510.83,
              "high": 2512.04,
              "low": 2508.25,
              "open": 2511.33,
              "timestamp": 1789186500000,
              "volume": 4480.0
            },
            {
              "close": 2511.74,
              "high": 2513.63,
              "low": 2510.83,
              "open": 2510.83,
              "timestamp": 1789187400000,
              "volume": 4481.0
            },
            {
              "close": 2511.17,
              "high": 2512.05,
              "low": 2510.56,
              "open": 2511.74,
              "timestamp": 1789188300000,
              "volume": 4476.0
            },
            {
              "close": 2509.45,
              "high": 2511.23,
              "low": 2508.97,
              "open": 2511.17,
              "timestamp": 1789189200000,
              "volume": 4482.0
            },
            {
              "close": 2508.0,
              "high": 2511.15,
              "low": 2507.75,
              "open": 2509.45,
              "timestamp": 1789190100000,
              "volume": 4483.0
            },
            {
              "close": 2510.1,
              "high": 2511.63,
              "low": 2507.27,
              "open": 2508.0,
              "timestamp": 1789191000000,
              "volume": 4481.0
            },
            {
              "close": 2510.27,
              "high": 2511.2,
              "low": 2510.04,
              "open": 2510.1,
              "timestamp": 1789191900000,
              "volume": 4477.0
            },
            {
              "close": 2509.2,
              "high": 2510.58,
              "low": 2508.88,
              "open": 2510.27,
              "timestamp": 1789192800000,
              "volume": 4475.0
            },
            {
              "close": 2510.78,
              "high": 2511.66,
              "low": 2509.07,
              "open": 2509.2,
              "timestamp": 1789193700000,
              "volume": 4482.0
            },
            {
              "close": 2517.24,
              "high": 2517.35,
              "low": 2510.78,
              "open": 2510.78,
              "timestamp": 1789194600000,
              "volume": 4478.0
            },
            {
              "close": 2517.87,
              "high": 2520.94,
              "low": 2516.67,
              "open": 2517.24,
              "timestamp": 1789195500000,
              "volume": 4480.0
            },
            {
              "close": 2522.88,
              "high": 2523.4,
              "low": 2517.87,
              "open": 2517.87,
              "timestamp": 1789196400000,
              "volume": 4480.0
            },
            {
              "close": 2521.5,
              "high": 2523.04,
              "low": 2520.67,
              "open": 2522.88,
              "timestamp": 1789197300000,
              "volume": 4485.0
            },
            {
              "close": 2521.78,
              "high": 2522.07,
              "low": 2520.73,
              "open": 2521.5,
              "timestamp": 1789198200000,
              "volume": 4478.0
            },
            {
              "close": 2522.66,
              "high": 2523.09,
              "low": 2520.83,
              "open": 2521.78,
              "timestamp": 1789199100000,
              "volume": 4479.0
            },
            {
              "close": 2524.44,
              "high": 2526.99,
              "low": 2521.67,
              "open": 2522.66,
              "timestamp": 1789200000000,
              "volume": 4472.0
            },
            {
              "close": 2527.52,
              "high": 2528.21,
              "low": 2524.27,
              "open": 2524.44,
              "timestamp": 1789200900000,
              "volume": 4479.0
            },
            {
              "close": 2531.19,
              "high": 2531.87,
              "low": 2526.18,
              "open": 2527.52,
              "timestamp": 1789201800000,
              "volume": 4477.0
            },
            {
              "close": 2531.96,
              "high": 2534.88,
              "low": 2530.93,
              "open": 2531.19,
              "timestamp": 1789202700000,
              "volume": 4476.0
            },
            {
              "close": 2533.76,
              "high": 2535.3,
              "low": 2530.67,
              "open": 2531.96,
              "timestamp": 1789203600000,
              "volume": 4478.0
            },
            {
              "close": 2534.46,
              "high": 2535.84,
              "low": 2531.3,
              "open": 2533.76,
              "timestamp": 1789204500000,
              "volume": 4475.0
            },
            {
              "close": 2530.9,
              "high": 2535.85,
              "low": 2530.33,
              "open": 2534.46,
              "timestamp": 1789205400000,
              "volume": 4490.0
            },
            {
              "close": 2529.66,
              "high": 2531.51,
              "low": 2527.84,
              "open": 2530.9,
              "timestamp": 1789206300000,
              "volume": 4488.0
            },
            {
              "close": 2532.67,
              "high": 2534.99,
              "low": 2529.66,
              "open": 2529.66,
              "timestamp": 1789207200000,
              "volume": 4490.0
            },
            {
              "close": 2530.69,
              "high": 2532.67,
              "low": 2530.5,
              "open": 2532.67,
              "timestamp": 1789208100000,
              "volume": 4483.0
            },
            {
              "close": 2531.89,
              "high": 2532.2,
              "low": 2529.95,
              "open": 2530.69,
              "timestamp": 1789209000000,
              "volume": 4479.0
            },
            {
              "close": 2532.18,
              "high": 2533.38,
              "low": 2530.0,
              "open": 2531.89,
              "timestamp": 1789209900000,
              "volume": 4485.0
            },
            {
              "close": 2530.67,
              "high": 2533.83,
              "low": 2529.83,
              "open": 2532.18,
              "timestamp": 1789210800000,
              "volume": 4487.0
            },
            {
              "close": 2531.41,
              "high": 2531.66,
              "low": 2529.51,
              "open": 2530.67,
              "timestamp": 1789211700000,
              "volume": 4481.0
            },
            {
              "close": 2535.42,
              "high": 2535.6,
              "low": 2531.41,
              "open": 2531.41,
              "timestamp": 1789212600000,
              "volume": 4485.0
            },
            {
              "close": 2534.87,
              "high": 2535.77,
              "low": 2534.01,
              "open": 2535.42,
              "timestamp": 1789213500000,
              "volume": 4488.0
            },
            {
              "close": 2532.66,
              "high": 2534.87,
              "low": 2532.25,
              "open": 2534.87,
              "timestamp": 1789214400000,
              "volume": 4482.0
            },
            {
              "close": 2532.22,
              "high": 2533.64,
              "low": 2531.68,
              "open": 2532.66,
              "timestamp": 1789215300000,
              "volume": 4482.0
            },
            {
              "close": 2533.03,
              "high": 2534.87,
              "low": 2531.68,
              "open": 2532.22,
              "timestamp": 1789216200000,
              "volume": 4480.0
            },
            {
              "close": 2534.06,
              "high": 2534.73,
              "low": 2530.39,
              "open": 2533.03,
              "timestamp": 1789217100000,
              "volume": 4484.0
            },
            {
              "close": 2537.67,
              "high": 2544.01,
              "low": 2531.99,
              "open": 2534.06,
              "timestamp": 1789218000000,
              "volume": 4482.0
            },
            {
              "close": 2539.35,
              "high": 2540.65,
              "low": 2535.07,
              "open": 2537.67,
              "timestamp": 1789218900000,
              "volume": 4479.0
            },
            {
              "close": 2537.06,
              "high": 2540.0,
              "low": 2536.27,
              "open": 2539.35,
              "timestamp": 1789219800000,
              "volume": 4484.0
            },
            {
              "close": 2543.29,
              "high": 2544.7,
              "low": 2536.07,
              "open": 2537.06,
              "timestamp": 1789220700000,
              "volume": 4484.0
            },
            {
              "close": 2539.86,
              "high": 2544.06,
              "low": 2539.31,
              "open": 2543.29,
              "timestamp": 1789221600000,
              "volume": 4484.0
            },
            {
              "close": 2541.17,
              "high": 2542.22,
              "low": 2539.4,
              "open": 2539.86,
              "timestamp": 1789222500000,
              "volume": 4478.0
            },
            {
              "close": 2538.23,
              "high": 2543.16,
              "low": 2537.72,
              "open": 2541.17,
              "timestamp": 1789223400000,
              "volume": 4471.0
            },
            {
              "close": 2538.45,
              "high": 2540.48,
              "low": 2537.88,
              "open": 2538.23,
              "timestamp": 1789224300000,
              "volume": 4476.0
            },
            {
              "close": 2538.83,
              "high": 2539.58,
              "low": 2536.03,
              "open": 2538.52,
              "timestamp": 1789225200000,
              "volume": 4472.0
            },
            {
              "close": 2538.67,
              "high": 2541.22,
              "low": 2537.68,
              "open": 2538.83,
              "timestamp": 1789226100000,
              "volume": 4469.0
            },
            {
              "close": 2533.68,
              "high": 2539.34,
              "low": 2530.38,
              "open": 2538.67,
              "timestamp": 1789227000000,
              "volume": 4477.0
            },
            {
              "close": 2533.66,
              "high": 2535.14,
              "low": 2530.72,
              "open": 2533.68,
              "timestamp": 1789227900000,
              "volume": 4478.0
            },
            {
              "close": 2533.72,
              "high": 2534.98,
              "low": 2531.03,
              "open": 2533.66,
              "timestamp": 1789228800000,
              "volume": 4477.0
            },
            {
              "close": 2531.21,
              "high": 2533.96,
              "low": 2531.03,
              "open": 2533.72,
              "timestamp": 1789229700000,
              "volume": 4476.0
            },
            {
              "close": 2529.19,
              "high": 2531.62,
              "low": 2529.19,
              "open": 2531.21,
              "timestamp": 1789230600000,
              "volume": 4480.0
            },
            {
              "close": 2530.35,
              "high": 2531.65,
              "low": 2528.85,
              "open": 2529.19,
              "timestamp": 1789231500000,
              "volume": 4471.0
            },
            {
              "close": 2530.35,
              "high": 2533.16,
              "low": 2529.37,
              "open": 2530.35,
              "timestamp": 1789232400000,
              "volume": 4470.0
            },
            {
              "close": 2526.34,
              "high": 2532.24,
              "low": 2525.81,
              "open": 2530.35,
              "timestamp": 1789233300000,
              "volume": 4475.0
            },
            {
              "close": 2525.52,
              "high": 2526.74,
              "low": 2523.41,
              "open": 2526.34,
              "timestamp": 1789234200000,
              "volume": 4480.0
            },
            {
              "close": 2524.6,
              "high": 2525.52,
              "low": 2523.72,
              "open": 2525.52,
              "timestamp": 1789235100000,
              "volume": 4471.0
            },
            {
              "close": 2522.61,
              "high": 2526.17,
              "low": 2522.18,
              "open": 2524.6,
              "timestamp": 1789236000000,
              "volume": 4474.0
            },
            {
              "close": 2523.54,
              "high": 2526.02,
              "low": 2520.9,
              "open": 2522.61,
              "timestamp": 1789236900000,
              "volume": 4471.0
            },
            {
              "close": 2522.79,
              "high": 2524.58,
              "low": 2519.83,
              "open": 2523.54,
              "timestamp": 1789237800000,
              "volume": 4477.0
            },
            {
              "close": 2521.24,
              "high": 2522.91,
              "low": 2519.12,
              "open": 2522.79,
              "timestamp": 1789238700000,
              "volume": 4478.0
            },
            {
              "close": 2521.16,
              "high": 2521.77,
              "low": 2518.15,
              "open": 2521.24,
              "timestamp": 1789239600000,
              "volume": 4484.0
            },
            {
              "close": 2518.29,
              "high": 2521.16,
              "low": 2517.91,
              "open": 2521.16,
              "timestamp": 1789240500000,
              "volume": 4475.0
            },
            {
              "close": 2514.03,
              "high": 2518.91,
              "low": 2513.47,
              "open": 2518.29,
              "timestamp": 1789241400000,
              "volume": 4479.0
            },
            {
              "close": 2517.82,
              "high": 2517.98,
              "low": 2513.85,
              "open": 2514.03,
              "timestamp": 1789242300000,
              "volume": 4475.0
            },
            {
              "close": 2520.81,
              "high": 2521.01,
              "low": 2517.81,
              "open": 2517.82,
              "timestamp": 1789243200000,
              "volume": 4475.0
            },
            {
              "close": 2521.35,
              "high": 2522.17,
              "low": 2519.45,
              "open": 2520.81,
              "timestamp": 1789244100000,
              "volume": 4474.0
            },
            {
              "close": 2520.79,
              "high": 2521.68,
              "low": 2519.6,
              "open": 2521.35,
              "timestamp": 1789245000000,
              "volume": 4472.0
            },
            {
              "close": 2519.11,
              "high": 2521.99,
              "low": 2518.79,
              "open": 2520.79,
              "timestamp": 1789245900000,
              "volume": 4479.0
            },
            {
              "close": 2524.39,
              "high": 2527.14,
              "low": 2518.48,
              "open": 2519.11,
              "timestamp": 1789246800000,
              "volume": 3481.0
            },
            {
              "close": 2523.34,
              "high": 2524.44,
              "low": 2521.7,
              "open": 2524.44,
              "timestamp": 1789247700000,
              "volume": 4470.0
            },
            {
              "close": 2522.32,
              "high": 2524.53,
              "low": 2521.97,
              "open": 2523.34,
              "timestamp": 1789248600000,
              "volume": 4473.0
            },
            {
              "close": 2522.68,
              "high": 2523.42,
              "low": 2520.89,
              "open": 2522.32,
              "timestamp": 1789249500000,
              "volume": 4470.0
            },
            {
              "close": 2522.22,
              "high": 2523.17,
              "low": 2520.02,
              "open": 2522.68,
              "timestamp": 1789250400000,
              "volume": 4471.0
            },
            {
              "close": 2519.33,
              "high": 2524.77,
              "low": 2519.33,
              "open": 2522.22,
              "timestamp": 1789251300000,
              "volume": 4477.0
            },
            {
              "close": 2520.2,
              "high": 2521.42,
              "low": 2518.7,
              "open": 2519.33,
              "timestamp": 1789252200000,
              "volume": 4466.0
            },
            {
              "close": 2521.45,
              "high": 2521.88,
              "low": 2520.18,
              "open": 2520.2,
              "timestamp": 1789253100000,
              "volume": 4469.0
            },
            {
              "close": 2523.23,
              "high": 2523.34,
              "low": 2521.0,
              "open": 2521.45,
              "timestamp": 1789254000000,
              "volume": 4478.0
            },
            {
              "close": 2523.25,
              "high": 2523.84,
              "low": 2522.53,
              "open": 2523.23,
              "timestamp": 1789254900000,
              "volume": 4476.0
            },
            {
              "close": 2523.81,
              "high": 2524.26,
              "low": 2522.75,
              "open": 2523.25,
              "timestamp": 1789255800000,
              "volume": 4473.0
            },
            {
              "close": 2524.43,
              "high": 2525.42,
              "low": 2523.81,
              "open": 2523.81,
              "timestamp": 1789256700000,
              "volume": 4467.0
            },
            {
              "close": 2523.5,
              "high": 2526.07,
              "low": 2523.5,
              "open": 2524.07,
              "timestamp": 1789257600000,
              "volume": 4172.0
            },
            {
              "close": 2524.08,
              "high": 2525.21,
              "low": 2523.48,
              "open": 2523.5,
              "timestamp": 1789258500000,
              "volume": 4476.0
            },
            {
              "close": 2522.67,
              "high": 2524.81,
              "low": 2521.78,
              "open": 2524.08,
              "timestamp": 1789259400000,
              "volume": 4474.0
            },
            {
              "close": 2523.89,
              "high": 2524.54,
              "low": 2522.67,
              "open": 2522.67,
              "timestamp": 1789260300000,
              "volume": 4472.0
            },
            {
              "close": 2523.67,
              "high": 2524.82,
              "low": 2522.36,
              "open": 2523.89,
              "timestamp": 1789261200000,
              "volume": 4478.0
            },
            {
              "close": 2523.14,
              "high": 2526.37,
              "low": 2522.08,
              "open": 2523.67,
              "timestamp": 1789262100000,
              "volume": 4475.0
            },
            {
              "close": 2523.77,
              "high": 2524.42,
              "low": 2520.96,
              "open": 2523.14,
              "timestamp": 1789263000000,
              "volume": 4478.0
            },
            {
              "close": 2524.48,
              "high": 2524.87,
              "low": 2523.44,
              "open": 2523.77,
              "timestamp": 1789263900000,
              "volume": 4471.0
            },
            {
              "close": 2521.77,
              "high": 2524.48,
              "low": 2521.33,
              "open": 2524.48,
              "timestamp": 1789264800000,
              "volume": 4474.0
            },
            {
              "close": 2520.98,
              "high": 2521.92,
              "low": 2520.37,
              "open": 2521.77,
              "timestamp": 1789265700000,
              "volume": 4475.0
            },
            {
              "close": 2521.79,
              "high": 2522.11,
              "low": 2519.68,
              "open": 2520.98,
              "timestamp": 1789266600000,
              "volume": 4479.0
            },
            {
              "close": 2520.15,
              "high": 2522.25,
              "low": 2520.07,
              "open": 2521.79,
              "timestamp": 1789267500000,
              "volume": 4472.0
            },
            {
              "close": 2519.43,
              "high": 2521.62,
              "low": 2518.67,
              "open": 2520.15,
              "timestamp": 1789268400000,
              "volume": 4477.0
            },
            {
              "close": 2519.58,
              "high": 2520.97,
              "low": 2518.76,
              "open": 2519.43,
              "timestamp": 1789269300000,
              "volume": 4476.0
            },
            {
              "close": 2520.59,
              "high": 2520.59,
              "low": 2517.9,
              "open": 2519.58,
              "timestamp": 1789270200000,
              "volume": 4481.0
            },
            {
              "close": 2519.42,
              "high": 2521.42,
              "low": 2518.5,
              "open": 2520.59,
              "timestamp": 1789271100000,
              "volume": 4474.0
            },
            {
              "close": 2520.14,
              "high": 2522.07,
              "low": 2518.8,
              "open": 2519.42,
              "timestamp": 1789272000000,
              "volume": 4476.0
            },
            {
              "close": 2521.63,
              "high": 2522.1,
              "low": 2520.14,
              "open": 2520.14,
              "timestamp": 1789272900000,
              "volume": 4479.0
            },
            {
              "close": 2518.73,
              "high": 2521.63,
              "low": 2517.8,
              "open": 2521.63,
              "timestamp": 1789273800000,
              "volume": 4474.0
            },
            {
              "close": 2518.89,
              "high": 2519.33,
              "low": 2518.14,
              "open": 2518.73,
              "timestamp": 1789274700000,
              "volume": 4477.0
            },
            {
              "close": 2520.72,
              "high": 2520.89,
              "low": 2518.89,
              "open": 2518.89,
              "timestamp": 1789275600000,
              "volume": 4475.0
            },
            {
              "close": 2521.37,
              "high": 2521.68,
              "low": 2519.69,
              "open": 2520.72,
              "timestamp": 1789276500000,
              "volume": 4478.0
            },
            {
              "close": 2521.99,
              "high": 2522.89,
              "low": 2521.27,
              "open": 2521.37,
              "timestamp": 1789277400000,
              "volume": 4475.0
            },
            {
              "close": 2521.17,
              "high": 2522.59,
              "low": 2521.17,
              "open": 2521.99,
              "timestamp": 1789278300000,
              "volume": 4474.0
            },
            {
              "close": 2521.12,
              "high": 2521.64,
              "low": 2520.92,
              "open": 2521.26,
              "timestamp": 1789279200000,
              "volume": 4478.0
            },
            {
              "close": 2520.19,
              "high": 2521.12,
              "low": 2519.73,
              "open": 2521.12,
              "timestamp": 1789280100000,
              "volume": 4472.0
            },
            {
              "close": 2518.23,
              "high": 2520.3,
              "low": 2516.95,
              "open": 2520.19,
              "timestamp": 1789281000000,
              "volume": 4474.0
            },
            {
              "close": 2511.39,
              "high": 2518.15,
              "low": 2508.05,
              "open": 2518.15,
              "timestamp": 1789281900000,
              "volume": 4483.0
            },
            {
              "close": 2513.46,
              "high": 2513.95,
              "low": 2510.32,
              "open": 2511.39,
              "timestamp": 1789282800000,
              "volume": 4475.0
            },
            {
              "close": 2513.99,
              "high": 2514.2,
              "low": 2512.03,
              "open": 2513.46,
              "timestamp": 1789283700000,
              "volume": 4480.0
            },
            {
              "close": 2518.28,
              "high": 2518.83,
              "low": 2512.51,
              "open": 2513.99,
              "timestamp": 1789284600000,
              "volume": 4473.0
            },
            {
              "close": 2516.28,
              "high": 2518.64,
              "low": 2515.67,
              "open": 2518.28,
              "timestamp": 1789285500000,
              "volume": 4478.0
            },
            {
              "close": 2513.64,
              "high": 2518.16,
              "low": 2511.01,
              "open": 2516.28,
              "timestamp": 1789286400000,
              "volume": 4480.0
            },
            {
              "close": 2508.95,
              "high": 2513.64,
              "low": 2508.68,
              "open": 2513.64,
              "timestamp": 1789287300000,
              "volume": 4475.0
            },
            {
              "close": 2491.59,
              "high": 2508.95,
              "low": 2486.16,
              "open": 2508.95,
              "timestamp": 1789288200000,
              "volume": 4479.0
            },
            {
              "close": 2492.91,
              "high": 2495.33,
              "low": 2490.53,
              "open": 2491.59,
              "timestamp": 1789289100000,
              "volume": 4475.0
            },
            {
              "close": 2491.49,
              "high": 2496.01,
              "low": 2491.17,
              "open": 2492.91,
              "timestamp": 1789290000000,
              "volume": 4477.0
            },
            {
              "close": 2480.17,
              "high": 2493.26,
              "low": 2473.87,
              "open": 2491.49,
              "timestamp": 1789290900000,
              "volume": 4479.0
            },
            {
              "close": 2479.03,
              "high": 2483.32,
              "low": 2469.23,
              "open": 2480.11,
              "timestamp": 1789291800000,
              "volume": 4481.0
            },
            {
              "close": 2483.35,
              "high": 2484.06,
              "low": 2477.91,
              "open": 2479.03,
              "timestamp": 1789292700000,
              "volume": 4478.0
            },
            {
              "close": 2481.66,
              "high": 2484.63,
              "low": 2480.64,
              "open": 2483.35,
              "timestamp": 1789293600000,
              "volume": 4478.0
            },
            {
              "close": 2478.28,
              "high": 2482.19,
              "low": 2478.24,
              "open": 2481.66,
              "timestamp": 1789294500000,
              "volume": 4478.0
            },
            {
              "close": 2473.66,
              "high": 2482.05,
              "low": 2471.76,
              "open": 2478.28,
              "timestamp": 1789295400000,
              "volume": 4476.0
            },
            {
              "close": 2470.75,
              "high": 2477.2,
              "low": 2466.29,
              "open": 2473.66,
              "timestamp": 1789296300000,
              "volume": 4479.0
            },
            {
              "close": 2468.16,
              "high": 2476.22,
              "low": 2466.17,
              "open": 2470.75,
              "timestamp": 1789297200000,
              "volume": 4475.0
            },
            {
              "close": 2473.62,
              "high": 2474.76,
              "low": 2468.16,
              "open": 2468.16,
              "timestamp": 1789298100000,
              "volume": 4479.0
            },
            {
              "close": 2478.81,
              "high": 2478.81,
              "low": 2471.96,
              "open": 2473.62,
              "timestamp": 1789299000000,
              "volume": 4472.0
            },
            {
              "close": 2479.79,
              "high": 2481.03,
              "low": 2477.7,
              "open": 2478.81,
              "timestamp": 1789299900000,
              "volume": 4479.0
            },
            {
              "close": 2479.9,
              "high": 2480.61,
              "low": 2477.34,
              "open": 2479.79,
              "timestamp": 1789300800000,
              "volume": 4477.0
            },
            {
              "close": 2479.03,
              "high": 2481.88,
              "low": 2479.03,
              "open": 2479.9,
              "timestamp": 1789301700000,
              "volume": 4480.0
            },
            {
              "close": 2474.67,
              "high": 2481.06,
              "low": 2473.37,
              "open": 2479.03,
              "timestamp": 1789302600000,
              "volume": 4476.0
            },
            {
              "close": 2475.87,
              "high": 2476.7,
              "low": 2473.48,
              "open": 2474.67,
              "timestamp": 1789303500000,
              "volume": 4480.0
            },
            {
              "close": 2475.82,
              "high": 2476.56,
              "low": 2471.44,
              "open": 2475.87,
              "timestamp": 1789304400000,
              "volume": 4478.0
            },
            {
              "close": 2465.61,
              "high": 2475.82,
              "low": 2460.37,
              "open": 2475.82,
              "timestamp": 1789305300000,
              "volume": 4474.0
            },
            {
              "close": 2474.42,
              "high": 2474.85,
              "low": 2465.42,
              "open": 2465.61,
              "timestamp": 1789306200000,
              "volume": 4481.0
            },
            {
              "close": 2477.5,
              "high": 2481.06,
              "low": 2474.42,
              "open": 2474.42,
              "timestamp": 1789307100000,
              "volume": 4479.0
            },
            {
              "close": 2483.55,
              "high": 2483.55,
              "low": 2477.16,
              "open": 2477.5,
              "timestamp": 1789308000000,
              "volume": 4481.0
            },
            {
              "close": 2488.77,
              "high": 2490.66,
              "low": 2483.44,
              "open": 2483.55,
              "timestamp": 1789308900000,
              "volume": 4480.0
            },
            {
              "close": 2491.09,
              "high": 2493.39,
              "low": 2487.31,
              "open": 2488.77,
              "timestamp": 1789309800000,
              "volume": 4478.0
            },
            {
              "close": 2490.96,
              "high": 2494.06,
              "low": 2488.49,
              "open": 2491.09,
              "timestamp": 1789310700000,
              "volume": 4478.0
            },
            {
              "close": 2486.2,
              "high": 2491.14,
              "low": 2483.67,
              "open": 2490.96,
              "timestamp": 1789311600000,
              "volume": 4483.0
            },
            {
              "close": 2485.35,
              "high": 2490.22,
              "low": 2481.37,
              "open": 2486.2,
              "timestamp": 1789312500000,
              "volume": 4477.0
            },
            {
              "close": 2489.0,
              "high": 2489.66,
              "low": 2485.35,
              "open": 2485.35,
              "timestamp": 1789313400000,
              "volume": 4477.0
            },
            {
              "close": 2489.22,
              "high": 2489.86,
              "low": 2487.59,
              "open": 2489.0,
              "timestamp": 1789314300000,
              "volume": 4479.0
            },
            {
              "close": 2499.17,
              "high": 2503.33,
              "low": 2488.85,
              "open": 2489.22,
              "timestamp": 1789315200000,
              "volume": 4480.0
            },
            {
              "close": 2501.05,
              "high": 2502.32,
              "low": 2496.42,
              "open": 2499.17,
              "timestamp": 1789316100000,
              "volume": 4481.0
            },
            {
              "close": 2502.35,
              "high": 2503.68,
              "low": 2498.46,
              "open": 2501.05,
              "timestamp": 1789317000000,
              "volume": 4480.0
            },
            {
              "close": 2503.11,
              "high": 2504.62,
              "low": 2500.6,
              "open": 2502.35,
              "timestamp": 1789317900000,
              "volume": 4475.0
            },
            {
              "close": 2507.74,
              "high": 2511.66,
              "low": 2502.64,
              "open": 2503.11,
              "timestamp": 1789318800000,
              "volume": 4479.0
            },
            {
              "close": 2504.22,
              "high": 2509.65,
              "low": 2503.96,
              "open": 2507.74,
              "timestamp": 1789319700000,
              "volume": 4478.0
            },
            {
              "close": 2502.38,
              "high": 2504.66,
              "low": 2501.38,
              "open": 2504.22,
              "timestamp": 1789320600000,
              "volume": 4478.0
            },
            {
              "close": 2503.65,
              "high": 2504.66,
              "low": 2502.38,
              "open": 2502.38,
              "timestamp": 1789321500000,
              "volume": 4478.0
            },
            {
              "close": 2505.08,
              "high": 2505.29,
              "low": 2502.97,
              "open": 2503.65,
              "timestamp": 1789322400000,
              "volume": 4478.0
            },
            {
              "close": 2504.88,
              "high": 2507.61,
              "low": 2504.31,
              "open": 2505.08,
              "timestamp": 1789323300000,
              "volume": 4479.0
            },
            {
              "close": 2507.18,
              "high": 2507.76,
              "low": 2504.88,
              "open": 2504.88,
              "timestamp": 1789324200000,
              "volume": 4476.0
            },
            {
              "close": 2508.01,
              "high": 2508.26,
              "low": 2506.9,
              "open": 2507.18,
              "timestamp": 1789325100000,
              "volume": 4479.0
            },
            {
              "close": 2507.61,
              "high": 2514.6,
              "low": 2507.37,
              "open": 2508.01,
              "timestamp": 1789326000000,
              "volume": 4485.0
            },
            {
              "close": 2506.74,
              "high": 2508.87,
              "low": 2504.88,
              "open": 2507.61,
              "timestamp": 1789326900000,
              "volume": 4479.0
            },
            {
              "close": 2504.03,
              "high": 2506.74,
              "low": 2501.98,
              "open": 2506.74,
              "timestamp": 1789327800000,
              "volume": 4474.0
            },
            {
              "close": 2504.76,
              "high": 2504.86,
              "low": 2502.9,
              "open": 2504.03,
              "timestamp": 1789328700000,
              "volume": 4473.0
            }
          ],
          "last_price": 2504.76,
          "momentum": "neutral",
          "rsi_14": 59.45,
          "structure": "bullish"
        },
        "1H": {
          "candle_count": 168,
          "candle_status": {
            "data_age_seconds": 3692,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789326000000,
            "latest_timestamp_utc": "2026-09-13T19:00:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 3600
          },
          "candles": [
            {
              "close": 2498.18,
              "high": 2498.98,
              "low": 2487.27,
              "open": 2489.3,
              "timestamp": 1788724800000,
              "volume": 17080.0
            },
            {
              "close": 2506.87,
              "high": 2514.56,
              "low": 2498.09,
              "open": 2498.18,
              "timestamp": 1788728400000,
              "volume": 17962.0
            },
            {
              "close": 2506.64,
              "high": 2509.47,
              "low": 2487.72,
              "open": 2506.87,
              "timestamp": 1788732000000,
              "volume": 17969.0
            },
            {
              "close": 2513.13,
              "high": 2525.1,
              "low": 2505.15,
              "open": 2506.64,
              "timestamp": 1788735600000,
              "volume": 17952.0
            },
            {
              "close": 2511.62,
              "high": 2521.29,
              "low": 2507.76,
              "open": 2513.13,
              "timestamp": 1788739200000,
              "volume": 17954.0
            },
            {
              "close": 2502.5,
              "high": 2515.06,
              "low": 2498.12,
              "open": 2511.66,
              "timestamp": 1788742800000,
              "volume": 17967.0
            },
            {
              "close": 2510.47,
              "high": 2535.21,
              "low": 2497.07,
              "open": 2502.5,
              "timestamp": 1788746400000,
              "volume": 17957.0
            },
            {
              "close": 2495.67,
              "high": 2514.63,
              "low": 2494.93,
              "open": 2510.47,
              "timestamp": 1788750000000,
              "volume": 17964.0
            },
            {
              "close": 2496.5,
              "high": 2498.22,
              "low": 2490.83,
              "open": 2495.67,
              "timestamp": 1788753600000,
              "volume": 17968.0
            },
            {
              "close": 2503.08,
              "high": 2512.62,
              "low": 2495.51,
              "open": 2496.5,
              "timestamp": 1788757200000,
              "volume": 17964.0
            },
            {
              "close": 2496.52,
              "high": 2508.82,
              "low": 2496.21,
              "open": 2503.08,
              "timestamp": 1788760800000,
              "volume": 17971.0
            },
            {
              "close": 2487.66,
              "high": 2500.75,
              "low": 2473.28,
              "open": 2496.52,
              "timestamp": 1788764400000,
              "volume": 17967.0
            },
            {
              "close": 2489.81,
              "high": 2492.36,
              "low": 2487.08,
              "open": 2487.66,
              "timestamp": 1788768000000,
              "volume": 17954.0
            },
            {
              "close": 2483.04,
              "high": 2495.93,
              "low": 2482.61,
              "open": 2489.81,
              "timestamp": 1788771600000,
              "volume": 17964.0
            },
            {
              "close": 2487.42,
              "high": 2490.91,
              "low": 2483.04,
              "open": 2483.04,
              "timestamp": 1788775200000,
              "volume": 17953.0
            },
            {
              "close": 2487.63,
              "high": 2492.03,
              "low": 2484.96,
              "open": 2487.42,
              "timestamp": 1788778800000,
              "volume": 17969.0
            },
            {
              "close": 2504.05,
              "high": 2506.43,
              "low": 2487.22,
              "open": 2487.63,
              "timestamp": 1788782400000,
              "volume": 17949.0
            },
            {
              "close": 2497.53,
              "high": 2510.41,
              "low": 2494.24,
              "open": 2504.05,
              "timestamp": 1788786000000,
              "volume": 18002.0
            },
            {
              "close": 2488.74,
              "high": 2498.19,
              "low": 2474.84,
              "open": 2497.53,
              "timestamp": 1788789600000,
              "volume": 17984.0
            },
            {
              "close": 2468.43,
              "high": 2488.74,
              "low": 2464.77,
              "open": 2488.74,
              "timestamp": 1788793200000,
              "volume": 17988.0
            },
            {
              "close": 2481.42,
              "high": 2481.67,
              "low": 2468.38,
              "open": 2468.6,
              "timestamp": 1788796800000,
              "volume": 17955.0
            },
            {
              "close": 2493.98,
              "high": 2498.09,
              "low": 2480.64,
              "open": 2481.42,
              "timestamp": 1788800400000,
              "volume": 17966.0
            },
            {
              "close": 2490.35,
              "high": 2496.02,
              "low": 2485.91,
              "open": 2493.98,
              "timestamp": 1788804000000,
              "volume": 17962.0
            },
            {
              "close": 2494.34,
              "high": 2496.39,
              "low": 2487.76,
              "open": 2490.35,
              "timestamp": 1788807600000,
              "volume": 17973.0
            },
            {
              "close": 2493.81,
              "high": 2495.81,
              "low": 2485.69,
              "open": 2494.34,
              "timestamp": 1788811200000,
              "volume": 17965.0
            },
            {
              "close": 2489.74,
              "high": 2495.55,
              "low": 2488.89,
              "open": 2493.81,
              "timestamp": 1788814800000,
              "volume": 16750.0
            },
            {
              "close": 2481.35,
              "high": 2490.66,
              "low": 2474.11,
              "open": 2489.74,
              "timestamp": 1788818400000,
              "volume": 17372.0
            },
            {
              "close": 2488.58,
              "high": 2492.38,
              "low": 2480.65,
              "open": 2481.35,
              "timestamp": 1788822000000,
              "volume": 17985.0
            },
            {
              "close": 2494.16,
              "high": 2494.38,
              "low": 2481.68,
              "open": 2488.58,
              "timestamp": 1788825600000,
              "volume": 17983.0
            },
            {
              "close": 2502.99,
              "high": 2504.19,
              "low": 2491.82,
              "open": 2494.16,
              "timestamp": 1788829200000,
              "volume": 17982.0
            },
            {
              "close": 2483.09,
              "high": 2506.81,
              "low": 2483.09,
              "open": 2502.99,
              "timestamp": 1788832800000,
              "volume": 18001.0
            },
            {
              "close": 2484.57,
              "high": 2487.03,
              "low": 2476.34,
              "open": 2483.09,
              "timestamp": 1788836400000,
              "volume": 17981.0
            },
            {
              "close": 2477.47,
              "high": 2484.82,
              "low": 2477.08,
              "open": 2484.57,
              "timestamp": 1788840000000,
              "volume": 17988.0
            },
            {
              "close": 2471.9,
              "high": 2483.08,
              "low": 2471.05,
              "open": 2477.47,
              "timestamp": 1788843600000,
              "volume": 17965.0
            },
            {
              "close": 2466.95,
              "high": 2475.66,
              "low": 2461.26,
              "open": 2471.9,
              "timestamp": 1788847200000,
              "volume": 17909.0
            },
            {
              "close": 2477.99,
              "high": 2483.62,
              "low": 2466.33,
              "open": 2466.95,
              "timestamp": 1788850800000,
              "volume": 17962.0
            },
            {
              "close": 2476.42,
              "high": 2482.1,
              "low": 2467.42,
              "open": 2477.99,
              "timestamp": 1788854400000,
              "volume": 17965.0
            },
            {
              "close": 2490.49,
              "high": 2494.43,
              "low": 2474.05,
              "open": 2476.42,
              "timestamp": 1788858000000,
              "volume": 17959.0
            },
            {
              "close": 2479.77,
              "high": 2498.8,
              "low": 2479.55,
              "open": 2490.49,
              "timestamp": 1788861600000,
              "volume": 17893.0
            },
            {
              "close": 2473.02,
              "high": 2481.14,
              "low": 2469.88,
              "open": 2479.8,
              "timestamp": 1788865200000,
              "volume": 17963.0
            },
            {
              "close": 2471.33,
              "high": 2474.64,
              "low": 2466.04,
              "open": 2473.02,
              "timestamp": 1788868800000,
              "volume": 17975.0
            },
            {
              "close": 2458.03,
              "high": 2474.13,
              "low": 2439.89,
              "open": 2471.38,
              "timestamp": 1788872400000,
              "volume": 17984.0
            },
            {
              "close": 2484.48,
              "high": 2485.72,
              "low": 2455.36,
              "open": 2458.03,
              "timestamp": 1788876000000,
              "volume": 17979.0
            },
            {
              "close": 2497.44,
              "high": 2500.7,
              "low": 2480.0,
              "open": 2484.48,
              "timestamp": 1788879600000,
              "volume": 17958.0
            },
            {
              "close": 2495.39,
              "high": 2504.37,
              "low": 2485.47,
              "open": 2497.44,
              "timestamp": 1788883200000,
              "volume": 17953.0
            },
            {
              "close": 2486.97,
              "high": 2501.39,
              "low": 2486.37,
              "open": 2495.39,
              "timestamp": 1788886800000,
              "volume": 17963.0
            },
            {
              "close": 2485.35,
              "high": 2505.91,
              "low": 2474.57,
              "open": 2486.97,
              "timestamp": 1788890400000,
              "volume": 17839.0
            },
            {
              "close": 2480.64,
              "high": 2490.31,
              "low": 2474.9,
              "open": 2485.35,
              "timestamp": 1788894000000,
              "volume": 17957.0
            },
            {
              "close": 2481.62,
              "high": 2490.11,
              "low": 2478.85,
              "open": 2480.65,
              "timestamp": 1788897600000,
              "volume": 17952.0
            },
            {
              "close": 2481.62,
              "high": 2485.97,
              "low": 2477.14,
              "open": 2481.62,
              "timestamp": 1788901200000,
              "volume": 16742.0
            },
            {
              "close": 2487.74,
              "high": 2488.93,
              "low": 2480.22,
              "open": 2481.57,
              "timestamp": 1788904800000,
              "volume": 17348.0
            },
            {
              "close": 2483.54,
              "high": 2489.19,
              "low": 2481.34,
              "open": 2487.74,
              "timestamp": 1788908400000,
              "volume": 17932.0
            },
            {
              "close": 2495.2,
              "high": 2496.01,
              "low": 2483.73,
              "open": 2483.73,
              "timestamp": 1788912000000,
              "volume": 17966.0
            },
            {
              "close": 2496.39,
              "high": 2498.53,
              "low": 2487.75,
              "open": 2495.2,
              "timestamp": 1788915600000,
              "volume": 17973.0
            },
            {
              "close": 2492.31,
              "high": 2498.98,
              "low": 2488.22,
              "open": 2496.39,
              "timestamp": 1788919200000,
              "volume": 17963.0
            },
            {
              "close": 2487.45,
              "high": 2492.48,
              "low": 2485.08,
              "open": 2492.31,
              "timestamp": 1788922800000,
              "volume": 17959.0
            },
            {
              "close": 2508.35,
              "high": 2512.86,
              "low": 2487.45,
              "open": 2487.45,
              "timestamp": 1788926400000,
              "volume": 17957.0
            },
            {
              "close": 2495.12,
              "high": 2510.3,
              "low": 2489.71,
              "open": 2508.35,
              "timestamp": 1788930000000,
              "volume": 17978.0
            },
            {
              "close": 2499.72,
              "high": 2504.39,
              "low": 2491.12,
              "open": 2495.12,
              "timestamp": 1788933600000,
              "volume": 17943.0
            },
            {
              "close": 2509.16,
              "high": 2516.08,
              "low": 2498.37,
              "open": 2499.72,
              "timestamp": 1788937200000,
              "volume": 17965.0
            },
            {
              "close": 2518.66,
              "high": 2522.18,
              "low": 2509.06,
              "open": 2509.16,
              "timestamp": 1788940800000,
              "volume": 17969.0
            },
            {
              "close": 2488.79,
              "high": 2519.21,
              "low": 2488.79,
              "open": 2518.66,
              "timestamp": 1788944400000,
              "volume": 17966.0
            },
            {
              "close": 2485.97,
              "high": 2492.74,
              "low": 2480.84,
              "open": 2488.79,
              "timestamp": 1788948000000,
              "volume": 17966.0
            },
            {
              "close": 2499.53,
              "high": 2504.34,
              "low": 2480.66,
              "open": 2485.97,
              "timestamp": 1788951600000,
              "volume": 17959.0
            },
            {
              "close": 2510.32,
              "high": 2511.56,
              "low": 2497.15,
              "open": 2499.53,
              "timestamp": 1788955200000,
              "volume": 17956.0
            },
            {
              "close": 2501.11,
              "high": 2520.24,
              "low": 2498.53,
              "open": 2510.32,
              "timestamp": 1788958800000,
              "volume": 17970.0
            },
            {
              "close": 2497.82,
              "high": 2513.09,
              "low": 2493.78,
              "open": 2501.11,
              "timestamp": 1788962400000,
              "volume": 17994.0
            },
            {
              "close": 2488.63,
              "high": 2511.12,
              "low": 2468.76,
              "open": 2497.82,
              "timestamp": 1788966000000,
              "volume": 17359.0
            },
            {
              "close": 2494.5,
              "high": 2498.16,
              "low": 2483.32,
              "open": 2488.63,
              "timestamp": 1788969600000,
              "volume": 17961.0
            },
            {
              "close": 2492.21,
              "high": 2498.23,
              "low": 2487.26,
              "open": 2494.5,
              "timestamp": 1788973200000,
              "volume": 17967.0
            },
            {
              "close": 2479.82,
              "high": 2494.44,
              "low": 2479.67,
              "open": 2492.21,
              "timestamp": 1788976800000,
              "volume": 17957.0
            },
            {
              "close": 2463.98,
              "high": 2483.45,
              "low": 2461.04,
              "open": 2479.82,
              "timestamp": 1788980400000,
              "volume": 17978.0
            },
            {
              "close": 2470.03,
              "high": 2470.62,
              "low": 2452.55,
              "open": 2463.98,
              "timestamp": 1788984000000,
              "volume": 17944.0
            },
            {
              "close": 2460.24,
              "high": 2470.03,
              "low": 2454.82,
              "open": 2470.03,
              "timestamp": 1788987600000,
              "volume": 16655.0
            },
            {
              "close": 2448.79,
              "high": 2461.79,
              "low": 2441.85,
              "open": 2460.24,
              "timestamp": 1788991200000,
              "volume": 17370.0
            },
            {
              "close": 2466.63,
              "high": 2467.37,
              "low": 2448.54,
              "open": 2448.79,
              "timestamp": 1788994800000,
              "volume": 18034.0
            },
            {
              "close": 2463.43,
              "high": 2470.29,
              "low": 2461.19,
              "open": 2466.63,
              "timestamp": 1788998400000,
              "volume": 17998.0
            },
            {
              "close": 2462.67,
              "high": 2477.96,
              "low": 2453.99,
              "open": 2463.43,
              "timestamp": 1789002000000,
              "volume": 18036.0
            },
            {
              "close": 2473.66,
              "high": 2474.8,
              "low": 2458.67,
              "open": 2462.67,
              "timestamp": 1789005600000,
              "volume": 18017.0
            },
            {
              "close": 2474.01,
              "high": 2477.9,
              "low": 2470.64,
              "open": 2473.66,
              "timestamp": 1789009200000,
              "volume": 18003.0
            },
            {
              "close": 2477.36,
              "high": 2479.77,
              "low": 2473.46,
              "open": 2474.01,
              "timestamp": 1789012800000,
              "volume": 18009.0
            },
            {
              "close": 2480.77,
              "high": 2482.66,
              "low": 2472.46,
              "open": 2477.36,
              "timestamp": 1789016400000,
              "volume": 17997.0
            },
            {
              "close": 2478.92,
              "high": 2483.65,
              "low": 2470.23,
              "open": 2480.77,
              "timestamp": 1789020000000,
              "volume": 17999.0
            },
            {
              "close": 2471.16,
              "high": 2478.92,
              "low": 2462.26,
              "open": 2478.92,
              "timestamp": 1789023600000,
              "volume": 18028.0
            },
            {
              "close": 2469.85,
              "high": 2473.32,
              "low": 2467.52,
              "open": 2471.16,
              "timestamp": 1789027200000,
              "volume": 17991.0
            },
            {
              "close": 2467.32,
              "high": 2476.6,
              "low": 2463.0,
              "open": 2469.85,
              "timestamp": 1789030800000,
              "volume": 17987.0
            },
            {
              "close": 2462.75,
              "high": 2470.57,
              "low": 2461.27,
              "open": 2467.32,
              "timestamp": 1789034400000,
              "volume": 17990.0
            },
            {
              "close": 2460.7,
              "high": 2468.49,
              "low": 2456.82,
              "open": 2462.75,
              "timestamp": 1789038000000,
              "volume": 17996.0
            },
            {
              "close": 2413.36,
              "high": 2465.11,
              "low": 2406.85,
              "open": 2460.7,
              "timestamp": 1789041600000,
              "volume": 18019.0
            },
            {
              "close": 2433.53,
              "high": 2435.04,
              "low": 2403.68,
              "open": 2413.1,
              "timestamp": 1789045200000,
              "volume": 18026.0
            },
            {
              "close": 2441.96,
              "high": 2442.63,
              "low": 2425.41,
              "open": 2433.53,
              "timestamp": 1789048800000,
              "volume": 17827.0
            },
            {
              "close": 2439.67,
              "high": 2443.38,
              "low": 2430.71,
              "open": 2441.96,
              "timestamp": 1789052400000,
              "volume": 18028.0
            },
            {
              "close": 2447.29,
              "high": 2449.5,
              "low": 2430.41,
              "open": 2439.67,
              "timestamp": 1789056000000,
              "volume": 18024.0
            },
            {
              "close": 2464.51,
              "high": 2473.84,
              "low": 2445.55,
              "open": 2447.29,
              "timestamp": 1789059600000,
              "volume": 18030.0
            },
            {
              "close": 2467.03,
              "high": 2467.67,
              "low": 2453.47,
              "open": 2464.51,
              "timestamp": 1789063200000,
              "volume": 18000.0
            },
            {
              "close": 2461.13,
              "high": 2470.91,
              "low": 2458.99,
              "open": 2467.03,
              "timestamp": 1789066800000,
              "volume": 17979.0
            },
            {
              "close": 2460.2,
              "high": 2467.75,
              "low": 2459.67,
              "open": 2461.13,
              "timestamp": 1789070400000,
              "volume": 17951.0
            },
            {
              "close": 2458.94,
              "high": 2461.78,
              "low": 2456.47,
              "open": 2460.2,
              "timestamp": 1789074000000,
              "volume": 16749.0
            },
            {
              "close": 2443.51,
              "high": 2460.66,
              "low": 2442.17,
              "open": 2458.94,
              "timestamp": 1789077600000,
              "volume": 17340.0
            },
            {
              "close": 2436.7,
              "high": 2445.81,
              "low": 2433.02,
              "open": 2443.51,
              "timestamp": 1789081200000,
              "volume": 17947.0
            },
            {
              "close": 2455.12,
              "high": 2457.02,
              "low": 2435.92,
              "open": 2436.7,
              "timestamp": 1789084800000,
              "volume": 17954.0
            },
            {
              "close": 2452.92,
              "high": 2458.95,
              "low": 2444.6,
              "open": 2455.12,
              "timestamp": 1789088400000,
              "volume": 17960.0
            },
            {
              "close": 2445.52,
              "high": 2453.62,
              "low": 2442.76,
              "open": 2452.92,
              "timestamp": 1789092000000,
              "volume": 17915.0
            },
            {
              "close": 2445.86,
              "high": 2447.49,
              "low": 2438.73,
              "open": 2445.52,
              "timestamp": 1789095600000,
              "volume": 17957.0
            },
            {
              "close": 2457.62,
              "high": 2463.05,
              "low": 2444.81,
              "open": 2445.86,
              "timestamp": 1789099200000,
              "volume": 17959.0
            },
            {
              "close": 2467.45,
              "high": 2467.45,
              "low": 2456.12,
              "open": 2457.62,
              "timestamp": 1789102800000,
              "volume": 17946.0
            },
            {
              "close": 2465.57,
              "high": 2469.93,
              "low": 2462.0,
              "open": 2467.45,
              "timestamp": 1789106400000,
              "volume": 17962.0
            },
            {
              "close": 2466.17,
              "high": 2472.4,
              "low": 2464.88,
              "open": 2465.57,
              "timestamp": 1789110000000,
              "volume": 17946.0
            },
            {
              "close": 2475.47,
              "high": 2483.34,
              "low": 2462.24,
              "open": 2466.17,
              "timestamp": 1789113600000,
              "volume": 17933.0
            },
            {
              "close": 2468.06,
              "high": 2476.45,
              "low": 2460.21,
              "open": 2475.47,
              "timestamp": 1789117200000,
              "volume": 17920.0
            },
            {
              "close": 2460.76,
              "high": 2473.83,
              "low": 2460.72,
              "open": 2468.06,
              "timestamp": 1789120800000,
              "volume": 17958.0
            },
            {
              "close": 2456.86,
              "high": 2460.76,
              "low": 2450.42,
              "open": 2460.76,
              "timestamp": 1789124400000,
              "volume": 17964.0
            },
            {
              "close": 2509.45,
              "high": 2514.13,
              "low": 2432.79,
              "open": 2456.86,
              "timestamp": 1789128000000,
              "volume": 17960.0
            },
            {
              "close": 2628.15,
              "high": 2646.21,
              "low": 2488.43,
              "open": 2509.21,
              "timestamp": 1789131600000,
              "volume": 17874.0
            },
            {
              "close": 2606.4,
              "high": 2665.66,
              "low": 2590.72,
              "open": 2628.29,
              "timestamp": 1789135200000,
              "volume": 17898.0
            },
            {
              "close": 2557.67,
              "high": 2615.51,
              "low": 2544.41,
              "open": 2606.19,
              "timestamp": 1789138800000,
              "volume": 17953.0
            },
            {
              "close": 2576.04,
              "high": 2582.19,
              "low": 2542.46,
              "open": 2557.67,
              "timestamp": 1789142400000,
              "volume": 17963.0
            },
            {
              "close": 2564.98,
              "high": 2580.33,
              "low": 2561.78,
              "open": 2576.04,
              "timestamp": 1789146000000,
              "volume": 17953.0
            },
            {
              "close": 2535.9,
              "high": 2566.9,
              "low": 2527.18,
              "open": 2564.98,
              "timestamp": 1789149600000,
              "volume": 17963.0
            },
            {
              "close": 2537.95,
              "high": 2546.91,
              "low": 2531.27,
              "open": 2535.9,
              "timestamp": 1789153200000,
              "volume": 17969.0
            },
            {
              "close": 2529.07,
              "high": 2545.95,
              "low": 2521.25,
              "open": 2537.96,
              "timestamp": 1789156800000,
              "volume": 17933.0
            },
            {
              "close": 2514.74,
              "high": 2539.17,
              "low": 2511.79,
              "open": 2529.07,
              "timestamp": 1789160400000,
              "volume": 16733.0
            },
            {
              "close": 2510.31,
              "high": 2522.15,
              "low": 2504.35,
              "open": 2514.74,
              "timestamp": 1789164000000,
              "volume": 17301.0
            },
            {
              "close": 2515.13,
              "high": 2515.26,
              "low": 2507.67,
              "open": 2510.31,
              "timestamp": 1789167600000,
              "volume": 17897.0
            },
            {
              "close": 2509.16,
              "high": 2516.39,
              "low": 2509.14,
              "open": 2515.13,
              "timestamp": 1789171200000,
              "volume": 17898.0
            },
            {
              "close": 2512.13,
              "high": 2515.79,
              "low": 2507.97,
              "open": 2509.16,
              "timestamp": 1789174800000,
              "volume": 17916.0
            },
            {
              "close": 2512.83,
              "high": 2514.39,
              "low": 2510.85,
              "open": 2512.13,
              "timestamp": 1789178400000,
              "volume": 17916.0
            },
            {
              "close": 2511.65,
              "high": 2514.56,
              "low": 2507.77,
              "open": 2512.77,
              "timestamp": 1789182000000,
              "volume": 17911.0
            },
            {
              "close": 2511.17,
              "high": 2513.63,
              "low": 2508.25,
              "open": 2511.65,
              "timestamp": 1789185600000,
              "volume": 17918.0
            },
            {
              "close": 2510.27,
              "high": 2511.63,
              "low": 2507.27,
              "open": 2511.17,
              "timestamp": 1789189200000,
              "volume": 17923.0
            },
            {
              "close": 2517.87,
              "high": 2520.94,
              "low": 2508.88,
              "open": 2510.27,
              "timestamp": 1789192800000,
              "volume": 17915.0
            },
            {
              "close": 2522.66,
              "high": 2523.4,
              "low": 2517.87,
              "open": 2517.87,
              "timestamp": 1789196400000,
              "volume": 17922.0
            },
            {
              "close": 2531.96,
              "high": 2534.88,
              "low": 2521.67,
              "open": 2522.66,
              "timestamp": 1789200000000,
              "volume": 17904.0
            },
            {
              "close": 2529.66,
              "high": 2535.85,
              "low": 2527.84,
              "open": 2531.96,
              "timestamp": 1789203600000,
              "volume": 17931.0
            },
            {
              "close": 2532.18,
              "high": 2534.99,
              "low": 2529.66,
              "open": 2529.66,
              "timestamp": 1789207200000,
              "volume": 17937.0
            },
            {
              "close": 2534.87,
              "high": 2535.77,
              "low": 2529.51,
              "open": 2532.18,
              "timestamp": 1789210800000,
              "volume": 17941.0
            },
            {
              "close": 2534.06,
              "high": 2534.87,
              "low": 2530.39,
              "open": 2534.87,
              "timestamp": 1789214400000,
              "volume": 17928.0
            },
            {
              "close": 2543.29,
              "high": 2544.7,
              "low": 2531.99,
              "open": 2534.06,
              "timestamp": 1789218000000,
              "volume": 17929.0
            },
            {
              "close": 2538.45,
              "high": 2544.06,
              "low": 2537.72,
              "open": 2543.29,
              "timestamp": 1789221600000,
              "volume": 17909.0
            },
            {
              "close": 2533.66,
              "high": 2541.22,
              "low": 2530.38,
              "open": 2538.52,
              "timestamp": 1789225200000,
              "volume": 17896.0
            },
            {
              "close": 2530.35,
              "high": 2534.98,
              "low": 2528.85,
              "open": 2533.66,
              "timestamp": 1789228800000,
              "volume": 17904.0
            },
            {
              "close": 2524.6,
              "high": 2533.16,
              "low": 2523.41,
              "open": 2530.35,
              "timestamp": 1789232400000,
              "volume": 17896.0
            },
            {
              "close": 2521.24,
              "high": 2526.17,
              "low": 2519.12,
              "open": 2524.6,
              "timestamp": 1789236000000,
              "volume": 17900.0
            },
            {
              "close": 2517.82,
              "high": 2521.77,
              "low": 2513.47,
              "open": 2521.24,
              "timestamp": 1789239600000,
              "volume": 17913.0
            },
            {
              "close": 2519.11,
              "high": 2522.17,
              "low": 2517.81,
              "open": 2517.82,
              "timestamp": 1789243200000,
              "volume": 17900.0
            },
            {
              "close": 2522.68,
              "high": 2527.14,
              "low": 2518.48,
              "open": 2519.11,
              "timestamp": 1789246800000,
              "volume": 16894.0
            },
            {
              "close": 2521.45,
              "high": 2524.77,
              "low": 2518.7,
              "open": 2522.68,
              "timestamp": 1789250400000,
              "volume": 17883.0
            },
            {
              "close": 2524.43,
              "high": 2525.42,
              "low": 2521.0,
              "open": 2521.45,
              "timestamp": 1789254000000,
              "volume": 17894.0
            },
            {
              "close": 2523.89,
              "high": 2526.07,
              "low": 2521.78,
              "open": 2524.07,
              "timestamp": 1789257600000,
              "volume": 17594.0
            },
            {
              "close": 2524.48,
              "high": 2526.37,
              "low": 2520.96,
              "open": 2523.89,
              "timestamp": 1789261200000,
              "volume": 17902.0
            },
            {
              "close": 2520.15,
              "high": 2524.48,
              "low": 2519.68,
              "open": 2524.48,
              "timestamp": 1789264800000,
              "volume": 17900.0
            },
            {
              "close": 2519.42,
              "high": 2521.62,
              "low": 2517.9,
              "open": 2520.15,
              "timestamp": 1789268400000,
              "volume": 17908.0
            },
            {
              "close": 2518.89,
              "high": 2522.1,
              "low": 2517.8,
              "open": 2519.42,
              "timestamp": 1789272000000,
              "volume": 17906.0
            },
            {
              "close": 2521.17,
              "high": 2522.89,
              "low": 2518.89,
              "open": 2518.89,
              "timestamp": 1789275600000,
              "volume": 17902.0
            },
            {
              "close": 2511.39,
              "high": 2521.64,
              "low": 2508.05,
              "open": 2521.26,
              "timestamp": 1789279200000,
              "volume": 17907.0
            },
            {
              "close": 2516.28,
              "high": 2518.83,
              "low": 2510.32,
              "open": 2511.39,
              "timestamp": 1789282800000,
              "volume": 17906.0
            },
            {
              "close": 2492.91,
              "high": 2518.16,
              "low": 2486.16,
              "open": 2516.28,
              "timestamp": 1789286400000,
              "volume": 17909.0
            },
            {
              "close": 2483.35,
              "high": 2496.01,
              "low": 2469.23,
              "open": 2492.91,
              "timestamp": 1789290000000,
              "volume": 17915.0
            },
            {
              "close": 2470.75,
              "high": 2484.63,
              "low": 2466.29,
              "open": 2483.35,
              "timestamp": 1789293600000,
              "volume": 17911.0
            },
            {
              "close": 2479.79,
              "high": 2481.03,
              "low": 2466.17,
              "open": 2470.75,
              "timestamp": 1789297200000,
              "volume": 17905.0
            },
            {
              "close": 2475.87,
              "high": 2481.88,
              "low": 2473.37,
              "open": 2479.79,
              "timestamp": 1789300800000,
              "volume": 17913.0
            },
            {
              "close": 2477.5,
              "high": 2481.06,
              "low": 2460.37,
              "open": 2475.87,
              "timestamp": 1789304400000,
              "volume": 17912.0
            },
            {
              "close": 2490.96,
              "high": 2494.06,
              "low": 2477.16,
              "open": 2477.5,
              "timestamp": 1789308000000,
              "volume": 17917.0
            },
            {
              "close": 2489.22,
              "high": 2491.14,
              "low": 2481.37,
              "open": 2490.96,
              "timestamp": 1789311600000,
              "volume": 17916.0
            },
            {
              "close": 2503.11,
              "high": 2504.62,
              "low": 2488.85,
              "open": 2489.22,
              "timestamp": 1789315200000,
              "volume": 17916.0
            },
            {
              "close": 2503.65,
              "high": 2511.66,
              "low": 2501.38,
              "open": 2503.11,
              "timestamp": 1789318800000,
              "volume": 17913.0
            },
            {
              "close": 2508.01,
              "high": 2508.26,
              "low": 2502.97,
              "open": 2503.65,
              "timestamp": 1789322400000,
              "volume": 17912.0
            },
            {
              "close": 2504.76,
              "high": 2514.6,
              "low": 2501.98,
              "open": 2508.01,
              "timestamp": 1789326000000,
              "volume": 17911.0
            }
          ],
          "last_price": 2504.76,
          "momentum": "neutral",
          "rsi_14": 50.44,
          "structure": "neutral"
        },
        "4H": {
          "candle_count": 84,
          "candle_status": {
            "data_age_seconds": 14492,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789315200000,
            "latest_timestamp_utc": "2026-09-13T16:00:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 14400
          },
          "candles": [
            {
              "close": 2415.23,
              "high": 2507.29,
              "low": 2384.85,
              "open": 2502.43,
              "timestamp": 1788120000000,
              "volume": 70979.0
            },
            {
              "close": 2419.62,
              "high": 2438.45,
              "low": 2399.86,
              "open": 2414.99,
              "timestamp": 1788134400000,
              "volume": 71792.0
            },
            {
              "close": 2438.68,
              "high": 2445.06,
              "low": 2409.82,
              "open": 2419.62,
              "timestamp": 1788148800000,
              "volume": 71829.0
            },
            {
              "close": 2444.77,
              "high": 2456.42,
              "low": 2432.02,
              "open": 2438.68,
              "timestamp": 1788163200000,
              "volume": 71828.0
            },
            {
              "close": 2466.07,
              "high": 2476.55,
              "low": 2435.72,
              "open": 2444.77,
              "timestamp": 1788177600000,
              "volume": 71808.0
            },
            {
              "close": 2480.47,
              "high": 2488.36,
              "low": 2459.56,
              "open": 2466.07,
              "timestamp": 1788192000000,
              "volume": 71898.0
            },
            {
              "close": 2466.29,
              "high": 2485.42,
              "low": 2460.5,
              "open": 2480.44,
              "timestamp": 1788206400000,
              "volume": 70006.0
            },
            {
              "close": 2471.06,
              "high": 2481.61,
              "low": 2453.51,
              "open": 2466.22,
              "timestamp": 1788220800000,
              "volume": 71803.0
            },
            {
              "close": 2471.1,
              "high": 2484.26,
              "low": 2465.04,
              "open": 2471.06,
              "timestamp": 1788235200000,
              "volume": 71816.0
            },
            {
              "close": 2457.54,
              "high": 2472.2,
              "low": 2441.81,
              "open": 2471.1,
              "timestamp": 1788249600000,
              "volume": 71843.0
            },
            {
              "close": 2447.56,
              "high": 2457.75,
              "low": 2423.7,
              "open": 2457.54,
              "timestamp": 1788264000000,
              "volume": 71806.0
            },
            {
              "close": 2417.65,
              "high": 2448.3,
              "low": 2381.37,
              "open": 2447.56,
              "timestamp": 1788278400000,
              "volume": 71663.0
            },
            {
              "close": 2417.12,
              "high": 2425.66,
              "low": 2398.86,
              "open": 2417.65,
              "timestamp": 1788292800000,
              "volume": 69636.0
            },
            {
              "close": 2413.01,
              "high": 2423.25,
              "low": 2385.14,
              "open": 2417.12,
              "timestamp": 1788307200000,
              "volume": 71803.0
            },
            {
              "close": 2416.31,
              "high": 2427.67,
              "low": 2403.98,
              "open": 2413.01,
              "timestamp": 1788321600000,
              "volume": 71870.0
            },
            {
              "close": 2380.25,
              "high": 2419.15,
              "low": 2354.87,
              "open": 2416.31,
              "timestamp": 1788336000000,
              "volume": 71801.0
            },
            {
              "close": 2389.82,
              "high": 2416.33,
              "low": 2375.45,
              "open": 2380.25,
              "timestamp": 1788350400000,
              "volume": 63026.0
            },
            {
              "close": 2391.7,
              "high": 2403.67,
              "low": 2371.1,
              "open": 2389.82,
              "timestamp": 1788364800000,
              "volume": 71607.0
            },
            {
              "close": 2390.58,
              "high": 2398.55,
              "low": 2376.18,
              "open": 2391.81,
              "timestamp": 1788379200000,
              "volume": 69998.0
            },
            {
              "close": 2402.05,
              "high": 2409.66,
              "low": 2368.68,
              "open": 2390.58,
              "timestamp": 1788393600000,
              "volume": 71783.0
            },
            {
              "close": 2396.78,
              "high": 2418.44,
              "low": 2377.67,
              "open": 2402.05,
              "timestamp": 1788408000000,
              "volume": 71792.0
            },
            {
              "close": 2405.79,
              "high": 2411.89,
              "low": 2388.18,
              "open": 2396.99,
              "timestamp": 1788422400000,
              "volume": 71127.0
            },
            {
              "close": 2515.66,
              "high": 2516.3,
              "low": 2404.02,
              "open": 2405.79,
              "timestamp": 1788436800000,
              "volume": 63034.0
            },
            {
              "close": 2516.39,
              "high": 2527.89,
              "low": 2487.2,
              "open": 2515.66,
              "timestamp": 1788451200000,
              "volume": 71850.0
            },
            {
              "close": 2506.09,
              "high": 2525.37,
              "low": 2488.37,
              "open": 2516.69,
              "timestamp": 1788465600000,
              "volume": 69918.0
            },
            {
              "close": 2503.4,
              "high": 2516.18,
              "low": 2495.72,
              "open": 2506.09,
              "timestamp": 1788480000000,
              "volume": 71814.0
            },
            {
              "close": 2503.2,
              "high": 2524.14,
              "low": 2498.37,
              "open": 2503.4,
              "timestamp": 1788494400000,
              "volume": 71702.0
            },
            {
              "close": 2521.55,
              "high": 2545.59,
              "low": 2501.97,
              "open": 2503.2,
              "timestamp": 1788508800000,
              "volume": 71771.0
            },
            {
              "close": 2450.62,
              "high": 2530.76,
              "low": 2430.34,
              "open": 2521.55,
              "timestamp": 1788523200000,
              "volume": 61878.0
            },
            {
              "close": 2454.25,
              "high": 2463.02,
              "low": 2441.67,
              "open": 2450.62,
              "timestamp": 1788537600000,
              "volume": 71816.0
            },
            {
              "close": 2454.23,
              "high": 2457.32,
              "low": 2448.22,
              "open": 2454.37,
              "timestamp": 1788552000000,
              "volume": 69747.0
            },
            {
              "close": 2451.23,
              "high": 2455.02,
              "low": 2448.38,
              "open": 2454.23,
              "timestamp": 1788566400000,
              "volume": 71532.0
            },
            {
              "close": 2453.12,
              "high": 2453.53,
              "low": 2443.36,
              "open": 2451.23,
              "timestamp": 1788580800000,
              "volume": 55515.0
            },
            {
              "close": 2452.26,
              "high": 2458.93,
              "low": 2451.47,
              "open": 2455.4,
              "timestamp": 1788595200000,
              "volume": 66516.0
            },
            {
              "close": 2458.32,
              "high": 2460.67,
              "low": 2448.17,
              "open": 2452.26,
              "timestamp": 1788609600000,
              "volume": 71700.0
            },
            {
              "close": 2476.21,
              "high": 2483.14,
              "low": 2457.37,
              "open": 2458.32,
              "timestamp": 1788624000000,
              "volume": 71696.0
            },
            {
              "close": 2478.84,
              "high": 2491.66,
              "low": 2473.68,
              "open": 2476.21,
              "timestamp": 1788638400000,
              "volume": 70647.0
            },
            {
              "close": 2508.23,
              "high": 2513.25,
              "low": 2477.8,
              "open": 2478.65,
              "timestamp": 1788652800000,
              "volume": 71359.0
            },
            {
              "close": 2495.27,
              "high": 2523.01,
              "low": 2481.87,
              "open": 2508.23,
              "timestamp": 1788667200000,
              "volume": 71338.0
            },
            {
              "close": 2500.29,
              "high": 2502.94,
              "low": 2490.27,
              "open": 2495.27,
              "timestamp": 1788681600000,
              "volume": 71742.0
            },
            {
              "close": 2478.1,
              "high": 2503.54,
              "low": 2458.73,
              "open": 2500.29,
              "timestamp": 1788696000000,
              "volume": 71713.0
            },
            {
              "close": 2489.3,
              "high": 2498.86,
              "low": 2473.75,
              "open": 2478.1,
              "timestamp": 1788710400000,
              "volume": 71640.0
            },
            {
              "close": 2513.13,
              "high": 2525.1,
              "low": 2487.27,
              "open": 2489.3,
              "timestamp": 1788724800000,
              "volume": 70963.0
            },
            {
              "close": 2495.67,
              "high": 2535.21,
              "low": 2494.93,
              "open": 2513.13,
              "timestamp": 1788739200000,
              "volume": 71842.0
            },
            {
              "close": 2487.66,
              "high": 2512.62,
              "low": 2473.28,
              "open": 2495.67,
              "timestamp": 1788753600000,
              "volume": 71870.0
            },
            {
              "close": 2487.63,
              "high": 2495.93,
              "low": 2482.61,
              "open": 2487.66,
              "timestamp": 1788768000000,
              "volume": 71840.0
            },
            {
              "close": 2468.43,
              "high": 2510.41,
              "low": 2464.77,
              "open": 2487.63,
              "timestamp": 1788782400000,
              "volume": 71923.0
            },
            {
              "close": 2494.34,
              "high": 2498.09,
              "low": 2468.38,
              "open": 2468.6,
              "timestamp": 1788796800000,
              "volume": 71856.0
            },
            {
              "close": 2488.58,
              "high": 2495.81,
              "low": 2474.11,
              "open": 2494.34,
              "timestamp": 1788811200000,
              "volume": 70072.0
            },
            {
              "close": 2484.57,
              "high": 2506.81,
              "low": 2476.34,
              "open": 2488.58,
              "timestamp": 1788825600000,
              "volume": 71947.0
            },
            {
              "close": 2477.99,
              "high": 2484.82,
              "low": 2461.26,
              "open": 2484.57,
              "timestamp": 1788840000000,
              "volume": 71824.0
            },
            {
              "close": 2473.02,
              "high": 2498.8,
              "low": 2467.42,
              "open": 2477.99,
              "timestamp": 1788854400000,
              "volume": 71780.0
            },
            {
              "close": 2497.44,
              "high": 2500.7,
              "low": 2439.89,
              "open": 2473.02,
              "timestamp": 1788868800000,
              "volume": 71896.0
            },
            {
              "close": 2480.64,
              "high": 2505.91,
              "low": 2474.57,
              "open": 2497.44,
              "timestamp": 1788883200000,
              "volume": 71712.0
            },
            {
              "close": 2483.54,
              "high": 2490.11,
              "low": 2477.14,
              "open": 2480.65,
              "timestamp": 1788897600000,
              "volume": 69974.0
            },
            {
              "close": 2487.45,
              "high": 2498.98,
              "low": 2483.73,
              "open": 2483.73,
              "timestamp": 1788912000000,
              "volume": 71861.0
            },
            {
              "close": 2509.16,
              "high": 2516.08,
              "low": 2487.45,
              "open": 2487.45,
              "timestamp": 1788926400000,
              "volume": 71843.0
            },
            {
              "close": 2499.53,
              "high": 2522.18,
              "low": 2480.66,
              "open": 2509.16,
              "timestamp": 1788940800000,
              "volume": 71860.0
            },
            {
              "close": 2488.63,
              "high": 2520.24,
              "low": 2468.76,
              "open": 2499.53,
              "timestamp": 1788955200000,
              "volume": 71279.0
            },
            {
              "close": 2463.98,
              "high": 2498.23,
              "low": 2461.04,
              "open": 2488.63,
              "timestamp": 1788969600000,
              "volume": 71863.0
            },
            {
              "close": 2466.63,
              "high": 2470.62,
              "low": 2441.85,
              "open": 2463.98,
              "timestamp": 1788984000000,
              "volume": 70003.0
            },
            {
              "close": 2474.01,
              "high": 2477.96,
              "low": 2453.99,
              "open": 2466.63,
              "timestamp": 1788998400000,
              "volume": 72054.0
            },
            {
              "close": 2471.16,
              "high": 2483.65,
              "low": 2462.26,
              "open": 2474.01,
              "timestamp": 1789012800000,
              "volume": 72033.0
            },
            {
              "close": 2460.7,
              "high": 2476.6,
              "low": 2456.82,
              "open": 2471.16,
              "timestamp": 1789027200000,
              "volume": 71964.0
            },
            {
              "close": 2439.67,
              "high": 2465.11,
              "low": 2403.68,
              "open": 2460.7,
              "timestamp": 1789041600000,
              "volume": 71900.0
            },
            {
              "close": 2461.13,
              "high": 2473.84,
              "low": 2430.41,
              "open": 2439.67,
              "timestamp": 1789056000000,
              "volume": 72033.0
            },
            {
              "close": 2436.7,
              "high": 2467.75,
              "low": 2433.02,
              "open": 2461.13,
              "timestamp": 1789070400000,
              "volume": 69987.0
            },
            {
              "close": 2445.86,
              "high": 2458.95,
              "low": 2435.92,
              "open": 2436.7,
              "timestamp": 1789084800000,
              "volume": 71786.0
            },
            {
              "close": 2466.17,
              "high": 2472.4,
              "low": 2444.81,
              "open": 2445.86,
              "timestamp": 1789099200000,
              "volume": 71813.0
            },
            {
              "close": 2456.86,
              "high": 2483.34,
              "low": 2450.42,
              "open": 2466.17,
              "timestamp": 1789113600000,
              "volume": 71775.0
            },
            {
              "close": 2557.67,
              "high": 2665.66,
              "low": 2432.79,
              "open": 2456.86,
              "timestamp": 1789128000000,
              "volume": 71685.0
            },
            {
              "close": 2537.95,
              "high": 2582.19,
              "low": 2527.18,
              "open": 2557.67,
              "timestamp": 1789142400000,
              "volume": 71848.0
            },
            {
              "close": 2515.13,
              "high": 2545.95,
              "low": 2504.35,
              "open": 2537.96,
              "timestamp": 1789156800000,
              "volume": 69864.0
            },
            {
              "close": 2511.65,
              "high": 2516.39,
              "low": 2507.77,
              "open": 2515.13,
              "timestamp": 1789171200000,
              "volume": 71641.0
            },
            {
              "close": 2522.66,
              "high": 2523.4,
              "low": 2507.27,
              "open": 2511.65,
              "timestamp": 1789185600000,
              "volume": 71678.0
            },
            {
              "close": 2534.87,
              "high": 2535.85,
              "low": 2521.67,
              "open": 2522.66,
              "timestamp": 1789200000000,
              "volume": 71713.0
            },
            {
              "close": 2533.66,
              "high": 2544.7,
              "low": 2530.38,
              "open": 2534.87,
              "timestamp": 1789214400000,
              "volume": 71662.0
            },
            {
              "close": 2517.82,
              "high": 2534.98,
              "low": 2513.47,
              "open": 2533.66,
              "timestamp": 1789228800000,
              "volume": 71613.0
            },
            {
              "close": 2524.43,
              "high": 2527.14,
              "low": 2517.81,
              "open": 2517.82,
              "timestamp": 1789243200000,
              "volume": 70571.0
            },
            {
              "close": 2519.42,
              "high": 2526.37,
              "low": 2517.9,
              "open": 2524.07,
              "timestamp": 1789257600000,
              "volume": 71304.0
            },
            {
              "close": 2516.28,
              "high": 2522.89,
              "low": 2508.05,
              "open": 2519.42,
              "timestamp": 1789272000000,
              "volume": 71621.0
            },
            {
              "close": 2479.79,
              "high": 2518.16,
              "low": 2466.17,
              "open": 2516.28,
              "timestamp": 1789286400000,
              "volume": 71640.0
            },
            {
              "close": 2489.22,
              "high": 2494.06,
              "low": 2460.37,
              "open": 2479.79,
              "timestamp": 1789300800000,
              "volume": 71658.0
            },
            {
              "close": 2504.76,
              "high": 2514.6,
              "low": 2488.85,
              "open": 2489.22,
              "timestamp": 1789315200000,
              "volume": 71652.0
            }
          ],
          "last_price": 2504.76,
          "momentum": "neutral",
          "rsi_14": 51.6,
          "structure": "neutral"
        },
        "5M": {
          "candle_count": 144,
          "candle_status": {
            "data_age_seconds": 392,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789329300000,
            "latest_timestamp_utc": "2026-09-13T19:55:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 300
          },
          "candles": [
            {
              "close": 2517.47,
              "high": 2518.16,
              "low": 2515.55,
              "open": 2516.28,
              "timestamp": 1789286400000,
              "volume": 1492.0
            },
            {
              "close": 2515.79,
              "high": 2517.47,
              "low": 2515.79,
              "open": 2517.47,
              "timestamp": 1789286700000,
              "volume": 1493.0
            },
            {
              "close": 2513.64,
              "high": 2515.79,
              "low": 2511.01,
              "open": 2515.79,
              "timestamp": 1789287000000,
              "volume": 1495.0
            },
            {
              "close": 2510.31,
              "high": 2513.64,
              "low": 2508.68,
              "open": 2513.64,
              "timestamp": 1789287300000,
              "volume": 1492.0
            },
            {
              "close": 2509.95,
              "high": 2511.41,
              "low": 2509.88,
              "open": 2510.31,
              "timestamp": 1789287600000,
              "volume": 1491.0
            },
            {
              "close": 2508.95,
              "high": 2510.1,
              "low": 2508.75,
              "open": 2509.95,
              "timestamp": 1789287900000,
              "volume": 1492.0
            },
            {
              "close": 2499.12,
              "high": 2508.95,
              "low": 2495.71,
              "open": 2508.95,
              "timestamp": 1789288200000,
              "volume": 1493.0
            },
            {
              "close": 2488.37,
              "high": 2500.21,
              "low": 2486.58,
              "open": 2499.12,
              "timestamp": 1789288500000,
              "volume": 1494.0
            },
            {
              "close": 2491.59,
              "high": 2495.0,
              "low": 2486.16,
              "open": 2488.37,
              "timestamp": 1789288800000,
              "volume": 1492.0
            },
            {
              "close": 2494.62,
              "high": 2495.07,
              "low": 2490.86,
              "open": 2491.59,
              "timestamp": 1789289100000,
              "volume": 1492.0
            },
            {
              "close": 2493.49,
              "high": 2495.33,
              "low": 2492.67,
              "open": 2494.62,
              "timestamp": 1789289400000,
              "volume": 1492.0
            },
            {
              "close": 2492.91,
              "high": 2494.02,
              "low": 2490.53,
              "open": 2493.49,
              "timestamp": 1789289700000,
              "volume": 1491.0
            },
            {
              "close": 2495.25,
              "high": 2495.25,
              "low": 2492.68,
              "open": 2492.91,
              "timestamp": 1789290000000,
              "volume": 1493.0
            },
            {
              "close": 2493.75,
              "high": 2496.01,
              "low": 2493.7,
              "open": 2495.25,
              "timestamp": 1789290300000,
              "volume": 1493.0
            },
            {
              "close": 2491.49,
              "high": 2493.75,
              "low": 2491.17,
              "open": 2493.75,
              "timestamp": 1789290600000,
              "volume": 1491.0
            },
            {
              "close": 2491.23,
              "high": 2492.39,
              "low": 2487.99,
              "open": 2491.49,
              "timestamp": 1789290900000,
              "volume": 1491.0
            },
            {
              "close": 2478.99,
              "high": 2493.26,
              "low": 2474.52,
              "open": 2491.23,
              "timestamp": 1789291200000,
              "volume": 1493.0
            },
            {
              "close": 2480.17,
              "high": 2484.64,
              "low": 2473.87,
              "open": 2479.0,
              "timestamp": 1789291500000,
              "volume": 1495.0
            },
            {
              "close": 2473.11,
              "high": 2482.29,
              "low": 2469.23,
              "open": 2480.11,
              "timestamp": 1789291800000,
              "volume": 1493.0
            },
            {
              "close": 2478.55,
              "high": 2483.32,
              "low": 2472.39,
              "open": 2473.11,
              "timestamp": 1789292100000,
              "volume": 1493.0
            },
            {
              "close": 2479.03,
              "high": 2480.81,
              "low": 2477.2,
              "open": 2478.55,
              "timestamp": 1789292400000,
              "volume": 1495.0
            },
            {
              "close": 2482.39,
              "high": 2482.39,
              "low": 2477.91,
              "open": 2479.03,
              "timestamp": 1789292700000,
              "volume": 1494.0
            },
            {
              "close": 2482.32,
              "high": 2482.71,
              "low": 2479.62,
              "open": 2482.39,
              "timestamp": 1789293000000,
              "volume": 1492.0
            },
            {
              "close": 2483.35,
              "high": 2484.06,
              "low": 2480.96,
              "open": 2482.32,
              "timestamp": 1789293300000,
              "volume": 1492.0
            },
            {
              "close": 2482.77,
              "high": 2484.04,
              "low": 2482.25,
              "open": 2483.35,
              "timestamp": 1789293600000,
              "volume": 1495.0
            },
            {
              "close": 2483.94,
              "high": 2484.63,
              "low": 2481.74,
              "open": 2482.77,
              "timestamp": 1789293900000,
              "volume": 1490.0
            },
            {
              "close": 2481.66,
              "high": 2483.94,
              "low": 2480.64,
              "open": 2483.94,
              "timestamp": 1789294200000,
              "volume": 1493.0
            },
            {
              "close": 2479.19,
              "high": 2482.19,
              "low": 2478.65,
              "open": 2481.66,
              "timestamp": 1789294500000,
              "volume": 1492.0
            },
            {
              "close": 2478.94,
              "high": 2479.66,
              "low": 2478.36,
              "open": 2479.19,
              "timestamp": 1789294800000,
              "volume": 1491.0
            },
            {
              "close": 2478.28,
              "high": 2479.04,
              "low": 2478.24,
              "open": 2478.94,
              "timestamp": 1789295100000,
              "volume": 1495.0
            },
            {
              "close": 2481.73,
              "high": 2482.05,
              "low": 2478.02,
              "open": 2478.28,
              "timestamp": 1789295400000,
              "volume": 1490.0
            },
            {
              "close": 2479.39,
              "high": 2481.74,
              "low": 2478.69,
              "open": 2481.73,
              "timestamp": 1789295700000,
              "volume": 1492.0
            },
            {
              "close": 2473.66,
              "high": 2479.39,
              "low": 2471.76,
              "open": 2479.39,
              "timestamp": 1789296000000,
              "volume": 1494.0
            },
            {
              "close": 2476.67,
              "high": 2477.2,
              "low": 2473.66,
              "open": 2473.66,
              "timestamp": 1789296300000,
              "volume": 1490.0
            },
            {
              "close": 2474.04,
              "high": 2476.67,
              "low": 2473.18,
              "open": 2476.67,
              "timestamp": 1789296600000,
              "volume": 1495.0
            },
            {
              "close": 2470.75,
              "high": 2475.16,
              "low": 2466.29,
              "open": 2474.04,
              "timestamp": 1789296900000,
              "volume": 1494.0
            },
            {
              "close": 2475.91,
              "high": 2476.2,
              "low": 2466.17,
              "open": 2470.75,
              "timestamp": 1789297200000,
              "volume": 1491.0
            },
            {
              "close": 2471.3,
              "high": 2476.22,
              "low": 2470.74,
              "open": 2475.91,
              "timestamp": 1789297500000,
              "volume": 1493.0
            },
            {
              "close": 2468.16,
              "high": 2472.56,
              "low": 2468.03,
              "open": 2471.3,
              "timestamp": 1789297800000,
              "volume": 1491.0
            },
            {
              "close": 2471.54,
              "high": 2473.15,
              "low": 2468.16,
              "open": 2468.16,
              "timestamp": 1789298100000,
              "volume": 1491.0
            },
            {
              "close": 2474.11,
              "high": 2474.76,
              "low": 2470.67,
              "open": 2471.54,
              "timestamp": 1789298400000,
              "volume": 1492.0
            },
            {
              "close": 2473.62,
              "high": 2474.35,
              "low": 2473.07,
              "open": 2474.11,
              "timestamp": 1789298700000,
              "volume": 1496.0
            },
            {
              "close": 2475.05,
              "high": 2475.13,
              "low": 2471.96,
              "open": 2473.62,
              "timestamp": 1789299000000,
              "volume": 1490.0
            },
            {
              "close": 2476.85,
              "high": 2477.06,
              "low": 2475.05,
              "open": 2475.05,
              "timestamp": 1789299300000,
              "volume": 1492.0
            },
            {
              "close": 2478.81,
              "high": 2478.81,
              "low": 2476.85,
              "open": 2476.85,
              "timestamp": 1789299600000,
              "volume": 1490.0
            },
            {
              "close": 2479.47,
              "high": 2480.02,
              "low": 2477.7,
              "open": 2478.81,
              "timestamp": 1789299900000,
              "volume": 1496.0
            },
            {
              "close": 2478.84,
              "high": 2481.03,
              "low": 2478.49,
              "open": 2479.47,
              "timestamp": 1789300200000,
              "volume": 1492.0
            },
            {
              "close": 2479.79,
              "high": 2479.79,
              "low": 2478.42,
              "open": 2478.84,
              "timestamp": 1789300500000,
              "volume": 1491.0
            },
            {
              "close": 2477.79,
              "high": 2479.91,
              "low": 2477.49,
              "open": 2479.79,
              "timestamp": 1789300800000,
              "volume": 1490.0
            },
            {
              "close": 2477.62,
              "high": 2479.07,
              "low": 2477.34,
              "open": 2477.79,
              "timestamp": 1789301100000,
              "volume": 1494.0
            },
            {
              "close": 2479.9,
              "high": 2480.61,
              "low": 2477.62,
              "open": 2477.62,
              "timestamp": 1789301400000,
              "volume": 1493.0
            },
            {
              "close": 2481.55,
              "high": 2481.88,
              "low": 2479.9,
              "open": 2479.9,
              "timestamp": 1789301700000,
              "volume": 1492.0
            },
            {
              "close": 2480.26,
              "high": 2481.55,
              "low": 2480.06,
              "open": 2481.55,
              "timestamp": 1789302000000,
              "volume": 1495.0
            },
            {
              "close": 2479.03,
              "high": 2480.32,
              "low": 2479.03,
              "open": 2480.26,
              "timestamp": 1789302300000,
              "volume": 1493.0
            },
            {
              "close": 2476.9,
              "high": 2481.06,
              "low": 2475.11,
              "open": 2479.03,
              "timestamp": 1789302600000,
              "volume": 1491.0
            },
            {
              "close": 2475.96,
              "high": 2477.24,
              "low": 2473.8,
              "open": 2476.9,
              "timestamp": 1789302900000,
              "volume": 1491.0
            },
            {
              "close": 2474.67,
              "high": 2476.26,
              "low": 2473.37,
              "open": 2476.12,
              "timestamp": 1789303200000,
              "volume": 1494.0
            },
            {
              "close": 2473.89,
              "high": 2475.35,
              "low": 2473.48,
              "open": 2474.67,
              "timestamp": 1789303500000,
              "volume": 1495.0
            },
            {
              "close": 2475.91,
              "high": 2476.7,
              "low": 2473.74,
              "open": 2473.89,
              "timestamp": 1789303800000,
              "volume": 1492.0
            },
            {
              "close": 2475.87,
              "high": 2476.66,
              "low": 2475.58,
              "open": 2475.91,
              "timestamp": 1789304100000,
              "volume": 1493.0
            },
            {
              "close": 2473.05,
              "high": 2475.87,
              "low": 2473.03,
              "open": 2475.87,
              "timestamp": 1789304400000,
              "volume": 1491.0
            },
            {
              "close": 2474.74,
              "high": 2474.74,
              "low": 2471.44,
              "open": 2473.05,
              "timestamp": 1789304700000,
              "volume": 1495.0
            },
            {
              "close": 2475.82,
              "high": 2476.56,
              "low": 2474.55,
              "open": 2474.74,
              "timestamp": 1789305000000,
              "volume": 1492.0
            },
            {
              "close": 2471.11,
              "high": 2475.82,
              "low": 2470.84,
              "open": 2475.82,
              "timestamp": 1789305300000,
              "volume": 1492.0
            },
            {
              "close": 2468.57,
              "high": 2471.66,
              "low": 2465.28,
              "open": 2471.11,
              "timestamp": 1789305600000,
              "volume": 1491.0
            },
            {
              "close": 2465.61,
              "high": 2468.66,
              "low": 2460.37,
              "open": 2468.66,
              "timestamp": 1789305900000,
              "volume": 1491.0
            },
            {
              "close": 2469.37,
              "high": 2470.45,
              "low": 2465.42,
              "open": 2465.61,
              "timestamp": 1789306200000,
              "volume": 1495.0
            },
            {
              "close": 2471.66,
              "high": 2471.66,
              "low": 2469.37,
              "open": 2469.37,
              "timestamp": 1789306500000,
              "volume": 1494.0
            },
            {
              "close": 2474.42,
              "high": 2474.85,
              "low": 2470.86,
              "open": 2471.66,
              "timestamp": 1789306800000,
              "volume": 1492.0
            },
            {
              "close": 2478.45,
              "high": 2478.57,
              "low": 2474.42,
              "open": 2474.42,
              "timestamp": 1789307100000,
              "volume": 1493.0
            },
            {
              "close": 2476.72,
              "high": 2481.06,
              "low": 2476.48,
              "open": 2478.45,
              "timestamp": 1789307400000,
              "volume": 1495.0
            },
            {
              "close": 2477.5,
              "high": 2477.62,
              "low": 2476.51,
              "open": 2476.72,
              "timestamp": 1789307700000,
              "volume": 1491.0
            },
            {
              "close": 2478.76,
              "high": 2479.33,
              "low": 2477.16,
              "open": 2477.5,
              "timestamp": 1789308000000,
              "volume": 1494.0
            },
            {
              "close": 2482.61,
              "high": 2482.61,
              "low": 2478.76,
              "open": 2478.76,
              "timestamp": 1789308300000,
              "volume": 1492.0
            },
            {
              "close": 2483.55,
              "high": 2483.55,
              "low": 2481.25,
              "open": 2482.61,
              "timestamp": 1789308600000,
              "volume": 1495.0
            },
            {
              "close": 2485.93,
              "high": 2488.21,
              "low": 2483.44,
              "open": 2483.55,
              "timestamp": 1789308900000,
              "volume": 1495.0
            },
            {
              "close": 2489.89,
              "high": 2490.28,
              "low": 2485.93,
              "open": 2485.93,
              "timestamp": 1789309200000,
              "volume": 1493.0
            },
            {
              "close": 2488.77,
              "high": 2490.66,
              "low": 2487.63,
              "open": 2489.89,
              "timestamp": 1789309500000,
              "volume": 1492.0
            },
            {
              "close": 2487.94,
              "high": 2490.2,
              "low": 2487.31,
              "open": 2488.77,
              "timestamp": 1789309800000,
              "volume": 1493.0
            },
            {
              "close": 2489.38,
              "high": 2493.39,
              "low": 2487.85,
              "open": 2487.94,
              "timestamp": 1789310100000,
              "volume": 1492.0
            },
            {
              "close": 2491.09,
              "high": 2492.18,
              "low": 2487.99,
              "open": 2489.65,
              "timestamp": 1789310400000,
              "volume": 1493.0
            },
            {
              "close": 2490.25,
              "high": 2494.06,
              "low": 2490.25,
              "open": 2491.09,
              "timestamp": 1789310700000,
              "volume": 1494.0
            },
            {
              "close": 2490.66,
              "high": 2490.66,
              "low": 2488.49,
              "open": 2490.25,
              "timestamp": 1789311000000,
              "volume": 1490.0
            },
            {
              "close": 2490.96,
              "high": 2491.34,
              "low": 2488.77,
              "open": 2490.66,
              "timestamp": 1789311300000,
              "volume": 1494.0
            },
            {
              "close": 2485.73,
              "high": 2491.14,
              "low": 2485.31,
              "open": 2490.96,
              "timestamp": 1789311600000,
              "volume": 1492.0
            },
            {
              "close": 2486.96,
              "high": 2488.29,
              "low": 2483.67,
              "open": 2485.73,
              "timestamp": 1789311900000,
              "volume": 1495.0
            },
            {
              "close": 2486.2,
              "high": 2486.96,
              "low": 2485.41,
              "open": 2486.96,
              "timestamp": 1789312200000,
              "volume": 1496.0
            },
            {
              "close": 2483.44,
              "high": 2486.2,
              "low": 2481.37,
              "open": 2486.2,
              "timestamp": 1789312500000,
              "volume": 1492.0
            },
            {
              "close": 2488.77,
              "high": 2490.22,
              "low": 2483.44,
              "open": 2483.44,
              "timestamp": 1789312800000,
              "volume": 1491.0
            },
            {
              "close": 2485.35,
              "high": 2488.77,
              "low": 2484.69,
              "open": 2488.77,
              "timestamp": 1789313100000,
              "volume": 1494.0
            },
            {
              "close": 2488.73,
              "high": 2488.76,
              "low": 2485.35,
              "open": 2485.35,
              "timestamp": 1789313400000,
              "volume": 1490.0
            },
            {
              "close": 2486.22,
              "high": 2488.73,
              "low": 2486.22,
              "open": 2488.73,
              "timestamp": 1789313700000,
              "volume": 1494.0
            },
            {
              "close": 2489.0,
              "high": 2489.66,
              "low": 2486.02,
              "open": 2486.22,
              "timestamp": 1789314000000,
              "volume": 1493.0
            },
            {
              "close": 2489.17,
              "high": 2489.22,
              "low": 2487.59,
              "open": 2489.0,
              "timestamp": 1789314300000,
              "volume": 1494.0
            },
            {
              "close": 2489.66,
              "high": 2489.66,
              "low": 2487.9,
              "open": 2489.17,
              "timestamp": 1789314600000,
              "volume": 1493.0
            },
            {
              "close": 2489.22,
              "high": 2489.86,
              "low": 2488.3,
              "open": 2489.66,
              "timestamp": 1789314900000,
              "volume": 1492.0
            },
            {
              "close": 2492.54,
              "high": 2494.39,
              "low": 2488.85,
              "open": 2489.22,
              "timestamp": 1789315200000,
              "volume": 1490.0
            },
            {
              "close": 2496.41,
              "high": 2498.42,
              "low": 2491.81,
              "open": 2492.54,
              "timestamp": 1789315500000,
              "volume": 1496.0
            },
            {
              "close": 2499.17,
              "high": 2503.33,
              "low": 2495.12,
              "open": 2496.37,
              "timestamp": 1789315800000,
              "volume": 1494.0
            },
            {
              "close": 2498.72,
              "high": 2499.17,
              "low": 2496.42,
              "open": 2499.17,
              "timestamp": 1789316100000,
              "volume": 1496.0
            },
            {
              "close": 2500.19,
              "high": 2500.19,
              "low": 2498.24,
              "open": 2498.72,
              "timestamp": 1789316400000,
              "volume": 1492.0
            },
            {
              "close": 2501.05,
              "high": 2502.32,
              "low": 2499.67,
              "open": 2500.19,
              "timestamp": 1789316700000,
              "volume": 1493.0
            },
            {
              "close": 2498.92,
              "high": 2502.13,
              "low": 2498.63,
              "open": 2501.05,
              "timestamp": 1789317000000,
              "volume": 1493.0
            },
            {
              "close": 2500.74,
              "high": 2501.25,
              "low": 2498.46,
              "open": 2498.92,
              "timestamp": 1789317300000,
              "volume": 1494.0
            },
            {
              "close": 2502.35,
              "high": 2503.68,
              "low": 2500.74,
              "open": 2500.74,
              "timestamp": 1789317600000,
              "volume": 1493.0
            },
            {
              "close": 2501.66,
              "high": 2503.57,
              "low": 2500.6,
              "open": 2502.35,
              "timestamp": 1789317900000,
              "volume": 1490.0
            },
            {
              "close": 2503.84,
              "high": 2503.87,
              "low": 2501.64,
              "open": 2501.66,
              "timestamp": 1789318200000,
              "volume": 1490.0
            },
            {
              "close": 2503.11,
              "high": 2504.62,
              "low": 2502.9,
              "open": 2503.84,
              "timestamp": 1789318500000,
              "volume": 1495.0
            },
            {
              "close": 2504.95,
              "high": 2505.16,
              "low": 2502.64,
              "open": 2503.11,
              "timestamp": 1789318800000,
              "volume": 1494.0
            },
            {
              "close": 2505.95,
              "high": 2507.3,
              "low": 2504.53,
              "open": 2504.95,
              "timestamp": 1789319100000,
              "volume": 1492.0
            },
            {
              "close": 2507.74,
              "high": 2511.66,
              "low": 2505.95,
              "open": 2505.95,
              "timestamp": 1789319400000,
              "volume": 1493.0
            },
            {
              "close": 2507.39,
              "high": 2509.65,
              "low": 2506.7,
              "open": 2507.74,
              "timestamp": 1789319700000,
              "volume": 1494.0
            },
            {
              "close": 2504.54,
              "high": 2507.39,
              "low": 2504.26,
              "open": 2507.39,
              "timestamp": 1789320000000,
              "volume": 1493.0
            },
            {
              "close": 2504.22,
              "high": 2504.83,
              "low": 2503.96,
              "open": 2504.54,
              "timestamp": 1789320300000,
              "volume": 1491.0
            },
            {
              "close": 2501.94,
              "high": 2504.66,
              "low": 2501.38,
              "open": 2504.22,
              "timestamp": 1789320600000,
              "volume": 1494.0
            },
            {
              "close": 2503.31,
              "high": 2503.9,
              "low": 2501.45,
              "open": 2501.94,
              "timestamp": 1789320900000,
              "volume": 1493.0
            },
            {
              "close": 2502.38,
              "high": 2503.43,
              "low": 2502.12,
              "open": 2503.31,
              "timestamp": 1789321200000,
              "volume": 1491.0
            },
            {
              "close": 2503.66,
              "high": 2504.16,
              "low": 2502.38,
              "open": 2502.38,
              "timestamp": 1789321500000,
              "volume": 1496.0
            },
            {
              "close": 2503.47,
              "high": 2504.66,
              "low": 2502.98,
              "open": 2503.66,
              "timestamp": 1789321800000,
              "volume": 1490.0
            },
            {
              "close": 2503.65,
              "high": 2504.4,
              "low": 2503.08,
              "open": 2503.47,
              "timestamp": 1789322100000,
              "volume": 1492.0
            },
            {
              "close": 2503.81,
              "high": 2504.65,
              "low": 2502.97,
              "open": 2503.65,
              "timestamp": 1789322400000,
              "volume": 1492.0
            },
            {
              "close": 2503.78,
              "high": 2504.27,
              "low": 2503.12,
              "open": 2503.81,
              "timestamp": 1789322700000,
              "volume": 1492.0
            },
            {
              "close": 2505.08,
              "high": 2505.29,
              "low": 2503.33,
              "open": 2503.78,
              "timestamp": 1789323000000,
              "volume": 1494.0
            },
            {
              "close": 2505.54,
              "high": 2507.61,
              "low": 2504.31,
              "open": 2505.08,
              "timestamp": 1789323300000,
              "volume": 1493.0
            },
            {
              "close": 2506.67,
              "high": 2507.03,
              "low": 2505.45,
              "open": 2505.54,
              "timestamp": 1789323600000,
              "volume": 1493.0
            },
            {
              "close": 2504.88,
              "high": 2507.22,
              "low": 2504.84,
              "open": 2506.67,
              "timestamp": 1789323900000,
              "volume": 1493.0
            },
            {
              "close": 2507.02,
              "high": 2507.02,
              "low": 2504.88,
              "open": 2504.88,
              "timestamp": 1789324200000,
              "volume": 1496.0
            },
            {
              "close": 2507.66,
              "high": 2507.76,
              "low": 2507.02,
              "open": 2507.02,
              "timestamp": 1789324500000,
              "volume": 1490.0
            },
            {
              "close": 2507.18,
              "high": 2507.66,
              "low": 2506.23,
              "open": 2507.66,
              "timestamp": 1789324800000,
              "volume": 1490.0
            },
            {
              "close": 2507.67,
              "high": 2507.8,
              "low": 2507.13,
              "open": 2507.18,
              "timestamp": 1789325100000,
              "volume": 1492.0
            },
            {
              "close": 2508.16,
              "high": 2508.26,
              "low": 2507.67,
              "open": 2507.67,
              "timestamp": 1789325400000,
              "volume": 1495.0
            },
            {
              "close": 2508.01,
              "high": 2508.26,
              "low": 2506.9,
              "open": 2508.16,
              "timestamp": 1789325700000,
              "volume": 1492.0
            },
            {
              "close": 2509.65,
              "high": 2511.03,
              "low": 2508.01,
              "open": 2508.01,
              "timestamp": 1789326000000,
              "volume": 1497.0
            },
            {
              "close": 2508.8,
              "high": 2514.6,
              "low": 2508.8,
              "open": 2509.65,
              "timestamp": 1789326300000,
              "volume": 1498.0
            },
            {
              "close": 2507.61,
              "high": 2509.66,
              "low": 2507.37,
              "open": 2508.8,
              "timestamp": 1789326600000,
              "volume": 1490.0
            },
            {
              "close": 2506.31,
              "high": 2508.87,
              "low": 2506.24,
              "open": 2507.61,
              "timestamp": 1789326900000,
              "volume": 1495.0
            },
            {
              "close": 2506.12,
              "high": 2506.65,
              "low": 2504.88,
              "open": 2506.31,
              "timestamp": 1789327200000,
              "volume": 1496.0
            },
            {
              "close": 2506.74,
              "high": 2506.95,
              "low": 2506.12,
              "open": 2506.12,
              "timestamp": 1789327500000,
              "volume": 1488.0
            },
            {
              "close": 2502.74,
              "high": 2506.74,
              "low": 2502.56,
              "open": 2506.74,
              "timestamp": 1789327800000,
              "volume": 1490.0
            },
            {
              "close": 2503.52,
              "high": 2503.65,
              "low": 2501.98,
              "open": 2502.74,
              "timestamp": 1789328100000,
              "volume": 1493.0
            },
            {
              "close": 2504.03,
              "high": 2504.27,
              "low": 2502.82,
              "open": 2503.52,
              "timestamp": 1789328400000,
              "volume": 1491.0
            },
            {
              "close": 2503.72,
              "high": 2504.63,
              "low": 2503.47,
              "open": 2504.03,
              "timestamp": 1789328700000,
              "volume": 1494.0
            },
            {
              "close": 2504.23,
              "high": 2504.4,
              "low": 2502.9,
              "open": 2503.72,
              "timestamp": 1789329000000,
              "volume": 1492.0
            },
            {
              "close": 2504.76,
              "high": 2504.86,
              "low": 2503.81,
              "open": 2504.23,
              "timestamp": 1789329300000,
              "volume": 1487.0
            }
          ],
          "last_price": 2504.76,
          "momentum": "neutral",
          "rsi_14": 50.08,
          "structure": "bearish"
        }
      }
    },
    {
      "bridge_analysis": {
        "decision": "REJECT",
        "directional_bias": "neutral",
        "execution_5m": {
          "candle_confirmed": false,
          "confirmed": false,
          "reason": "No directional bias is established.",
          "rsi_confirmed": false,
          "structure_shift": false
        },
        "execution_context": {
          "atr_14": 1.064773,
          "distance_to_high": 2.119999999999891,
          "distance_to_low": 3.6900000000000546,
          "extension": "normal",
          "range_position": 0.6351,
          "recent_high": 723.56,
          "recent_low": 717.75
        },
        "geometry": {
          "entry_quality": "unknown",
          "invalidation": null,
          "reward_to_risk": null,
          "risk_distance": null,
          "room_to_target": null,
          "target_reference": null
        },
        "multi_horizon_state": "conflicted",
        "reason": "Directional evidence is materially conflicted and lacks sufficient edge.",
        "setup_grade": "REJECT",
        "symbol": "BNBUSD",
        "timeframes": {
          "15M": {
            "candle_count": 192,
            "last_price": 721.44,
            "momentum": "neutral",
            "rsi_14": 55.58,
            "structure": "bullish"
          },
          "1H": {
            "candle_count": 168,
            "last_price": 721.44,
            "momentum": "neutral",
            "rsi_14": 45.15,
            "structure": "neutral"
          },
          "4H": {
            "candle_count": 84,
            "last_price": 721.44,
            "momentum": "neutral",
            "rsi_14": 44.89,
            "structure": "neutral"
          },
          "5M": {
            "candle_count": 144,
            "last_price": 721.44,
            "momentum": "neutral",
            "rsi_14": 47.79,
            "structure": "bearish"
          }
        },
        "trade_plan": {
          "entry_reference": null,
          "live_market_entry_reference": null,
          "live_market_entry_reference_is_authorization": false,
          "live_market_entry_reference_side": null,
          "reason": "No directional bias is established.",
          "reward_to_tp1": null,
          "reward_to_tp2": null,
          "reward_to_tp3": null,
          "risk_distance": null,
          "rr_tp1": null,
          "rr_tp2": null,
          "rr_tp3": null,
          "safe_loss": null,
          "tp1": null,
          "tp2": null,
          "tp3": null,
          "valid": false
        }
      },
      "broker": {
        "route_id": 452,
        "tradable_instrument_id": 205
      },
      "instrument_specs": {
        "available": true,
        "bar_source": "BID",
        "base_currency": "BNB",
        "cache": {
          "age_seconds": 636964.982,
          "captured_at": "2026-09-06T11:05:34.400049+00:00",
          "source": "stale_cache",
          "stale": true
        },
        "contract_size": 10,
        "error": null,
        "leverage": "3.00",
        "lot_step": 0.01,
        "margin_hedging_type": "fx_cfd",
        "maximum_lot": null,
        "minimum_lot": 0.01,
        "minimum_stop_distance": null,
        "quote_currency": "USD",
        "raw_details": {
          "d": {
            "barSource": "BID",
            "baseCurrency": "BNB",
            "betSize": null,
            "betStep": null,
            "bettingCurrency": null,
            "contractMonth": null,
            "country": null,
            "deliveryStatus": null,
            "description": "Binance Coin vs US Dollar",
            "exerciseStyle": null,
            "firstTradeDate": null,
            "hasDaily": true,
            "hasIntraday": true,
            "industry": null,
            "isin": "",
            "lastTradeDate": null,
            "leverage": "3.00",
            "localizedName": "BNBUSD",
            "logoUrl": null,
            "lotSize": 10,
            "lotStep": 0.01,
            "margin_hedging_type": "fx_cfd",
            "marketCap": null,
            "marketDataExchange": "Cryptos",
            "maxLot": null,
            "minLot": 0.01,
            "name": "BNBUSD",
            "noticeDate": null,
            "quotingCurrency": "USD",
            "sector": null,
            "settlementDate": null,
            "settlementSystem": "Immediate",
            "strikePrice": null,
            "strikeType": null,
            "symbolStatus": "FULLY_OPEN",
            "tickCost": [
              {
                "leftRangeLimit": null,
                "tickCost": 0.0
              }
            ],
            "tickSize": [
              {
                "leftRangeLimit": null,
                "tickSize": 0.001
              }
            ],
            "tradeSessionId": 1547,
            "tradeSessionStatusId": 20,
            "tradingExchange": "Crypto",
            "type": "CRYPTO"
          },
          "s": "ok"
        },
        "route_id": 9912,
        "symbol_status": "FULLY_OPEN",
        "tick_cost_raw": 0.0,
        "tick_size": 0.001,
        "tick_value": null,
        "tradable_instrument_id": 205,
        "trading_session_id": 1547,
        "trading_session_status_id": 20
      },
      "market_snapshot": {
        "analysis_price": 721.44,
        "analysis_price_source": "latest_5m_bar",
        "ask": 721.64,
        "ask_size": 100.0,
        "atlas_received_at": "2026-09-13T20:01:35.148749+00:00",
        "bid": 721.63,
        "bid_size": 100.0,
        "broker_staleness_known": false,
        "cache": {
          "age_seconds": 0,
          "captured_at": "2026-09-13T20:01:35.148729+00:00",
          "source": "live",
          "stale": false
        },
        "live_ask": 721.64,
        "live_bid": 721.63,
        "live_executable_market_entry": null,
        "live_executable_market_entry_is_authorization": false,
        "live_executable_market_entry_side": null,
        "live_mid": 721.635,
        "market_entry_price_policy": "LONG market execution evaluates live ask; SHORT market execution evaluates live bid. Structural or pending entry_reference remains context and must be reassessed before approval.",
        "price_semantics": "analysis_price is the latest 5M bar/reference price, not an executable quote. live_bid and live_ask are current TradeLocker quote values; live_mid is their midpoint. For market-entry evaluation use live_ask for LONG and live_bid for SHORT.",
        "quote_age_seconds": null,
        "quote_error": null,
        "quote_note": "Bid/ask values are live TradeLocker quote values. The broker response does not currently expose a quote timestamp, so broker quote age/staleness is left null rather than estimated.",
        "quote_timestamp": null,
        "quotes_available": true,
        "raw_quote": {
          "d": {
            "ap": 721.64,
            "as": 100.0,
            "bp": 721.63,
            "bs": 100.0
          },
          "s": "ok"
        },
        "spread": 0.009999999999990905
      },
      "symbol": "BNBUSD",
      "timeframes": {
        "15M": {
          "candle_count": 192,
          "candle_status": {
            "data_age_seconds": 993,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789328700000,
            "latest_timestamp_utc": "2026-09-13T19:45:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 900
          },
          "candles": [
            {
              "close": 727.16,
              "high": 727.76,
              "low": 725.07,
              "open": 725.37,
              "timestamp": 1789156800000,
              "volume": 4454.0
            },
            {
              "close": 726.5,
              "high": 727.25,
              "low": 726.03,
              "open": 727.16,
              "timestamp": 1789157700000,
              "volume": 4449.0
            },
            {
              "close": 727.45,
              "high": 727.97,
              "low": 725.1,
              "open": 726.5,
              "timestamp": 1789158600000,
              "volume": 4459.0
            },
            {
              "close": 726.54,
              "high": 727.68,
              "low": 724.75,
              "open": 727.45,
              "timestamp": 1789159500000,
              "volume": 4472.0
            },
            {
              "close": 727.0,
              "high": 727.63,
              "low": 726.06,
              "open": 726.54,
              "timestamp": 1789160400000,
              "volume": 3260.0
            },
            {
              "close": 727.07,
              "high": 727.89,
              "low": 727.0,
              "open": 727.0,
              "timestamp": 1789161300000,
              "volume": 4424.0
            },
            {
              "close": 726.66,
              "high": 727.31,
              "low": 726.5,
              "open": 727.07,
              "timestamp": 1789162200000,
              "volume": 4399.0
            },
            {
              "close": 723.57,
              "high": 726.71,
              "low": 723.2,
              "open": 726.66,
              "timestamp": 1789163100000,
              "volume": 4445.0
            },
            {
              "close": 724.6,
              "high": 725.47,
              "low": 722.09,
              "open": 723.57,
              "timestamp": 1789164000000,
              "volume": 3843.0
            },
            {
              "close": 724.61,
              "high": 725.91,
              "low": 723.78,
              "open": 724.6,
              "timestamp": 1789164900000,
              "volume": 4427.0
            },
            {
              "close": 724.74,
              "high": 725.48,
              "low": 723.16,
              "open": 724.61,
              "timestamp": 1789165800000,
              "volume": 4440.0
            },
            {
              "close": 724.65,
              "high": 724.76,
              "low": 723.24,
              "open": 724.74,
              "timestamp": 1789166700000,
              "volume": 4433.0
            },
            {
              "close": 725.5,
              "high": 726.35,
              "low": 724.14,
              "open": 724.65,
              "timestamp": 1789167600000,
              "volume": 4434.0
            },
            {
              "close": 725.79,
              "high": 726.11,
              "low": 724.83,
              "open": 725.5,
              "timestamp": 1789168500000,
              "volume": 4410.0
            },
            {
              "close": 726.58,
              "high": 726.95,
              "low": 725.61,
              "open": 725.79,
              "timestamp": 1789169400000,
              "volume": 4410.0
            },
            {
              "close": 727.1,
              "high": 728.1,
              "low": 726.58,
              "open": 726.58,
              "timestamp": 1789170300000,
              "volume": 4406.0
            },
            {
              "close": 727.7,
              "high": 728.34,
              "low": 726.44,
              "open": 727.1,
              "timestamp": 1789171200000,
              "volume": 4373.0
            },
            {
              "close": 728.01,
              "high": 728.52,
              "low": 727.65,
              "open": 727.7,
              "timestamp": 1789172100000,
              "volume": 4298.0
            },
            {
              "close": 727.9,
              "high": 728.87,
              "low": 727.72,
              "open": 728.01,
              "timestamp": 1789173000000,
              "volume": 4406.0
            },
            {
              "close": 727.02,
              "high": 728.25,
              "low": 727.02,
              "open": 727.9,
              "timestamp": 1789173900000,
              "volume": 4404.0
            },
            {
              "close": 728.79,
              "high": 729.07,
              "low": 726.44,
              "open": 727.02,
              "timestamp": 1789174800000,
              "volume": 4420.0
            },
            {
              "close": 729.63,
              "high": 730.46,
              "low": 728.75,
              "open": 728.79,
              "timestamp": 1789175700000,
              "volume": 4421.0
            },
            {
              "close": 729.68,
              "high": 729.86,
              "low": 728.7,
              "open": 729.63,
              "timestamp": 1789176600000,
              "volume": 4420.0
            },
            {
              "close": 730.68,
              "high": 731.33,
              "low": 729.6,
              "open": 729.68,
              "timestamp": 1789177500000,
              "volume": 4402.0
            },
            {
              "close": 730.38,
              "high": 731.6,
              "low": 730.38,
              "open": 730.68,
              "timestamp": 1789178400000,
              "volume": 4413.0
            },
            {
              "close": 730.4,
              "high": 731.29,
              "low": 729.89,
              "open": 730.38,
              "timestamp": 1789179300000,
              "volume": 4407.0
            },
            {
              "close": 730.26,
              "high": 730.9,
              "low": 729.73,
              "open": 730.4,
              "timestamp": 1789180200000,
              "volume": 4407.0
            },
            {
              "close": 732.15,
              "high": 732.23,
              "low": 730.12,
              "open": 730.26,
              "timestamp": 1789181100000,
              "volume": 4406.0
            },
            {
              "close": 735.38,
              "high": 736.01,
              "low": 732.11,
              "open": 732.15,
              "timestamp": 1789182000000,
              "volume": 4445.0
            },
            {
              "close": 734.69,
              "high": 735.91,
              "low": 733.48,
              "open": 735.38,
              "timestamp": 1789182900000,
              "volume": 4422.0
            },
            {
              "close": 734.53,
              "high": 736.72,
              "low": 733.61,
              "open": 734.69,
              "timestamp": 1789183800000,
              "volume": 4423.0
            },
            {
              "close": 733.92,
              "high": 734.93,
              "low": 733.88,
              "open": 734.53,
              "timestamp": 1789184700000,
              "volume": 4382.0
            },
            {
              "close": 734.53,
              "high": 735.33,
              "low": 733.82,
              "open": 733.92,
              "timestamp": 1789185600000,
              "volume": 4421.0
            },
            {
              "close": 734.45,
              "high": 734.93,
              "low": 733.44,
              "open": 734.53,
              "timestamp": 1789186500000,
              "volume": 4403.0
            },
            {
              "close": 735.33,
              "high": 735.8,
              "low": 734.44,
              "open": 734.45,
              "timestamp": 1789187400000,
              "volume": 4401.0
            },
            {
              "close": 734.1,
              "high": 735.51,
              "low": 733.88,
              "open": 735.33,
              "timestamp": 1789188300000,
              "volume": 4405.0
            },
            {
              "close": 735.4,
              "high": 735.75,
              "low": 733.58,
              "open": 734.1,
              "timestamp": 1789189200000,
              "volume": 4408.0
            },
            {
              "close": 732.93,
              "high": 735.4,
              "low": 732.93,
              "open": 735.4,
              "timestamp": 1789190100000,
              "volume": 4417.0
            },
            {
              "close": 733.54,
              "high": 734.33,
              "low": 732.68,
              "open": 732.93,
              "timestamp": 1789191000000,
              "volume": 4400.0
            },
            {
              "close": 733.41,
              "high": 734.09,
              "low": 733.23,
              "open": 733.54,
              "timestamp": 1789191900000,
              "volume": 4378.0
            },
            {
              "close": 732.91,
              "high": 733.83,
              "low": 732.74,
              "open": 733.41,
              "timestamp": 1789192800000,
              "volume": 4393.0
            },
            {
              "close": 732.23,
              "high": 733.17,
              "low": 731.94,
              "open": 732.91,
              "timestamp": 1789193700000,
              "volume": 4396.0
            },
            {
              "close": 732.78,
              "high": 732.95,
              "low": 731.99,
              "open": 732.23,
              "timestamp": 1789194600000,
              "volume": 4400.0
            },
            {
              "close": 732.24,
              "high": 733.42,
              "low": 731.97,
              "open": 732.78,
              "timestamp": 1789195500000,
              "volume": 4420.0
            },
            {
              "close": 733.77,
              "high": 733.77,
              "low": 732.11,
              "open": 732.24,
              "timestamp": 1789196400000,
              "volume": 4413.0
            },
            {
              "close": 734.0,
              "high": 734.76,
              "low": 733.54,
              "open": 733.77,
              "timestamp": 1789197300000,
              "volume": 4405.0
            },
            {
              "close": 734.2,
              "high": 734.62,
              "low": 733.44,
              "open": 734.0,
              "timestamp": 1789198200000,
              "volume": 4383.0
            },
            {
              "close": 733.89,
              "high": 734.99,
              "low": 733.84,
              "open": 734.2,
              "timestamp": 1789199100000,
              "volume": 4399.0
            },
            {
              "close": 734.44,
              "high": 734.91,
              "low": 733.6,
              "open": 733.89,
              "timestamp": 1789200000000,
              "volume": 4411.0
            },
            {
              "close": 733.6,
              "high": 735.26,
              "low": 733.55,
              "open": 734.44,
              "timestamp": 1789200900000,
              "volume": 4416.0
            },
            {
              "close": 734.72,
              "high": 734.81,
              "low": 733.01,
              "open": 733.6,
              "timestamp": 1789201800000,
              "volume": 4394.0
            },
            {
              "close": 735.29,
              "high": 735.32,
              "low": 734.64,
              "open": 734.7,
              "timestamp": 1789202700000,
              "volume": 4398.0
            },
            {
              "close": 735.73,
              "high": 735.74,
              "low": 734.95,
              "open": 735.29,
              "timestamp": 1789203600000,
              "volume": 4424.0
            },
            {
              "close": 735.73,
              "high": 735.92,
              "low": 735.04,
              "open": 735.73,
              "timestamp": 1789204500000,
              "volume": 4386.0
            },
            {
              "close": 735.49,
              "high": 737.26,
              "low": 735.44,
              "open": 735.73,
              "timestamp": 1789205400000,
              "volume": 4401.0
            },
            {
              "close": 735.8,
              "high": 735.94,
              "low": 734.83,
              "open": 735.49,
              "timestamp": 1789206300000,
              "volume": 4371.0
            },
            {
              "close": 736.65,
              "high": 737.09,
              "low": 735.71,
              "open": 735.8,
              "timestamp": 1789207200000,
              "volume": 4411.0
            },
            {
              "close": 738.29,
              "high": 738.95,
              "low": 736.64,
              "open": 736.65,
              "timestamp": 1789208100000,
              "volume": 4421.0
            },
            {
              "close": 739.19,
              "high": 739.61,
              "low": 737.49,
              "open": 738.29,
              "timestamp": 1789209000000,
              "volume": 4427.0
            },
            {
              "close": 738.25,
              "high": 740.33,
              "low": 738.22,
              "open": 739.19,
              "timestamp": 1789209900000,
              "volume": 4408.0
            },
            {
              "close": 737.49,
              "high": 738.6,
              "low": 737.3,
              "open": 738.25,
              "timestamp": 1789210800000,
              "volume": 4421.0
            },
            {
              "close": 736.82,
              "high": 737.51,
              "low": 736.56,
              "open": 737.49,
              "timestamp": 1789211700000,
              "volume": 4401.0
            },
            {
              "close": 736.47,
              "high": 737.34,
              "low": 736.47,
              "open": 736.82,
              "timestamp": 1789212600000,
              "volume": 4394.0
            },
            {
              "close": 737.16,
              "high": 737.16,
              "low": 736.39,
              "open": 736.47,
              "timestamp": 1789213500000,
              "volume": 4418.0
            },
            {
              "close": 736.81,
              "high": 737.71,
              "low": 736.56,
              "open": 737.16,
              "timestamp": 1789214400000,
              "volume": 4409.0
            },
            {
              "close": 736.47,
              "high": 737.03,
              "low": 736.17,
              "open": 736.81,
              "timestamp": 1789215300000,
              "volume": 4407.0
            },
            {
              "close": 736.92,
              "high": 737.96,
              "low": 736.47,
              "open": 736.47,
              "timestamp": 1789216200000,
              "volume": 4400.0
            },
            {
              "close": 736.75,
              "high": 737.37,
              "low": 736.08,
              "open": 736.92,
              "timestamp": 1789217100000,
              "volume": 4406.0
            },
            {
              "close": 735.99,
              "high": 737.23,
              "low": 735.65,
              "open": 736.75,
              "timestamp": 1789218000000,
              "volume": 4428.0
            },
            {
              "close": 736.24,
              "high": 736.57,
              "low": 735.43,
              "open": 735.99,
              "timestamp": 1789218900000,
              "volume": 4422.0
            },
            {
              "close": 736.51,
              "high": 736.8,
              "low": 735.57,
              "open": 736.24,
              "timestamp": 1789219800000,
              "volume": 4391.0
            },
            {
              "close": 737.09,
              "high": 737.1,
              "low": 735.91,
              "open": 736.51,
              "timestamp": 1789220700000,
              "volume": 4405.0
            },
            {
              "close": 736.43,
              "high": 737.25,
              "low": 736.29,
              "open": 737.09,
              "timestamp": 1789221600000,
              "volume": 4406.0
            },
            {
              "close": 735.8,
              "high": 736.63,
              "low": 735.44,
              "open": 736.43,
              "timestamp": 1789222500000,
              "volume": 4399.0
            },
            {
              "close": 735.63,
              "high": 736.28,
              "low": 735.1,
              "open": 735.8,
              "timestamp": 1789223400000,
              "volume": 4405.0
            },
            {
              "close": 736.17,
              "high": 736.17,
              "low": 735.09,
              "open": 735.63,
              "timestamp": 1789224300000,
              "volume": 4407.0
            },
            {
              "close": 737.27,
              "high": 737.37,
              "low": 736.0,
              "open": 736.17,
              "timestamp": 1789225200000,
              "volume": 4436.0
            },
            {
              "close": 736.83,
              "high": 737.45,
              "low": 736.8,
              "open": 737.27,
              "timestamp": 1789226100000,
              "volume": 4415.0
            },
            {
              "close": 736.13,
              "high": 736.89,
              "low": 735.73,
              "open": 736.83,
              "timestamp": 1789227000000,
              "volume": 4391.0
            },
            {
              "close": 735.58,
              "high": 736.31,
              "low": 735.39,
              "open": 736.13,
              "timestamp": 1789227900000,
              "volume": 4388.0
            },
            {
              "close": 734.78,
              "high": 735.62,
              "low": 734.3,
              "open": 735.58,
              "timestamp": 1789228800000,
              "volume": 4411.0
            },
            {
              "close": 734.4,
              "high": 734.97,
              "low": 734.34,
              "open": 734.78,
              "timestamp": 1789229700000,
              "volume": 4393.0
            },
            {
              "close": 732.73,
              "high": 734.64,
              "low": 732.7,
              "open": 734.4,
              "timestamp": 1789230600000,
              "volume": 4420.0
            },
            {
              "close": 732.62,
              "high": 732.99,
              "low": 732.35,
              "open": 732.73,
              "timestamp": 1789231500000,
              "volume": 4409.0
            },
            {
              "close": 732.52,
              "high": 732.85,
              "low": 732.19,
              "open": 732.62,
              "timestamp": 1789232400000,
              "volume": 4407.0
            },
            {
              "close": 731.86,
              "high": 732.75,
              "low": 731.66,
              "open": 732.52,
              "timestamp": 1789233300000,
              "volume": 4394.0
            },
            {
              "close": 731.28,
              "high": 731.95,
              "low": 731.06,
              "open": 731.86,
              "timestamp": 1789234200000,
              "volume": 4407.0
            },
            {
              "close": 731.35,
              "high": 731.52,
              "low": 730.78,
              "open": 731.28,
              "timestamp": 1789235100000,
              "volume": 4368.0
            },
            {
              "close": 730.99,
              "high": 731.49,
              "low": 730.85,
              "open": 731.35,
              "timestamp": 1789236000000,
              "volume": 4349.0
            },
            {
              "close": 731.2,
              "high": 731.31,
              "low": 730.68,
              "open": 730.99,
              "timestamp": 1789236900000,
              "volume": 4387.0
            },
            {
              "close": 730.02,
              "high": 731.47,
              "low": 729.88,
              "open": 731.2,
              "timestamp": 1789237800000,
              "volume": 4346.0
            },
            {
              "close": 729.82,
              "high": 730.1,
              "low": 729.36,
              "open": 730.02,
              "timestamp": 1789238700000,
              "volume": 4290.0
            },
            {
              "close": 728.68,
              "high": 729.92,
              "low": 728.09,
              "open": 729.82,
              "timestamp": 1789239600000,
              "volume": 4385.0
            },
            {
              "close": 726.17,
              "high": 728.68,
              "low": 725.79,
              "open": 728.68,
              "timestamp": 1789240500000,
              "volume": 4353.0
            },
            {
              "close": 725.99,
              "high": 726.39,
              "low": 725.5,
              "open": 726.17,
              "timestamp": 1789241400000,
              "volume": 4322.0
            },
            {
              "close": 726.61,
              "high": 726.89,
              "low": 725.99,
              "open": 725.99,
              "timestamp": 1789242300000,
              "volume": 4380.0
            },
            {
              "close": 727.15,
              "high": 727.5,
              "low": 726.39,
              "open": 726.61,
              "timestamp": 1789243200000,
              "volume": 4372.0
            },
            {
              "close": 727.25,
              "high": 727.25,
              "low": 726.59,
              "open": 727.15,
              "timestamp": 1789244100000,
              "volume": 4349.0
            },
            {
              "close": 727.22,
              "high": 727.68,
              "low": 727.01,
              "open": 727.25,
              "timestamp": 1789245000000,
              "volume": 4364.0
            },
            {
              "close": 726.89,
              "high": 727.53,
              "low": 726.66,
              "open": 727.22,
              "timestamp": 1789245900000,
              "volume": 4305.0
            },
            {
              "close": 727.13,
              "high": 727.68,
              "low": 726.88,
              "open": 726.89,
              "timestamp": 1789246800000,
              "volume": 3403.0
            },
            {
              "close": 727.19,
              "high": 727.19,
              "low": 726.84,
              "open": 727.13,
              "timestamp": 1789247700000,
              "volume": 4333.0
            },
            {
              "close": 727.48,
              "high": 727.65,
              "low": 727.19,
              "open": 727.19,
              "timestamp": 1789248600000,
              "volume": 4343.0
            },
            {
              "close": 726.87,
              "high": 727.48,
              "low": 726.78,
              "open": 727.48,
              "timestamp": 1789249500000,
              "volume": 4363.0
            },
            {
              "close": 726.86,
              "high": 727.37,
              "low": 726.37,
              "open": 726.87,
              "timestamp": 1789250400000,
              "volume": 4311.0
            },
            {
              "close": 726.17,
              "high": 727.69,
              "low": 726.17,
              "open": 726.86,
              "timestamp": 1789251300000,
              "volume": 4298.0
            },
            {
              "close": 726.2,
              "high": 726.59,
              "low": 725.88,
              "open": 726.17,
              "timestamp": 1789252200000,
              "volume": 4339.0
            },
            {
              "close": 726.57,
              "high": 726.57,
              "low": 726.2,
              "open": 726.2,
              "timestamp": 1789253100000,
              "volume": 4298.0
            },
            {
              "close": 727.36,
              "high": 727.44,
              "low": 726.44,
              "open": 726.57,
              "timestamp": 1789254000000,
              "volume": 4357.0
            },
            {
              "close": 727.24,
              "high": 727.77,
              "low": 727.24,
              "open": 727.36,
              "timestamp": 1789254900000,
              "volume": 4288.0
            },
            {
              "close": 727.72,
              "high": 727.82,
              "low": 726.88,
              "open": 727.24,
              "timestamp": 1789255800000,
              "volume": 4303.0
            },
            {
              "close": 727.95,
              "high": 728.37,
              "low": 727.72,
              "open": 727.72,
              "timestamp": 1789256700000,
              "volume": 4277.0
            },
            {
              "close": 727.67,
              "high": 728.22,
              "low": 727.56,
              "open": 727.74,
              "timestamp": 1789257600000,
              "volume": 3982.0
            },
            {
              "close": 727.9,
              "high": 728.2,
              "low": 727.41,
              "open": 727.67,
              "timestamp": 1789258500000,
              "volume": 4155.0
            },
            {
              "close": 727.31,
              "high": 727.93,
              "low": 727.29,
              "open": 727.9,
              "timestamp": 1789259400000,
              "volume": 4319.0
            },
            {
              "close": 728.36,
              "high": 728.37,
              "low": 727.31,
              "open": 727.31,
              "timestamp": 1789260300000,
              "volume": 4368.0
            },
            {
              "close": 729.17,
              "high": 729.46,
              "low": 728.3,
              "open": 728.36,
              "timestamp": 1789261200000,
              "volume": 4399.0
            },
            {
              "close": 729.2,
              "high": 730.19,
              "low": 728.77,
              "open": 729.17,
              "timestamp": 1789262100000,
              "volume": 4387.0
            },
            {
              "close": 729.53,
              "high": 730.11,
              "low": 728.88,
              "open": 729.2,
              "timestamp": 1789263000000,
              "volume": 4370.0
            },
            {
              "close": 728.63,
              "high": 729.53,
              "low": 728.55,
              "open": 729.53,
              "timestamp": 1789263900000,
              "volume": 4338.0
            },
            {
              "close": 728.69,
              "high": 728.73,
              "low": 728.38,
              "open": 728.63,
              "timestamp": 1789264800000,
              "volume": 4330.0
            },
            {
              "close": 728.96,
              "high": 729.16,
              "low": 728.59,
              "open": 728.69,
              "timestamp": 1789265700000,
              "volume": 4314.0
            },
            {
              "close": 728.74,
              "high": 729.37,
              "low": 728.02,
              "open": 728.96,
              "timestamp": 1789266600000,
              "volume": 4343.0
            },
            {
              "close": 728.41,
              "high": 728.74,
              "low": 728.18,
              "open": 728.74,
              "timestamp": 1789267500000,
              "volume": 4246.0
            },
            {
              "close": 728.29,
              "high": 728.9,
              "low": 728.17,
              "open": 728.41,
              "timestamp": 1789268400000,
              "volume": 4294.0
            },
            {
              "close": 728.33,
              "high": 728.9,
              "low": 728.01,
              "open": 728.29,
              "timestamp": 1789269300000,
              "volume": 4393.0
            },
            {
              "close": 728.13,
              "high": 728.33,
              "low": 727.52,
              "open": 728.33,
              "timestamp": 1789270200000,
              "volume": 4384.0
            },
            {
              "close": 727.33,
              "high": 728.13,
              "low": 727.33,
              "open": 728.13,
              "timestamp": 1789271100000,
              "volume": 4393.0
            },
            {
              "close": 726.96,
              "high": 727.58,
              "low": 726.8,
              "open": 727.33,
              "timestamp": 1789272000000,
              "volume": 4419.0
            },
            {
              "close": 727.44,
              "high": 727.8,
              "low": 726.96,
              "open": 726.96,
              "timestamp": 1789272900000,
              "volume": 4388.0
            },
            {
              "close": 727.0,
              "high": 727.62,
              "low": 726.87,
              "open": 727.44,
              "timestamp": 1789273800000,
              "volume": 4390.0
            },
            {
              "close": 726.73,
              "high": 727.01,
              "low": 726.66,
              "open": 727.0,
              "timestamp": 1789274700000,
              "volume": 4353.0
            },
            {
              "close": 726.82,
              "high": 727.09,
              "low": 726.64,
              "open": 726.73,
              "timestamp": 1789275600000,
              "volume": 4376.0
            },
            {
              "close": 726.45,
              "high": 726.82,
              "low": 726.27,
              "open": 726.82,
              "timestamp": 1789276500000,
              "volume": 4377.0
            },
            {
              "close": 726.5,
              "high": 726.76,
              "low": 726.45,
              "open": 726.71,
              "timestamp": 1789277400000,
              "volume": 4362.0
            },
            {
              "close": 726.66,
              "high": 726.75,
              "low": 726.46,
              "open": 726.5,
              "timestamp": 1789278300000,
              "volume": 4387.0
            },
            {
              "close": 726.28,
              "high": 726.66,
              "low": 726.26,
              "open": 726.66,
              "timestamp": 1789279200000,
              "volume": 4398.0
            },
            {
              "close": 724.35,
              "high": 726.28,
              "low": 724.29,
              "open": 726.28,
              "timestamp": 1789280100000,
              "volume": 4382.0
            },
            {
              "close": 724.26,
              "high": 724.4,
              "low": 723.56,
              "open": 724.35,
              "timestamp": 1789281000000,
              "volume": 4410.0
            },
            {
              "close": 722.24,
              "high": 724.26,
              "low": 721.86,
              "open": 724.26,
              "timestamp": 1789281900000,
              "volume": 4409.0
            },
            {
              "close": 723.03,
              "high": 723.31,
              "low": 721.98,
              "open": 722.24,
              "timestamp": 1789282800000,
              "volume": 4373.0
            },
            {
              "close": 723.3,
              "high": 723.93,
              "low": 722.92,
              "open": 723.03,
              "timestamp": 1789283700000,
              "volume": 4390.0
            },
            {
              "close": 723.53,
              "high": 723.83,
              "low": 722.94,
              "open": 723.3,
              "timestamp": 1789284600000,
              "volume": 4385.0
            },
            {
              "close": 722.55,
              "high": 723.53,
              "low": 722.52,
              "open": 723.53,
              "timestamp": 1789285500000,
              "volume": 4392.0
            },
            {
              "close": 722.68,
              "high": 722.94,
              "low": 722.02,
              "open": 722.55,
              "timestamp": 1789286400000,
              "volume": 4400.0
            },
            {
              "close": 721.43,
              "high": 722.73,
              "low": 721.38,
              "open": 722.68,
              "timestamp": 1789287300000,
              "volume": 4384.0
            },
            {
              "close": 717.96,
              "high": 721.43,
              "low": 717.87,
              "open": 721.43,
              "timestamp": 1789288200000,
              "volume": 4456.0
            },
            {
              "close": 718.47,
              "high": 719.16,
              "low": 717.7,
              "open": 717.95,
              "timestamp": 1789289100000,
              "volume": 4393.0
            },
            {
              "close": 718.51,
              "high": 719.4,
              "low": 718.09,
              "open": 718.47,
              "timestamp": 1789290000000,
              "volume": 4418.0
            },
            {
              "close": 715.6,
              "high": 718.51,
              "low": 715.56,
              "open": 718.51,
              "timestamp": 1789290900000,
              "volume": 4418.0
            },
            {
              "close": 716.35,
              "high": 717.57,
              "low": 714.88,
              "open": 715.6,
              "timestamp": 1789291800000,
              "volume": 4429.0
            },
            {
              "close": 716.8,
              "high": 717.17,
              "low": 716.14,
              "open": 716.35,
              "timestamp": 1789292700000,
              "volume": 4404.0
            },
            {
              "close": 716.79,
              "high": 716.99,
              "low": 716.45,
              "open": 716.8,
              "timestamp": 1789293600000,
              "volume": 4396.0
            },
            {
              "close": 716.19,
              "high": 716.95,
              "low": 715.97,
              "open": 716.79,
              "timestamp": 1789294500000,
              "volume": 4375.0
            },
            {
              "close": 715.22,
              "high": 716.89,
              "low": 715.05,
              "open": 716.19,
              "timestamp": 1789295400000,
              "volume": 4408.0
            },
            {
              "close": 715.59,
              "high": 715.8,
              "low": 714.83,
              "open": 715.22,
              "timestamp": 1789296300000,
              "volume": 4423.0
            },
            {
              "close": 715.24,
              "high": 716.17,
              "low": 714.42,
              "open": 715.59,
              "timestamp": 1789297200000,
              "volume": 4409.0
            },
            {
              "close": 715.96,
              "high": 715.99,
              "low": 714.96,
              "open": 715.24,
              "timestamp": 1789298100000,
              "volume": 4356.0
            },
            {
              "close": 716.95,
              "high": 717.0,
              "low": 715.66,
              "open": 715.96,
              "timestamp": 1789299000000,
              "volume": 4390.0
            },
            {
              "close": 716.77,
              "high": 717.31,
              "low": 716.7,
              "open": 716.95,
              "timestamp": 1789299900000,
              "volume": 4366.0
            },
            {
              "close": 716.93,
              "high": 716.96,
              "low": 716.44,
              "open": 716.77,
              "timestamp": 1789300800000,
              "volume": 4406.0
            },
            {
              "close": 716.64,
              "high": 717.37,
              "low": 716.64,
              "open": 716.93,
              "timestamp": 1789301700000,
              "volume": 4374.0
            },
            {
              "close": 715.8,
              "high": 717.18,
              "low": 715.8,
              "open": 716.64,
              "timestamp": 1789302600000,
              "volume": 4386.0
            },
            {
              "close": 715.98,
              "high": 716.1,
              "low": 715.51,
              "open": 715.8,
              "timestamp": 1789303500000,
              "volume": 4381.0
            },
            {
              "close": 716.09,
              "high": 716.25,
              "low": 715.66,
              "open": 715.98,
              "timestamp": 1789304400000,
              "volume": 4390.0
            },
            {
              "close": 714.02,
              "high": 716.13,
              "low": 713.54,
              "open": 716.09,
              "timestamp": 1789305300000,
              "volume": 4411.0
            },
            {
              "close": 716.82,
              "high": 716.82,
              "low": 714.02,
              "open": 714.02,
              "timestamp": 1789306200000,
              "volume": 4420.0
            },
            {
              "close": 718.39,
              "high": 718.78,
              "low": 716.78,
              "open": 716.82,
              "timestamp": 1789307100000,
              "volume": 4433.0
            },
            {
              "close": 719.72,
              "high": 719.75,
              "low": 718.41,
              "open": 718.41,
              "timestamp": 1789308000000,
              "volume": 4443.0
            },
            {
              "close": 719.73,
              "high": 720.4,
              "low": 719.42,
              "open": 719.72,
              "timestamp": 1789308900000,
              "volume": 4418.0
            },
            {
              "close": 719.88,
              "high": 720.66,
              "low": 719.4,
              "open": 719.73,
              "timestamp": 1789309800000,
              "volume": 4424.0
            },
            {
              "close": 718.96,
              "high": 720.21,
              "low": 718.51,
              "open": 719.88,
              "timestamp": 1789310700000,
              "volume": 4406.0
            },
            {
              "close": 718.12,
              "high": 719.03,
              "low": 717.75,
              "open": 718.96,
              "timestamp": 1789311600000,
              "volume": 4433.0
            },
            {
              "close": 718.59,
              "high": 719.69,
              "low": 717.75,
              "open": 718.12,
              "timestamp": 1789312500000,
              "volume": 4447.0
            },
            {
              "close": 719.87,
              "high": 720.1,
              "low": 718.49,
              "open": 718.59,
              "timestamp": 1789313400000,
              "volume": 4395.0
            },
            {
              "close": 719.14,
              "high": 719.87,
              "low": 719.0,
              "open": 719.87,
              "timestamp": 1789314300000,
              "volume": 4383.0
            },
            {
              "close": 721.12,
              "high": 721.77,
              "low": 719.14,
              "open": 719.14,
              "timestamp": 1789315200000,
              "volume": 4445.0
            },
            {
              "close": 721.39,
              "high": 721.51,
              "low": 720.68,
              "open": 721.12,
              "timestamp": 1789316100000,
              "volume": 4410.0
            },
            {
              "close": 721.52,
              "high": 721.65,
              "low": 720.83,
              "open": 721.39,
              "timestamp": 1789317000000,
              "volume": 4407.0
            },
            {
              "close": 721.36,
              "high": 721.67,
              "low": 720.88,
              "open": 721.52,
              "timestamp": 1789317900000,
              "volume": 4396.0
            },
            {
              "close": 721.72,
              "high": 722.56,
              "low": 721.31,
              "open": 721.36,
              "timestamp": 1789318800000,
              "volume": 4423.0
            },
            {
              "close": 721.7,
              "high": 721.93,
              "low": 721.29,
              "open": 721.72,
              "timestamp": 1789319700000,
              "volume": 4405.0
            },
            {
              "close": 721.32,
              "high": 721.7,
              "low": 721.16,
              "open": 721.7,
              "timestamp": 1789320600000,
              "volume": 4405.0
            },
            {
              "close": 721.58,
              "high": 721.99,
              "low": 721.26,
              "open": 721.32,
              "timestamp": 1789321500000,
              "volume": 4361.0
            },
            {
              "close": 721.62,
              "high": 721.76,
              "low": 721.16,
              "open": 721.58,
              "timestamp": 1789322400000,
              "volume": 4371.0
            },
            {
              "close": 721.86,
              "high": 722.18,
              "low": 721.23,
              "open": 721.62,
              "timestamp": 1789323300000,
              "volume": 4386.0
            },
            {
              "close": 721.66,
              "high": 722.39,
              "low": 721.43,
              "open": 721.86,
              "timestamp": 1789324200000,
              "volume": 4349.0
            },
            {
              "close": 722.44,
              "high": 722.71,
              "low": 721.52,
              "open": 721.66,
              "timestamp": 1789325100000,
              "volume": 4367.0
            },
            {
              "close": 721.76,
              "high": 723.56,
              "low": 721.76,
              "open": 722.44,
              "timestamp": 1789326000000,
              "volume": 4412.0
            },
            {
              "close": 721.68,
              "high": 721.84,
              "low": 721.2,
              "open": 721.76,
              "timestamp": 1789326900000,
              "volume": 4431.0
            },
            {
              "close": 721.77,
              "high": 721.84,
              "low": 721.38,
              "open": 721.68,
              "timestamp": 1789327800000,
              "volume": 4389.0
            },
            {
              "close": 721.44,
              "high": 721.91,
              "low": 721.17,
              "open": 721.77,
              "timestamp": 1789328700000,
              "volume": 4334.0
            }
          ],
          "last_price": 721.44,
          "momentum": "neutral",
          "rsi_14": 55.58,
          "structure": "bullish"
        },
        "1H": {
          "candle_count": 168,
          "candle_status": {
            "data_age_seconds": 3693,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789326000000,
            "latest_timestamp_utc": "2026-09-13T19:00:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 3600
          },
          "candles": [
            {
              "close": 751.91,
              "high": 752.16,
              "low": 749.39,
              "open": 749.63,
              "timestamp": 1788724800000,
              "volume": 16873.0
            },
            {
              "close": 751.83,
              "high": 754.27,
              "low": 751.55,
              "open": 751.91,
              "timestamp": 1788728400000,
              "volume": 17794.0
            },
            {
              "close": 751.91,
              "high": 752.35,
              "low": 748.74,
              "open": 751.83,
              "timestamp": 1788732000000,
              "volume": 17832.0
            },
            {
              "close": 753.47,
              "high": 755.34,
              "low": 751.47,
              "open": 751.91,
              "timestamp": 1788735600000,
              "volume": 17819.0
            },
            {
              "close": 750.93,
              "high": 757.0,
              "low": 750.43,
              "open": 753.47,
              "timestamp": 1788739200000,
              "volume": 17844.0
            },
            {
              "close": 749.16,
              "high": 751.52,
              "low": 746.07,
              "open": 750.93,
              "timestamp": 1788742800000,
              "volume": 17888.0
            },
            {
              "close": 748.99,
              "high": 756.23,
              "low": 747.76,
              "open": 749.16,
              "timestamp": 1788746400000,
              "volume": 17876.0
            },
            {
              "close": 746.7,
              "high": 750.64,
              "low": 745.47,
              "open": 748.99,
              "timestamp": 1788750000000,
              "volume": 17870.0
            },
            {
              "close": 747.58,
              "high": 747.99,
              "low": 745.92,
              "open": 746.7,
              "timestamp": 1788753600000,
              "volume": 17828.0
            },
            {
              "close": 749.04,
              "high": 750.61,
              "low": 747.21,
              "open": 747.58,
              "timestamp": 1788757200000,
              "volume": 17835.0
            },
            {
              "close": 745.96,
              "high": 749.79,
              "low": 745.5,
              "open": 749.04,
              "timestamp": 1788760800000,
              "volume": 17817.0
            },
            {
              "close": 744.39,
              "high": 746.01,
              "low": 740.85,
              "open": 745.96,
              "timestamp": 1788764400000,
              "volume": 17862.0
            },
            {
              "close": 745.66,
              "high": 746.02,
              "low": 744.3,
              "open": 744.39,
              "timestamp": 1788768000000,
              "volume": 17814.0
            },
            {
              "close": 743.28,
              "high": 747.18,
              "low": 743.09,
              "open": 745.66,
              "timestamp": 1788771600000,
              "volume": 17811.0
            },
            {
              "close": 744.19,
              "high": 745.46,
              "low": 743.04,
              "open": 743.28,
              "timestamp": 1788775200000,
              "volume": 17779.0
            },
            {
              "close": 745.4,
              "high": 745.4,
              "low": 743.66,
              "open": 744.19,
              "timestamp": 1788778800000,
              "volume": 17767.0
            },
            {
              "close": 747.57,
              "high": 747.84,
              "low": 745.01,
              "open": 745.4,
              "timestamp": 1788782400000,
              "volume": 17807.0
            },
            {
              "close": 745.99,
              "high": 748.07,
              "low": 744.5,
              "open": 747.57,
              "timestamp": 1788786000000,
              "volume": 17864.0
            },
            {
              "close": 743.97,
              "high": 746.04,
              "low": 741.32,
              "open": 745.99,
              "timestamp": 1788789600000,
              "volume": 17890.0
            },
            {
              "close": 735.11,
              "high": 743.97,
              "low": 734.27,
              "open": 743.97,
              "timestamp": 1788793200000,
              "volume": 17909.0
            },
            {
              "close": 740.4,
              "high": 740.6,
              "low": 734.8,
              "open": 735.12,
              "timestamp": 1788796800000,
              "volume": 17789.0
            },
            {
              "close": 741.15,
              "high": 742.01,
              "low": 739.71,
              "open": 740.4,
              "timestamp": 1788800400000,
              "volume": 17779.0
            },
            {
              "close": 740.2,
              "high": 741.73,
              "low": 739.03,
              "open": 741.15,
              "timestamp": 1788804000000,
              "volume": 17760.0
            },
            {
              "close": 742.27,
              "high": 742.47,
              "low": 739.37,
              "open": 740.2,
              "timestamp": 1788807600000,
              "volume": 17650.0
            },
            {
              "close": 740.6,
              "high": 742.4,
              "low": 739.48,
              "open": 742.27,
              "timestamp": 1788811200000,
              "volume": 17706.0
            },
            {
              "close": 739.68,
              "high": 740.7,
              "low": 739.07,
              "open": 740.6,
              "timestamp": 1788814800000,
              "volume": 16324.0
            },
            {
              "close": 738.85,
              "high": 740.24,
              "low": 736.41,
              "open": 739.68,
              "timestamp": 1788818400000,
              "volume": 17218.0
            },
            {
              "close": 740.39,
              "high": 741.32,
              "low": 738.57,
              "open": 738.85,
              "timestamp": 1788822000000,
              "volume": 17763.0
            },
            {
              "close": 741.01,
              "high": 741.7,
              "low": 738.75,
              "open": 740.39,
              "timestamp": 1788825600000,
              "volume": 17656.0
            },
            {
              "close": 742.93,
              "high": 743.36,
              "low": 740.58,
              "open": 741.04,
              "timestamp": 1788829200000,
              "volume": 17748.0
            },
            {
              "close": 738.8,
              "high": 743.87,
              "low": 738.79,
              "open": 742.93,
              "timestamp": 1788832800000,
              "volume": 17706.0
            },
            {
              "close": 743.28,
              "high": 745.74,
              "low": 737.28,
              "open": 738.8,
              "timestamp": 1788836400000,
              "volume": 17880.0
            },
            {
              "close": 745.89,
              "high": 747.32,
              "low": 742.13,
              "open": 743.28,
              "timestamp": 1788840000000,
              "volume": 17873.0
            },
            {
              "close": 751.29,
              "high": 754.85,
              "low": 744.1,
              "open": 745.89,
              "timestamp": 1788843600000,
              "volume": 17910.0
            },
            {
              "close": 748.0,
              "high": 751.68,
              "low": 745.45,
              "open": 751.29,
              "timestamp": 1788847200000,
              "volume": 17862.0
            },
            {
              "close": 755.1,
              "high": 758.03,
              "low": 747.77,
              "open": 748.0,
              "timestamp": 1788850800000,
              "volume": 17895.0
            },
            {
              "close": 755.36,
              "high": 761.57,
              "low": 753.84,
              "open": 755.1,
              "timestamp": 1788854400000,
              "volume": 17920.0
            },
            {
              "close": 755.05,
              "high": 757.47,
              "low": 750.59,
              "open": 755.33,
              "timestamp": 1788858000000,
              "volume": 17891.0
            },
            {
              "close": 756.65,
              "high": 758.47,
              "low": 753.89,
              "open": 755.05,
              "timestamp": 1788861600000,
              "volume": 17760.0
            },
            {
              "close": 752.75,
              "high": 757.18,
              "low": 750.79,
              "open": 756.65,
              "timestamp": 1788865200000,
              "volume": 17884.0
            },
            {
              "close": 752.14,
              "high": 753.14,
              "low": 749.73,
              "open": 752.75,
              "timestamp": 1788868800000,
              "volume": 17865.0
            },
            {
              "close": 747.48,
              "high": 753.27,
              "low": 742.65,
              "open": 752.14,
              "timestamp": 1788872400000,
              "volume": 17901.0
            },
            {
              "close": 751.1,
              "high": 751.98,
              "low": 746.43,
              "open": 747.43,
              "timestamp": 1788876000000,
              "volume": 17940.0
            },
            {
              "close": 756.66,
              "high": 757.4,
              "low": 749.63,
              "open": 751.1,
              "timestamp": 1788879600000,
              "volume": 17916.0
            },
            {
              "close": 756.1,
              "high": 758.36,
              "low": 753.8,
              "open": 756.66,
              "timestamp": 1788883200000,
              "volume": 17903.0
            },
            {
              "close": 752.37,
              "high": 756.95,
              "low": 752.23,
              "open": 756.1,
              "timestamp": 1788886800000,
              "volume": 17860.0
            },
            {
              "close": 749.58,
              "high": 754.69,
              "low": 747.92,
              "open": 752.37,
              "timestamp": 1788890400000,
              "volume": 17722.0
            },
            {
              "close": 749.26,
              "high": 750.64,
              "low": 747.8,
              "open": 749.58,
              "timestamp": 1788894000000,
              "volume": 17863.0
            },
            {
              "close": 751.35,
              "high": 751.99,
              "low": 749.26,
              "open": 749.26,
              "timestamp": 1788897600000,
              "volume": 17812.0
            },
            {
              "close": 752.25,
              "high": 753.35,
              "low": 751.26,
              "open": 751.35,
              "timestamp": 1788901200000,
              "volume": 16584.0
            },
            {
              "close": 755.21,
              "high": 755.34,
              "low": 751.41,
              "open": 752.25,
              "timestamp": 1788904800000,
              "volume": 17098.0
            },
            {
              "close": 752.45,
              "high": 755.33,
              "low": 752.45,
              "open": 755.21,
              "timestamp": 1788908400000,
              "volume": 17623.0
            },
            {
              "close": 755.04,
              "high": 757.27,
              "low": 752.42,
              "open": 752.46,
              "timestamp": 1788912000000,
              "volume": 17686.0
            },
            {
              "close": 754.97,
              "high": 756.52,
              "low": 750.6,
              "open": 755.04,
              "timestamp": 1788915600000,
              "volume": 17691.0
            },
            {
              "close": 752.06,
              "high": 755.45,
              "low": 751.69,
              "open": 754.97,
              "timestamp": 1788919200000,
              "volume": 17751.0
            },
            {
              "close": 749.8,
              "high": 752.06,
              "low": 747.52,
              "open": 752.06,
              "timestamp": 1788922800000,
              "volume": 17789.0
            },
            {
              "close": 755.04,
              "high": 755.77,
              "low": 749.8,
              "open": 749.8,
              "timestamp": 1788926400000,
              "volume": 17801.0
            },
            {
              "close": 751.99,
              "high": 755.49,
              "low": 750.58,
              "open": 755.04,
              "timestamp": 1788930000000,
              "volume": 17851.0
            },
            {
              "close": 755.2,
              "high": 756.63,
              "low": 751.48,
              "open": 751.99,
              "timestamp": 1788933600000,
              "volume": 17803.0
            },
            {
              "close": 754.93,
              "high": 757.94,
              "low": 753.1,
              "open": 755.2,
              "timestamp": 1788937200000,
              "volume": 17821.0
            },
            {
              "close": 757.81,
              "high": 757.99,
              "low": 754.18,
              "open": 754.93,
              "timestamp": 1788940800000,
              "volume": 17833.0
            },
            {
              "close": 751.42,
              "high": 757.93,
              "low": 751.13,
              "open": 757.81,
              "timestamp": 1788944400000,
              "volume": 17869.0
            },
            {
              "close": 750.9,
              "high": 752.61,
              "low": 749.57,
              "open": 751.42,
              "timestamp": 1788948000000,
              "volume": 17880.0
            },
            {
              "close": 750.53,
              "high": 751.92,
              "low": 748.0,
              "open": 750.9,
              "timestamp": 1788951600000,
              "volume": 17868.0
            },
            {
              "close": 750.69,
              "high": 752.04,
              "low": 749.93,
              "open": 750.53,
              "timestamp": 1788955200000,
              "volume": 17878.0
            },
            {
              "close": 745.6,
              "high": 751.47,
              "low": 745.3,
              "open": 750.69,
              "timestamp": 1788958800000,
              "volume": 17897.0
            },
            {
              "close": 743.84,
              "high": 747.06,
              "low": 741.93,
              "open": 745.6,
              "timestamp": 1788962400000,
              "volume": 17939.0
            },
            {
              "close": 739.38,
              "high": 746.52,
              "low": 735.1,
              "open": 743.84,
              "timestamp": 1788966000000,
              "volume": 17282.0
            },
            {
              "close": 741.03,
              "high": 742.13,
              "low": 738.11,
              "open": 739.38,
              "timestamp": 1788969600000,
              "volume": 17906.0
            },
            {
              "close": 741.65,
              "high": 742.57,
              "low": 740.36,
              "open": 741.03,
              "timestamp": 1788973200000,
              "volume": 17888.0
            },
            {
              "close": 740.26,
              "high": 741.84,
              "low": 739.96,
              "open": 741.65,
              "timestamp": 1788976800000,
              "volume": 17854.0
            },
            {
              "close": 737.56,
              "high": 742.0,
              "low": 736.67,
              "open": 740.26,
              "timestamp": 1788980400000,
              "volume": 17864.0
            },
            {
              "close": 734.15,
              "high": 738.34,
              "low": 732.48,
              "open": 737.56,
              "timestamp": 1788984000000,
              "volume": 17847.0
            },
            {
              "close": 725.74,
              "high": 734.16,
              "low": 722.64,
              "open": 734.15,
              "timestamp": 1788987600000,
              "volume": 16575.0
            },
            {
              "close": 719.23,
              "high": 726.38,
              "low": 717.72,
              "open": 725.74,
              "timestamp": 1788991200000,
              "volume": 17301.0
            },
            {
              "close": 722.77,
              "high": 723.92,
              "low": 718.98,
              "open": 719.25,
              "timestamp": 1788994800000,
              "volume": 17858.0
            },
            {
              "close": 721.11,
              "high": 724.56,
              "low": 720.76,
              "open": 722.77,
              "timestamp": 1788998400000,
              "volume": 17829.0
            },
            {
              "close": 721.1,
              "high": 724.9,
              "low": 717.24,
              "open": 721.11,
              "timestamp": 1789002000000,
              "volume": 17915.0
            },
            {
              "close": 725.35,
              "high": 725.38,
              "low": 720.79,
              "open": 721.1,
              "timestamp": 1789005600000,
              "volume": 17893.0
            },
            {
              "close": 723.79,
              "high": 726.46,
              "low": 723.27,
              "open": 725.35,
              "timestamp": 1789009200000,
              "volume": 17843.0
            },
            {
              "close": 722.83,
              "high": 723.98,
              "low": 722.08,
              "open": 723.79,
              "timestamp": 1789012800000,
              "volume": 17825.0
            },
            {
              "close": 723.62,
              "high": 723.89,
              "low": 721.0,
              "open": 722.83,
              "timestamp": 1789016400000,
              "volume": 17843.0
            },
            {
              "close": 721.24,
              "high": 723.65,
              "low": 718.47,
              "open": 723.62,
              "timestamp": 1789020000000,
              "volume": 17874.0
            },
            {
              "close": 719.22,
              "high": 721.29,
              "low": 715.56,
              "open": 721.24,
              "timestamp": 1789023600000,
              "volume": 17888.0
            },
            {
              "close": 718.66,
              "high": 719.83,
              "low": 718.41,
              "open": 719.22,
              "timestamp": 1789027200000,
              "volume": 17799.0
            },
            {
              "close": 717.62,
              "high": 719.34,
              "low": 715.68,
              "open": 718.66,
              "timestamp": 1789030800000,
              "volume": 17857.0
            },
            {
              "close": 717.23,
              "high": 718.87,
              "low": 716.54,
              "open": 717.58,
              "timestamp": 1789034400000,
              "volume": 17825.0
            },
            {
              "close": 716.65,
              "high": 719.25,
              "low": 715.8,
              "open": 717.23,
              "timestamp": 1789038000000,
              "volume": 17830.0
            },
            {
              "close": 705.82,
              "high": 718.38,
              "low": 703.54,
              "open": 716.65,
              "timestamp": 1789041600000,
              "volume": 17919.0
            },
            {
              "close": 710.64,
              "high": 711.16,
              "low": 705.24,
              "open": 705.74,
              "timestamp": 1789045200000,
              "volume": 17934.0
            },
            {
              "close": 710.2,
              "high": 712.06,
              "low": 707.19,
              "open": 710.64,
              "timestamp": 1789048800000,
              "volume": 17738.0
            },
            {
              "close": 708.16,
              "high": 710.8,
              "low": 706.72,
              "open": 710.2,
              "timestamp": 1789052400000,
              "volume": 17916.0
            },
            {
              "close": 708.61,
              "high": 709.43,
              "low": 704.65,
              "open": 708.16,
              "timestamp": 1789056000000,
              "volume": 17908.0
            },
            {
              "close": 713.05,
              "high": 713.92,
              "low": 708.21,
              "open": 708.66,
              "timestamp": 1789059600000,
              "volume": 17901.0
            },
            {
              "close": 714.34,
              "high": 714.34,
              "low": 710.53,
              "open": 713.0,
              "timestamp": 1789063200000,
              "volume": 17859.0
            },
            {
              "close": 714.68,
              "high": 716.33,
              "low": 713.47,
              "open": 714.34,
              "timestamp": 1789066800000,
              "volume": 17872.0
            },
            {
              "close": 715.37,
              "high": 716.67,
              "low": 714.14,
              "open": 714.68,
              "timestamp": 1789070400000,
              "volume": 17772.0
            },
            {
              "close": 714.78,
              "high": 715.86,
              "low": 714.18,
              "open": 715.37,
              "timestamp": 1789074000000,
              "volume": 16485.0
            },
            {
              "close": 712.32,
              "high": 716.18,
              "low": 711.78,
              "open": 714.78,
              "timestamp": 1789077600000,
              "volume": 17166.0
            },
            {
              "close": 709.13,
              "high": 712.99,
              "low": 708.79,
              "open": 712.32,
              "timestamp": 1789081200000,
              "volume": 17862.0
            },
            {
              "close": 713.87,
              "high": 713.91,
              "low": 709.13,
              "open": 709.13,
              "timestamp": 1789084800000,
              "volume": 17808.0
            },
            {
              "close": 713.9,
              "high": 715.29,
              "low": 711.13,
              "open": 713.87,
              "timestamp": 1789088400000,
              "volume": 17869.0
            },
            {
              "close": 711.64,
              "high": 714.05,
              "low": 710.74,
              "open": 713.9,
              "timestamp": 1789092000000,
              "volume": 17799.0
            },
            {
              "close": 712.62,
              "high": 712.9,
              "low": 710.53,
              "open": 711.64,
              "timestamp": 1789095600000,
              "volume": 17810.0
            },
            {
              "close": 717.04,
              "high": 717.77,
              "low": 712.47,
              "open": 712.62,
              "timestamp": 1789099200000,
              "volume": 17843.0
            },
            {
              "close": 717.03,
              "high": 717.7,
              "low": 715.68,
              "open": 717.04,
              "timestamp": 1789102800000,
              "volume": 17735.0
            },
            {
              "close": 715.6,
              "high": 717.48,
              "low": 714.55,
              "open": 717.03,
              "timestamp": 1789106400000,
              "volume": 17636.0
            },
            {
              "close": 714.09,
              "high": 716.36,
              "low": 713.31,
              "open": 715.6,
              "timestamp": 1789110000000,
              "volume": 17703.0
            },
            {
              "close": 714.33,
              "high": 716.35,
              "low": 712.88,
              "open": 714.09,
              "timestamp": 1789113600000,
              "volume": 17659.0
            },
            {
              "close": 713.26,
              "high": 714.63,
              "low": 711.37,
              "open": 714.39,
              "timestamp": 1789117200000,
              "volume": 17679.0
            },
            {
              "close": 713.03,
              "high": 715.28,
              "low": 712.65,
              "open": 713.26,
              "timestamp": 1789120800000,
              "volume": 17813.0
            },
            {
              "close": 713.64,
              "high": 713.67,
              "low": 710.69,
              "open": 713.02,
              "timestamp": 1789124400000,
              "volume": 17813.0
            },
            {
              "close": 723.99,
              "high": 725.0,
              "low": 707.01,
              "open": 713.64,
              "timestamp": 1789128000000,
              "volume": 17889.0
            },
            {
              "close": 737.09,
              "high": 737.16,
              "low": 717.28,
              "open": 723.99,
              "timestamp": 1789131600000,
              "volume": 17807.0
            },
            {
              "close": 733.3,
              "high": 741.67,
              "low": 730.32,
              "open": 737.09,
              "timestamp": 1789135200000,
              "volume": 17850.0
            },
            {
              "close": 728.88,
              "high": 740.77,
              "low": 726.98,
              "open": 733.3,
              "timestamp": 1789138800000,
              "volume": 17918.0
            },
            {
              "close": 730.74,
              "high": 733.94,
              "low": 727.69,
              "open": 728.87,
              "timestamp": 1789142400000,
              "volume": 17934.0
            },
            {
              "close": 727.79,
              "high": 731.45,
              "low": 726.91,
              "open": 730.74,
              "timestamp": 1789146000000,
              "volume": 17898.0
            },
            {
              "close": 722.63,
              "high": 728.33,
              "low": 721.17,
              "open": 727.79,
              "timestamp": 1789149600000,
              "volume": 17918.0
            },
            {
              "close": 725.37,
              "high": 726.26,
              "low": 721.59,
              "open": 722.63,
              "timestamp": 1789153200000,
              "volume": 17916.0
            },
            {
              "close": 726.54,
              "high": 727.97,
              "low": 724.75,
              "open": 725.37,
              "timestamp": 1789156800000,
              "volume": 17834.0
            },
            {
              "close": 723.57,
              "high": 727.89,
              "low": 723.2,
              "open": 726.54,
              "timestamp": 1789160400000,
              "volume": 16528.0
            },
            {
              "close": 724.65,
              "high": 725.91,
              "low": 722.09,
              "open": 723.57,
              "timestamp": 1789164000000,
              "volume": 17143.0
            },
            {
              "close": 727.1,
              "high": 728.1,
              "low": 724.14,
              "open": 724.65,
              "timestamp": 1789167600000,
              "volume": 17660.0
            },
            {
              "close": 727.02,
              "high": 728.87,
              "low": 726.44,
              "open": 727.1,
              "timestamp": 1789171200000,
              "volume": 17481.0
            },
            {
              "close": 730.68,
              "high": 731.33,
              "low": 726.44,
              "open": 727.02,
              "timestamp": 1789174800000,
              "volume": 17663.0
            },
            {
              "close": 732.15,
              "high": 732.23,
              "low": 729.73,
              "open": 730.68,
              "timestamp": 1789178400000,
              "volume": 17633.0
            },
            {
              "close": 733.92,
              "high": 736.72,
              "low": 732.11,
              "open": 732.15,
              "timestamp": 1789182000000,
              "volume": 17672.0
            },
            {
              "close": 734.1,
              "high": 735.8,
              "low": 733.44,
              "open": 733.92,
              "timestamp": 1789185600000,
              "volume": 17630.0
            },
            {
              "close": 733.41,
              "high": 735.75,
              "low": 732.68,
              "open": 734.1,
              "timestamp": 1789189200000,
              "volume": 17603.0
            },
            {
              "close": 732.24,
              "high": 733.83,
              "low": 731.94,
              "open": 733.41,
              "timestamp": 1789192800000,
              "volume": 17609.0
            },
            {
              "close": 733.89,
              "high": 734.99,
              "low": 732.11,
              "open": 732.24,
              "timestamp": 1789196400000,
              "volume": 17600.0
            },
            {
              "close": 735.29,
              "high": 735.32,
              "low": 733.01,
              "open": 733.89,
              "timestamp": 1789200000000,
              "volume": 17619.0
            },
            {
              "close": 735.8,
              "high": 737.26,
              "low": 734.83,
              "open": 735.29,
              "timestamp": 1789203600000,
              "volume": 17582.0
            },
            {
              "close": 738.25,
              "high": 740.33,
              "low": 735.71,
              "open": 735.8,
              "timestamp": 1789207200000,
              "volume": 17667.0
            },
            {
              "close": 737.16,
              "high": 738.6,
              "low": 736.39,
              "open": 738.25,
              "timestamp": 1789210800000,
              "volume": 17634.0
            },
            {
              "close": 736.75,
              "high": 737.96,
              "low": 736.08,
              "open": 737.16,
              "timestamp": 1789214400000,
              "volume": 17622.0
            },
            {
              "close": 737.09,
              "high": 737.23,
              "low": 735.43,
              "open": 736.75,
              "timestamp": 1789218000000,
              "volume": 17646.0
            },
            {
              "close": 736.17,
              "high": 737.25,
              "low": 735.09,
              "open": 737.09,
              "timestamp": 1789221600000,
              "volume": 17617.0
            },
            {
              "close": 735.58,
              "high": 737.45,
              "low": 735.39,
              "open": 736.17,
              "timestamp": 1789225200000,
              "volume": 17630.0
            },
            {
              "close": 732.62,
              "high": 735.62,
              "low": 732.35,
              "open": 735.58,
              "timestamp": 1789228800000,
              "volume": 17633.0
            },
            {
              "close": 731.35,
              "high": 732.85,
              "low": 730.78,
              "open": 732.62,
              "timestamp": 1789232400000,
              "volume": 17576.0
            },
            {
              "close": 729.82,
              "high": 731.49,
              "low": 729.36,
              "open": 731.35,
              "timestamp": 1789236000000,
              "volume": 17372.0
            },
            {
              "close": 726.61,
              "high": 729.92,
              "low": 725.5,
              "open": 729.82,
              "timestamp": 1789239600000,
              "volume": 17440.0
            },
            {
              "close": 726.89,
              "high": 727.68,
              "low": 726.39,
              "open": 726.61,
              "timestamp": 1789243200000,
              "volume": 17390.0
            },
            {
              "close": 726.87,
              "high": 727.68,
              "low": 726.78,
              "open": 726.89,
              "timestamp": 1789246800000,
              "volume": 16442.0
            },
            {
              "close": 726.57,
              "high": 727.69,
              "low": 725.88,
              "open": 726.87,
              "timestamp": 1789250400000,
              "volume": 17246.0
            },
            {
              "close": 727.95,
              "high": 728.37,
              "low": 726.44,
              "open": 726.57,
              "timestamp": 1789254000000,
              "volume": 17225.0
            },
            {
              "close": 728.36,
              "high": 728.37,
              "low": 727.29,
              "open": 727.74,
              "timestamp": 1789257600000,
              "volume": 16824.0
            },
            {
              "close": 728.63,
              "high": 730.19,
              "low": 728.3,
              "open": 728.36,
              "timestamp": 1789261200000,
              "volume": 17494.0
            },
            {
              "close": 728.41,
              "high": 729.37,
              "low": 728.02,
              "open": 728.63,
              "timestamp": 1789264800000,
              "volume": 17233.0
            },
            {
              "close": 727.33,
              "high": 728.9,
              "low": 727.33,
              "open": 728.41,
              "timestamp": 1789268400000,
              "volume": 17464.0
            },
            {
              "close": 726.73,
              "high": 727.8,
              "low": 726.66,
              "open": 727.33,
              "timestamp": 1789272000000,
              "volume": 17550.0
            },
            {
              "close": 726.66,
              "high": 727.09,
              "low": 726.27,
              "open": 726.73,
              "timestamp": 1789275600000,
              "volume": 17502.0
            },
            {
              "close": 722.24,
              "high": 726.66,
              "low": 721.86,
              "open": 726.66,
              "timestamp": 1789279200000,
              "volume": 17599.0
            },
            {
              "close": 722.55,
              "high": 723.93,
              "low": 721.98,
              "open": 722.24,
              "timestamp": 1789282800000,
              "volume": 17540.0
            },
            {
              "close": 718.47,
              "high": 722.94,
              "low": 717.7,
              "open": 722.55,
              "timestamp": 1789286400000,
              "volume": 17633.0
            },
            {
              "close": 716.8,
              "high": 719.4,
              "low": 714.88,
              "open": 718.47,
              "timestamp": 1789290000000,
              "volume": 17669.0
            },
            {
              "close": 715.59,
              "high": 716.99,
              "low": 714.83,
              "open": 716.8,
              "timestamp": 1789293600000,
              "volume": 17602.0
            },
            {
              "close": 716.77,
              "high": 717.31,
              "low": 714.42,
              "open": 715.59,
              "timestamp": 1789297200000,
              "volume": 17521.0
            },
            {
              "close": 715.98,
              "high": 717.37,
              "low": 715.51,
              "open": 716.77,
              "timestamp": 1789300800000,
              "volume": 17547.0
            },
            {
              "close": 718.39,
              "high": 718.78,
              "low": 713.54,
              "open": 715.98,
              "timestamp": 1789304400000,
              "volume": 17654.0
            },
            {
              "close": 718.96,
              "high": 720.66,
              "low": 718.41,
              "open": 718.41,
              "timestamp": 1789308000000,
              "volume": 17691.0
            },
            {
              "close": 719.14,
              "high": 720.1,
              "low": 717.75,
              "open": 718.96,
              "timestamp": 1789311600000,
              "volume": 17658.0
            },
            {
              "close": 721.36,
              "high": 721.77,
              "low": 719.14,
              "open": 719.14,
              "timestamp": 1789315200000,
              "volume": 17658.0
            },
            {
              "close": 721.58,
              "high": 722.56,
              "low": 721.16,
              "open": 721.36,
              "timestamp": 1789318800000,
              "volume": 17594.0
            },
            {
              "close": 722.44,
              "high": 722.71,
              "low": 721.16,
              "open": 721.58,
              "timestamp": 1789322400000,
              "volume": 17473.0
            },
            {
              "close": 721.44,
              "high": 723.56,
              "low": 721.17,
              "open": 722.44,
              "timestamp": 1789326000000,
              "volume": 17566.0
            }
          ],
          "last_price": 721.44,
          "momentum": "neutral",
          "rsi_14": 45.15,
          "structure": "neutral"
        },
        "4H": {
          "candle_count": 84,
          "candle_status": {
            "data_age_seconds": 14493,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789315200000,
            "latest_timestamp_utc": "2026-09-13T16:00:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 14400
          },
          "candles": [
            {
              "close": 685.02,
              "high": 700.78,
              "low": 679.3,
              "open": 699.95,
              "timestamp": 1788120000000,
              "volume": 70116.0
            },
            {
              "close": 685.67,
              "high": 688.74,
              "low": 682.53,
              "open": 685.02,
              "timestamp": 1788134400000,
              "volume": 71437.0
            },
            {
              "close": 687.12,
              "high": 688.49,
              "low": 683.08,
              "open": 685.67,
              "timestamp": 1788148800000,
              "volume": 71107.0
            },
            {
              "close": 687.42,
              "high": 689.93,
              "low": 685.06,
              "open": 687.12,
              "timestamp": 1788163200000,
              "volume": 71152.0
            },
            {
              "close": 689.92,
              "high": 691.79,
              "low": 684.62,
              "open": 687.42,
              "timestamp": 1788177600000,
              "volume": 71533.0
            },
            {
              "close": 691.96,
              "high": 694.9,
              "low": 688.39,
              "open": 689.92,
              "timestamp": 1788192000000,
              "volume": 71382.0
            },
            {
              "close": 691.66,
              "high": 693.39,
              "low": 690.33,
              "open": 691.96,
              "timestamp": 1788206400000,
              "volume": 68674.0
            },
            {
              "close": 693.86,
              "high": 695.22,
              "low": 690.42,
              "open": 691.66,
              "timestamp": 1788220800000,
              "volume": 70456.0
            },
            {
              "close": 690.87,
              "high": 694.69,
              "low": 689.31,
              "open": 693.79,
              "timestamp": 1788235200000,
              "volume": 70799.0
            },
            {
              "close": 687.69,
              "high": 691.09,
              "low": 685.8,
              "open": 690.87,
              "timestamp": 1788249600000,
              "volume": 71132.0
            },
            {
              "close": 687.08,
              "high": 689.13,
              "low": 683.79,
              "open": 687.69,
              "timestamp": 1788264000000,
              "volume": 71390.0
            },
            {
              "close": 680.2,
              "high": 687.23,
              "low": 675.0,
              "open": 687.08,
              "timestamp": 1788278400000,
              "volume": 71339.0
            },
            {
              "close": 683.34,
              "high": 684.42,
              "low": 677.96,
              "open": 680.2,
              "timestamp": 1788292800000,
              "volume": 68558.0
            },
            {
              "close": 687.83,
              "high": 689.92,
              "low": 679.95,
              "open": 683.34,
              "timestamp": 1788307200000,
              "volume": 71268.0
            },
            {
              "close": 688.03,
              "high": 690.02,
              "low": 686.25,
              "open": 687.83,
              "timestamp": 1788321600000,
              "volume": 71209.0
            },
            {
              "close": 684.21,
              "high": 688.43,
              "low": 680.69,
              "open": 688.03,
              "timestamp": 1788336000000,
              "volume": 71408.0
            },
            {
              "close": 688.01,
              "high": 689.73,
              "low": 683.18,
              "open": 684.21,
              "timestamp": 1788350400000,
              "volume": 60635.0
            },
            {
              "close": 686.95,
              "high": 689.47,
              "low": 685.05,
              "open": 688.01,
              "timestamp": 1788364800000,
              "volume": 71139.0
            },
            {
              "close": 689.07,
              "high": 689.4,
              "low": 685.86,
              "open": 686.95,
              "timestamp": 1788379200000,
              "volume": 69392.0
            },
            {
              "close": 693.02,
              "high": 695.38,
              "low": 686.6,
              "open": 689.22,
              "timestamp": 1788393600000,
              "volume": 71274.0
            },
            {
              "close": 698.4,
              "high": 699.98,
              "low": 690.16,
              "open": 693.02,
              "timestamp": 1788408000000,
              "volume": 71511.0
            },
            {
              "close": 711.91,
              "high": 716.14,
              "low": 698.4,
              "open": 698.4,
              "timestamp": 1788422400000,
              "volume": 70758.0
            },
            {
              "close": 728.17,
              "high": 728.76,
              "low": 710.94,
              "open": 711.91,
              "timestamp": 1788436800000,
              "volume": 61056.0
            },
            {
              "close": 725.05,
              "high": 728.55,
              "low": 719.28,
              "open": 728.17,
              "timestamp": 1788451200000,
              "volume": 71692.0
            },
            {
              "close": 725.6,
              "high": 728.12,
              "low": 721.07,
              "open": 725.05,
              "timestamp": 1788465600000,
              "volume": 69626.0
            },
            {
              "close": 724.01,
              "high": 730.6,
              "low": 719.56,
              "open": 725.56,
              "timestamp": 1788480000000,
              "volume": 71457.0
            },
            {
              "close": 714.95,
              "high": 729.99,
              "low": 714.49,
              "open": 724.01,
              "timestamp": 1788494400000,
              "volume": 71499.0
            },
            {
              "close": 724.74,
              "high": 725.56,
              "low": 714.15,
              "open": 714.95,
              "timestamp": 1788508800000,
              "volume": 71499.0
            },
            {
              "close": 717.11,
              "high": 727.87,
              "low": 709.34,
              "open": 724.74,
              "timestamp": 1788523200000,
              "volume": 59708.0
            },
            {
              "close": 720.45,
              "high": 721.88,
              "low": 716.49,
              "open": 717.11,
              "timestamp": 1788537600000,
              "volume": 71475.0
            },
            {
              "close": 721.8,
              "high": 721.87,
              "low": 717.09,
              "open": 720.53,
              "timestamp": 1788552000000,
              "volume": 68664.0
            },
            {
              "close": 723.91,
              "high": 725.43,
              "low": 719.72,
              "open": 721.8,
              "timestamp": 1788566400000,
              "volume": 69955.0
            },
            {
              "close": 727.63,
              "high": 728.13,
              "low": 720.95,
              "open": 723.91,
              "timestamp": 1788580800000,
              "volume": 54809.0
            },
            {
              "close": 748.39,
              "high": 757.51,
              "low": 740.89,
              "open": 742.56,
              "timestamp": 1788595200000,
              "volume": 66063.0
            },
            {
              "close": 770.44,
              "high": 772.79,
              "low": 748.39,
              "open": 748.39,
              "timestamp": 1788609600000,
              "volume": 71422.0
            },
            {
              "close": 773.88,
              "high": 781.39,
              "low": 768.19,
              "open": 770.44,
              "timestamp": 1788624000000,
              "volume": 71376.0
            },
            {
              "close": 766.95,
              "high": 774.54,
              "low": 764.11,
              "open": 773.88,
              "timestamp": 1788638400000,
              "volume": 70061.0
            },
            {
              "close": 765.24,
              "high": 769.41,
              "low": 761.62,
              "open": 766.75,
              "timestamp": 1788652800000,
              "volume": 70806.0
            },
            {
              "close": 756.94,
              "high": 765.68,
              "low": 755.37,
              "open": 765.24,
              "timestamp": 1788667200000,
              "volume": 70665.0
            },
            {
              "close": 758.59,
              "high": 759.4,
              "low": 754.64,
              "open": 756.94,
              "timestamp": 1788681600000,
              "volume": 70954.0
            },
            {
              "close": 746.32,
              "high": 758.89,
              "low": 740.59,
              "open": 758.59,
              "timestamp": 1788696000000,
              "volume": 71194.0
            },
            {
              "close": 749.63,
              "high": 750.89,
              "low": 745.41,
              "open": 746.32,
              "timestamp": 1788710400000,
              "volume": 70879.0
            },
            {
              "close": 753.47,
              "high": 755.34,
              "low": 748.74,
              "open": 749.63,
              "timestamp": 1788724800000,
              "volume": 70318.0
            },
            {
              "close": 746.7,
              "high": 757.0,
              "low": 745.47,
              "open": 753.47,
              "timestamp": 1788739200000,
              "volume": 71478.0
            },
            {
              "close": 744.39,
              "high": 750.61,
              "low": 740.85,
              "open": 746.7,
              "timestamp": 1788753600000,
              "volume": 71342.0
            },
            {
              "close": 745.4,
              "high": 747.18,
              "low": 743.04,
              "open": 744.39,
              "timestamp": 1788768000000,
              "volume": 71171.0
            },
            {
              "close": 735.11,
              "high": 748.07,
              "low": 734.27,
              "open": 745.4,
              "timestamp": 1788782400000,
              "volume": 71470.0
            },
            {
              "close": 742.27,
              "high": 742.47,
              "low": 734.8,
              "open": 735.12,
              "timestamp": 1788796800000,
              "volume": 70978.0
            },
            {
              "close": 740.39,
              "high": 742.4,
              "low": 736.41,
              "open": 742.27,
              "timestamp": 1788811200000,
              "volume": 69011.0
            },
            {
              "close": 743.28,
              "high": 745.74,
              "low": 737.28,
              "open": 740.39,
              "timestamp": 1788825600000,
              "volume": 70990.0
            },
            {
              "close": 755.1,
              "high": 758.03,
              "low": 742.13,
              "open": 743.28,
              "timestamp": 1788840000000,
              "volume": 71540.0
            },
            {
              "close": 752.75,
              "high": 761.57,
              "low": 750.59,
              "open": 755.1,
              "timestamp": 1788854400000,
              "volume": 71455.0
            },
            {
              "close": 756.66,
              "high": 757.4,
              "low": 742.65,
              "open": 752.75,
              "timestamp": 1788868800000,
              "volume": 71622.0
            },
            {
              "close": 749.26,
              "high": 758.36,
              "low": 747.8,
              "open": 756.66,
              "timestamp": 1788883200000,
              "volume": 71348.0
            },
            {
              "close": 752.45,
              "high": 755.34,
              "low": 749.26,
              "open": 749.26,
              "timestamp": 1788897600000,
              "volume": 69117.0
            },
            {
              "close": 749.8,
              "high": 757.27,
              "low": 747.52,
              "open": 752.46,
              "timestamp": 1788912000000,
              "volume": 70917.0
            },
            {
              "close": 754.93,
              "high": 757.94,
              "low": 749.8,
              "open": 749.8,
              "timestamp": 1788926400000,
              "volume": 71276.0
            },
            {
              "close": 750.53,
              "high": 757.99,
              "low": 748.0,
              "open": 754.93,
              "timestamp": 1788940800000,
              "volume": 71450.0
            },
            {
              "close": 739.38,
              "high": 752.04,
              "low": 735.1,
              "open": 750.53,
              "timestamp": 1788955200000,
              "volume": 70996.0
            },
            {
              "close": 737.56,
              "high": 742.57,
              "low": 736.67,
              "open": 739.38,
              "timestamp": 1788969600000,
              "volume": 71512.0
            },
            {
              "close": 722.77,
              "high": 738.34,
              "low": 717.72,
              "open": 737.56,
              "timestamp": 1788984000000,
              "volume": 69581.0
            },
            {
              "close": 723.79,
              "high": 726.46,
              "low": 717.24,
              "open": 722.77,
              "timestamp": 1788998400000,
              "volume": 71480.0
            },
            {
              "close": 719.22,
              "high": 723.98,
              "low": 715.56,
              "open": 723.79,
              "timestamp": 1789012800000,
              "volume": 71430.0
            },
            {
              "close": 716.65,
              "high": 719.83,
              "low": 715.68,
              "open": 719.22,
              "timestamp": 1789027200000,
              "volume": 71311.0
            },
            {
              "close": 708.16,
              "high": 718.38,
              "low": 703.54,
              "open": 716.65,
              "timestamp": 1789041600000,
              "volume": 71507.0
            },
            {
              "close": 714.68,
              "high": 716.33,
              "low": 704.65,
              "open": 708.16,
              "timestamp": 1789056000000,
              "volume": 71540.0
            },
            {
              "close": 709.13,
              "high": 716.67,
              "low": 708.79,
              "open": 714.68,
              "timestamp": 1789070400000,
              "volume": 69285.0
            },
            {
              "close": 712.62,
              "high": 715.29,
              "low": 709.13,
              "open": 709.13,
              "timestamp": 1789084800000,
              "volume": 71286.0
            },
            {
              "close": 714.09,
              "high": 717.77,
              "low": 712.47,
              "open": 712.62,
              "timestamp": 1789099200000,
              "volume": 70917.0
            },
            {
              "close": 713.64,
              "high": 716.35,
              "low": 710.69,
              "open": 714.09,
              "timestamp": 1789113600000,
              "volume": 70964.0
            },
            {
              "close": 728.88,
              "high": 741.67,
              "low": 707.01,
              "open": 713.64,
              "timestamp": 1789128000000,
              "volume": 71464.0
            },
            {
              "close": 725.37,
              "high": 733.94,
              "low": 721.17,
              "open": 728.87,
              "timestamp": 1789142400000,
              "volume": 71666.0
            },
            {
              "close": 727.1,
              "high": 728.1,
              "low": 722.09,
              "open": 725.37,
              "timestamp": 1789156800000,
              "volume": 69165.0
            },
            {
              "close": 733.92,
              "high": 736.72,
              "low": 726.44,
              "open": 727.1,
              "timestamp": 1789171200000,
              "volume": 70449.0
            },
            {
              "close": 733.89,
              "high": 735.8,
              "low": 731.94,
              "open": 733.92,
              "timestamp": 1789185600000,
              "volume": 70442.0
            },
            {
              "close": 737.16,
              "high": 740.33,
              "low": 733.01,
              "open": 733.89,
              "timestamp": 1789200000000,
              "volume": 70502.0
            },
            {
              "close": 735.58,
              "high": 737.96,
              "low": 735.09,
              "open": 737.16,
              "timestamp": 1789214400000,
              "volume": 70515.0
            },
            {
              "close": 726.61,
              "high": 735.62,
              "low": 725.5,
              "open": 735.58,
              "timestamp": 1789228800000,
              "volume": 70021.0
            },
            {
              "close": 727.95,
              "high": 728.37,
              "low": 725.88,
              "open": 726.61,
              "timestamp": 1789243200000,
              "volume": 68303.0
            },
            {
              "close": 727.33,
              "high": 730.19,
              "low": 727.29,
              "open": 727.74,
              "timestamp": 1789257600000,
              "volume": 69015.0
            },
            {
              "close": 722.55,
              "high": 727.8,
              "low": 721.86,
              "open": 727.33,
              "timestamp": 1789272000000,
              "volume": 70191.0
            },
            {
              "close": 716.77,
              "high": 722.94,
              "low": 714.42,
              "open": 722.55,
              "timestamp": 1789286400000,
              "volume": 70425.0
            },
            {
              "close": 719.14,
              "high": 720.66,
              "low": 713.54,
              "open": 716.77,
              "timestamp": 1789300800000,
              "volume": 70550.0
            },
            {
              "close": 721.44,
              "high": 723.56,
              "low": 719.14,
              "open": 719.14,
              "timestamp": 1789315200000,
              "volume": 70291.0
            }
          ],
          "last_price": 721.44,
          "momentum": "neutral",
          "rsi_14": 44.89,
          "structure": "neutral"
        },
        "5M": {
          "candle_count": 144,
          "candle_status": {
            "data_age_seconds": 393,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789329300000,
            "latest_timestamp_utc": "2026-09-13T19:55:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 300
          },
          "candles": [
            {
              "close": 722.65,
              "high": 722.86,
              "low": 722.39,
              "open": 722.55,
              "timestamp": 1789286400000,
              "volume": 1468.0
            },
            {
              "close": 722.77,
              "high": 722.94,
              "low": 722.54,
              "open": 722.65,
              "timestamp": 1789286700000,
              "volume": 1460.0
            },
            {
              "close": 722.68,
              "high": 722.77,
              "low": 722.02,
              "open": 722.77,
              "timestamp": 1789287000000,
              "volume": 1472.0
            },
            {
              "close": 721.6,
              "high": 722.73,
              "low": 721.42,
              "open": 722.68,
              "timestamp": 1789287300000,
              "volume": 1480.0
            },
            {
              "close": 721.59,
              "high": 721.83,
              "low": 721.44,
              "open": 721.6,
              "timestamp": 1789287600000,
              "volume": 1451.0
            },
            {
              "close": 721.43,
              "high": 721.71,
              "low": 721.38,
              "open": 721.59,
              "timestamp": 1789287900000,
              "volume": 1453.0
            },
            {
              "close": 720.21,
              "high": 721.43,
              "low": 719.63,
              "open": 721.43,
              "timestamp": 1789288200000,
              "volume": 1484.0
            },
            {
              "close": 719.51,
              "high": 720.38,
              "low": 719.34,
              "open": 720.21,
              "timestamp": 1789288500000,
              "volume": 1485.0
            },
            {
              "close": 717.96,
              "high": 720.32,
              "low": 717.87,
              "open": 719.51,
              "timestamp": 1789288800000,
              "volume": 1487.0
            },
            {
              "close": 718.86,
              "high": 718.92,
              "low": 717.7,
              "open": 717.95,
              "timestamp": 1789289100000,
              "volume": 1480.0
            },
            {
              "close": 718.52,
              "high": 719.16,
              "low": 718.45,
              "open": 718.86,
              "timestamp": 1789289400000,
              "volume": 1460.0
            },
            {
              "close": 718.47,
              "high": 718.71,
              "low": 718.22,
              "open": 718.52,
              "timestamp": 1789289700000,
              "volume": 1453.0
            },
            {
              "close": 718.8,
              "high": 718.8,
              "low": 718.09,
              "open": 718.47,
              "timestamp": 1789290000000,
              "volume": 1473.0
            },
            {
              "close": 719.25,
              "high": 719.4,
              "low": 718.8,
              "open": 718.8,
              "timestamp": 1789290300000,
              "volume": 1474.0
            },
            {
              "close": 718.51,
              "high": 719.25,
              "low": 718.51,
              "open": 719.25,
              "timestamp": 1789290600000,
              "volume": 1471.0
            },
            {
              "close": 717.78,
              "high": 718.51,
              "low": 717.73,
              "open": 718.51,
              "timestamp": 1789290900000,
              "volume": 1463.0
            },
            {
              "close": 716.82,
              "high": 718.07,
              "low": 716.03,
              "open": 717.78,
              "timestamp": 1789291200000,
              "volume": 1470.0
            },
            {
              "close": 715.6,
              "high": 717.12,
              "low": 715.56,
              "open": 716.82,
              "timestamp": 1789291500000,
              "volume": 1485.0
            },
            {
              "close": 715.52,
              "high": 716.22,
              "low": 714.88,
              "open": 715.6,
              "timestamp": 1789291800000,
              "volume": 1486.0
            },
            {
              "close": 716.49,
              "high": 717.57,
              "low": 715.52,
              "open": 715.52,
              "timestamp": 1789292100000,
              "volume": 1485.0
            },
            {
              "close": 716.35,
              "high": 716.75,
              "low": 716.04,
              "open": 716.49,
              "timestamp": 1789292400000,
              "volume": 1458.0
            },
            {
              "close": 716.69,
              "high": 716.79,
              "low": 716.14,
              "open": 716.35,
              "timestamp": 1789292700000,
              "volume": 1474.0
            },
            {
              "close": 716.62,
              "high": 716.8,
              "low": 716.36,
              "open": 716.69,
              "timestamp": 1789293000000,
              "volume": 1462.0
            },
            {
              "close": 716.8,
              "high": 717.17,
              "low": 716.17,
              "open": 716.62,
              "timestamp": 1789293300000,
              "volume": 1468.0
            },
            {
              "close": 716.77,
              "high": 716.99,
              "low": 716.52,
              "open": 716.8,
              "timestamp": 1789293600000,
              "volume": 1473.0
            },
            {
              "close": 716.73,
              "high": 716.8,
              "low": 716.45,
              "open": 716.77,
              "timestamp": 1789293900000,
              "volume": 1465.0
            },
            {
              "close": 716.79,
              "high": 716.95,
              "low": 716.6,
              "open": 716.73,
              "timestamp": 1789294200000,
              "volume": 1458.0
            },
            {
              "close": 716.33,
              "high": 716.95,
              "low": 716.33,
              "open": 716.79,
              "timestamp": 1789294500000,
              "volume": 1466.0
            },
            {
              "close": 716.05,
              "high": 716.38,
              "low": 716.05,
              "open": 716.33,
              "timestamp": 1789294800000,
              "volume": 1458.0
            },
            {
              "close": 716.19,
              "high": 716.19,
              "low": 715.97,
              "open": 716.05,
              "timestamp": 1789295100000,
              "volume": 1451.0
            },
            {
              "close": 716.83,
              "high": 716.89,
              "low": 716.04,
              "open": 716.19,
              "timestamp": 1789295400000,
              "volume": 1470.0
            },
            {
              "close": 716.22,
              "high": 716.88,
              "low": 716.22,
              "open": 716.83,
              "timestamp": 1789295700000,
              "volume": 1462.0
            },
            {
              "close": 715.22,
              "high": 716.22,
              "low": 715.05,
              "open": 716.22,
              "timestamp": 1789296000000,
              "volume": 1476.0
            },
            {
              "close": 715.75,
              "high": 715.8,
              "low": 715.22,
              "open": 715.22,
              "timestamp": 1789296300000,
              "volume": 1470.0
            },
            {
              "close": 715.44,
              "high": 715.75,
              "low": 715.1,
              "open": 715.75,
              "timestamp": 1789296600000,
              "volume": 1474.0
            },
            {
              "close": 715.59,
              "high": 715.76,
              "low": 714.83,
              "open": 715.44,
              "timestamp": 1789296900000,
              "volume": 1479.0
            },
            {
              "close": 715.97,
              "high": 715.97,
              "low": 714.42,
              "open": 715.59,
              "timestamp": 1789297200000,
              "volume": 1478.0
            },
            {
              "close": 715.33,
              "high": 716.17,
              "low": 715.3,
              "open": 715.97,
              "timestamp": 1789297500000,
              "volume": 1469.0
            },
            {
              "close": 715.24,
              "high": 715.59,
              "low": 714.93,
              "open": 715.33,
              "timestamp": 1789297800000,
              "volume": 1462.0
            },
            {
              "close": 715.33,
              "high": 715.77,
              "low": 714.96,
              "open": 715.24,
              "timestamp": 1789298100000,
              "volume": 1457.0
            },
            {
              "close": 715.92,
              "high": 715.99,
              "low": 715.3,
              "open": 715.33,
              "timestamp": 1789298400000,
              "volume": 1453.0
            },
            {
              "close": 715.96,
              "high": 715.98,
              "low": 715.67,
              "open": 715.92,
              "timestamp": 1789298700000,
              "volume": 1446.0
            },
            {
              "close": 715.98,
              "high": 715.98,
              "low": 715.66,
              "open": 715.96,
              "timestamp": 1789299000000,
              "volume": 1458.0
            },
            {
              "close": 716.71,
              "high": 716.72,
              "low": 715.98,
              "open": 715.98,
              "timestamp": 1789299300000,
              "volume": 1469.0
            },
            {
              "close": 716.95,
              "high": 717.0,
              "low": 716.71,
              "open": 716.71,
              "timestamp": 1789299600000,
              "volume": 1463.0
            },
            {
              "close": 717.12,
              "high": 717.31,
              "low": 716.87,
              "open": 716.95,
              "timestamp": 1789299900000,
              "volume": 1466.0
            },
            {
              "close": 716.95,
              "high": 717.3,
              "low": 716.89,
              "open": 717.12,
              "timestamp": 1789300200000,
              "volume": 1453.0
            },
            {
              "close": 716.77,
              "high": 716.95,
              "low": 716.7,
              "open": 716.95,
              "timestamp": 1789300500000,
              "volume": 1447.0
            },
            {
              "close": 716.49,
              "high": 716.77,
              "low": 716.49,
              "open": 716.77,
              "timestamp": 1789300800000,
              "volume": 1472.0
            },
            {
              "close": 716.54,
              "high": 716.62,
              "low": 716.44,
              "open": 716.49,
              "timestamp": 1789301100000,
              "volume": 1474.0
            },
            {
              "close": 716.93,
              "high": 716.96,
              "low": 716.54,
              "open": 716.54,
              "timestamp": 1789301400000,
              "volume": 1460.0
            },
            {
              "close": 717.23,
              "high": 717.37,
              "low": 716.93,
              "open": 716.93,
              "timestamp": 1789301700000,
              "volume": 1456.0
            },
            {
              "close": 717.2,
              "high": 717.36,
              "low": 717.02,
              "open": 717.23,
              "timestamp": 1789302000000,
              "volume": 1464.0
            },
            {
              "close": 716.64,
              "high": 717.34,
              "low": 716.64,
              "open": 717.2,
              "timestamp": 1789302300000,
              "volume": 1454.0
            },
            {
              "close": 716.35,
              "high": 717.18,
              "low": 716.35,
              "open": 716.64,
              "timestamp": 1789302600000,
              "volume": 1472.0
            },
            {
              "close": 716.19,
              "high": 716.68,
              "low": 715.94,
              "open": 716.35,
              "timestamp": 1789302900000,
              "volume": 1465.0
            },
            {
              "close": 715.8,
              "high": 716.22,
              "low": 715.8,
              "open": 716.21,
              "timestamp": 1789303200000,
              "volume": 1449.0
            },
            {
              "close": 715.53,
              "high": 715.8,
              "low": 715.53,
              "open": 715.8,
              "timestamp": 1789303500000,
              "volume": 1469.0
            },
            {
              "close": 715.85,
              "high": 716.07,
              "low": 715.51,
              "open": 715.53,
              "timestamp": 1789303800000,
              "volume": 1460.0
            },
            {
              "close": 715.98,
              "high": 716.1,
              "low": 715.75,
              "open": 715.9,
              "timestamp": 1789304100000,
              "volume": 1452.0
            },
            {
              "close": 715.84,
              "high": 716.0,
              "low": 715.81,
              "open": 715.98,
              "timestamp": 1789304400000,
              "volume": 1459.0
            },
            {
              "close": 716.11,
              "high": 716.13,
              "low": 715.66,
              "open": 715.84,
              "timestamp": 1789304700000,
              "volume": 1473.0
            },
            {
              "close": 716.09,
              "high": 716.25,
              "low": 715.92,
              "open": 716.11,
              "timestamp": 1789305000000,
              "volume": 1458.0
            },
            {
              "close": 715.22,
              "high": 716.13,
              "low": 715.22,
              "open": 716.09,
              "timestamp": 1789305300000,
              "volume": 1462.0
            },
            {
              "close": 715.3,
              "high": 715.48,
              "low": 714.8,
              "open": 715.22,
              "timestamp": 1789305600000,
              "volume": 1468.0
            },
            {
              "close": 714.02,
              "high": 715.3,
              "low": 713.54,
              "open": 715.3,
              "timestamp": 1789305900000,
              "volume": 1481.0
            },
            {
              "close": 715.38,
              "high": 715.74,
              "low": 714.02,
              "open": 714.02,
              "timestamp": 1789306200000,
              "volume": 1472.0
            },
            {
              "close": 716.29,
              "high": 716.29,
              "low": 715.38,
              "open": 715.38,
              "timestamp": 1789306500000,
              "volume": 1475.0
            },
            {
              "close": 716.82,
              "high": 716.82,
              "low": 716.14,
              "open": 716.29,
              "timestamp": 1789306800000,
              "volume": 1473.0
            },
            {
              "close": 717.99,
              "high": 717.99,
              "low": 716.78,
              "open": 716.82,
              "timestamp": 1789307100000,
              "volume": 1479.0
            },
            {
              "close": 718.26,
              "high": 718.78,
              "low": 717.89,
              "open": 717.99,
              "timestamp": 1789307400000,
              "volume": 1482.0
            },
            {
              "close": 718.39,
              "high": 718.54,
              "low": 718.2,
              "open": 718.26,
              "timestamp": 1789307700000,
              "volume": 1472.0
            },
            {
              "close": 718.51,
              "high": 718.81,
              "low": 718.41,
              "open": 718.41,
              "timestamp": 1789308000000,
              "volume": 1477.0
            },
            {
              "close": 719.37,
              "high": 719.37,
              "low": 718.51,
              "open": 718.51,
              "timestamp": 1789308300000,
              "volume": 1483.0
            },
            {
              "close": 719.72,
              "high": 719.75,
              "low": 719.22,
              "open": 719.37,
              "timestamp": 1789308600000,
              "volume": 1483.0
            },
            {
              "close": 719.58,
              "high": 720.4,
              "low": 719.42,
              "open": 719.72,
              "timestamp": 1789308900000,
              "volume": 1480.0
            },
            {
              "close": 719.57,
              "high": 719.86,
              "low": 719.48,
              "open": 719.58,
              "timestamp": 1789309200000,
              "volume": 1466.0
            },
            {
              "close": 719.73,
              "high": 719.89,
              "low": 719.48,
              "open": 719.57,
              "timestamp": 1789309500000,
              "volume": 1472.0
            },
            {
              "close": 719.52,
              "high": 719.9,
              "low": 719.4,
              "open": 719.73,
              "timestamp": 1789309800000,
              "volume": 1473.0
            },
            {
              "close": 720.18,
              "high": 720.66,
              "low": 719.42,
              "open": 719.52,
              "timestamp": 1789310100000,
              "volume": 1474.0
            },
            {
              "close": 719.88,
              "high": 720.28,
              "low": 719.76,
              "open": 720.18,
              "timestamp": 1789310400000,
              "volume": 1477.0
            },
            {
              "close": 719.44,
              "high": 720.21,
              "low": 719.42,
              "open": 719.88,
              "timestamp": 1789310700000,
              "volume": 1468.0
            },
            {
              "close": 718.96,
              "high": 719.48,
              "low": 718.94,
              "open": 719.44,
              "timestamp": 1789311000000,
              "volume": 1466.0
            },
            {
              "close": 718.96,
              "high": 718.96,
              "low": 718.51,
              "open": 718.96,
              "timestamp": 1789311300000,
              "volume": 1472.0
            },
            {
              "close": 717.82,
              "high": 719.03,
              "low": 717.81,
              "open": 718.96,
              "timestamp": 1789311600000,
              "volume": 1475.0
            },
            {
              "close": 718.3,
              "high": 718.35,
              "low": 717.75,
              "open": 717.85,
              "timestamp": 1789311900000,
              "volume": 1483.0
            },
            {
              "close": 718.12,
              "high": 718.3,
              "low": 717.97,
              "open": 718.3,
              "timestamp": 1789312200000,
              "volume": 1475.0
            },
            {
              "close": 718.11,
              "high": 718.15,
              "low": 717.75,
              "open": 718.12,
              "timestamp": 1789312500000,
              "volume": 1480.0
            },
            {
              "close": 719.56,
              "high": 719.69,
              "low": 718.11,
              "open": 718.11,
              "timestamp": 1789312800000,
              "volume": 1483.0
            },
            {
              "close": 718.59,
              "high": 719.56,
              "low": 718.24,
              "open": 719.56,
              "timestamp": 1789313100000,
              "volume": 1484.0
            },
            {
              "close": 719.59,
              "high": 719.59,
              "low": 718.49,
              "open": 718.59,
              "timestamp": 1789313400000,
              "volume": 1474.0
            },
            {
              "close": 719.3,
              "high": 719.78,
              "low": 719.3,
              "open": 719.59,
              "timestamp": 1789313700000,
              "volume": 1459.0
            },
            {
              "close": 719.87,
              "high": 720.1,
              "low": 719.06,
              "open": 719.3,
              "timestamp": 1789314000000,
              "volume": 1462.0
            },
            {
              "close": 719.43,
              "high": 719.87,
              "low": 719.16,
              "open": 719.87,
              "timestamp": 1789314300000,
              "volume": 1464.0
            },
            {
              "close": 719.35,
              "high": 719.51,
              "low": 719.0,
              "open": 719.43,
              "timestamp": 1789314600000,
              "volume": 1464.0
            },
            {
              "close": 719.14,
              "high": 719.41,
              "low": 719.14,
              "open": 719.35,
              "timestamp": 1789314900000,
              "volume": 1455.0
            },
            {
              "close": 720.53,
              "high": 720.53,
              "low": 719.14,
              "open": 719.14,
              "timestamp": 1789315200000,
              "volume": 1480.0
            },
            {
              "close": 721.0,
              "high": 721.12,
              "low": 720.22,
              "open": 720.53,
              "timestamp": 1789315500000,
              "volume": 1479.0
            },
            {
              "close": 721.12,
              "high": 721.77,
              "low": 720.8,
              "open": 721.0,
              "timestamp": 1789315800000,
              "volume": 1486.0
            },
            {
              "close": 720.82,
              "high": 721.19,
              "low": 720.68,
              "open": 721.12,
              "timestamp": 1789316100000,
              "volume": 1468.0
            },
            {
              "close": 720.96,
              "high": 721.09,
              "low": 720.76,
              "open": 720.82,
              "timestamp": 1789316400000,
              "volume": 1470.0
            },
            {
              "close": 721.39,
              "high": 721.51,
              "low": 720.95,
              "open": 720.96,
              "timestamp": 1789316700000,
              "volume": 1472.0
            },
            {
              "close": 720.92,
              "high": 721.59,
              "low": 720.9,
              "open": 721.39,
              "timestamp": 1789317000000,
              "volume": 1464.0
            },
            {
              "close": 721.03,
              "high": 721.16,
              "low": 720.83,
              "open": 720.92,
              "timestamp": 1789317300000,
              "volume": 1464.0
            },
            {
              "close": 721.52,
              "high": 721.65,
              "low": 720.98,
              "open": 721.03,
              "timestamp": 1789317600000,
              "volume": 1479.0
            },
            {
              "close": 720.88,
              "high": 721.59,
              "low": 720.88,
              "open": 721.52,
              "timestamp": 1789317900000,
              "volume": 1465.0
            },
            {
              "close": 721.54,
              "high": 721.65,
              "low": 720.88,
              "open": 720.88,
              "timestamp": 1789318200000,
              "volume": 1466.0
            },
            {
              "close": 721.36,
              "high": 721.67,
              "low": 721.33,
              "open": 721.54,
              "timestamp": 1789318500000,
              "volume": 1465.0
            },
            {
              "close": 722.03,
              "high": 722.2,
              "low": 721.31,
              "open": 721.36,
              "timestamp": 1789318800000,
              "volume": 1475.0
            },
            {
              "close": 721.87,
              "high": 722.11,
              "low": 721.71,
              "open": 722.03,
              "timestamp": 1789319100000,
              "volume": 1468.0
            },
            {
              "close": 721.72,
              "high": 722.56,
              "low": 721.62,
              "open": 721.87,
              "timestamp": 1789319400000,
              "volume": 1480.0
            },
            {
              "close": 721.57,
              "high": 721.93,
              "low": 721.29,
              "open": 721.72,
              "timestamp": 1789319700000,
              "volume": 1478.0
            },
            {
              "close": 721.33,
              "high": 721.71,
              "low": 721.32,
              "open": 721.66,
              "timestamp": 1789320000000,
              "volume": 1464.0
            },
            {
              "close": 721.7,
              "high": 721.93,
              "low": 721.33,
              "open": 721.33,
              "timestamp": 1789320300000,
              "volume": 1463.0
            },
            {
              "close": 721.25,
              "high": 721.7,
              "low": 721.17,
              "open": 721.7,
              "timestamp": 1789320600000,
              "volume": 1473.0
            },
            {
              "close": 721.54,
              "high": 721.56,
              "low": 721.16,
              "open": 721.25,
              "timestamp": 1789320900000,
              "volume": 1467.0
            },
            {
              "close": 721.32,
              "high": 721.54,
              "low": 721.31,
              "open": 721.54,
              "timestamp": 1789321200000,
              "volume": 1465.0
            },
            {
              "close": 721.86,
              "high": 721.86,
              "low": 721.32,
              "open": 721.32,
              "timestamp": 1789321500000,
              "volume": 1455.0
            },
            {
              "close": 721.46,
              "high": 721.99,
              "low": 721.46,
              "open": 721.78,
              "timestamp": 1789321800000,
              "volume": 1448.0
            },
            {
              "close": 721.58,
              "high": 721.7,
              "low": 721.26,
              "open": 721.46,
              "timestamp": 1789322100000,
              "volume": 1458.0
            },
            {
              "close": 721.26,
              "high": 721.76,
              "low": 721.26,
              "open": 721.58,
              "timestamp": 1789322400000,
              "volume": 1460.0
            },
            {
              "close": 721.26,
              "high": 721.38,
              "low": 721.24,
              "open": 721.26,
              "timestamp": 1789322700000,
              "volume": 1455.0
            },
            {
              "close": 721.62,
              "high": 721.67,
              "low": 721.16,
              "open": 721.26,
              "timestamp": 1789323000000,
              "volume": 1456.0
            },
            {
              "close": 721.55,
              "high": 722.18,
              "low": 721.39,
              "open": 721.62,
              "timestamp": 1789323300000,
              "volume": 1477.0
            },
            {
              "close": 721.51,
              "high": 721.63,
              "low": 721.36,
              "open": 721.55,
              "timestamp": 1789323600000,
              "volume": 1458.0
            },
            {
              "close": 721.86,
              "high": 721.86,
              "low": 721.23,
              "open": 721.51,
              "timestamp": 1789323900000,
              "volume": 1451.0
            },
            {
              "close": 721.73,
              "high": 722.39,
              "low": 721.52,
              "open": 721.86,
              "timestamp": 1789324200000,
              "volume": 1463.0
            },
            {
              "close": 721.61,
              "high": 721.73,
              "low": 721.6,
              "open": 721.73,
              "timestamp": 1789324500000,
              "volume": 1442.0
            },
            {
              "close": 721.66,
              "high": 722.1,
              "low": 721.43,
              "open": 721.61,
              "timestamp": 1789324800000,
              "volume": 1444.0
            },
            {
              "close": 721.63,
              "high": 721.74,
              "low": 721.52,
              "open": 721.66,
              "timestamp": 1789325100000,
              "volume": 1443.0
            },
            {
              "close": 722.44,
              "high": 722.71,
              "low": 721.59,
              "open": 721.63,
              "timestamp": 1789325400000,
              "volume": 1464.0
            },
            {
              "close": 722.44,
              "high": 722.58,
              "low": 722.08,
              "open": 722.44,
              "timestamp": 1789325700000,
              "volume": 1460.0
            },
            {
              "close": 723.19,
              "high": 723.21,
              "low": 722.44,
              "open": 722.44,
              "timestamp": 1789326000000,
              "volume": 1471.0
            },
            {
              "close": 722.32,
              "high": 723.56,
              "low": 722.32,
              "open": 723.19,
              "timestamp": 1789326300000,
              "volume": 1463.0
            },
            {
              "close": 721.76,
              "high": 722.32,
              "low": 721.76,
              "open": 722.32,
              "timestamp": 1789326600000,
              "volume": 1478.0
            },
            {
              "close": 721.4,
              "high": 721.84,
              "low": 721.4,
              "open": 721.76,
              "timestamp": 1789326900000,
              "volume": 1480.0
            },
            {
              "close": 721.56,
              "high": 721.56,
              "low": 721.2,
              "open": 721.4,
              "timestamp": 1789327200000,
              "volume": 1471.0
            },
            {
              "close": 721.68,
              "high": 721.73,
              "low": 721.56,
              "open": 721.56,
              "timestamp": 1789327500000,
              "volume": 1480.0
            },
            {
              "close": 721.63,
              "high": 721.84,
              "low": 721.52,
              "open": 721.68,
              "timestamp": 1789327800000,
              "volume": 1480.0
            },
            {
              "close": 721.41,
              "high": 721.74,
              "low": 721.41,
              "open": 721.63,
              "timestamp": 1789328100000,
              "volume": 1466.0
            },
            {
              "close": 721.77,
              "high": 721.77,
              "low": 721.38,
              "open": 721.41,
              "timestamp": 1789328400000,
              "volume": 1443.0
            },
            {
              "close": 721.49,
              "high": 721.77,
              "low": 721.38,
              "open": 721.77,
              "timestamp": 1789328700000,
              "volume": 1457.0
            },
            {
              "close": 721.56,
              "high": 721.56,
              "low": 721.17,
              "open": 721.49,
              "timestamp": 1789329000000,
              "volume": 1455.0
            },
            {
              "close": 721.44,
              "high": 721.91,
              "low": 721.25,
              "open": 721.56,
              "timestamp": 1789329300000,
              "volume": 1422.0
            }
          ],
          "last_price": 721.44,
          "momentum": "neutral",
          "rsi_14": 47.79,
          "structure": "bearish"
        }
      }
    },
    {
      "bridge_analysis": {
        "decision": "REJECT",
        "directional_bias": "neutral",
        "execution_5m": {
          "candle_confirmed": false,
          "confirmed": false,
          "reason": "No directional bias is established.",
          "rsi_confirmed": false,
          "structure_shift": false
        },
        "execution_context": {
          "atr_14": 0.000215,
          "distance_to_high": 0.0004799999999999943,
          "distance_to_low": 0.0007100000000000023,
          "extension": "normal",
          "range_position": 0.5966,
          "recent_high": 0.08459,
          "recent_low": 0.0834
        },
        "geometry": {
          "entry_quality": "unknown",
          "invalidation": null,
          "reward_to_risk": null,
          "risk_distance": null,
          "room_to_target": null,
          "target_reference": null
        },
        "multi_horizon_state": "conflicted",
        "reason": "Directional evidence is materially conflicted and lacks sufficient edge.",
        "setup_grade": "REJECT",
        "symbol": "DOGEUSD",
        "timeframes": {
          "15M": {
            "candle_count": 192,
            "last_price": 0.08411,
            "momentum": "neutral",
            "rsi_14": 52.67,
            "structure": "neutral"
          },
          "1H": {
            "candle_count": 168,
            "last_price": 0.08411,
            "momentum": "neutral",
            "rsi_14": 49.42,
            "structure": "neutral"
          },
          "4H": {
            "candle_count": 84,
            "last_price": 0.08411,
            "momentum": "neutral",
            "rsi_14": 42.36,
            "structure": "neutral"
          },
          "5M": {
            "candle_count": 144,
            "last_price": 0.08411,
            "momentum": "neutral",
            "rsi_14": 41.91,
            "structure": "bearish"
          }
        },
        "trade_plan": {
          "entry_reference": null,
          "live_market_entry_reference": null,
          "live_market_entry_reference_is_authorization": false,
          "live_market_entry_reference_side": null,
          "reason": "No directional bias is established.",
          "reward_to_tp1": null,
          "reward_to_tp2": null,
          "reward_to_tp3": null,
          "risk_distance": null,
          "rr_tp1": null,
          "rr_tp2": null,
          "rr_tp3": null,
          "safe_loss": null,
          "tp1": null,
          "tp2": null,
          "tp3": null,
          "valid": false
        }
      },
      "broker": {
        "route_id": 452,
        "tradable_instrument_id": 208
      },
      "instrument_specs": {
        "available": true,
        "bar_source": "BID",
        "base_currency": "DOGE",
        "cache": {
          "age_seconds": 635738.131,
          "captured_at": "2026-09-06T11:26:01.251480+00:00",
          "source": "stale_cache",
          "stale": true
        },
        "contract_size": 10000,
        "error": null,
        "leverage": "3.00",
        "lot_step": 0.01,
        "margin_hedging_type": "fx_cfd",
        "maximum_lot": null,
        "minimum_lot": 0.01,
        "minimum_stop_distance": null,
        "quote_currency": "USD",
        "raw_details": {
          "d": {
            "barSource": "BID",
            "baseCurrency": "DOGE",
            "betSize": null,
            "betStep": null,
            "bettingCurrency": null,
            "contractMonth": null,
            "country": null,
            "deliveryStatus": null,
            "description": "Dogecoin vs US Dollar",
            "exerciseStyle": null,
            "firstTradeDate": null,
            "hasDaily": true,
            "hasIntraday": true,
            "industry": null,
            "isin": "",
            "lastTradeDate": null,
            "leverage": "3.00",
            "localizedName": "DOGEUSD",
            "logoUrl": null,
            "lotSize": 10000,
            "lotStep": 0.01,
            "margin_hedging_type": "fx_cfd",
            "marketCap": null,
            "marketDataExchange": "Cryptos",
            "maxLot": null,
            "minLot": 0.01,
            "name": "DOGEUSD",
            "noticeDate": null,
            "quotingCurrency": "USD",
            "sector": null,
            "settlementDate": null,
            "settlementSystem": "Immediate",
            "strikePrice": null,
            "strikeType": null,
            "symbolStatus": "FULLY_OPEN",
            "tickCost": [
              {
                "leftRangeLimit": null,
                "tickCost": 0.0
              }
            ],
            "tickSize": [
              {
                "leftRangeLimit": null,
                "tickSize": 1e-05
              }
            ],
            "tradeSessionId": 1547,
            "tradeSessionStatusId": 20,
            "tradingExchange": "Crypto",
            "type": "CRYPTO"
          },
          "s": "ok"
        },
        "route_id": 9912,
        "symbol_status": "FULLY_OPEN",
        "tick_cost_raw": 0.0,
        "tick_size": 1e-05,
        "tick_value": null,
        "tradable_instrument_id": 208,
        "trading_session_id": 1547,
        "trading_session_status_id": 20
      },
      "market_snapshot": {
        "analysis_price": 0.08411,
        "analysis_price_source": "latest_5m_bar",
        "ask": 0.08418,
        "ask_size": 100000.0,
        "atlas_received_at": "2026-09-13T20:01:36.693565+00:00",
        "bid": 0.08413,
        "bid_size": 100000.0,
        "broker_staleness_known": false,
        "cache": {
          "age_seconds": 0,
          "captured_at": "2026-09-13T20:01:36.693544+00:00",
          "source": "live",
          "stale": false
        },
        "live_ask": 0.08418,
        "live_bid": 0.08413,
        "live_executable_market_entry": null,
        "live_executable_market_entry_is_authorization": false,
        "live_executable_market_entry_side": null,
        "live_mid": 0.08415500000000001,
        "market_entry_price_policy": "LONG market execution evaluates live ask; SHORT market execution evaluates live bid. Structural or pending entry_reference remains context and must be reassessed before approval.",
        "price_semantics": "analysis_price is the latest 5M bar/reference price, not an executable quote. live_bid and live_ask are current TradeLocker quote values; live_mid is their midpoint. For market-entry evaluation use live_ask for LONG and live_bid for SHORT.",
        "quote_age_seconds": null,
        "quote_error": null,
        "quote_note": "Bid/ask values are live TradeLocker quote values. The broker response does not currently expose a quote timestamp, so broker quote age/staleness is left null rather than estimated.",
        "quote_timestamp": null,
        "quotes_available": true,
        "raw_quote": {
          "d": {
            "ap": 0.08418,
            "as": 100000.0,
            "bp": 0.08413,
            "bs": 100000.0
          },
          "s": "ok"
        },
        "spread": 5.000000000000837e-05
      },
      "symbol": "DOGEUSD",
      "timeframes": {
        "15M": {
          "candle_count": 192,
          "candle_status": {
            "data_age_seconds": 995,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789328700000,
            "latest_timestamp_utc": "2026-09-13T19:45:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 900
          },
          "candles": [
            {
              "close": 0.08461,
              "high": 0.0847,
              "low": 0.08441,
              "open": 0.08441,
              "timestamp": 1789156800000,
              "volume": 4446.0
            },
            {
              "close": 0.08433,
              "high": 0.08465,
              "low": 0.08429,
              "open": 0.08461,
              "timestamp": 1789157700000,
              "volume": 4450.0
            },
            {
              "close": 0.08442,
              "high": 0.08466,
              "low": 0.08405,
              "open": 0.08433,
              "timestamp": 1789158600000,
              "volume": 4460.0
            },
            {
              "close": 0.0843,
              "high": 0.08445,
              "low": 0.08399,
              "open": 0.08442,
              "timestamp": 1789159500000,
              "volume": 4452.0
            },
            {
              "close": 0.0845,
              "high": 0.08464,
              "low": 0.08424,
              "open": 0.0843,
              "timestamp": 1789160400000,
              "volume": 3260.0
            },
            {
              "close": 0.08443,
              "high": 0.08459,
              "low": 0.08441,
              "open": 0.0845,
              "timestamp": 1789161300000,
              "volume": 4411.0
            },
            {
              "close": 0.08431,
              "high": 0.08453,
              "low": 0.08431,
              "open": 0.08443,
              "timestamp": 1789162200000,
              "volume": 4421.0
            },
            {
              "close": 0.0839,
              "high": 0.08435,
              "low": 0.08375,
              "open": 0.08431,
              "timestamp": 1789163100000,
              "volume": 4453.0
            },
            {
              "close": 0.08413,
              "high": 0.08425,
              "low": 0.08358,
              "open": 0.0839,
              "timestamp": 1789164000000,
              "volume": 3854.0
            },
            {
              "close": 0.08394,
              "high": 0.08422,
              "low": 0.08391,
              "open": 0.08413,
              "timestamp": 1789164900000,
              "volume": 4430.0
            },
            {
              "close": 0.08383,
              "high": 0.08402,
              "low": 0.08361,
              "open": 0.08394,
              "timestamp": 1789165800000,
              "volume": 4451.0
            },
            {
              "close": 0.08375,
              "high": 0.08384,
              "low": 0.08349,
              "open": 0.08383,
              "timestamp": 1789166700000,
              "volume": 4445.0
            },
            {
              "close": 0.08399,
              "high": 0.08406,
              "low": 0.08369,
              "open": 0.08375,
              "timestamp": 1789167600000,
              "volume": 4434.0
            },
            {
              "close": 0.08406,
              "high": 0.08412,
              "low": 0.08393,
              "open": 0.08399,
              "timestamp": 1789168500000,
              "volume": 4416.0
            },
            {
              "close": 0.08413,
              "high": 0.0842,
              "low": 0.08404,
              "open": 0.08406,
              "timestamp": 1789169400000,
              "volume": 4396.0
            },
            {
              "close": 0.08425,
              "high": 0.08428,
              "low": 0.08413,
              "open": 0.08413,
              "timestamp": 1789170300000,
              "volume": 4417.0
            },
            {
              "close": 0.08419,
              "high": 0.08428,
              "low": 0.08405,
              "open": 0.08425,
              "timestamp": 1789171200000,
              "volume": 4433.0
            },
            {
              "close": 0.08427,
              "high": 0.0843,
              "low": 0.08413,
              "open": 0.08419,
              "timestamp": 1789172100000,
              "volume": 4421.0
            },
            {
              "close": 0.08416,
              "high": 0.08436,
              "low": 0.08415,
              "open": 0.08427,
              "timestamp": 1789173000000,
              "volume": 4440.0
            },
            {
              "close": 0.08413,
              "high": 0.08423,
              "low": 0.08411,
              "open": 0.08416,
              "timestamp": 1789173900000,
              "volume": 4436.0
            },
            {
              "close": 0.0844,
              "high": 0.0844,
              "low": 0.08406,
              "open": 0.08413,
              "timestamp": 1789174800000,
              "volume": 4428.0
            },
            {
              "close": 0.08429,
              "high": 0.08445,
              "low": 0.08423,
              "open": 0.0844,
              "timestamp": 1789175700000,
              "volume": 4414.0
            },
            {
              "close": 0.08438,
              "high": 0.08439,
              "low": 0.08421,
              "open": 0.08429,
              "timestamp": 1789176600000,
              "volume": 4418.0
            },
            {
              "close": 0.08435,
              "high": 0.08452,
              "low": 0.0843,
              "open": 0.08438,
              "timestamp": 1789177500000,
              "volume": 4428.0
            },
            {
              "close": 0.08437,
              "high": 0.08445,
              "low": 0.0843,
              "open": 0.08435,
              "timestamp": 1789178400000,
              "volume": 4414.0
            },
            {
              "close": 0.08442,
              "high": 0.08452,
              "low": 0.08437,
              "open": 0.08437,
              "timestamp": 1789179300000,
              "volume": 4405.0
            },
            {
              "close": 0.08434,
              "high": 0.08449,
              "low": 0.08433,
              "open": 0.08442,
              "timestamp": 1789180200000,
              "volume": 4430.0
            },
            {
              "close": 0.0844,
              "high": 0.0845,
              "low": 0.08427,
              "open": 0.08434,
              "timestamp": 1789181100000,
              "volume": 4423.0
            },
            {
              "close": 0.08436,
              "high": 0.08452,
              "low": 0.08431,
              "open": 0.0844,
              "timestamp": 1789182000000,
              "volume": 4431.0
            },
            {
              "close": 0.0844,
              "high": 0.08451,
              "low": 0.08429,
              "open": 0.08436,
              "timestamp": 1789182900000,
              "volume": 4423.0
            },
            {
              "close": 0.08437,
              "high": 0.08442,
              "low": 0.08434,
              "open": 0.0844,
              "timestamp": 1789183800000,
              "volume": 4416.0
            },
            {
              "close": 0.08438,
              "high": 0.08439,
              "low": 0.08429,
              "open": 0.08437,
              "timestamp": 1789184700000,
              "volume": 4421.0
            },
            {
              "close": 0.08434,
              "high": 0.08444,
              "low": 0.08433,
              "open": 0.08438,
              "timestamp": 1789185600000,
              "volume": 4413.0
            },
            {
              "close": 0.08434,
              "high": 0.08439,
              "low": 0.0842,
              "open": 0.08434,
              "timestamp": 1789186500000,
              "volume": 4389.0
            },
            {
              "close": 0.08433,
              "high": 0.08445,
              "low": 0.08432,
              "open": 0.08434,
              "timestamp": 1789187400000,
              "volume": 4443.0
            },
            {
              "close": 0.08432,
              "high": 0.08435,
              "low": 0.08425,
              "open": 0.08433,
              "timestamp": 1789188300000,
              "volume": 4423.0
            },
            {
              "close": 0.08433,
              "high": 0.08435,
              "low": 0.08424,
              "open": 0.08432,
              "timestamp": 1789189200000,
              "volume": 4434.0
            },
            {
              "close": 0.08418,
              "high": 0.08437,
              "low": 0.08418,
              "open": 0.08433,
              "timestamp": 1789190100000,
              "volume": 4416.0
            },
            {
              "close": 0.08437,
              "high": 0.08446,
              "low": 0.08417,
              "open": 0.08418,
              "timestamp": 1789191000000,
              "volume": 4434.0
            },
            {
              "close": 0.08435,
              "high": 0.08441,
              "low": 0.08434,
              "open": 0.08437,
              "timestamp": 1789191900000,
              "volume": 4418.0
            },
            {
              "close": 0.08433,
              "high": 0.08436,
              "low": 0.0843,
              "open": 0.08435,
              "timestamp": 1789192800000,
              "volume": 4423.0
            },
            {
              "close": 0.08436,
              "high": 0.08443,
              "low": 0.08429,
              "open": 0.08433,
              "timestamp": 1789193700000,
              "volume": 4403.0
            },
            {
              "close": 0.08446,
              "high": 0.08451,
              "low": 0.08434,
              "open": 0.08436,
              "timestamp": 1789194600000,
              "volume": 4419.0
            },
            {
              "close": 0.08436,
              "high": 0.08449,
              "low": 0.08429,
              "open": 0.08446,
              "timestamp": 1789195500000,
              "volume": 4416.0
            },
            {
              "close": 0.08451,
              "high": 0.08454,
              "low": 0.08434,
              "open": 0.08436,
              "timestamp": 1789196400000,
              "volume": 4435.0
            },
            {
              "close": 0.08455,
              "high": 0.0846,
              "low": 0.08449,
              "open": 0.08451,
              "timestamp": 1789197300000,
              "volume": 4412.0
            },
            {
              "close": 0.08462,
              "high": 0.08462,
              "low": 0.08452,
              "open": 0.08455,
              "timestamp": 1789198200000,
              "volume": 4392.0
            },
            {
              "close": 0.08469,
              "high": 0.08475,
              "low": 0.08459,
              "open": 0.08462,
              "timestamp": 1789199100000,
              "volume": 4425.0
            },
            {
              "close": 0.08466,
              "high": 0.08481,
              "low": 0.08461,
              "open": 0.08469,
              "timestamp": 1789200000000,
              "volume": 4439.0
            },
            {
              "close": 0.08463,
              "high": 0.08483,
              "low": 0.08461,
              "open": 0.08466,
              "timestamp": 1789200900000,
              "volume": 4437.0
            },
            {
              "close": 0.08469,
              "high": 0.08469,
              "low": 0.08456,
              "open": 0.08463,
              "timestamp": 1789201800000,
              "volume": 4413.0
            },
            {
              "close": 0.08473,
              "high": 0.08477,
              "low": 0.08469,
              "open": 0.08469,
              "timestamp": 1789202700000,
              "volume": 4408.0
            },
            {
              "close": 0.08484,
              "high": 0.08486,
              "low": 0.08469,
              "open": 0.08473,
              "timestamp": 1789203600000,
              "volume": 4424.0
            },
            {
              "close": 0.08483,
              "high": 0.08491,
              "low": 0.08473,
              "open": 0.08484,
              "timestamp": 1789204500000,
              "volume": 4425.0
            },
            {
              "close": 0.08476,
              "high": 0.08492,
              "low": 0.08472,
              "open": 0.08483,
              "timestamp": 1789205400000,
              "volume": 4419.0
            },
            {
              "close": 0.08489,
              "high": 0.0849,
              "low": 0.08474,
              "open": 0.08476,
              "timestamp": 1789206300000,
              "volume": 4416.0
            },
            {
              "close": 0.08498,
              "high": 0.08511,
              "low": 0.08488,
              "open": 0.08489,
              "timestamp": 1789207200000,
              "volume": 4446.0
            },
            {
              "close": 0.08496,
              "high": 0.08501,
              "low": 0.08493,
              "open": 0.08498,
              "timestamp": 1789208100000,
              "volume": 4422.0
            },
            {
              "close": 0.08496,
              "high": 0.08499,
              "low": 0.08487,
              "open": 0.08496,
              "timestamp": 1789209000000,
              "volume": 4411.0
            },
            {
              "close": 0.08496,
              "high": 0.08501,
              "low": 0.08481,
              "open": 0.08496,
              "timestamp": 1789209900000,
              "volume": 4413.0
            },
            {
              "close": 0.08495,
              "high": 0.08504,
              "low": 0.08487,
              "open": 0.08496,
              "timestamp": 1789210800000,
              "volume": 4425.0
            },
            {
              "close": 0.08491,
              "high": 0.08497,
              "low": 0.08485,
              "open": 0.08495,
              "timestamp": 1789211700000,
              "volume": 4416.0
            },
            {
              "close": 0.08504,
              "high": 0.08505,
              "low": 0.08488,
              "open": 0.08491,
              "timestamp": 1789212600000,
              "volume": 4423.0
            },
            {
              "close": 0.085,
              "high": 0.08505,
              "low": 0.085,
              "open": 0.08504,
              "timestamp": 1789213500000,
              "volume": 4410.0
            },
            {
              "close": 0.08495,
              "high": 0.08511,
              "low": 0.08495,
              "open": 0.085,
              "timestamp": 1789214400000,
              "volume": 4448.0
            },
            {
              "close": 0.08493,
              "high": 0.08506,
              "low": 0.0849,
              "open": 0.08495,
              "timestamp": 1789215300000,
              "volume": 4433.0
            },
            {
              "close": 0.08497,
              "high": 0.08503,
              "low": 0.08493,
              "open": 0.08493,
              "timestamp": 1789216200000,
              "volume": 4403.0
            },
            {
              "close": 0.085,
              "high": 0.08507,
              "low": 0.08491,
              "open": 0.085,
              "timestamp": 1789217100000,
              "volume": 4414.0
            },
            {
              "close": 0.0848,
              "high": 0.08505,
              "low": 0.08479,
              "open": 0.085,
              "timestamp": 1789218000000,
              "volume": 4446.0
            },
            {
              "close": 0.0849,
              "high": 0.08494,
              "low": 0.08477,
              "open": 0.0848,
              "timestamp": 1789218900000,
              "volume": 4427.0
            },
            {
              "close": 0.08488,
              "high": 0.08493,
              "low": 0.08481,
              "open": 0.0849,
              "timestamp": 1789219800000,
              "volume": 4391.0
            },
            {
              "close": 0.08492,
              "high": 0.08492,
              "low": 0.08478,
              "open": 0.08488,
              "timestamp": 1789220700000,
              "volume": 4411.0
            },
            {
              "close": 0.08497,
              "high": 0.08505,
              "low": 0.0849,
              "open": 0.08492,
              "timestamp": 1789221600000,
              "volume": 4416.0
            },
            {
              "close": 0.08502,
              "high": 0.08514,
              "low": 0.08496,
              "open": 0.08497,
              "timestamp": 1789222500000,
              "volume": 4408.0
            },
            {
              "close": 0.08503,
              "high": 0.08512,
              "low": 0.085,
              "open": 0.08502,
              "timestamp": 1789223400000,
              "volume": 4404.0
            },
            {
              "close": 0.08509,
              "high": 0.0851,
              "low": 0.08503,
              "open": 0.08503,
              "timestamp": 1789224300000,
              "volume": 4421.0
            },
            {
              "close": 0.08518,
              "high": 0.0853,
              "low": 0.08509,
              "open": 0.08509,
              "timestamp": 1789225200000,
              "volume": 4451.0
            },
            {
              "close": 0.08511,
              "high": 0.08518,
              "low": 0.08501,
              "open": 0.08518,
              "timestamp": 1789226100000,
              "volume": 4439.0
            },
            {
              "close": 0.08513,
              "high": 0.08517,
              "low": 0.08492,
              "open": 0.08511,
              "timestamp": 1789227000000,
              "volume": 4429.0
            },
            {
              "close": 0.08504,
              "high": 0.08515,
              "low": 0.08493,
              "open": 0.08513,
              "timestamp": 1789227900000,
              "volume": 4418.0
            },
            {
              "close": 0.08497,
              "high": 0.08509,
              "low": 0.0849,
              "open": 0.08504,
              "timestamp": 1789228800000,
              "volume": 4437.0
            },
            {
              "close": 0.08501,
              "high": 0.08501,
              "low": 0.08492,
              "open": 0.08497,
              "timestamp": 1789229700000,
              "volume": 4420.0
            },
            {
              "close": 0.0849,
              "high": 0.08501,
              "low": 0.0849,
              "open": 0.08501,
              "timestamp": 1789230600000,
              "volume": 4422.0
            },
            {
              "close": 0.08496,
              "high": 0.08505,
              "low": 0.0849,
              "open": 0.08491,
              "timestamp": 1789231500000,
              "volume": 4427.0
            },
            {
              "close": 0.08496,
              "high": 0.08505,
              "low": 0.08487,
              "open": 0.08496,
              "timestamp": 1789232400000,
              "volume": 4426.0
            },
            {
              "close": 0.08483,
              "high": 0.08499,
              "low": 0.08483,
              "open": 0.08496,
              "timestamp": 1789233300000,
              "volume": 4422.0
            },
            {
              "close": 0.08492,
              "high": 0.08492,
              "low": 0.08475,
              "open": 0.08483,
              "timestamp": 1789234200000,
              "volume": 4423.0
            },
            {
              "close": 0.08492,
              "high": 0.08496,
              "low": 0.08485,
              "open": 0.08492,
              "timestamp": 1789235100000,
              "volume": 4401.0
            },
            {
              "close": 0.08476,
              "high": 0.08492,
              "low": 0.08473,
              "open": 0.08492,
              "timestamp": 1789236000000,
              "volume": 4432.0
            },
            {
              "close": 0.08484,
              "high": 0.08487,
              "low": 0.08467,
              "open": 0.08476,
              "timestamp": 1789236900000,
              "volume": 4410.0
            },
            {
              "close": 0.08478,
              "high": 0.08485,
              "low": 0.08464,
              "open": 0.08484,
              "timestamp": 1789237800000,
              "volume": 4401.0
            },
            {
              "close": 0.08468,
              "high": 0.0848,
              "low": 0.08462,
              "open": 0.08478,
              "timestamp": 1789238700000,
              "volume": 4391.0
            },
            {
              "close": 0.08482,
              "high": 0.08483,
              "low": 0.08463,
              "open": 0.08468,
              "timestamp": 1789239600000,
              "volume": 4417.0
            },
            {
              "close": 0.08475,
              "high": 0.08482,
              "low": 0.08467,
              "open": 0.08482,
              "timestamp": 1789240500000,
              "volume": 4398.0
            },
            {
              "close": 0.08464,
              "high": 0.08477,
              "low": 0.08455,
              "open": 0.08475,
              "timestamp": 1789241400000,
              "volume": 4412.0
            },
            {
              "close": 0.08473,
              "high": 0.08476,
              "low": 0.08462,
              "open": 0.08464,
              "timestamp": 1789242300000,
              "volume": 4404.0
            },
            {
              "close": 0.08485,
              "high": 0.08488,
              "low": 0.08472,
              "open": 0.08473,
              "timestamp": 1789243200000,
              "volume": 4419.0
            },
            {
              "close": 0.08483,
              "high": 0.08488,
              "low": 0.08481,
              "open": 0.08485,
              "timestamp": 1789244100000,
              "volume": 4390.0
            },
            {
              "close": 0.08485,
              "high": 0.08491,
              "low": 0.08477,
              "open": 0.08483,
              "timestamp": 1789245000000,
              "volume": 4383.0
            },
            {
              "close": 0.08472,
              "high": 0.08491,
              "low": 0.08471,
              "open": 0.08485,
              "timestamp": 1789245900000,
              "volume": 4387.0
            },
            {
              "close": 0.08477,
              "high": 0.0849,
              "low": 0.0847,
              "open": 0.08472,
              "timestamp": 1789246800000,
              "volume": 3406.0
            },
            {
              "close": 0.08469,
              "high": 0.08477,
              "low": 0.08468,
              "open": 0.08477,
              "timestamp": 1789247700000,
              "volume": 4384.0
            },
            {
              "close": 0.08467,
              "high": 0.08472,
              "low": 0.08462,
              "open": 0.08469,
              "timestamp": 1789248600000,
              "volume": 4396.0
            },
            {
              "close": 0.08456,
              "high": 0.08467,
              "low": 0.08454,
              "open": 0.08467,
              "timestamp": 1789249500000,
              "volume": 4407.0
            },
            {
              "close": 0.08466,
              "high": 0.08473,
              "low": 0.08449,
              "open": 0.08456,
              "timestamp": 1789250400000,
              "volume": 4419.0
            },
            {
              "close": 0.08456,
              "high": 0.08483,
              "low": 0.08455,
              "open": 0.08466,
              "timestamp": 1789251300000,
              "volume": 4404.0
            },
            {
              "close": 0.08456,
              "high": 0.08467,
              "low": 0.0845,
              "open": 0.08456,
              "timestamp": 1789252200000,
              "volume": 4403.0
            },
            {
              "close": 0.08459,
              "high": 0.08461,
              "low": 0.08455,
              "open": 0.08456,
              "timestamp": 1789253100000,
              "volume": 4377.0
            },
            {
              "close": 0.08467,
              "high": 0.08469,
              "low": 0.08458,
              "open": 0.08459,
              "timestamp": 1789254000000,
              "volume": 4420.0
            },
            {
              "close": 0.08466,
              "high": 0.08474,
              "low": 0.08464,
              "open": 0.08467,
              "timestamp": 1789254900000,
              "volume": 4408.0
            },
            {
              "close": 0.08477,
              "high": 0.08477,
              "low": 0.08465,
              "open": 0.08466,
              "timestamp": 1789255800000,
              "volume": 4393.0
            },
            {
              "close": 0.08477,
              "high": 0.08484,
              "low": 0.08474,
              "open": 0.08477,
              "timestamp": 1789256700000,
              "volume": 4399.0
            },
            {
              "close": 0.08473,
              "high": 0.08483,
              "low": 0.08471,
              "open": 0.08473,
              "timestamp": 1789257600000,
              "volume": 4129.0
            },
            {
              "close": 0.08477,
              "high": 0.08482,
              "low": 0.08472,
              "open": 0.08473,
              "timestamp": 1789258500000,
              "volume": 4397.0
            },
            {
              "close": 0.08469,
              "high": 0.08479,
              "low": 0.08464,
              "open": 0.08477,
              "timestamp": 1789259400000,
              "volume": 4422.0
            },
            {
              "close": 0.08478,
              "high": 0.08479,
              "low": 0.08467,
              "open": 0.08469,
              "timestamp": 1789260300000,
              "volume": 4410.0
            },
            {
              "close": 0.08475,
              "high": 0.08488,
              "low": 0.08474,
              "open": 0.08478,
              "timestamp": 1789261200000,
              "volume": 4442.0
            },
            {
              "close": 0.08482,
              "high": 0.085,
              "low": 0.08473,
              "open": 0.08475,
              "timestamp": 1789262100000,
              "volume": 4432.0
            },
            {
              "close": 0.08488,
              "high": 0.08493,
              "low": 0.08473,
              "open": 0.08482,
              "timestamp": 1789263000000,
              "volume": 4442.0
            },
            {
              "close": 0.08492,
              "high": 0.08493,
              "low": 0.08486,
              "open": 0.08488,
              "timestamp": 1789263900000,
              "volume": 4420.0
            },
            {
              "close": 0.08481,
              "high": 0.08492,
              "low": 0.08481,
              "open": 0.08492,
              "timestamp": 1789264800000,
              "volume": 4411.0
            },
            {
              "close": 0.08483,
              "high": 0.08489,
              "low": 0.08475,
              "open": 0.08481,
              "timestamp": 1789265700000,
              "volume": 4403.0
            },
            {
              "close": 0.08505,
              "high": 0.08506,
              "low": 0.08482,
              "open": 0.08483,
              "timestamp": 1789266600000,
              "volume": 4393.0
            },
            {
              "close": 0.08488,
              "high": 0.08512,
              "low": 0.08488,
              "open": 0.08505,
              "timestamp": 1789267500000,
              "volume": 4407.0
            },
            {
              "close": 0.08482,
              "high": 0.08508,
              "low": 0.08482,
              "open": 0.08488,
              "timestamp": 1789268400000,
              "volume": 4433.0
            },
            {
              "close": 0.0848,
              "high": 0.08496,
              "low": 0.0848,
              "open": 0.08482,
              "timestamp": 1789269300000,
              "volume": 4424.0
            },
            {
              "close": 0.08476,
              "high": 0.0848,
              "low": 0.08456,
              "open": 0.0848,
              "timestamp": 1789270200000,
              "volume": 4426.0
            },
            {
              "close": 0.08465,
              "high": 0.08478,
              "low": 0.0846,
              "open": 0.08476,
              "timestamp": 1789271100000,
              "volume": 4414.0
            },
            {
              "close": 0.0847,
              "high": 0.0848,
              "low": 0.0846,
              "open": 0.08465,
              "timestamp": 1789272000000,
              "volume": 4414.0
            },
            {
              "close": 0.08466,
              "high": 0.08475,
              "low": 0.08458,
              "open": 0.0847,
              "timestamp": 1789272900000,
              "volume": 4410.0
            },
            {
              "close": 0.08462,
              "high": 0.08466,
              "low": 0.08456,
              "open": 0.08465,
              "timestamp": 1789273800000,
              "volume": 4391.0
            },
            {
              "close": 0.08465,
              "high": 0.08467,
              "low": 0.08458,
              "open": 0.08462,
              "timestamp": 1789274700000,
              "volume": 4409.0
            },
            {
              "close": 0.08472,
              "high": 0.08474,
              "low": 0.08463,
              "open": 0.08465,
              "timestamp": 1789275600000,
              "volume": 4424.0
            },
            {
              "close": 0.08477,
              "high": 0.08477,
              "low": 0.0847,
              "open": 0.08472,
              "timestamp": 1789276500000,
              "volume": 4415.0
            },
            {
              "close": 0.08477,
              "high": 0.08482,
              "low": 0.08471,
              "open": 0.08477,
              "timestamp": 1789277400000,
              "volume": 4392.0
            },
            {
              "close": 0.08478,
              "high": 0.08487,
              "low": 0.08477,
              "open": 0.08477,
              "timestamp": 1789278300000,
              "volume": 4383.0
            },
            {
              "close": 0.08474,
              "high": 0.0848,
              "low": 0.08471,
              "open": 0.08478,
              "timestamp": 1789279200000,
              "volume": 4405.0
            },
            {
              "close": 0.08468,
              "high": 0.08474,
              "low": 0.0846,
              "open": 0.08474,
              "timestamp": 1789280100000,
              "volume": 4411.0
            },
            {
              "close": 0.0846,
              "high": 0.08468,
              "low": 0.08455,
              "open": 0.08468,
              "timestamp": 1789281000000,
              "volume": 4414.0
            },
            {
              "close": 0.08437,
              "high": 0.08461,
              "low": 0.08425,
              "open": 0.08459,
              "timestamp": 1789281900000,
              "volume": 4432.0
            },
            {
              "close": 0.08445,
              "high": 0.08447,
              "low": 0.08433,
              "open": 0.08437,
              "timestamp": 1789282800000,
              "volume": 4412.0
            },
            {
              "close": 0.08442,
              "high": 0.08454,
              "low": 0.08441,
              "open": 0.08445,
              "timestamp": 1789283700000,
              "volume": 4409.0
            },
            {
              "close": 0.08433,
              "high": 0.08444,
              "low": 0.08414,
              "open": 0.08442,
              "timestamp": 1789284600000,
              "volume": 4416.0
            },
            {
              "close": 0.08411,
              "high": 0.08433,
              "low": 0.08408,
              "open": 0.08433,
              "timestamp": 1789285500000,
              "volume": 4416.0
            },
            {
              "close": 0.084,
              "high": 0.08422,
              "low": 0.08392,
              "open": 0.08411,
              "timestamp": 1789286400000,
              "volume": 4439.0
            },
            {
              "close": 0.08377,
              "high": 0.08401,
              "low": 0.08376,
              "open": 0.084,
              "timestamp": 1789287300000,
              "volume": 4432.0
            },
            {
              "close": 0.08327,
              "high": 0.08378,
              "low": 0.08322,
              "open": 0.08377,
              "timestamp": 1789288200000,
              "volume": 4463.0
            },
            {
              "close": 0.08349,
              "high": 0.08355,
              "low": 0.08328,
              "open": 0.08328,
              "timestamp": 1789289100000,
              "volume": 4455.0
            },
            {
              "close": 0.08357,
              "high": 0.08363,
              "low": 0.08347,
              "open": 0.08349,
              "timestamp": 1789290000000,
              "volume": 4440.0
            },
            {
              "close": 0.08329,
              "high": 0.0836,
              "low": 0.08315,
              "open": 0.08357,
              "timestamp": 1789290900000,
              "volume": 4437.0
            },
            {
              "close": 0.08342,
              "high": 0.08356,
              "low": 0.08307,
              "open": 0.08329,
              "timestamp": 1789291800000,
              "volume": 4452.0
            },
            {
              "close": 0.08349,
              "high": 0.08353,
              "low": 0.0834,
              "open": 0.08342,
              "timestamp": 1789292700000,
              "volume": 4422.0
            },
            {
              "close": 0.08354,
              "high": 0.08358,
              "low": 0.08348,
              "open": 0.08349,
              "timestamp": 1789293600000,
              "volume": 4413.0
            },
            {
              "close": 0.08351,
              "high": 0.08356,
              "low": 0.08346,
              "open": 0.08354,
              "timestamp": 1789294500000,
              "volume": 4391.0
            },
            {
              "close": 0.0833,
              "high": 0.08355,
              "low": 0.08321,
              "open": 0.08351,
              "timestamp": 1789295400000,
              "volume": 4413.0
            },
            {
              "close": 0.08326,
              "high": 0.08337,
              "low": 0.08315,
              "open": 0.0833,
              "timestamp": 1789296300000,
              "volume": 4422.0
            },
            {
              "close": 0.08333,
              "high": 0.08344,
              "low": 0.08318,
              "open": 0.08326,
              "timestamp": 1789297200000,
              "volume": 4445.0
            },
            {
              "close": 0.08344,
              "high": 0.08348,
              "low": 0.08332,
              "open": 0.08333,
              "timestamp": 1789298100000,
              "volume": 4412.0
            },
            {
              "close": 0.08347,
              "high": 0.08351,
              "low": 0.0834,
              "open": 0.08344,
              "timestamp": 1789299000000,
              "volume": 4408.0
            },
            {
              "close": 0.08349,
              "high": 0.08354,
              "low": 0.08344,
              "open": 0.08347,
              "timestamp": 1789299900000,
              "volume": 4402.0
            },
            {
              "close": 0.08339,
              "high": 0.08349,
              "low": 0.08335,
              "open": 0.08349,
              "timestamp": 1789300800000,
              "volume": 4437.0
            },
            {
              "close": 0.08342,
              "high": 0.0835,
              "low": 0.08338,
              "open": 0.08339,
              "timestamp": 1789301700000,
              "volume": 4421.0
            },
            {
              "close": 0.08326,
              "high": 0.08354,
              "low": 0.08324,
              "open": 0.08342,
              "timestamp": 1789302600000,
              "volume": 4426.0
            },
            {
              "close": 0.08337,
              "high": 0.08338,
              "low": 0.08322,
              "open": 0.08326,
              "timestamp": 1789303500000,
              "volume": 4420.0
            },
            {
              "close": 0.08343,
              "high": 0.08344,
              "low": 0.08329,
              "open": 0.08337,
              "timestamp": 1789304400000,
              "volume": 4439.0
            },
            {
              "close": 0.08285,
              "high": 0.08344,
              "low": 0.08275,
              "open": 0.08343,
              "timestamp": 1789305300000,
              "volume": 4443.0
            },
            {
              "close": 0.08321,
              "high": 0.08323,
              "low": 0.08283,
              "open": 0.08285,
              "timestamp": 1789306200000,
              "volume": 4460.0
            },
            {
              "close": 0.08334,
              "high": 0.08344,
              "low": 0.08321,
              "open": 0.08321,
              "timestamp": 1789307100000,
              "volume": 4440.0
            },
            {
              "close": 0.08359,
              "high": 0.08363,
              "low": 0.08333,
              "open": 0.08334,
              "timestamp": 1789308000000,
              "volume": 4453.0
            },
            {
              "close": 0.08358,
              "high": 0.08371,
              "low": 0.08352,
              "open": 0.08359,
              "timestamp": 1789308900000,
              "volume": 4464.0
            },
            {
              "close": 0.08372,
              "high": 0.08387,
              "low": 0.08352,
              "open": 0.08358,
              "timestamp": 1789309800000,
              "volume": 4451.0
            },
            {
              "close": 0.08371,
              "high": 0.08377,
              "low": 0.08364,
              "open": 0.08372,
              "timestamp": 1789310700000,
              "volume": 4433.0
            },
            {
              "close": 0.08359,
              "high": 0.08375,
              "low": 0.08352,
              "open": 0.08371,
              "timestamp": 1789311600000,
              "volume": 4461.0
            },
            {
              "close": 0.08347,
              "high": 0.08368,
              "low": 0.08341,
              "open": 0.08359,
              "timestamp": 1789312500000,
              "volume": 4460.0
            },
            {
              "close": 0.08353,
              "high": 0.08357,
              "low": 0.0834,
              "open": 0.08347,
              "timestamp": 1789313400000,
              "volume": 4437.0
            },
            {
              "close": 0.08343,
              "high": 0.08357,
              "low": 0.08341,
              "open": 0.08353,
              "timestamp": 1789314300000,
              "volume": 4425.0
            },
            {
              "close": 0.08369,
              "high": 0.08384,
              "low": 0.08342,
              "open": 0.08343,
              "timestamp": 1789315200000,
              "volume": 4457.0
            },
            {
              "close": 0.08373,
              "high": 0.08379,
              "low": 0.08363,
              "open": 0.08369,
              "timestamp": 1789316100000,
              "volume": 4437.0
            },
            {
              "close": 0.0838,
              "high": 0.08384,
              "low": 0.08371,
              "open": 0.08373,
              "timestamp": 1789317000000,
              "volume": 4441.0
            },
            {
              "close": 0.08391,
              "high": 0.08392,
              "low": 0.08371,
              "open": 0.0838,
              "timestamp": 1789317900000,
              "volume": 4435.0
            },
            {
              "close": 0.08433,
              "high": 0.0845,
              "low": 0.08391,
              "open": 0.08391,
              "timestamp": 1789318800000,
              "volume": 4451.0
            },
            {
              "close": 0.08455,
              "high": 0.08459,
              "low": 0.08432,
              "open": 0.08433,
              "timestamp": 1789319700000,
              "volume": 4449.0
            },
            {
              "close": 0.08435,
              "high": 0.08457,
              "low": 0.08425,
              "open": 0.08455,
              "timestamp": 1789320600000,
              "volume": 4443.0
            },
            {
              "close": 0.08438,
              "high": 0.08449,
              "low": 0.08435,
              "open": 0.08435,
              "timestamp": 1789321500000,
              "volume": 4424.0
            },
            {
              "close": 0.08436,
              "high": 0.0844,
              "low": 0.08426,
              "open": 0.08438,
              "timestamp": 1789322400000,
              "volume": 4443.0
            },
            {
              "close": 0.08441,
              "high": 0.08451,
              "low": 0.08433,
              "open": 0.08436,
              "timestamp": 1789323300000,
              "volume": 4426.0
            },
            {
              "close": 0.08438,
              "high": 0.0845,
              "low": 0.08436,
              "open": 0.08441,
              "timestamp": 1789324200000,
              "volume": 4414.0
            },
            {
              "close": 0.08445,
              "high": 0.08453,
              "low": 0.08438,
              "open": 0.08438,
              "timestamp": 1789325100000,
              "volume": 4403.0
            },
            {
              "close": 0.08435,
              "high": 0.08457,
              "low": 0.08431,
              "open": 0.08445,
              "timestamp": 1789326000000,
              "volume": 4430.0
            },
            {
              "close": 0.08429,
              "high": 0.08436,
              "low": 0.08421,
              "open": 0.08435,
              "timestamp": 1789326900000,
              "volume": 4397.0
            },
            {
              "close": 0.08406,
              "high": 0.08431,
              "low": 0.08405,
              "open": 0.08429,
              "timestamp": 1789327800000,
              "volume": 4429.0
            },
            {
              "close": 0.08411,
              "high": 0.08412,
              "low": 0.08405,
              "open": 0.08406,
              "timestamp": 1789328700000,
              "volume": 4399.0
            }
          ],
          "last_price": 0.08411,
          "momentum": "neutral",
          "rsi_14": 52.67,
          "structure": "neutral"
        },
        "1H": {
          "candle_count": 168,
          "candle_status": {
            "data_age_seconds": 3695,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789326000000,
            "latest_timestamp_utc": "2026-09-13T19:00:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 3600
          },
          "candles": [
            {
              "close": 0.09021,
              "high": 0.09034,
              "low": 0.0894,
              "open": 0.0895,
              "timestamp": 1788724800000,
              "volume": 16944.0
            },
            {
              "close": 0.0904,
              "high": 0.09071,
              "low": 0.09005,
              "open": 0.09021,
              "timestamp": 1788728400000,
              "volume": 17863.0
            },
            {
              "close": 0.09021,
              "high": 0.09041,
              "low": 0.08957,
              "open": 0.0904,
              "timestamp": 1788732000000,
              "volume": 17883.0
            },
            {
              "close": 0.09085,
              "high": 0.09101,
              "low": 0.09015,
              "open": 0.09021,
              "timestamp": 1788735600000,
              "volume": 17859.0
            },
            {
              "close": 0.09093,
              "high": 0.09116,
              "low": 0.09064,
              "open": 0.09085,
              "timestamp": 1788739200000,
              "volume": 17873.0
            },
            {
              "close": 0.09006,
              "high": 0.09106,
              "low": 0.08964,
              "open": 0.09093,
              "timestamp": 1788742800000,
              "volume": 17896.0
            },
            {
              "close": 0.09006,
              "high": 0.0913,
              "low": 0.08974,
              "open": 0.09007,
              "timestamp": 1788746400000,
              "volume": 17895.0
            },
            {
              "close": 0.08928,
              "high": 0.09031,
              "low": 0.08912,
              "open": 0.09006,
              "timestamp": 1788750000000,
              "volume": 17893.0
            },
            {
              "close": 0.08969,
              "high": 0.08975,
              "low": 0.08924,
              "open": 0.08929,
              "timestamp": 1788753600000,
              "volume": 17837.0
            },
            {
              "close": 0.09008,
              "high": 0.09057,
              "low": 0.08965,
              "open": 0.08969,
              "timestamp": 1788757200000,
              "volume": 17857.0
            },
            {
              "close": 0.08977,
              "high": 0.09053,
              "low": 0.08972,
              "open": 0.09008,
              "timestamp": 1788760800000,
              "volume": 17832.0
            },
            {
              "close": 0.08932,
              "high": 0.09001,
              "low": 0.08849,
              "open": 0.08977,
              "timestamp": 1788764400000,
              "volume": 17887.0
            },
            {
              "close": 0.08951,
              "high": 0.08998,
              "low": 0.08926,
              "open": 0.08932,
              "timestamp": 1788768000000,
              "volume": 17831.0
            },
            {
              "close": 0.0892,
              "high": 0.09004,
              "low": 0.08916,
              "open": 0.08951,
              "timestamp": 1788771600000,
              "volume": 17830.0
            },
            {
              "close": 0.08952,
              "high": 0.08974,
              "low": 0.08916,
              "open": 0.0892,
              "timestamp": 1788775200000,
              "volume": 17786.0
            },
            {
              "close": 0.08974,
              "high": 0.08977,
              "low": 0.08936,
              "open": 0.08952,
              "timestamp": 1788778800000,
              "volume": 17790.0
            },
            {
              "close": 0.09127,
              "high": 0.09141,
              "low": 0.08968,
              "open": 0.08974,
              "timestamp": 1788782400000,
              "volume": 17867.0
            },
            {
              "close": 0.09086,
              "high": 0.09179,
              "low": 0.09037,
              "open": 0.09127,
              "timestamp": 1788786000000,
              "volume": 17912.0
            },
            {
              "close": 0.09055,
              "high": 0.09093,
              "low": 0.08971,
              "open": 0.09086,
              "timestamp": 1788789600000,
              "volume": 17909.0
            },
            {
              "close": 0.0889,
              "high": 0.09058,
              "low": 0.08859,
              "open": 0.09055,
              "timestamp": 1788793200000,
              "volume": 17908.0
            },
            {
              "close": 0.09004,
              "high": 0.09021,
              "low": 0.08888,
              "open": 0.08892,
              "timestamp": 1788796800000,
              "volume": 17859.0
            },
            {
              "close": 0.09003,
              "high": 0.09037,
              "low": 0.08992,
              "open": 0.09004,
              "timestamp": 1788800400000,
              "volume": 17845.0
            },
            {
              "close": 0.08981,
              "high": 0.09011,
              "low": 0.08951,
              "open": 0.09003,
              "timestamp": 1788804000000,
              "volume": 17812.0
            },
            {
              "close": 0.09048,
              "high": 0.09061,
              "low": 0.08964,
              "open": 0.08981,
              "timestamp": 1788807600000,
              "volume": 17773.0
            },
            {
              "close": 0.09051,
              "high": 0.09092,
              "low": 0.08996,
              "open": 0.09048,
              "timestamp": 1788811200000,
              "volume": 17844.0
            },
            {
              "close": 0.09028,
              "high": 0.09066,
              "low": 0.09017,
              "open": 0.09051,
              "timestamp": 1788814800000,
              "volume": 16576.0
            },
            {
              "close": 0.09004,
              "high": 0.09067,
              "low": 0.08961,
              "open": 0.09028,
              "timestamp": 1788818400000,
              "volume": 17262.0
            },
            {
              "close": 0.09044,
              "high": 0.09082,
              "low": 0.09,
              "open": 0.09004,
              "timestamp": 1788822000000,
              "volume": 17823.0
            },
            {
              "close": 0.09129,
              "high": 0.0916,
              "low": 0.09025,
              "open": 0.09044,
              "timestamp": 1788825600000,
              "volume": 17893.0
            },
            {
              "close": 0.09117,
              "high": 0.09162,
              "low": 0.09093,
              "open": 0.09129,
              "timestamp": 1788829200000,
              "volume": 17858.0
            },
            {
              "close": 0.0899,
              "high": 0.09146,
              "low": 0.0899,
              "open": 0.09117,
              "timestamp": 1788832800000,
              "volume": 17867.0
            },
            {
              "close": 0.08988,
              "high": 0.0902,
              "low": 0.0895,
              "open": 0.08988,
              "timestamp": 1788836400000,
              "volume": 17879.0
            },
            {
              "close": 0.08958,
              "high": 0.08997,
              "low": 0.08948,
              "open": 0.08988,
              "timestamp": 1788840000000,
              "volume": 17861.0
            },
            {
              "close": 0.08954,
              "high": 0.09018,
              "low": 0.08936,
              "open": 0.08957,
              "timestamp": 1788843600000,
              "volume": 17877.0
            },
            {
              "close": 0.08918,
              "high": 0.08973,
              "low": 0.08889,
              "open": 0.08954,
              "timestamp": 1788847200000,
              "volume": 17841.0
            },
            {
              "close": 0.08923,
              "high": 0.08977,
              "low": 0.08889,
              "open": 0.08918,
              "timestamp": 1788850800000,
              "volume": 17849.0
            },
            {
              "close": 0.08926,
              "high": 0.08956,
              "low": 0.08875,
              "open": 0.08922,
              "timestamp": 1788854400000,
              "volume": 17862.0
            },
            {
              "close": 0.09036,
              "high": 0.09072,
              "low": 0.08898,
              "open": 0.08926,
              "timestamp": 1788858000000,
              "volume": 17856.0
            },
            {
              "close": 0.09008,
              "high": 0.0909,
              "low": 0.09007,
              "open": 0.09036,
              "timestamp": 1788861600000,
              "volume": 17764.0
            },
            {
              "close": 0.08948,
              "high": 0.09014,
              "low": 0.0892,
              "open": 0.09008,
              "timestamp": 1788865200000,
              "volume": 17865.0
            },
            {
              "close": 0.08924,
              "high": 0.08949,
              "low": 0.08841,
              "open": 0.08948,
              "timestamp": 1788868800000,
              "volume": 17899.0
            },
            {
              "close": 0.08903,
              "high": 0.08941,
              "low": 0.08792,
              "open": 0.08924,
              "timestamp": 1788872400000,
              "volume": 17927.0
            },
            {
              "close": 0.08964,
              "high": 0.08977,
              "low": 0.08889,
              "open": 0.08902,
              "timestamp": 1788876000000,
              "volume": 17935.0
            },
            {
              "close": 0.09057,
              "high": 0.09075,
              "low": 0.08956,
              "open": 0.08964,
              "timestamp": 1788879600000,
              "volume": 17924.0
            },
            {
              "close": 0.09058,
              "high": 0.09082,
              "low": 0.08976,
              "open": 0.09057,
              "timestamp": 1788883200000,
              "volume": 17920.0
            },
            {
              "close": 0.08999,
              "high": 0.09079,
              "low": 0.08988,
              "open": 0.09059,
              "timestamp": 1788886800000,
              "volume": 17923.0
            },
            {
              "close": 0.08947,
              "high": 0.09072,
              "low": 0.08915,
              "open": 0.08999,
              "timestamp": 1788890400000,
              "volume": 17794.0
            },
            {
              "close": 0.0895,
              "high": 0.09002,
              "low": 0.08925,
              "open": 0.08947,
              "timestamp": 1788894000000,
              "volume": 17919.0
            },
            {
              "close": 0.08959,
              "high": 0.09038,
              "low": 0.08941,
              "open": 0.08949,
              "timestamp": 1788897600000,
              "volume": 17878.0
            },
            {
              "close": 0.08949,
              "high": 0.08999,
              "low": 0.0892,
              "open": 0.08959,
              "timestamp": 1788901200000,
              "volume": 16653.0
            },
            {
              "close": 0.08995,
              "high": 0.09004,
              "low": 0.08945,
              "open": 0.08949,
              "timestamp": 1788904800000,
              "volume": 17247.0
            },
            {
              "close": 0.08998,
              "high": 0.09007,
              "low": 0.08977,
              "open": 0.08995,
              "timestamp": 1788908400000,
              "volume": 17836.0
            },
            {
              "close": 0.09048,
              "high": 0.09086,
              "low": 0.08995,
              "open": 0.08998,
              "timestamp": 1788912000000,
              "volume": 17895.0
            },
            {
              "close": 0.09019,
              "high": 0.0906,
              "low": 0.0898,
              "open": 0.09048,
              "timestamp": 1788915600000,
              "volume": 17898.0
            },
            {
              "close": 0.08986,
              "high": 0.09039,
              "low": 0.08959,
              "open": 0.09019,
              "timestamp": 1788919200000,
              "volume": 17869.0
            },
            {
              "close": 0.08952,
              "high": 0.08989,
              "low": 0.08932,
              "open": 0.08986,
              "timestamp": 1788922800000,
              "volume": 17883.0
            },
            {
              "close": 0.09055,
              "high": 0.09077,
              "low": 0.08952,
              "open": 0.08952,
              "timestamp": 1788926400000,
              "volume": 17884.0
            },
            {
              "close": 0.09003,
              "high": 0.09069,
              "low": 0.08979,
              "open": 0.09055,
              "timestamp": 1788930000000,
              "volume": 17877.0
            },
            {
              "close": 0.09039,
              "high": 0.09064,
              "low": 0.0899,
              "open": 0.09003,
              "timestamp": 1788933600000,
              "volume": 17848.0
            },
            {
              "close": 0.09081,
              "high": 0.0909,
              "low": 0.09035,
              "open": 0.09039,
              "timestamp": 1788937200000,
              "volume": 17861.0
            },
            {
              "close": 0.09136,
              "high": 0.09139,
              "low": 0.09072,
              "open": 0.09081,
              "timestamp": 1788940800000,
              "volume": 17874.0
            },
            {
              "close": 0.09003,
              "high": 0.09138,
              "low": 0.08999,
              "open": 0.09136,
              "timestamp": 1788944400000,
              "volume": 17884.0
            },
            {
              "close": 0.0907,
              "high": 0.09076,
              "low": 0.09003,
              "open": 0.09003,
              "timestamp": 1788948000000,
              "volume": 17885.0
            },
            {
              "close": 0.09078,
              "high": 0.0909,
              "low": 0.09009,
              "open": 0.0907,
              "timestamp": 1788951600000,
              "volume": 17880.0
            },
            {
              "close": 0.09129,
              "high": 0.09154,
              "low": 0.09061,
              "open": 0.09078,
              "timestamp": 1788955200000,
              "volume": 17893.0
            },
            {
              "close": 0.09026,
              "high": 0.09135,
              "low": 0.09009,
              "open": 0.09129,
              "timestamp": 1788958800000,
              "volume": 17921.0
            },
            {
              "close": 0.08972,
              "high": 0.09057,
              "low": 0.08958,
              "open": 0.09026,
              "timestamp": 1788962400000,
              "volume": 17943.0
            },
            {
              "close": 0.08885,
              "high": 0.0903,
              "low": 0.088,
              "open": 0.08973,
              "timestamp": 1788966000000,
              "volume": 17309.0
            },
            {
              "close": 0.0891,
              "high": 0.08934,
              "low": 0.08849,
              "open": 0.08885,
              "timestamp": 1788969600000,
              "volume": 17910.0
            },
            {
              "close": 0.08904,
              "high": 0.08932,
              "low": 0.08881,
              "open": 0.0891,
              "timestamp": 1788973200000,
              "volume": 17866.0
            },
            {
              "close": 0.08851,
              "high": 0.08909,
              "low": 0.08849,
              "open": 0.08904,
              "timestamp": 1788976800000,
              "volume": 17869.0
            },
            {
              "close": 0.08695,
              "high": 0.08866,
              "low": 0.08643,
              "open": 0.08851,
              "timestamp": 1788980400000,
              "volume": 17901.0
            },
            {
              "close": 0.08696,
              "high": 0.08706,
              "low": 0.08584,
              "open": 0.08694,
              "timestamp": 1788984000000,
              "volume": 17903.0
            },
            {
              "close": 0.0864,
              "high": 0.08699,
              "low": 0.08605,
              "open": 0.08696,
              "timestamp": 1788987600000,
              "volume": 16589.0
            },
            {
              "close": 0.08549,
              "high": 0.08651,
              "low": 0.08466,
              "open": 0.0864,
              "timestamp": 1788991200000,
              "volume": 17295.0
            },
            {
              "close": 0.08609,
              "high": 0.08615,
              "low": 0.08547,
              "open": 0.08549,
              "timestamp": 1788994800000,
              "volume": 17846.0
            },
            {
              "close": 0.08554,
              "high": 0.08616,
              "low": 0.08547,
              "open": 0.08609,
              "timestamp": 1788998400000,
              "volume": 17886.0
            },
            {
              "close": 0.08544,
              "high": 0.08619,
              "low": 0.08505,
              "open": 0.08554,
              "timestamp": 1789002000000,
              "volume": 17892.0
            },
            {
              "close": 0.08595,
              "high": 0.08598,
              "low": 0.08521,
              "open": 0.08544,
              "timestamp": 1789005600000,
              "volume": 17838.0
            },
            {
              "close": 0.0859,
              "high": 0.0861,
              "low": 0.08575,
              "open": 0.08595,
              "timestamp": 1789009200000,
              "volume": 17825.0
            },
            {
              "close": 0.08568,
              "high": 0.08605,
              "low": 0.08565,
              "open": 0.0859,
              "timestamp": 1789012800000,
              "volume": 17753.0
            },
            {
              "close": 0.08599,
              "high": 0.08611,
              "low": 0.08542,
              "open": 0.08568,
              "timestamp": 1789016400000,
              "volume": 17809.0
            },
            {
              "close": 0.08572,
              "high": 0.086,
              "low": 0.08536,
              "open": 0.08599,
              "timestamp": 1789020000000,
              "volume": 17804.0
            },
            {
              "close": 0.08528,
              "high": 0.08573,
              "low": 0.08473,
              "open": 0.08572,
              "timestamp": 1789023600000,
              "volume": 17833.0
            },
            {
              "close": 0.08523,
              "high": 0.08546,
              "low": 0.08514,
              "open": 0.08528,
              "timestamp": 1789027200000,
              "volume": 17808.0
            },
            {
              "close": 0.0849,
              "high": 0.08531,
              "low": 0.08476,
              "open": 0.08522,
              "timestamp": 1789030800000,
              "volume": 17813.0
            },
            {
              "close": 0.08499,
              "high": 0.08537,
              "low": 0.08485,
              "open": 0.0849,
              "timestamp": 1789034400000,
              "volume": 17804.0
            },
            {
              "close": 0.08504,
              "high": 0.08546,
              "low": 0.08472,
              "open": 0.08499,
              "timestamp": 1789038000000,
              "volume": 17830.0
            },
            {
              "close": 0.08369,
              "high": 0.0854,
              "low": 0.08214,
              "open": 0.08504,
              "timestamp": 1789041600000,
              "volume": 17903.0
            },
            {
              "close": 0.08393,
              "high": 0.08413,
              "low": 0.08314,
              "open": 0.08368,
              "timestamp": 1789045200000,
              "volume": 17931.0
            },
            {
              "close": 0.08373,
              "high": 0.08421,
              "low": 0.08339,
              "open": 0.08393,
              "timestamp": 1789048800000,
              "volume": 17715.0
            },
            {
              "close": 0.08365,
              "high": 0.08378,
              "low": 0.08322,
              "open": 0.08373,
              "timestamp": 1789052400000,
              "volume": 17894.0
            },
            {
              "close": 0.08346,
              "high": 0.08376,
              "low": 0.08264,
              "open": 0.08365,
              "timestamp": 1789056000000,
              "volume": 17919.0
            },
            {
              "close": 0.0838,
              "high": 0.08413,
              "low": 0.08333,
              "open": 0.08346,
              "timestamp": 1789059600000,
              "volume": 17888.0
            },
            {
              "close": 0.08394,
              "high": 0.08397,
              "low": 0.08322,
              "open": 0.08382,
              "timestamp": 1789063200000,
              "volume": 17882.0
            },
            {
              "close": 0.08388,
              "high": 0.08425,
              "low": 0.08373,
              "open": 0.08394,
              "timestamp": 1789066800000,
              "volume": 17860.0
            },
            {
              "close": 0.08411,
              "high": 0.08427,
              "low": 0.08381,
              "open": 0.08388,
              "timestamp": 1789070400000,
              "volume": 17759.0
            },
            {
              "close": 0.08401,
              "high": 0.08423,
              "low": 0.08389,
              "open": 0.08411,
              "timestamp": 1789074000000,
              "volume": 16568.0
            },
            {
              "close": 0.08348,
              "high": 0.08421,
              "low": 0.08343,
              "open": 0.08401,
              "timestamp": 1789077600000,
              "volume": 17197.0
            },
            {
              "close": 0.08284,
              "high": 0.08355,
              "low": 0.08274,
              "open": 0.08348,
              "timestamp": 1789081200000,
              "volume": 17851.0
            },
            {
              "close": 0.08338,
              "high": 0.08349,
              "low": 0.08279,
              "open": 0.08284,
              "timestamp": 1789084800000,
              "volume": 17845.0
            },
            {
              "close": 0.08349,
              "high": 0.08359,
              "low": 0.08292,
              "open": 0.08338,
              "timestamp": 1789088400000,
              "volume": 17869.0
            },
            {
              "close": 0.08342,
              "high": 0.08355,
              "low": 0.08309,
              "open": 0.08349,
              "timestamp": 1789092000000,
              "volume": 17780.0
            },
            {
              "close": 0.08367,
              "high": 0.0837,
              "low": 0.0832,
              "open": 0.08342,
              "timestamp": 1789095600000,
              "volume": 17779.0
            },
            {
              "close": 0.084,
              "high": 0.08412,
              "low": 0.08361,
              "open": 0.08367,
              "timestamp": 1789099200000,
              "volume": 17760.0
            },
            {
              "close": 0.08404,
              "high": 0.08408,
              "low": 0.08381,
              "open": 0.084,
              "timestamp": 1789102800000,
              "volume": 17720.0
            },
            {
              "close": 0.08393,
              "high": 0.08411,
              "low": 0.0838,
              "open": 0.08404,
              "timestamp": 1789106400000,
              "volume": 17673.0
            },
            {
              "close": 0.08374,
              "high": 0.08412,
              "low": 0.08371,
              "open": 0.08393,
              "timestamp": 1789110000000,
              "volume": 17716.0
            },
            {
              "close": 0.08397,
              "high": 0.08418,
              "low": 0.08364,
              "open": 0.08374,
              "timestamp": 1789113600000,
              "volume": 17744.0
            },
            {
              "close": 0.08361,
              "high": 0.08403,
              "low": 0.0833,
              "open": 0.08397,
              "timestamp": 1789117200000,
              "volume": 17751.0
            },
            {
              "close": 0.08332,
              "high": 0.08384,
              "low": 0.08332,
              "open": 0.08361,
              "timestamp": 1789120800000,
              "volume": 17775.0
            },
            {
              "close": 0.08361,
              "high": 0.08364,
              "low": 0.08287,
              "open": 0.08332,
              "timestamp": 1789124400000,
              "volume": 17833.0
            },
            {
              "close": 0.08509,
              "high": 0.08545,
              "low": 0.08225,
              "open": 0.08361,
              "timestamp": 1789128000000,
              "volume": 17920.0
            },
            {
              "close": 0.08734,
              "high": 0.0874,
              "low": 0.0842,
              "open": 0.08509,
              "timestamp": 1789131600000,
              "volume": 17829.0
            },
            {
              "close": 0.08642,
              "high": 0.08821,
              "low": 0.08594,
              "open": 0.08734,
              "timestamp": 1789135200000,
              "volume": 17863.0
            },
            {
              "close": 0.0849,
              "high": 0.0868,
              "low": 0.08437,
              "open": 0.08642,
              "timestamp": 1789138800000,
              "volume": 17901.0
            },
            {
              "close": 0.08576,
              "high": 0.08579,
              "low": 0.08464,
              "open": 0.08491,
              "timestamp": 1789142400000,
              "volume": 17924.0
            },
            {
              "close": 0.08488,
              "high": 0.08587,
              "low": 0.08478,
              "open": 0.08576,
              "timestamp": 1789146000000,
              "volume": 17896.0
            },
            {
              "close": 0.08401,
              "high": 0.08498,
              "low": 0.08354,
              "open": 0.08488,
              "timestamp": 1789149600000,
              "volume": 17918.0
            },
            {
              "close": 0.08441,
              "high": 0.0845,
              "low": 0.08366,
              "open": 0.08401,
              "timestamp": 1789153200000,
              "volume": 17894.0
            },
            {
              "close": 0.0843,
              "high": 0.0847,
              "low": 0.08399,
              "open": 0.08441,
              "timestamp": 1789156800000,
              "volume": 17808.0
            },
            {
              "close": 0.0839,
              "high": 0.08464,
              "low": 0.08375,
              "open": 0.0843,
              "timestamp": 1789160400000,
              "volume": 16545.0
            },
            {
              "close": 0.08375,
              "high": 0.08425,
              "low": 0.08349,
              "open": 0.0839,
              "timestamp": 1789164000000,
              "volume": 17180.0
            },
            {
              "close": 0.08425,
              "high": 0.08428,
              "low": 0.08369,
              "open": 0.08375,
              "timestamp": 1789167600000,
              "volume": 17663.0
            },
            {
              "close": 0.08413,
              "high": 0.08436,
              "low": 0.08405,
              "open": 0.08425,
              "timestamp": 1789171200000,
              "volume": 17730.0
            },
            {
              "close": 0.08435,
              "high": 0.08452,
              "low": 0.08406,
              "open": 0.08413,
              "timestamp": 1789174800000,
              "volume": 17688.0
            },
            {
              "close": 0.0844,
              "high": 0.08452,
              "low": 0.08427,
              "open": 0.08435,
              "timestamp": 1789178400000,
              "volume": 17672.0
            },
            {
              "close": 0.08438,
              "high": 0.08452,
              "low": 0.08429,
              "open": 0.0844,
              "timestamp": 1789182000000,
              "volume": 17691.0
            },
            {
              "close": 0.08432,
              "high": 0.08445,
              "low": 0.0842,
              "open": 0.08438,
              "timestamp": 1789185600000,
              "volume": 17668.0
            },
            {
              "close": 0.08435,
              "high": 0.08446,
              "low": 0.08417,
              "open": 0.08432,
              "timestamp": 1789189200000,
              "volume": 17702.0
            },
            {
              "close": 0.08436,
              "high": 0.08451,
              "low": 0.08429,
              "open": 0.08435,
              "timestamp": 1789192800000,
              "volume": 17661.0
            },
            {
              "close": 0.08469,
              "high": 0.08475,
              "low": 0.08434,
              "open": 0.08436,
              "timestamp": 1789196400000,
              "volume": 17664.0
            },
            {
              "close": 0.08473,
              "high": 0.08483,
              "low": 0.08456,
              "open": 0.08469,
              "timestamp": 1789200000000,
              "volume": 17697.0
            },
            {
              "close": 0.08489,
              "high": 0.08492,
              "low": 0.08469,
              "open": 0.08473,
              "timestamp": 1789203600000,
              "volume": 17684.0
            },
            {
              "close": 0.08496,
              "high": 0.08511,
              "low": 0.08481,
              "open": 0.08489,
              "timestamp": 1789207200000,
              "volume": 17692.0
            },
            {
              "close": 0.085,
              "high": 0.08505,
              "low": 0.08485,
              "open": 0.08496,
              "timestamp": 1789210800000,
              "volume": 17674.0
            },
            {
              "close": 0.085,
              "high": 0.08511,
              "low": 0.0849,
              "open": 0.085,
              "timestamp": 1789214400000,
              "volume": 17698.0
            },
            {
              "close": 0.08492,
              "high": 0.08505,
              "low": 0.08477,
              "open": 0.085,
              "timestamp": 1789218000000,
              "volume": 17675.0
            },
            {
              "close": 0.08509,
              "high": 0.08514,
              "low": 0.0849,
              "open": 0.08492,
              "timestamp": 1789221600000,
              "volume": 17649.0
            },
            {
              "close": 0.08504,
              "high": 0.0853,
              "low": 0.08492,
              "open": 0.08509,
              "timestamp": 1789225200000,
              "volume": 17737.0
            },
            {
              "close": 0.08496,
              "high": 0.08509,
              "low": 0.0849,
              "open": 0.08504,
              "timestamp": 1789228800000,
              "volume": 17706.0
            },
            {
              "close": 0.08492,
              "high": 0.08505,
              "low": 0.08475,
              "open": 0.08496,
              "timestamp": 1789232400000,
              "volume": 17672.0
            },
            {
              "close": 0.08468,
              "high": 0.08492,
              "low": 0.08462,
              "open": 0.08492,
              "timestamp": 1789236000000,
              "volume": 17634.0
            },
            {
              "close": 0.08473,
              "high": 0.08483,
              "low": 0.08455,
              "open": 0.08468,
              "timestamp": 1789239600000,
              "volume": 17631.0
            },
            {
              "close": 0.08472,
              "high": 0.08491,
              "low": 0.08471,
              "open": 0.08473,
              "timestamp": 1789243200000,
              "volume": 17579.0
            },
            {
              "close": 0.08456,
              "high": 0.0849,
              "low": 0.08454,
              "open": 0.08472,
              "timestamp": 1789246800000,
              "volume": 16593.0
            },
            {
              "close": 0.08459,
              "high": 0.08483,
              "low": 0.08449,
              "open": 0.08456,
              "timestamp": 1789250400000,
              "volume": 17603.0
            },
            {
              "close": 0.08477,
              "high": 0.08484,
              "low": 0.08458,
              "open": 0.08459,
              "timestamp": 1789254000000,
              "volume": 17620.0
            },
            {
              "close": 0.08478,
              "high": 0.08483,
              "low": 0.08464,
              "open": 0.08473,
              "timestamp": 1789257600000,
              "volume": 17358.0
            },
            {
              "close": 0.08492,
              "high": 0.085,
              "low": 0.08473,
              "open": 0.08478,
              "timestamp": 1789261200000,
              "volume": 17736.0
            },
            {
              "close": 0.08488,
              "high": 0.08512,
              "low": 0.08475,
              "open": 0.08492,
              "timestamp": 1789264800000,
              "volume": 17614.0
            },
            {
              "close": 0.08465,
              "high": 0.08508,
              "low": 0.08456,
              "open": 0.08488,
              "timestamp": 1789268400000,
              "volume": 17697.0
            },
            {
              "close": 0.08465,
              "high": 0.0848,
              "low": 0.08456,
              "open": 0.08465,
              "timestamp": 1789272000000,
              "volume": 17624.0
            },
            {
              "close": 0.08478,
              "high": 0.08487,
              "low": 0.08463,
              "open": 0.08465,
              "timestamp": 1789275600000,
              "volume": 17614.0
            },
            {
              "close": 0.08437,
              "high": 0.0848,
              "low": 0.08425,
              "open": 0.08478,
              "timestamp": 1789279200000,
              "volume": 17662.0
            },
            {
              "close": 0.08411,
              "high": 0.08454,
              "low": 0.08408,
              "open": 0.08437,
              "timestamp": 1789282800000,
              "volume": 17653.0
            },
            {
              "close": 0.08349,
              "high": 0.08422,
              "low": 0.08322,
              "open": 0.08411,
              "timestamp": 1789286400000,
              "volume": 17789.0
            },
            {
              "close": 0.08349,
              "high": 0.08363,
              "low": 0.08307,
              "open": 0.08349,
              "timestamp": 1789290000000,
              "volume": 17751.0
            },
            {
              "close": 0.08326,
              "high": 0.08358,
              "low": 0.08315,
              "open": 0.08349,
              "timestamp": 1789293600000,
              "volume": 17639.0
            },
            {
              "close": 0.08349,
              "high": 0.08354,
              "low": 0.08318,
              "open": 0.08326,
              "timestamp": 1789297200000,
              "volume": 17667.0
            },
            {
              "close": 0.08337,
              "high": 0.08354,
              "low": 0.08322,
              "open": 0.08349,
              "timestamp": 1789300800000,
              "volume": 17704.0
            },
            {
              "close": 0.08334,
              "high": 0.08344,
              "low": 0.08275,
              "open": 0.08337,
              "timestamp": 1789304400000,
              "volume": 17782.0
            },
            {
              "close": 0.08371,
              "high": 0.08387,
              "low": 0.08333,
              "open": 0.08334,
              "timestamp": 1789308000000,
              "volume": 17801.0
            },
            {
              "close": 0.08343,
              "high": 0.08375,
              "low": 0.0834,
              "open": 0.08371,
              "timestamp": 1789311600000,
              "volume": 17783.0
            },
            {
              "close": 0.08391,
              "high": 0.08392,
              "low": 0.08342,
              "open": 0.08343,
              "timestamp": 1789315200000,
              "volume": 17770.0
            },
            {
              "close": 0.08438,
              "high": 0.08459,
              "low": 0.08391,
              "open": 0.08391,
              "timestamp": 1789318800000,
              "volume": 17767.0
            },
            {
              "close": 0.08445,
              "high": 0.08453,
              "low": 0.08426,
              "open": 0.08438,
              "timestamp": 1789322400000,
              "volume": 17686.0
            },
            {
              "close": 0.08411,
              "high": 0.08457,
              "low": 0.08405,
              "open": 0.08445,
              "timestamp": 1789326000000,
              "volume": 17655.0
            }
          ],
          "last_price": 0.08411,
          "momentum": "neutral",
          "rsi_14": 49.42,
          "structure": "neutral"
        },
        "4H": {
          "candle_count": 84,
          "candle_status": {
            "data_age_seconds": 14495,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789315200000,
            "latest_timestamp_utc": "2026-09-13T16:00:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 14400
          },
          "candles": [
            {
              "close": 0.08197,
              "high": 0.08591,
              "low": 0.08071,
              "open": 0.08574,
              "timestamp": 1788120000000,
              "volume": 70583.0
            },
            {
              "close": 0.08221,
              "high": 0.08266,
              "low": 0.08137,
              "open": 0.08197,
              "timestamp": 1788134400000,
              "volume": 71579.0
            },
            {
              "close": 0.08266,
              "high": 0.083,
              "low": 0.08183,
              "open": 0.08221,
              "timestamp": 1788148800000,
              "volume": 71260.0
            },
            {
              "close": 0.08259,
              "high": 0.0832,
              "low": 0.08233,
              "open": 0.08266,
              "timestamp": 1788163200000,
              "volume": 71172.0
            },
            {
              "close": 0.08276,
              "high": 0.08324,
              "low": 0.08196,
              "open": 0.08259,
              "timestamp": 1788177600000,
              "volume": 71524.0
            },
            {
              "close": 0.08318,
              "high": 0.08392,
              "low": 0.08261,
              "open": 0.08276,
              "timestamp": 1788192000000,
              "volume": 71456.0
            },
            {
              "close": 0.08279,
              "high": 0.0835,
              "low": 0.0826,
              "open": 0.08318,
              "timestamp": 1788206400000,
              "volume": 69142.0
            },
            {
              "close": 0.08313,
              "high": 0.0834,
              "low": 0.08239,
              "open": 0.08279,
              "timestamp": 1788220800000,
              "volume": 71214.0
            },
            {
              "close": 0.08331,
              "high": 0.08388,
              "low": 0.08304,
              "open": 0.08313,
              "timestamp": 1788235200000,
              "volume": 71124.0
            },
            {
              "close": 0.08313,
              "high": 0.08336,
              "low": 0.08208,
              "open": 0.08331,
              "timestamp": 1788249600000,
              "volume": 71400.0
            },
            {
              "close": 0.08266,
              "high": 0.08316,
              "low": 0.08159,
              "open": 0.08313,
              "timestamp": 1788264000000,
              "volume": 71527.0
            },
            {
              "close": 0.08189,
              "high": 0.08268,
              "low": 0.08063,
              "open": 0.08266,
              "timestamp": 1788278400000,
              "volume": 71407.0
            },
            {
              "close": 0.08161,
              "high": 0.08208,
              "low": 0.08094,
              "open": 0.0819,
              "timestamp": 1788292800000,
              "volume": 69041.0
            },
            {
              "close": 0.08146,
              "high": 0.08171,
              "low": 0.08021,
              "open": 0.08163,
              "timestamp": 1788307200000,
              "volume": 71296.0
            },
            {
              "close": 0.08161,
              "high": 0.08204,
              "low": 0.08109,
              "open": 0.08146,
              "timestamp": 1788321600000,
              "volume": 71142.0
            },
            {
              "close": 0.08118,
              "high": 0.08169,
              "low": 0.08007,
              "open": 0.08161,
              "timestamp": 1788336000000,
              "volume": 71414.0
            },
            {
              "close": 0.08161,
              "high": 0.08196,
              "low": 0.08063,
              "open": 0.08118,
              "timestamp": 1788350400000,
              "volume": 62728.0
            },
            {
              "close": 0.08124,
              "high": 0.08184,
              "low": 0.0808,
              "open": 0.08161,
              "timestamp": 1788364800000,
              "volume": 71035.0
            },
            {
              "close": 0.0817,
              "high": 0.08187,
              "low": 0.08082,
              "open": 0.08124,
              "timestamp": 1788379200000,
              "volume": 69228.0
            },
            {
              "close": 0.08272,
              "high": 0.08323,
              "low": 0.08109,
              "open": 0.0817,
              "timestamp": 1788393600000,
              "volume": 71330.0
            },
            {
              "close": 0.08284,
              "high": 0.08363,
              "low": 0.08201,
              "open": 0.08272,
              "timestamp": 1788408000000,
              "volume": 71286.0
            },
            {
              "close": 0.08321,
              "high": 0.08356,
              "low": 0.08249,
              "open": 0.08285,
              "timestamp": 1788422400000,
              "volume": 70485.0
            },
            {
              "close": 0.08916,
              "high": 0.08936,
              "low": 0.08305,
              "open": 0.08321,
              "timestamp": 1788436800000,
              "volume": 62864.0
            },
            {
              "close": 0.08927,
              "high": 0.08994,
              "low": 0.08804,
              "open": 0.08915,
              "timestamp": 1788451200000,
              "volume": 71681.0
            },
            {
              "close": 0.08776,
              "high": 0.08933,
              "low": 0.08707,
              "open": 0.08926,
              "timestamp": 1788465600000,
              "volume": 69606.0
            },
            {
              "close": 0.08711,
              "high": 0.08806,
              "low": 0.08656,
              "open": 0.08776,
              "timestamp": 1788480000000,
              "volume": 71352.0
            },
            {
              "close": 0.08696,
              "high": 0.08753,
              "low": 0.08647,
              "open": 0.0871,
              "timestamp": 1788494400000,
              "volume": 71397.0
            },
            {
              "close": 0.08769,
              "high": 0.08828,
              "low": 0.08669,
              "open": 0.08696,
              "timestamp": 1788508800000,
              "volume": 71443.0
            },
            {
              "close": 0.08433,
              "high": 0.08798,
              "low": 0.08372,
              "open": 0.08769,
              "timestamp": 1788523200000,
              "volume": 61682.0
            },
            {
              "close": 0.08466,
              "high": 0.08497,
              "low": 0.08395,
              "open": 0.08433,
              "timestamp": 1788537600000,
              "volume": 71323.0
            },
            {
              "close": 0.08472,
              "high": 0.0849,
              "low": 0.08435,
              "open": 0.08466,
              "timestamp": 1788552000000,
              "volume": 68384.0
            },
            {
              "close": 0.08455,
              "high": 0.08489,
              "low": 0.08429,
              "open": 0.08472,
              "timestamp": 1788566400000,
              "volume": 70322.0
            },
            {
              "close": 0.0856,
              "high": 0.08573,
              "low": 0.08442,
              "open": 0.08457,
              "timestamp": 1788580800000,
              "volume": 54375.0
            },
            {
              "close": 0.08606,
              "high": 0.08628,
              "low": 0.08542,
              "open": 0.08555,
              "timestamp": 1788595200000,
              "volume": 64038.0
            },
            {
              "close": 0.08752,
              "high": 0.0881,
              "low": 0.08604,
              "open": 0.08606,
              "timestamp": 1788609600000,
              "volume": 71219.0
            },
            {
              "close": 0.09071,
              "high": 0.09491,
              "low": 0.08727,
              "open": 0.08753,
              "timestamp": 1788624000000,
              "volume": 71391.0
            },
            {
              "close": 0.08961,
              "high": 0.09127,
              "low": 0.08921,
              "open": 0.09071,
              "timestamp": 1788638400000,
              "volume": 70239.0
            },
            {
              "close": 0.09124,
              "high": 0.09166,
              "low": 0.08969,
              "open": 0.0897,
              "timestamp": 1788652800000,
              "volume": 70997.0
            },
            {
              "close": 0.09079,
              "high": 0.09194,
              "low": 0.09021,
              "open": 0.09124,
              "timestamp": 1788667200000,
              "volume": 70914.0
            },
            {
              "close": 0.09005,
              "high": 0.0911,
              "low": 0.08824,
              "open": 0.09079,
              "timestamp": 1788681600000,
              "volume": 71139.0
            },
            {
              "close": 0.08888,
              "high": 0.09006,
              "low": 0.0875,
              "open": 0.09005,
              "timestamp": 1788696000000,
              "volume": 71228.0
            },
            {
              "close": 0.0895,
              "high": 0.08953,
              "low": 0.08861,
              "open": 0.08888,
              "timestamp": 1788710400000,
              "volume": 70971.0
            },
            {
              "close": 0.09085,
              "high": 0.09101,
              "low": 0.0894,
              "open": 0.0895,
              "timestamp": 1788724800000,
              "volume": 70549.0
            },
            {
              "close": 0.08928,
              "high": 0.0913,
              "low": 0.08912,
              "open": 0.09085,
              "timestamp": 1788739200000,
              "volume": 71557.0
            },
            {
              "close": 0.08932,
              "high": 0.09057,
              "low": 0.08849,
              "open": 0.08929,
              "timestamp": 1788753600000,
              "volume": 71413.0
            },
            {
              "close": 0.08974,
              "high": 0.09004,
              "low": 0.08916,
              "open": 0.08932,
              "timestamp": 1788768000000,
              "volume": 71237.0
            },
            {
              "close": 0.0889,
              "high": 0.09179,
              "low": 0.08859,
              "open": 0.08974,
              "timestamp": 1788782400000,
              "volume": 71596.0
            },
            {
              "close": 0.09048,
              "high": 0.09061,
              "low": 0.08888,
              "open": 0.08892,
              "timestamp": 1788796800000,
              "volume": 71289.0
            },
            {
              "close": 0.09044,
              "high": 0.09092,
              "low": 0.08961,
              "open": 0.09048,
              "timestamp": 1788811200000,
              "volume": 69505.0
            },
            {
              "close": 0.08988,
              "high": 0.09162,
              "low": 0.0895,
              "open": 0.09044,
              "timestamp": 1788825600000,
              "volume": 71497.0
            },
            {
              "close": 0.08923,
              "high": 0.09018,
              "low": 0.08889,
              "open": 0.08988,
              "timestamp": 1788840000000,
              "volume": 71428.0
            },
            {
              "close": 0.08948,
              "high": 0.0909,
              "low": 0.08875,
              "open": 0.08922,
              "timestamp": 1788854400000,
              "volume": 71347.0
            },
            {
              "close": 0.09057,
              "high": 0.09075,
              "low": 0.08792,
              "open": 0.08948,
              "timestamp": 1788868800000,
              "volume": 71685.0
            },
            {
              "close": 0.0895,
              "high": 0.09082,
              "low": 0.08915,
              "open": 0.09057,
              "timestamp": 1788883200000,
              "volume": 71556.0
            },
            {
              "close": 0.08998,
              "high": 0.09038,
              "low": 0.0892,
              "open": 0.08949,
              "timestamp": 1788897600000,
              "volume": 69614.0
            },
            {
              "close": 0.08952,
              "high": 0.09086,
              "low": 0.08932,
              "open": 0.08998,
              "timestamp": 1788912000000,
              "volume": 71545.0
            },
            {
              "close": 0.09081,
              "high": 0.0909,
              "low": 0.08952,
              "open": 0.08952,
              "timestamp": 1788926400000,
              "volume": 71470.0
            },
            {
              "close": 0.09078,
              "high": 0.09139,
              "low": 0.08999,
              "open": 0.09081,
              "timestamp": 1788940800000,
              "volume": 71523.0
            },
            {
              "close": 0.08885,
              "high": 0.09154,
              "low": 0.088,
              "open": 0.09078,
              "timestamp": 1788955200000,
              "volume": 71066.0
            },
            {
              "close": 0.08695,
              "high": 0.08934,
              "low": 0.08643,
              "open": 0.08885,
              "timestamp": 1788969600000,
              "volume": 71546.0
            },
            {
              "close": 0.08609,
              "high": 0.08706,
              "low": 0.08466,
              "open": 0.08694,
              "timestamp": 1788984000000,
              "volume": 69633.0
            },
            {
              "close": 0.0859,
              "high": 0.08619,
              "low": 0.08505,
              "open": 0.08609,
              "timestamp": 1788998400000,
              "volume": 71441.0
            },
            {
              "close": 0.08528,
              "high": 0.08611,
              "low": 0.08473,
              "open": 0.0859,
              "timestamp": 1789012800000,
              "volume": 71199.0
            },
            {
              "close": 0.08504,
              "high": 0.08546,
              "low": 0.08472,
              "open": 0.08528,
              "timestamp": 1789027200000,
              "volume": 71255.0
            },
            {
              "close": 0.08365,
              "high": 0.0854,
              "low": 0.08214,
              "open": 0.08504,
              "timestamp": 1789041600000,
              "volume": 71443.0
            },
            {
              "close": 0.08388,
              "high": 0.08425,
              "low": 0.08264,
              "open": 0.08365,
              "timestamp": 1789056000000,
              "volume": 71549.0
            },
            {
              "close": 0.08284,
              "high": 0.08427,
              "low": 0.08274,
              "open": 0.08388,
              "timestamp": 1789070400000,
              "volume": 69375.0
            },
            {
              "close": 0.08367,
              "high": 0.0837,
              "low": 0.08279,
              "open": 0.08284,
              "timestamp": 1789084800000,
              "volume": 71273.0
            },
            {
              "close": 0.08374,
              "high": 0.08412,
              "low": 0.08361,
              "open": 0.08367,
              "timestamp": 1789099200000,
              "volume": 70869.0
            },
            {
              "close": 0.08361,
              "high": 0.08418,
              "low": 0.08287,
              "open": 0.08374,
              "timestamp": 1789113600000,
              "volume": 71103.0
            },
            {
              "close": 0.0849,
              "high": 0.08821,
              "low": 0.08225,
              "open": 0.08361,
              "timestamp": 1789128000000,
              "volume": 71513.0
            },
            {
              "close": 0.08441,
              "high": 0.08587,
              "low": 0.08354,
              "open": 0.08491,
              "timestamp": 1789142400000,
              "volume": 71632.0
            },
            {
              "close": 0.08425,
              "high": 0.0847,
              "low": 0.08349,
              "open": 0.08441,
              "timestamp": 1789156800000,
              "volume": 69196.0
            },
            {
              "close": 0.08438,
              "high": 0.08452,
              "low": 0.08405,
              "open": 0.08425,
              "timestamp": 1789171200000,
              "volume": 70781.0
            },
            {
              "close": 0.08469,
              "high": 0.08475,
              "low": 0.08417,
              "open": 0.08438,
              "timestamp": 1789185600000,
              "volume": 70695.0
            },
            {
              "close": 0.085,
              "high": 0.08511,
              "low": 0.08456,
              "open": 0.08469,
              "timestamp": 1789200000000,
              "volume": 70747.0
            },
            {
              "close": 0.08504,
              "high": 0.0853,
              "low": 0.08477,
              "open": 0.085,
              "timestamp": 1789214400000,
              "volume": 70759.0
            },
            {
              "close": 0.08473,
              "high": 0.08509,
              "low": 0.08455,
              "open": 0.08504,
              "timestamp": 1789228800000,
              "volume": 70643.0
            },
            {
              "close": 0.08477,
              "high": 0.08491,
              "low": 0.08449,
              "open": 0.08473,
              "timestamp": 1789243200000,
              "volume": 69395.0
            },
            {
              "close": 0.08465,
              "high": 0.08512,
              "low": 0.08456,
              "open": 0.08473,
              "timestamp": 1789257600000,
              "volume": 70405.0
            },
            {
              "close": 0.08411,
              "high": 0.08487,
              "low": 0.08408,
              "open": 0.08465,
              "timestamp": 1789272000000,
              "volume": 70553.0
            },
            {
              "close": 0.08349,
              "high": 0.08422,
              "low": 0.08307,
              "open": 0.08411,
              "timestamp": 1789286400000,
              "volume": 70846.0
            },
            {
              "close": 0.08343,
              "high": 0.08387,
              "low": 0.08275,
              "open": 0.08349,
              "timestamp": 1789300800000,
              "volume": 71070.0
            },
            {
              "close": 0.08411,
              "high": 0.08459,
              "low": 0.08342,
              "open": 0.08343,
              "timestamp": 1789315200000,
              "volume": 70878.0
            }
          ],
          "last_price": 0.08411,
          "momentum": "neutral",
          "rsi_14": 42.36,
          "structure": "neutral"
        },
        "5M": {
          "candle_count": 144,
          "candle_status": {
            "data_age_seconds": 395,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789329300000,
            "latest_timestamp_utc": "2026-09-13T19:55:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 300
          },
          "candles": [
            {
              "close": 0.08412,
              "high": 0.08422,
              "low": 0.08406,
              "open": 0.08411,
              "timestamp": 1789286400000,
              "volume": 1481.0
            },
            {
              "close": 0.08404,
              "high": 0.08412,
              "low": 0.08399,
              "open": 0.08412,
              "timestamp": 1789286700000,
              "volume": 1477.0
            },
            {
              "close": 0.084,
              "high": 0.08404,
              "low": 0.08392,
              "open": 0.08404,
              "timestamp": 1789287000000,
              "volume": 1481.0
            },
            {
              "close": 0.08392,
              "high": 0.08401,
              "low": 0.08387,
              "open": 0.084,
              "timestamp": 1789287300000,
              "volume": 1478.0
            },
            {
              "close": 0.08389,
              "high": 0.08398,
              "low": 0.08388,
              "open": 0.08392,
              "timestamp": 1789287600000,
              "volume": 1474.0
            },
            {
              "close": 0.08377,
              "high": 0.08391,
              "low": 0.08376,
              "open": 0.08389,
              "timestamp": 1789287900000,
              "volume": 1480.0
            },
            {
              "close": 0.08353,
              "high": 0.08378,
              "low": 0.08328,
              "open": 0.08377,
              "timestamp": 1789288200000,
              "volume": 1487.0
            },
            {
              "close": 0.08335,
              "high": 0.08361,
              "low": 0.08333,
              "open": 0.08353,
              "timestamp": 1789288500000,
              "volume": 1490.0
            },
            {
              "close": 0.08327,
              "high": 0.08347,
              "low": 0.08322,
              "open": 0.08335,
              "timestamp": 1789288800000,
              "volume": 1486.0
            },
            {
              "close": 0.08351,
              "high": 0.08355,
              "low": 0.08328,
              "open": 0.08328,
              "timestamp": 1789289100000,
              "volume": 1488.0
            },
            {
              "close": 0.08347,
              "high": 0.08353,
              "low": 0.0834,
              "open": 0.08351,
              "timestamp": 1789289400000,
              "volume": 1483.0
            },
            {
              "close": 0.08349,
              "high": 0.08353,
              "low": 0.08341,
              "open": 0.08347,
              "timestamp": 1789289700000,
              "volume": 1484.0
            },
            {
              "close": 0.08359,
              "high": 0.0836,
              "low": 0.08347,
              "open": 0.08349,
              "timestamp": 1789290000000,
              "volume": 1483.0
            },
            {
              "close": 0.0836,
              "high": 0.08363,
              "low": 0.08358,
              "open": 0.0836,
              "timestamp": 1789290300000,
              "volume": 1478.0
            },
            {
              "close": 0.08357,
              "high": 0.08361,
              "low": 0.08353,
              "open": 0.0836,
              "timestamp": 1789290600000,
              "volume": 1479.0
            },
            {
              "close": 0.08353,
              "high": 0.0836,
              "low": 0.08351,
              "open": 0.08357,
              "timestamp": 1789290900000,
              "volume": 1479.0
            },
            {
              "close": 0.08334,
              "high": 0.08359,
              "low": 0.08328,
              "open": 0.08353,
              "timestamp": 1789291200000,
              "volume": 1474.0
            },
            {
              "close": 0.08329,
              "high": 0.08343,
              "low": 0.08315,
              "open": 0.08334,
              "timestamp": 1789291500000,
              "volume": 1484.0
            },
            {
              "close": 0.08316,
              "high": 0.08335,
              "low": 0.08307,
              "open": 0.08329,
              "timestamp": 1789291800000,
              "volume": 1486.0
            },
            {
              "close": 0.08346,
              "high": 0.08356,
              "low": 0.08315,
              "open": 0.08316,
              "timestamp": 1789292100000,
              "volume": 1487.0
            },
            {
              "close": 0.08342,
              "high": 0.08349,
              "low": 0.0834,
              "open": 0.08346,
              "timestamp": 1789292400000,
              "volume": 1479.0
            },
            {
              "close": 0.08353,
              "high": 0.08353,
              "low": 0.0834,
              "open": 0.08342,
              "timestamp": 1789292700000,
              "volume": 1478.0
            },
            {
              "close": 0.0835,
              "high": 0.08353,
              "low": 0.08347,
              "open": 0.08353,
              "timestamp": 1789293000000,
              "volume": 1474.0
            },
            {
              "close": 0.08349,
              "high": 0.08353,
              "low": 0.08344,
              "open": 0.0835,
              "timestamp": 1789293300000,
              "volume": 1470.0
            },
            {
              "close": 0.08355,
              "high": 0.08358,
              "low": 0.08348,
              "open": 0.08349,
              "timestamp": 1789293600000,
              "volume": 1467.0
            },
            {
              "close": 0.08352,
              "high": 0.08355,
              "low": 0.0835,
              "open": 0.08355,
              "timestamp": 1789293900000,
              "volume": 1471.0
            },
            {
              "close": 0.08354,
              "high": 0.08354,
              "low": 0.08348,
              "open": 0.08352,
              "timestamp": 1789294200000,
              "volume": 1475.0
            },
            {
              "close": 0.08349,
              "high": 0.08356,
              "low": 0.08348,
              "open": 0.08354,
              "timestamp": 1789294500000,
              "volume": 1467.0
            },
            {
              "close": 0.08351,
              "high": 0.08353,
              "low": 0.08349,
              "open": 0.08349,
              "timestamp": 1789294800000,
              "volume": 1455.0
            },
            {
              "close": 0.08351,
              "high": 0.08356,
              "low": 0.08346,
              "open": 0.08351,
              "timestamp": 1789295100000,
              "volume": 1469.0
            },
            {
              "close": 0.08347,
              "high": 0.08355,
              "low": 0.08347,
              "open": 0.08351,
              "timestamp": 1789295400000,
              "volume": 1470.0
            },
            {
              "close": 0.08346,
              "high": 0.08347,
              "low": 0.0834,
              "open": 0.08347,
              "timestamp": 1789295700000,
              "volume": 1467.0
            },
            {
              "close": 0.0833,
              "high": 0.08346,
              "low": 0.08321,
              "open": 0.08346,
              "timestamp": 1789296000000,
              "volume": 1476.0
            },
            {
              "close": 0.08334,
              "high": 0.08337,
              "low": 0.0833,
              "open": 0.0833,
              "timestamp": 1789296300000,
              "volume": 1471.0
            },
            {
              "close": 0.08325,
              "high": 0.08334,
              "low": 0.08321,
              "open": 0.08334,
              "timestamp": 1789296600000,
              "volume": 1474.0
            },
            {
              "close": 0.08326,
              "high": 0.08332,
              "low": 0.08315,
              "open": 0.08325,
              "timestamp": 1789296900000,
              "volume": 1477.0
            },
            {
              "close": 0.08342,
              "high": 0.08343,
              "low": 0.08318,
              "open": 0.08326,
              "timestamp": 1789297200000,
              "volume": 1484.0
            },
            {
              "close": 0.08333,
              "high": 0.08344,
              "low": 0.0833,
              "open": 0.08343,
              "timestamp": 1789297500000,
              "volume": 1482.0
            },
            {
              "close": 0.08333,
              "high": 0.08338,
              "low": 0.08331,
              "open": 0.08333,
              "timestamp": 1789297800000,
              "volume": 1479.0
            },
            {
              "close": 0.08343,
              "high": 0.08345,
              "low": 0.08332,
              "open": 0.08333,
              "timestamp": 1789298100000,
              "volume": 1474.0
            },
            {
              "close": 0.08345,
              "high": 0.08347,
              "low": 0.08341,
              "open": 0.08343,
              "timestamp": 1789298400000,
              "volume": 1473.0
            },
            {
              "close": 0.08344,
              "high": 0.08348,
              "low": 0.08344,
              "open": 0.08345,
              "timestamp": 1789298700000,
              "volume": 1465.0
            },
            {
              "close": 0.08345,
              "high": 0.08346,
              "low": 0.0834,
              "open": 0.08344,
              "timestamp": 1789299000000,
              "volume": 1468.0
            },
            {
              "close": 0.08349,
              "high": 0.08349,
              "low": 0.08343,
              "open": 0.08345,
              "timestamp": 1789299300000,
              "volume": 1471.0
            },
            {
              "close": 0.08347,
              "high": 0.08351,
              "low": 0.08346,
              "open": 0.08349,
              "timestamp": 1789299600000,
              "volume": 1469.0
            },
            {
              "close": 0.08347,
              "high": 0.08349,
              "low": 0.08344,
              "open": 0.08347,
              "timestamp": 1789299900000,
              "volume": 1467.0
            },
            {
              "close": 0.08352,
              "high": 0.08353,
              "low": 0.08347,
              "open": 0.08347,
              "timestamp": 1789300200000,
              "volume": 1468.0
            },
            {
              "close": 0.08349,
              "high": 0.08354,
              "low": 0.08347,
              "open": 0.08352,
              "timestamp": 1789300500000,
              "volume": 1467.0
            },
            {
              "close": 0.0834,
              "high": 0.08349,
              "low": 0.0834,
              "open": 0.08349,
              "timestamp": 1789300800000,
              "volume": 1474.0
            },
            {
              "close": 0.08338,
              "high": 0.08341,
              "low": 0.08335,
              "open": 0.0834,
              "timestamp": 1789301100000,
              "volume": 1484.0
            },
            {
              "close": 0.08339,
              "high": 0.08343,
              "low": 0.08338,
              "open": 0.08338,
              "timestamp": 1789301400000,
              "volume": 1479.0
            },
            {
              "close": 0.08343,
              "high": 0.08346,
              "low": 0.08338,
              "open": 0.08339,
              "timestamp": 1789301700000,
              "volume": 1480.0
            },
            {
              "close": 0.08348,
              "high": 0.08349,
              "low": 0.08341,
              "open": 0.08343,
              "timestamp": 1789302000000,
              "volume": 1468.0
            },
            {
              "close": 0.08342,
              "high": 0.0835,
              "low": 0.08342,
              "open": 0.08348,
              "timestamp": 1789302300000,
              "volume": 1473.0
            },
            {
              "close": 0.08339,
              "high": 0.08354,
              "low": 0.08339,
              "open": 0.08342,
              "timestamp": 1789302600000,
              "volume": 1473.0
            },
            {
              "close": 0.08332,
              "high": 0.08341,
              "low": 0.08324,
              "open": 0.08339,
              "timestamp": 1789302900000,
              "volume": 1474.0
            },
            {
              "close": 0.08326,
              "high": 0.08333,
              "low": 0.08325,
              "open": 0.08332,
              "timestamp": 1789303200000,
              "volume": 1479.0
            },
            {
              "close": 0.08327,
              "high": 0.08328,
              "low": 0.08322,
              "open": 0.08326,
              "timestamp": 1789303500000,
              "volume": 1475.0
            },
            {
              "close": 0.08334,
              "high": 0.08337,
              "low": 0.08326,
              "open": 0.08327,
              "timestamp": 1789303800000,
              "volume": 1476.0
            },
            {
              "close": 0.08337,
              "high": 0.08338,
              "low": 0.08333,
              "open": 0.08334,
              "timestamp": 1789304100000,
              "volume": 1469.0
            },
            {
              "close": 0.08331,
              "high": 0.08337,
              "low": 0.0833,
              "open": 0.08337,
              "timestamp": 1789304400000,
              "volume": 1476.0
            },
            {
              "close": 0.0834,
              "high": 0.0834,
              "low": 0.08329,
              "open": 0.08331,
              "timestamp": 1789304700000,
              "volume": 1484.0
            },
            {
              "close": 0.08343,
              "high": 0.08344,
              "low": 0.08338,
              "open": 0.0834,
              "timestamp": 1789305000000,
              "volume": 1479.0
            },
            {
              "close": 0.08328,
              "high": 0.08344,
              "low": 0.08328,
              "open": 0.08343,
              "timestamp": 1789305300000,
              "volume": 1476.0
            },
            {
              "close": 0.08322,
              "high": 0.08331,
              "low": 0.08315,
              "open": 0.08328,
              "timestamp": 1789305600000,
              "volume": 1480.0
            },
            {
              "close": 0.08285,
              "high": 0.08323,
              "low": 0.08275,
              "open": 0.08322,
              "timestamp": 1789305900000,
              "volume": 1487.0
            },
            {
              "close": 0.08305,
              "high": 0.08307,
              "low": 0.08283,
              "open": 0.08285,
              "timestamp": 1789306200000,
              "volume": 1489.0
            },
            {
              "close": 0.08316,
              "high": 0.08316,
              "low": 0.08305,
              "open": 0.08305,
              "timestamp": 1789306500000,
              "volume": 1488.0
            },
            {
              "close": 0.08321,
              "high": 0.08323,
              "low": 0.08312,
              "open": 0.08316,
              "timestamp": 1789306800000,
              "volume": 1483.0
            },
            {
              "close": 0.08338,
              "high": 0.08338,
              "low": 0.08321,
              "open": 0.08321,
              "timestamp": 1789307100000,
              "volume": 1484.0
            },
            {
              "close": 0.08334,
              "high": 0.08344,
              "low": 0.08328,
              "open": 0.08338,
              "timestamp": 1789307400000,
              "volume": 1481.0
            },
            {
              "close": 0.08334,
              "high": 0.08337,
              "low": 0.08332,
              "open": 0.08334,
              "timestamp": 1789307700000,
              "volume": 1475.0
            },
            {
              "close": 0.08339,
              "high": 0.08342,
              "low": 0.08333,
              "open": 0.08334,
              "timestamp": 1789308000000,
              "volume": 1478.0
            },
            {
              "close": 0.08357,
              "high": 0.08357,
              "low": 0.08339,
              "open": 0.08339,
              "timestamp": 1789308300000,
              "volume": 1487.0
            },
            {
              "close": 0.08359,
              "high": 0.08363,
              "low": 0.0835,
              "open": 0.08357,
              "timestamp": 1789308600000,
              "volume": 1488.0
            },
            {
              "close": 0.08359,
              "high": 0.08371,
              "low": 0.08355,
              "open": 0.08359,
              "timestamp": 1789308900000,
              "volume": 1493.0
            },
            {
              "close": 0.08361,
              "high": 0.08367,
              "low": 0.08357,
              "open": 0.08359,
              "timestamp": 1789309200000,
              "volume": 1484.0
            },
            {
              "close": 0.08358,
              "high": 0.08363,
              "low": 0.08352,
              "open": 0.08361,
              "timestamp": 1789309500000,
              "volume": 1487.0
            },
            {
              "close": 0.08358,
              "high": 0.08362,
              "low": 0.08354,
              "open": 0.08358,
              "timestamp": 1789309800000,
              "volume": 1482.0
            },
            {
              "close": 0.08372,
              "high": 0.08387,
              "low": 0.08352,
              "open": 0.08358,
              "timestamp": 1789310100000,
              "volume": 1487.0
            },
            {
              "close": 0.08372,
              "high": 0.08381,
              "low": 0.08367,
              "open": 0.08372,
              "timestamp": 1789310400000,
              "volume": 1482.0
            },
            {
              "close": 0.0837,
              "high": 0.08377,
              "low": 0.08369,
              "open": 0.08372,
              "timestamp": 1789310700000,
              "volume": 1481.0
            },
            {
              "close": 0.08371,
              "high": 0.08377,
              "low": 0.08366,
              "open": 0.0837,
              "timestamp": 1789311000000,
              "volume": 1478.0
            },
            {
              "close": 0.08371,
              "high": 0.08373,
              "low": 0.08364,
              "open": 0.08371,
              "timestamp": 1789311300000,
              "volume": 1474.0
            },
            {
              "close": 0.08354,
              "high": 0.08375,
              "low": 0.08352,
              "open": 0.08371,
              "timestamp": 1789311600000,
              "volume": 1487.0
            },
            {
              "close": 0.08358,
              "high": 0.08361,
              "low": 0.08352,
              "open": 0.08354,
              "timestamp": 1789311900000,
              "volume": 1488.0
            },
            {
              "close": 0.08359,
              "high": 0.08359,
              "low": 0.08355,
              "open": 0.08358,
              "timestamp": 1789312200000,
              "volume": 1486.0
            },
            {
              "close": 0.08343,
              "high": 0.08359,
              "low": 0.08341,
              "open": 0.08359,
              "timestamp": 1789312500000,
              "volume": 1488.0
            },
            {
              "close": 0.08365,
              "high": 0.08368,
              "low": 0.08343,
              "open": 0.08343,
              "timestamp": 1789312800000,
              "volume": 1485.0
            },
            {
              "close": 0.08347,
              "high": 0.08365,
              "low": 0.08343,
              "open": 0.08365,
              "timestamp": 1789313100000,
              "volume": 1487.0
            },
            {
              "close": 0.08352,
              "high": 0.08353,
              "low": 0.08342,
              "open": 0.08347,
              "timestamp": 1789313400000,
              "volume": 1482.0
            },
            {
              "close": 0.08342,
              "high": 0.08352,
              "low": 0.08342,
              "open": 0.08352,
              "timestamp": 1789313700000,
              "volume": 1473.0
            },
            {
              "close": 0.08353,
              "high": 0.08357,
              "low": 0.0834,
              "open": 0.08342,
              "timestamp": 1789314000000,
              "volume": 1482.0
            },
            {
              "close": 0.08353,
              "high": 0.08357,
              "low": 0.08347,
              "open": 0.08353,
              "timestamp": 1789314300000,
              "volume": 1472.0
            },
            {
              "close": 0.08349,
              "high": 0.08355,
              "low": 0.08344,
              "open": 0.08353,
              "timestamp": 1789314600000,
              "volume": 1477.0
            },
            {
              "close": 0.08343,
              "high": 0.08349,
              "low": 0.08341,
              "open": 0.08349,
              "timestamp": 1789314900000,
              "volume": 1476.0
            },
            {
              "close": 0.08353,
              "high": 0.08357,
              "low": 0.08342,
              "open": 0.08343,
              "timestamp": 1789315200000,
              "volume": 1483.0
            },
            {
              "close": 0.08372,
              "high": 0.08374,
              "low": 0.0835,
              "open": 0.08353,
              "timestamp": 1789315500000,
              "volume": 1486.0
            },
            {
              "close": 0.08369,
              "high": 0.08384,
              "low": 0.08367,
              "open": 0.08371,
              "timestamp": 1789315800000,
              "volume": 1488.0
            },
            {
              "close": 0.0837,
              "high": 0.08371,
              "low": 0.08363,
              "open": 0.08369,
              "timestamp": 1789316100000,
              "volume": 1477.0
            },
            {
              "close": 0.08374,
              "high": 0.08375,
              "low": 0.08368,
              "open": 0.0837,
              "timestamp": 1789316400000,
              "volume": 1481.0
            },
            {
              "close": 0.08373,
              "high": 0.08379,
              "low": 0.08368,
              "open": 0.08374,
              "timestamp": 1789316700000,
              "volume": 1479.0
            },
            {
              "close": 0.08372,
              "high": 0.08376,
              "low": 0.08371,
              "open": 0.08373,
              "timestamp": 1789317000000,
              "volume": 1479.0
            },
            {
              "close": 0.08375,
              "high": 0.08377,
              "low": 0.08371,
              "open": 0.08372,
              "timestamp": 1789317300000,
              "volume": 1477.0
            },
            {
              "close": 0.0838,
              "high": 0.08384,
              "low": 0.08374,
              "open": 0.08375,
              "timestamp": 1789317600000,
              "volume": 1485.0
            },
            {
              "close": 0.08375,
              "high": 0.08382,
              "low": 0.08371,
              "open": 0.0838,
              "timestamp": 1789317900000,
              "volume": 1479.0
            },
            {
              "close": 0.08383,
              "high": 0.08385,
              "low": 0.08374,
              "open": 0.08375,
              "timestamp": 1789318200000,
              "volume": 1476.0
            },
            {
              "close": 0.08391,
              "high": 0.08392,
              "low": 0.08383,
              "open": 0.08383,
              "timestamp": 1789318500000,
              "volume": 1480.0
            },
            {
              "close": 0.08408,
              "high": 0.0841,
              "low": 0.08391,
              "open": 0.08391,
              "timestamp": 1789318800000,
              "volume": 1482.0
            },
            {
              "close": 0.0842,
              "high": 0.08424,
              "low": 0.08406,
              "open": 0.08408,
              "timestamp": 1789319100000,
              "volume": 1482.0
            },
            {
              "close": 0.08433,
              "high": 0.0845,
              "low": 0.0842,
              "open": 0.0842,
              "timestamp": 1789319400000,
              "volume": 1487.0
            },
            {
              "close": 0.08451,
              "high": 0.08451,
              "low": 0.08432,
              "open": 0.08433,
              "timestamp": 1789319700000,
              "volume": 1482.0
            },
            {
              "close": 0.08441,
              "high": 0.08453,
              "low": 0.0844,
              "open": 0.08452,
              "timestamp": 1789320000000,
              "volume": 1485.0
            },
            {
              "close": 0.08455,
              "high": 0.08459,
              "low": 0.0844,
              "open": 0.08441,
              "timestamp": 1789320300000,
              "volume": 1482.0
            },
            {
              "close": 0.08434,
              "high": 0.08457,
              "low": 0.08428,
              "open": 0.08455,
              "timestamp": 1789320600000,
              "volume": 1487.0
            },
            {
              "close": 0.08437,
              "high": 0.08444,
              "low": 0.08425,
              "open": 0.08434,
              "timestamp": 1789320900000,
              "volume": 1484.0
            },
            {
              "close": 0.08435,
              "high": 0.08441,
              "low": 0.08432,
              "open": 0.08437,
              "timestamp": 1789321200000,
              "volume": 1472.0
            },
            {
              "close": 0.08443,
              "high": 0.08445,
              "low": 0.08435,
              "open": 0.08435,
              "timestamp": 1789321500000,
              "volume": 1482.0
            },
            {
              "close": 0.08441,
              "high": 0.08449,
              "low": 0.08437,
              "open": 0.08443,
              "timestamp": 1789321800000,
              "volume": 1476.0
            },
            {
              "close": 0.08438,
              "high": 0.08445,
              "low": 0.08438,
              "open": 0.08441,
              "timestamp": 1789322100000,
              "volume": 1466.0
            },
            {
              "close": 0.08432,
              "high": 0.0844,
              "low": 0.08431,
              "open": 0.08438,
              "timestamp": 1789322400000,
              "volume": 1480.0
            },
            {
              "close": 0.08428,
              "high": 0.08435,
              "low": 0.08426,
              "open": 0.08432,
              "timestamp": 1789322700000,
              "volume": 1482.0
            },
            {
              "close": 0.08436,
              "high": 0.08436,
              "low": 0.08426,
              "open": 0.08428,
              "timestamp": 1789323000000,
              "volume": 1481.0
            },
            {
              "close": 0.08445,
              "high": 0.08447,
              "low": 0.08433,
              "open": 0.08436,
              "timestamp": 1789323300000,
              "volume": 1480.0
            },
            {
              "close": 0.08449,
              "high": 0.08451,
              "low": 0.08442,
              "open": 0.08445,
              "timestamp": 1789323600000,
              "volume": 1475.0
            },
            {
              "close": 0.08441,
              "high": 0.0845,
              "low": 0.08439,
              "open": 0.08449,
              "timestamp": 1789323900000,
              "volume": 1471.0
            },
            {
              "close": 0.08442,
              "high": 0.0845,
              "low": 0.08436,
              "open": 0.08441,
              "timestamp": 1789324200000,
              "volume": 1472.0
            },
            {
              "close": 0.08442,
              "high": 0.08446,
              "low": 0.08441,
              "open": 0.08442,
              "timestamp": 1789324500000,
              "volume": 1467.0
            },
            {
              "close": 0.08438,
              "high": 0.08444,
              "low": 0.08436,
              "open": 0.08442,
              "timestamp": 1789324800000,
              "volume": 1475.0
            },
            {
              "close": 0.08446,
              "high": 0.08451,
              "low": 0.08438,
              "open": 0.08438,
              "timestamp": 1789325100000,
              "volume": 1471.0
            },
            {
              "close": 0.08451,
              "high": 0.08453,
              "low": 0.08446,
              "open": 0.08446,
              "timestamp": 1789325400000,
              "volume": 1468.0
            },
            {
              "close": 0.08445,
              "high": 0.08451,
              "low": 0.08443,
              "open": 0.08451,
              "timestamp": 1789325700000,
              "volume": 1464.0
            },
            {
              "close": 0.08451,
              "high": 0.08455,
              "low": 0.08445,
              "open": 0.08445,
              "timestamp": 1789326000000,
              "volume": 1476.0
            },
            {
              "close": 0.08441,
              "high": 0.08457,
              "low": 0.0844,
              "open": 0.08451,
              "timestamp": 1789326300000,
              "volume": 1477.0
            },
            {
              "close": 0.08435,
              "high": 0.08443,
              "low": 0.08431,
              "open": 0.08441,
              "timestamp": 1789326600000,
              "volume": 1477.0
            },
            {
              "close": 0.08425,
              "high": 0.08436,
              "low": 0.08425,
              "open": 0.08435,
              "timestamp": 1789326900000,
              "volume": 1469.0
            },
            {
              "close": 0.08428,
              "high": 0.08428,
              "low": 0.08421,
              "open": 0.08425,
              "timestamp": 1789327200000,
              "volume": 1469.0
            },
            {
              "close": 0.08429,
              "high": 0.08432,
              "low": 0.08427,
              "open": 0.08428,
              "timestamp": 1789327500000,
              "volume": 1459.0
            },
            {
              "close": 0.08409,
              "high": 0.08431,
              "low": 0.08407,
              "open": 0.08429,
              "timestamp": 1789327800000,
              "volume": 1479.0
            },
            {
              "close": 0.0841,
              "high": 0.08412,
              "low": 0.08405,
              "open": 0.08409,
              "timestamp": 1789328100000,
              "volume": 1475.0
            },
            {
              "close": 0.08406,
              "high": 0.08413,
              "low": 0.08405,
              "open": 0.0841,
              "timestamp": 1789328400000,
              "volume": 1475.0
            },
            {
              "close": 0.08408,
              "high": 0.0841,
              "low": 0.08406,
              "open": 0.08406,
              "timestamp": 1789328700000,
              "volume": 1467.0
            },
            {
              "close": 0.08409,
              "high": 0.0841,
              "low": 0.08405,
              "open": 0.08408,
              "timestamp": 1789329000000,
              "volume": 1472.0
            },
            {
              "close": 0.08411,
              "high": 0.08412,
              "low": 0.08409,
              "open": 0.08409,
              "timestamp": 1789329300000,
              "volume": 1460.0
            }
          ],
          "last_price": 0.08411,
          "momentum": "neutral",
          "rsi_14": 41.91,
          "structure": "bearish"
        }
      }
    },
    {
      "bridge_analysis": {
        "decision": "WATCH",
        "directional_bias": "bearish",
        "execution_5m": {
          "candle_confirmed": true,
          "confirmed": false,
          "reason": "5M momentum is aligned, but a structural trigger is still missing.",
          "rsi_14": 34.87,
          "rsi_confirmed": true,
          "structure_shift": false
        },
        "execution_context": {
          "atr_14": 0.328373,
          "distance_to_high": 0.9299999999999997,
          "distance_to_low": 0.8500000000000014,
          "extension": "normal",
          "range_position": 0.4775,
          "recent_high": 55.0,
          "recent_low": 53.22
        },
        "geometry": {
          "entry_quality": "acceptable",
          "invalidation": 55.0,
          "reward_to_risk": 0.91,
          "risk_distance": 0.9299999999999997,
          "room_to_target": 0.8500000000000014,
          "target_reference": 53.22
        },
        "multi_horizon_state": "transitioning",
        "reason": "The setup has not earned approval under current multi-horizon evidence.",
        "setup_grade": "WATCH",
        "symbol": "DASHUSD",
        "timeframes": {
          "15M": {
            "candle_count": 192,
            "last_price": 54.07,
            "momentum": "neutral",
            "rsi_14": 46.28,
            "structure": "neutral"
          },
          "1H": {
            "candle_count": 168,
            "last_price": 54.07,
            "momentum": "neutral",
            "rsi_14": 44.43,
            "structure": "bearish"
          },
          "4H": {
            "candle_count": 84,
            "last_price": 54.07,
            "momentum": "bearish",
            "rsi_14": 38.85,
            "structure": "bearish"
          },
          "5M": {
            "candle_count": 144,
            "last_price": 54.07,
            "momentum": "bearish",
            "rsi_14": 34.87,
            "structure": "bearish"
          }
        },
        "trade_plan": {
          "distinct_targets": [
            53.22
          ],
          "entry_reference": 54.07,
          "final_safe_loss": 55.0,
          "geometry_policy": "structural_invalidation_no_synthetic_buffer",
          "live_market_entry_reference": null,
          "live_market_entry_reference_is_authorization": false,
          "live_market_entry_reference_side": null,
          "reason": "Structural trade geometry is viable.",
          "reward_to_tp1": 0.8500000000000014,
          "reward_to_tp2": null,
          "reward_to_tp3": null,
          "risk_distance": 0.9299999999999997,
          "rr_tp1": 0.91,
          "rr_tp2": null,
          "rr_tp3": null,
          "safe_loss": 55.0,
          "stop_buffer": 0.0,
          "stop_buffer_basis": "No synthetic buffer applied. Structural invalidation is the authoritative Bridge stop until Atlas defines an explicit buffer rule.",
          "structure_invalidation": 55.0,
          "target_count": 1,
          "tp1": 53.22,
          "tp2": null,
          "tp3": null,
          "valid": true
        }
      },
      "broker": {
        "route_id": 452,
        "tradable_instrument_id": 207
      },
      "instrument_specs": {
        "available": true,
        "bar_source": "BID",
        "base_currency": "DASH",
        "cache": {
          "age_seconds": 635167.007,
          "captured_at": "2026-09-06T11:35:32.376041+00:00",
          "source": "stale_cache",
          "stale": true
        },
        "contract_size": 10,
        "error": null,
        "leverage": "3.00",
        "lot_step": 0.01,
        "margin_hedging_type": "fx_cfd",
        "maximum_lot": null,
        "minimum_lot": 0.01,
        "minimum_stop_distance": null,
        "quote_currency": "USD",
        "raw_details": {
          "d": {
            "barSource": "BID",
            "baseCurrency": "DASH",
            "betSize": null,
            "betStep": null,
            "bettingCurrency": null,
            "contractMonth": null,
            "country": null,
            "deliveryStatus": null,
            "description": "Dash vs US Dollar",
            "exerciseStyle": null,
            "firstTradeDate": null,
            "hasDaily": true,
            "hasIntraday": true,
            "industry": null,
            "isin": "",
            "lastTradeDate": null,
            "leverage": "3.00",
            "localizedName": "DASHUSD",
            "logoUrl": null,
            "lotSize": 10,
            "lotStep": 0.01,
            "margin_hedging_type": "fx_cfd",
            "marketCap": null,
            "marketDataExchange": "Cryptos",
            "maxLot": null,
            "minLot": 0.01,
            "name": "DASHUSD",
            "noticeDate": null,
            "quotingCurrency": "USD",
            "sector": null,
            "settlementDate": null,
            "settlementSystem": "Immediate",
            "strikePrice": null,
            "strikeType": null,
            "symbolStatus": "FULLY_OPEN",
            "tickCost": [
              {
                "leftRangeLimit": null,
                "tickCost": 0.0
              }
            ],
            "tickSize": [
              {
                "leftRangeLimit": null,
                "tickSize": 0.01
              }
            ],
            "tradeSessionId": 1547,
            "tradeSessionStatusId": 20,
            "tradingExchange": "Crypto",
            "type": "CRYPTO"
          },
          "s": "ok"
        },
        "route_id": 9912,
        "symbol_status": "FULLY_OPEN",
        "tick_cost_raw": 0.0,
        "tick_size": 0.01,
        "tick_value": null,
        "tradable_instrument_id": 207,
        "trading_session_id": 1547,
        "trading_session_status_id": 20
      },
      "market_snapshot": {
        "analysis_price": 54.07,
        "analysis_price_source": "latest_5m_bar",
        "ask": 54.13,
        "ask_size": 100.0,
        "atlas_received_at": "2026-09-13T20:01:38.137266+00:00",
        "bid": 54.09,
        "bid_size": 100.0,
        "broker_staleness_known": false,
        "cache": {
          "age_seconds": 0,
          "captured_at": "2026-09-13T20:01:38.137248+00:00",
          "source": "live",
          "stale": false
        },
        "live_ask": 54.13,
        "live_bid": 54.09,
        "live_executable_market_entry": null,
        "live_executable_market_entry_is_authorization": false,
        "live_executable_market_entry_side": null,
        "live_mid": 54.11,
        "market_entry_price_policy": "LONG market execution evaluates live ask; SHORT market execution evaluates live bid. Structural or pending entry_reference remains context and must be reassessed before approval.",
        "price_semantics": "analysis_price is the latest 5M bar/reference price, not an executable quote. live_bid and live_ask are current TradeLocker quote values; live_mid is their midpoint. For market-entry evaluation use live_ask for LONG and live_bid for SHORT.",
        "quote_age_seconds": null,
        "quote_error": null,
        "quote_note": "Bid/ask values are live TradeLocker quote values. The broker response does not currently expose a quote timestamp, so broker quote age/staleness is left null rather than estimated.",
        "quote_timestamp": null,
        "quotes_available": true,
        "raw_quote": {
          "d": {
            "ap": 54.13,
            "as": 100.0,
            "bp": 54.09,
            "bs": 100.0
          },
          "s": "ok"
        },
        "spread": 0.03999999999999915
      },
      "symbol": "DASHUSD",
      "timeframes": {
        "15M": {
          "candle_count": 192,
          "candle_status": {
            "data_age_seconds": 996,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789328700000,
            "latest_timestamp_utc": "2026-09-13T19:45:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 900
          },
          "candles": [
            {
              "close": 56.69,
              "high": 56.81,
              "low": 56.28,
              "open": 56.3,
              "timestamp": 1789156800000,
              "volume": 3780.0
            },
            {
              "close": 56.46,
              "high": 56.76,
              "low": 56.41,
              "open": 56.69,
              "timestamp": 1789157700000,
              "volume": 3442.0
            },
            {
              "close": 56.57,
              "high": 56.8,
              "low": 56.16,
              "open": 56.46,
              "timestamp": 1789158600000,
              "volume": 3622.0
            },
            {
              "close": 56.45,
              "high": 56.65,
              "low": 56.07,
              "open": 56.57,
              "timestamp": 1789159500000,
              "volume": 3631.0
            },
            {
              "close": 56.72,
              "high": 56.75,
              "low": 56.31,
              "open": 56.45,
              "timestamp": 1789160400000,
              "volume": 2666.0
            },
            {
              "close": 56.24,
              "high": 56.75,
              "low": 56.22,
              "open": 56.72,
              "timestamp": 1789161300000,
              "volume": 3245.0
            },
            {
              "close": 56.25,
              "high": 56.38,
              "low": 56.18,
              "open": 56.24,
              "timestamp": 1789162200000,
              "volume": 3229.0
            },
            {
              "close": 55.52,
              "high": 56.28,
              "low": 55.47,
              "open": 56.25,
              "timestamp": 1789163100000,
              "volume": 3912.0
            },
            {
              "close": 55.78,
              "high": 55.79,
              "low": 55.17,
              "open": 55.52,
              "timestamp": 1789164000000,
              "volume": 3375.0
            },
            {
              "close": 55.57,
              "high": 55.83,
              "low": 55.54,
              "open": 55.78,
              "timestamp": 1789164900000,
              "volume": 3257.0
            },
            {
              "close": 55.67,
              "high": 55.83,
              "low": 55.36,
              "open": 55.56,
              "timestamp": 1789165800000,
              "volume": 3526.0
            },
            {
              "close": 55.45,
              "high": 55.68,
              "low": 55.25,
              "open": 55.68,
              "timestamp": 1789166700000,
              "volume": 3412.0
            },
            {
              "close": 55.55,
              "high": 55.7,
              "low": 55.38,
              "open": 55.46,
              "timestamp": 1789167600000,
              "volume": 3669.0
            },
            {
              "close": 56.12,
              "high": 56.2,
              "low": 55.5,
              "open": 55.55,
              "timestamp": 1789168500000,
              "volume": 3582.0
            },
            {
              "close": 56.25,
              "high": 56.44,
              "low": 56.11,
              "open": 56.12,
              "timestamp": 1789169400000,
              "volume": 3455.0
            },
            {
              "close": 56.84,
              "high": 56.96,
              "low": 56.25,
              "open": 56.25,
              "timestamp": 1789170300000,
              "volume": 3596.0
            },
            {
              "close": 56.78,
              "high": 57.07,
              "low": 56.65,
              "open": 56.82,
              "timestamp": 1789171200000,
              "volume": 3853.0
            },
            {
              "close": 56.95,
              "high": 56.98,
              "low": 56.69,
              "open": 56.78,
              "timestamp": 1789172100000,
              "volume": 3323.0
            },
            {
              "close": 57.11,
              "high": 57.23,
              "low": 56.86,
              "open": 56.95,
              "timestamp": 1789173000000,
              "volume": 3495.0
            },
            {
              "close": 57.02,
              "high": 57.19,
              "low": 56.86,
              "open": 57.1,
              "timestamp": 1789173900000,
              "volume": 3364.0
            },
            {
              "close": 57.09,
              "high": 57.18,
              "low": 56.78,
              "open": 57.02,
              "timestamp": 1789174800000,
              "volume": 3388.0
            },
            {
              "close": 56.94,
              "high": 57.2,
              "low": 56.94,
              "open": 57.09,
              "timestamp": 1789175700000,
              "volume": 3165.0
            },
            {
              "close": 56.72,
              "high": 57.0,
              "low": 56.57,
              "open": 56.94,
              "timestamp": 1789176600000,
              "volume": 3458.0
            },
            {
              "close": 56.74,
              "high": 56.92,
              "low": 56.67,
              "open": 56.72,
              "timestamp": 1789177500000,
              "volume": 2990.0
            },
            {
              "close": 56.66,
              "high": 56.91,
              "low": 56.58,
              "open": 56.74,
              "timestamp": 1789178400000,
              "volume": 3130.0
            },
            {
              "close": 56.46,
              "high": 56.7,
              "low": 56.38,
              "open": 56.66,
              "timestamp": 1789179300000,
              "volume": 3145.0
            },
            {
              "close": 56.4,
              "high": 56.58,
              "low": 56.19,
              "open": 56.46,
              "timestamp": 1789180200000,
              "volume": 3301.0
            },
            {
              "close": 56.36,
              "high": 56.47,
              "low": 56.26,
              "open": 56.4,
              "timestamp": 1789181100000,
              "volume": 2854.0
            },
            {
              "close": 55.99,
              "high": 56.52,
              "low": 55.96,
              "open": 56.36,
              "timestamp": 1789182000000,
              "volume": 3200.0
            },
            {
              "close": 56.09,
              "high": 56.13,
              "low": 55.87,
              "open": 55.99,
              "timestamp": 1789182900000,
              "volume": 3231.0
            },
            {
              "close": 56.3,
              "high": 56.38,
              "low": 55.94,
              "open": 56.09,
              "timestamp": 1789183800000,
              "volume": 3138.0
            },
            {
              "close": 56.37,
              "high": 56.41,
              "low": 56.17,
              "open": 56.3,
              "timestamp": 1789184700000,
              "volume": 3030.0
            },
            {
              "close": 56.42,
              "high": 56.52,
              "low": 56.3,
              "open": 56.37,
              "timestamp": 1789185600000,
              "volume": 3090.0
            },
            {
              "close": 56.3,
              "high": 56.42,
              "low": 56.14,
              "open": 56.42,
              "timestamp": 1789186500000,
              "volume": 2995.0
            },
            {
              "close": 56.44,
              "high": 56.58,
              "low": 56.29,
              "open": 56.3,
              "timestamp": 1789187400000,
              "volume": 2942.0
            },
            {
              "close": 56.39,
              "high": 56.52,
              "low": 56.34,
              "open": 56.44,
              "timestamp": 1789188300000,
              "volume": 2721.0
            },
            {
              "close": 56.18,
              "high": 56.39,
              "low": 56.12,
              "open": 56.39,
              "timestamp": 1789189200000,
              "volume": 3047.0
            },
            {
              "close": 56.07,
              "high": 56.42,
              "low": 56.06,
              "open": 56.18,
              "timestamp": 1789190100000,
              "volume": 2780.0
            },
            {
              "close": 56.19,
              "high": 56.43,
              "low": 56.02,
              "open": 56.07,
              "timestamp": 1789191000000,
              "volume": 2808.0
            },
            {
              "close": 56.16,
              "high": 56.2,
              "low": 56.02,
              "open": 56.19,
              "timestamp": 1789191900000,
              "volume": 2659.0
            },
            {
              "close": 56.13,
              "high": 56.4,
              "low": 56.06,
              "open": 56.16,
              "timestamp": 1789192800000,
              "volume": 3116.0
            },
            {
              "close": 56.29,
              "high": 56.4,
              "low": 56.13,
              "open": 56.13,
              "timestamp": 1789193700000,
              "volume": 2506.0
            },
            {
              "close": 56.2,
              "high": 56.4,
              "low": 56.14,
              "open": 56.29,
              "timestamp": 1789194600000,
              "volume": 2735.0
            },
            {
              "close": 55.99,
              "high": 56.21,
              "low": 55.95,
              "open": 56.2,
              "timestamp": 1789195500000,
              "volume": 2946.0
            },
            {
              "close": 56.83,
              "high": 56.83,
              "low": 55.93,
              "open": 55.99,
              "timestamp": 1789196400000,
              "volume": 3496.0
            },
            {
              "close": 56.57,
              "high": 56.98,
              "low": 56.56,
              "open": 56.82,
              "timestamp": 1789197300000,
              "volume": 3203.0
            },
            {
              "close": 56.57,
              "high": 56.69,
              "low": 56.49,
              "open": 56.57,
              "timestamp": 1789198200000,
              "volume": 2848.0
            },
            {
              "close": 56.85,
              "high": 56.93,
              "low": 56.49,
              "open": 56.57,
              "timestamp": 1789199100000,
              "volume": 3035.0
            },
            {
              "close": 56.56,
              "high": 56.85,
              "low": 56.52,
              "open": 56.85,
              "timestamp": 1789200000000,
              "volume": 3029.0
            },
            {
              "close": 56.41,
              "high": 56.67,
              "low": 56.37,
              "open": 56.56,
              "timestamp": 1789200900000,
              "volume": 2925.0
            },
            {
              "close": 56.38,
              "high": 56.45,
              "low": 56.22,
              "open": 56.41,
              "timestamp": 1789201800000,
              "volume": 3019.0
            },
            {
              "close": 56.38,
              "high": 56.5,
              "low": 56.33,
              "open": 56.38,
              "timestamp": 1789202700000,
              "volume": 2871.0
            },
            {
              "close": 56.12,
              "high": 56.45,
              "low": 56.02,
              "open": 56.38,
              "timestamp": 1789203600000,
              "volume": 3214.0
            },
            {
              "close": 56.03,
              "high": 56.21,
              "low": 55.99,
              "open": 56.12,
              "timestamp": 1789204500000,
              "volume": 3108.0
            },
            {
              "close": 56.1,
              "high": 56.2,
              "low": 55.98,
              "open": 56.03,
              "timestamp": 1789205400000,
              "volume": 2876.0
            },
            {
              "close": 56.12,
              "high": 56.17,
              "low": 56.0,
              "open": 56.1,
              "timestamp": 1789206300000,
              "volume": 2675.0
            },
            {
              "close": 56.26,
              "high": 56.37,
              "low": 56.09,
              "open": 56.12,
              "timestamp": 1789207200000,
              "volume": 3033.0
            },
            {
              "close": 56.35,
              "high": 56.39,
              "low": 56.18,
              "open": 56.26,
              "timestamp": 1789208100000,
              "volume": 2773.0
            },
            {
              "close": 56.24,
              "high": 56.35,
              "low": 56.17,
              "open": 56.35,
              "timestamp": 1789209000000,
              "volume": 2625.0
            },
            {
              "close": 56.13,
              "high": 56.25,
              "low": 56.06,
              "open": 56.24,
              "timestamp": 1789209900000,
              "volume": 2450.0
            },
            {
              "close": 56.18,
              "high": 56.21,
              "low": 56.04,
              "open": 56.13,
              "timestamp": 1789210800000,
              "volume": 2816.0
            },
            {
              "close": 56.04,
              "high": 56.19,
              "low": 56.03,
              "open": 56.18,
              "timestamp": 1789211700000,
              "volume": 2327.0
            },
            {
              "close": 56.24,
              "high": 56.27,
              "low": 56.02,
              "open": 56.04,
              "timestamp": 1789212600000,
              "volume": 2513.0
            },
            {
              "close": 56.2,
              "high": 56.26,
              "low": 56.13,
              "open": 56.25,
              "timestamp": 1789213500000,
              "volume": 2283.0
            },
            {
              "close": 56.19,
              "high": 56.36,
              "low": 56.1,
              "open": 56.2,
              "timestamp": 1789214400000,
              "volume": 2976.0
            },
            {
              "close": 56.19,
              "high": 56.26,
              "low": 55.96,
              "open": 56.19,
              "timestamp": 1789215300000,
              "volume": 2706.0
            },
            {
              "close": 56.4,
              "high": 56.53,
              "low": 56.15,
              "open": 56.19,
              "timestamp": 1789216200000,
              "volume": 3024.0
            },
            {
              "close": 56.29,
              "high": 56.58,
              "low": 56.25,
              "open": 56.4,
              "timestamp": 1789217100000,
              "volume": 3029.0
            },
            {
              "close": 56.18,
              "high": 56.48,
              "low": 56.17,
              "open": 56.29,
              "timestamp": 1789218000000,
              "volume": 3310.0
            },
            {
              "close": 56.14,
              "high": 56.26,
              "low": 56.1,
              "open": 56.18,
              "timestamp": 1789218900000,
              "volume": 3099.0
            },
            {
              "close": 56.24,
              "high": 56.28,
              "low": 56.05,
              "open": 56.14,
              "timestamp": 1789219800000,
              "volume": 2807.0
            },
            {
              "close": 56.02,
              "high": 56.24,
              "low": 55.89,
              "open": 56.24,
              "timestamp": 1789220700000,
              "volume": 2973.0
            },
            {
              "close": 56.26,
              "high": 56.34,
              "low": 55.98,
              "open": 56.02,
              "timestamp": 1789221600000,
              "volume": 3294.0
            },
            {
              "close": 56.38,
              "high": 56.46,
              "low": 56.26,
              "open": 56.26,
              "timestamp": 1789222500000,
              "volume": 3002.0
            },
            {
              "close": 56.29,
              "high": 56.46,
              "low": 56.24,
              "open": 56.38,
              "timestamp": 1789223400000,
              "volume": 3053.0
            },
            {
              "close": 56.22,
              "high": 56.32,
              "low": 56.13,
              "open": 56.29,
              "timestamp": 1789224300000,
              "volume": 2888.0
            },
            {
              "close": 56.33,
              "high": 56.45,
              "low": 56.1,
              "open": 56.22,
              "timestamp": 1789225200000,
              "volume": 3232.0
            },
            {
              "close": 56.39,
              "high": 56.43,
              "low": 56.26,
              "open": 56.33,
              "timestamp": 1789226100000,
              "volume": 2729.0
            },
            {
              "close": 56.39,
              "high": 56.42,
              "low": 56.16,
              "open": 56.39,
              "timestamp": 1789227000000,
              "volume": 2952.0
            },
            {
              "close": 56.2,
              "high": 56.51,
              "low": 56.2,
              "open": 56.39,
              "timestamp": 1789227900000,
              "volume": 2914.0
            },
            {
              "close": 56.09,
              "high": 56.26,
              "low": 56.03,
              "open": 56.2,
              "timestamp": 1789228800000,
              "volume": 2957.0
            },
            {
              "close": 55.89,
              "high": 56.13,
              "low": 55.8,
              "open": 56.09,
              "timestamp": 1789229700000,
              "volume": 2811.0
            },
            {
              "close": 55.67,
              "high": 55.92,
              "low": 55.56,
              "open": 55.91,
              "timestamp": 1789230600000,
              "volume": 3277.0
            },
            {
              "close": 55.84,
              "high": 55.87,
              "low": 55.67,
              "open": 55.67,
              "timestamp": 1789231500000,
              "volume": 2905.0
            },
            {
              "close": 55.76,
              "high": 55.92,
              "low": 55.7,
              "open": 55.84,
              "timestamp": 1789232400000,
              "volume": 3080.0
            },
            {
              "close": 55.85,
              "high": 55.88,
              "low": 55.73,
              "open": 55.76,
              "timestamp": 1789233300000,
              "volume": 2877.0
            },
            {
              "close": 55.77,
              "high": 55.86,
              "low": 55.73,
              "open": 55.85,
              "timestamp": 1789234200000,
              "volume": 2436.0
            },
            {
              "close": 55.79,
              "high": 55.85,
              "low": 55.65,
              "open": 55.77,
              "timestamp": 1789235100000,
              "volume": 2719.0
            },
            {
              "close": 55.59,
              "high": 55.79,
              "low": 55.5,
              "open": 55.79,
              "timestamp": 1789236000000,
              "volume": 3089.0
            },
            {
              "close": 55.56,
              "high": 55.67,
              "low": 55.53,
              "open": 55.59,
              "timestamp": 1789236900000,
              "volume": 2535.0
            },
            {
              "close": 55.61,
              "high": 55.64,
              "low": 55.35,
              "open": 55.56,
              "timestamp": 1789237800000,
              "volume": 2842.0
            },
            {
              "close": 55.34,
              "high": 55.63,
              "low": 55.32,
              "open": 55.61,
              "timestamp": 1789238700000,
              "volume": 2753.0
            },
            {
              "close": 55.4,
              "high": 55.48,
              "low": 55.28,
              "open": 55.34,
              "timestamp": 1789239600000,
              "volume": 2985.0
            },
            {
              "close": 55.34,
              "high": 55.44,
              "low": 55.25,
              "open": 55.4,
              "timestamp": 1789240500000,
              "volume": 2584.0
            },
            {
              "close": 54.89,
              "high": 55.35,
              "low": 54.68,
              "open": 55.34,
              "timestamp": 1789241400000,
              "volume": 3323.0
            },
            {
              "close": 54.84,
              "high": 54.98,
              "low": 54.75,
              "open": 54.89,
              "timestamp": 1789242300000,
              "volume": 2766.0
            },
            {
              "close": 54.89,
              "high": 54.93,
              "low": 54.67,
              "open": 54.84,
              "timestamp": 1789243200000,
              "volume": 3020.0
            },
            {
              "close": 54.97,
              "high": 54.97,
              "low": 54.83,
              "open": 54.89,
              "timestamp": 1789244100000,
              "volume": 2502.0
            },
            {
              "close": 54.97,
              "high": 55.03,
              "low": 54.86,
              "open": 54.97,
              "timestamp": 1789245000000,
              "volume": 2638.0
            },
            {
              "close": 54.79,
              "high": 55.09,
              "low": 54.78,
              "open": 54.97,
              "timestamp": 1789245900000,
              "volume": 2439.0
            },
            {
              "close": 54.73,
              "high": 54.99,
              "low": 54.72,
              "open": 54.79,
              "timestamp": 1789246800000,
              "volume": 2249.0
            },
            {
              "close": 54.86,
              "high": 54.86,
              "low": 54.55,
              "open": 54.72,
              "timestamp": 1789247700000,
              "volume": 2786.0
            },
            {
              "close": 54.99,
              "high": 55.06,
              "low": 54.78,
              "open": 54.86,
              "timestamp": 1789248600000,
              "volume": 3084.0
            },
            {
              "close": 54.94,
              "high": 54.99,
              "low": 54.82,
              "open": 54.99,
              "timestamp": 1789249500000,
              "volume": 2475.0
            },
            {
              "close": 54.94,
              "high": 55.04,
              "low": 54.85,
              "open": 54.94,
              "timestamp": 1789250400000,
              "volume": 2597.0
            },
            {
              "close": 54.79,
              "high": 55.06,
              "low": 54.75,
              "open": 54.94,
              "timestamp": 1789251300000,
              "volume": 2312.0
            },
            {
              "close": 54.79,
              "high": 54.83,
              "low": 54.65,
              "open": 54.79,
              "timestamp": 1789252200000,
              "volume": 2679.0
            },
            {
              "close": 54.71,
              "high": 54.85,
              "low": 54.66,
              "open": 54.79,
              "timestamp": 1789253100000,
              "volume": 2158.0
            },
            {
              "close": 54.71,
              "high": 54.8,
              "low": 54.64,
              "open": 54.71,
              "timestamp": 1789254000000,
              "volume": 2516.0
            },
            {
              "close": 54.71,
              "high": 54.77,
              "low": 54.66,
              "open": 54.71,
              "timestamp": 1789254900000,
              "volume": 2220.0
            },
            {
              "close": 54.65,
              "high": 54.73,
              "low": 54.62,
              "open": 54.71,
              "timestamp": 1789255800000,
              "volume": 2842.0
            },
            {
              "close": 54.7,
              "high": 54.85,
              "low": 54.65,
              "open": 54.65,
              "timestamp": 1789256700000,
              "volume": 2816.0
            },
            {
              "close": 54.88,
              "high": 54.94,
              "low": 54.51,
              "open": 54.52,
              "timestamp": 1789257600000,
              "volume": 3003.0
            },
            {
              "close": 54.9,
              "high": 54.96,
              "low": 54.69,
              "open": 54.88,
              "timestamp": 1789258500000,
              "volume": 2700.0
            },
            {
              "close": 54.66,
              "high": 54.95,
              "low": 54.62,
              "open": 54.9,
              "timestamp": 1789259400000,
              "volume": 2811.0
            },
            {
              "close": 54.83,
              "high": 54.9,
              "low": 54.62,
              "open": 54.66,
              "timestamp": 1789260300000,
              "volume": 2704.0
            },
            {
              "close": 54.74,
              "high": 54.87,
              "low": 54.64,
              "open": 54.83,
              "timestamp": 1789261200000,
              "volume": 2957.0
            },
            {
              "close": 54.86,
              "high": 54.99,
              "low": 54.56,
              "open": 54.74,
              "timestamp": 1789262100000,
              "volume": 3164.0
            },
            {
              "close": 54.89,
              "high": 54.89,
              "low": 54.65,
              "open": 54.86,
              "timestamp": 1789263000000,
              "volume": 2620.0
            },
            {
              "close": 54.9,
              "high": 54.96,
              "low": 54.8,
              "open": 54.89,
              "timestamp": 1789263900000,
              "volume": 2621.0
            },
            {
              "close": 54.65,
              "high": 54.92,
              "low": 54.62,
              "open": 54.9,
              "timestamp": 1789264800000,
              "volume": 2801.0
            },
            {
              "close": 54.6,
              "high": 54.76,
              "low": 54.59,
              "open": 54.65,
              "timestamp": 1789265700000,
              "volume": 2586.0
            },
            {
              "close": 54.72,
              "high": 54.76,
              "low": 54.45,
              "open": 54.6,
              "timestamp": 1789266600000,
              "volume": 2843.0
            },
            {
              "close": 54.77,
              "high": 54.9,
              "low": 54.68,
              "open": 54.72,
              "timestamp": 1789267500000,
              "volume": 2615.0
            },
            {
              "close": 54.61,
              "high": 54.88,
              "low": 54.57,
              "open": 54.77,
              "timestamp": 1789268400000,
              "volume": 2900.0
            },
            {
              "close": 54.59,
              "high": 54.91,
              "low": 54.44,
              "open": 54.61,
              "timestamp": 1789269300000,
              "volume": 3256.0
            },
            {
              "close": 54.57,
              "high": 54.65,
              "low": 54.45,
              "open": 54.59,
              "timestamp": 1789270200000,
              "volume": 3270.0
            },
            {
              "close": 54.53,
              "high": 54.6,
              "low": 54.39,
              "open": 54.57,
              "timestamp": 1789271100000,
              "volume": 3021.0
            },
            {
              "close": 54.82,
              "high": 54.84,
              "low": 54.44,
              "open": 54.53,
              "timestamp": 1789272000000,
              "volume": 3395.0
            },
            {
              "close": 55.31,
              "high": 55.36,
              "low": 54.75,
              "open": 54.84,
              "timestamp": 1789272900000,
              "volume": 3263.0
            },
            {
              "close": 55.26,
              "high": 55.46,
              "low": 55.12,
              "open": 55.31,
              "timestamp": 1789273800000,
              "volume": 3190.0
            },
            {
              "close": 55.16,
              "high": 55.26,
              "low": 55.1,
              "open": 55.26,
              "timestamp": 1789274700000,
              "volume": 2445.0
            },
            {
              "close": 55.38,
              "high": 55.44,
              "low": 55.1,
              "open": 55.16,
              "timestamp": 1789275600000,
              "volume": 2665.0
            },
            {
              "close": 55.79,
              "high": 55.85,
              "low": 55.35,
              "open": 55.38,
              "timestamp": 1789276500000,
              "volume": 3025.0
            },
            {
              "close": 55.79,
              "high": 55.88,
              "low": 55.67,
              "open": 55.79,
              "timestamp": 1789277400000,
              "volume": 3012.0
            },
            {
              "close": 56.0,
              "high": 56.1,
              "low": 55.74,
              "open": 55.79,
              "timestamp": 1789278300000,
              "volume": 2855.0
            },
            {
              "close": 55.63,
              "high": 56.02,
              "low": 55.55,
              "open": 56.0,
              "timestamp": 1789279200000,
              "volume": 3135.0
            },
            {
              "close": 55.66,
              "high": 55.73,
              "low": 55.5,
              "open": 55.63,
              "timestamp": 1789280100000,
              "volume": 2795.0
            },
            {
              "close": 55.69,
              "high": 55.76,
              "low": 55.55,
              "open": 55.66,
              "timestamp": 1789281000000,
              "volume": 2574.0
            },
            {
              "close": 55.49,
              "high": 55.74,
              "low": 55.36,
              "open": 55.69,
              "timestamp": 1789281900000,
              "volume": 3139.0
            },
            {
              "close": 55.45,
              "high": 55.75,
              "low": 55.4,
              "open": 55.47,
              "timestamp": 1789282800000,
              "volume": 3058.0
            },
            {
              "close": 55.56,
              "high": 55.65,
              "low": 55.42,
              "open": 55.45,
              "timestamp": 1789283700000,
              "volume": 2449.0
            },
            {
              "close": 55.29,
              "high": 55.56,
              "low": 55.24,
              "open": 55.56,
              "timestamp": 1789284600000,
              "volume": 2792.0
            },
            {
              "close": 55.05,
              "high": 55.3,
              "low": 55.03,
              "open": 55.29,
              "timestamp": 1789285500000,
              "volume": 2793.0
            },
            {
              "close": 54.81,
              "high": 55.08,
              "low": 54.8,
              "open": 55.05,
              "timestamp": 1789286400000,
              "volume": 3204.0
            },
            {
              "close": 54.32,
              "high": 54.81,
              "low": 54.3,
              "open": 54.8,
              "timestamp": 1789287300000,
              "volume": 3280.0
            },
            {
              "close": 53.61,
              "high": 54.39,
              "low": 53.53,
              "open": 54.32,
              "timestamp": 1789288200000,
              "volume": 3992.0
            },
            {
              "close": 53.88,
              "high": 53.99,
              "low": 53.6,
              "open": 53.61,
              "timestamp": 1789289100000,
              "volume": 3686.0
            },
            {
              "close": 54.14,
              "high": 54.28,
              "low": 53.87,
              "open": 53.89,
              "timestamp": 1789290000000,
              "volume": 3499.0
            },
            {
              "close": 53.7,
              "high": 54.25,
              "low": 53.69,
              "open": 54.14,
              "timestamp": 1789290900000,
              "volume": 3545.0
            },
            {
              "close": 54.14,
              "high": 54.22,
              "low": 53.57,
              "open": 53.7,
              "timestamp": 1789291800000,
              "volume": 3864.0
            },
            {
              "close": 54.45,
              "high": 54.54,
              "low": 54.04,
              "open": 54.14,
              "timestamp": 1789292700000,
              "volume": 3484.0
            },
            {
              "close": 54.44,
              "high": 54.56,
              "low": 54.36,
              "open": 54.45,
              "timestamp": 1789293600000,
              "volume": 3310.0
            },
            {
              "close": 54.46,
              "high": 54.47,
              "low": 54.25,
              "open": 54.44,
              "timestamp": 1789294500000,
              "volume": 2749.0
            },
            {
              "close": 54.07,
              "high": 54.47,
              "low": 54.03,
              "open": 54.46,
              "timestamp": 1789295400000,
              "volume": 2987.0
            },
            {
              "close": 54.01,
              "high": 54.2,
              "low": 53.88,
              "open": 54.05,
              "timestamp": 1789296300000,
              "volume": 3123.0
            },
            {
              "close": 54.08,
              "high": 54.3,
              "low": 54.01,
              "open": 54.01,
              "timestamp": 1789297200000,
              "volume": 3233.0
            },
            {
              "close": 54.06,
              "high": 54.26,
              "low": 54.03,
              "open": 54.08,
              "timestamp": 1789298100000,
              "volume": 2662.0
            },
            {
              "close": 54.23,
              "high": 54.25,
              "low": 54.04,
              "open": 54.06,
              "timestamp": 1789299000000,
              "volume": 2626.0
            },
            {
              "close": 53.93,
              "high": 54.26,
              "low": 53.9,
              "open": 54.23,
              "timestamp": 1789299900000,
              "volume": 2682.0
            },
            {
              "close": 53.92,
              "high": 53.99,
              "low": 53.85,
              "open": 53.93,
              "timestamp": 1789300800000,
              "volume": 2860.0
            },
            {
              "close": 53.95,
              "high": 54.05,
              "low": 53.86,
              "open": 53.92,
              "timestamp": 1789301700000,
              "volume": 2467.0
            },
            {
              "close": 53.84,
              "high": 54.15,
              "low": 53.81,
              "open": 53.95,
              "timestamp": 1789302600000,
              "volume": 2998.0
            },
            {
              "close": 53.95,
              "high": 53.95,
              "low": 53.76,
              "open": 53.84,
              "timestamp": 1789303500000,
              "volume": 2767.0
            },
            {
              "close": 53.8,
              "high": 53.96,
              "low": 53.74,
              "open": 53.95,
              "timestamp": 1789304400000,
              "volume": 2838.0
            },
            {
              "close": 53.3,
              "high": 53.8,
              "low": 53.26,
              "open": 53.8,
              "timestamp": 1789305300000,
              "volume": 3411.0
            },
            {
              "close": 53.7,
              "high": 53.73,
              "low": 53.29,
              "open": 53.3,
              "timestamp": 1789306200000,
              "volume": 3203.0
            },
            {
              "close": 53.94,
              "high": 54.24,
              "low": 53.7,
              "open": 53.7,
              "timestamp": 1789307100000,
              "volume": 3517.0
            },
            {
              "close": 54.25,
              "high": 54.25,
              "low": 53.9,
              "open": 53.96,
              "timestamp": 1789308000000,
              "volume": 3230.0
            },
            {
              "close": 54.33,
              "high": 54.42,
              "low": 54.19,
              "open": 54.25,
              "timestamp": 1789308900000,
              "volume": 3261.0
            },
            {
              "close": 54.38,
              "high": 54.54,
              "low": 54.2,
              "open": 54.33,
              "timestamp": 1789309800000,
              "volume": 3288.0
            },
            {
              "close": 54.26,
              "high": 54.46,
              "low": 54.17,
              "open": 54.38,
              "timestamp": 1789310700000,
              "volume": 3014.0
            },
            {
              "close": 53.67,
              "high": 54.29,
              "low": 53.62,
              "open": 54.26,
              "timestamp": 1789311600000,
              "volume": 3480.0
            },
            {
              "close": 53.44,
              "high": 53.74,
              "low": 53.36,
              "open": 53.67,
              "timestamp": 1789312500000,
              "volume": 3435.0
            },
            {
              "close": 53.53,
              "high": 53.57,
              "low": 53.31,
              "open": 53.42,
              "timestamp": 1789313400000,
              "volume": 3092.0
            },
            {
              "close": 53.31,
              "high": 53.53,
              "low": 53.22,
              "open": 53.53,
              "timestamp": 1789314300000,
              "volume": 2969.0
            },
            {
              "close": 53.56,
              "high": 53.88,
              "low": 53.28,
              "open": 53.31,
              "timestamp": 1789315200000,
              "volume": 3636.0
            },
            {
              "close": 53.71,
              "high": 53.82,
              "low": 53.54,
              "open": 53.57,
              "timestamp": 1789316100000,
              "volume": 3055.0
            },
            {
              "close": 53.88,
              "high": 53.88,
              "low": 53.59,
              "open": 53.71,
              "timestamp": 1789317000000,
              "volume": 2742.0
            },
            {
              "close": 54.03,
              "high": 54.08,
              "low": 53.78,
              "open": 53.88,
              "timestamp": 1789317900000,
              "volume": 2920.0
            },
            {
              "close": 54.73,
              "high": 54.93,
              "low": 54.02,
              "open": 54.03,
              "timestamp": 1789318800000,
              "volume": 3602.0
            },
            {
              "close": 54.8,
              "high": 55.0,
              "low": 54.7,
              "open": 54.73,
              "timestamp": 1789319700000,
              "volume": 3355.0
            },
            {
              "close": 54.48,
              "high": 54.83,
              "low": 54.43,
              "open": 54.8,
              "timestamp": 1789320600000,
              "volume": 3104.0
            },
            {
              "close": 54.68,
              "high": 54.76,
              "low": 54.48,
              "open": 54.48,
              "timestamp": 1789321500000,
              "volume": 2768.0
            },
            {
              "close": 54.63,
              "high": 54.76,
              "low": 54.54,
              "open": 54.68,
              "timestamp": 1789322400000,
              "volume": 2690.0
            },
            {
              "close": 54.58,
              "high": 54.73,
              "low": 54.56,
              "open": 54.63,
              "timestamp": 1789323300000,
              "volume": 2450.0
            },
            {
              "close": 54.8,
              "high": 54.88,
              "low": 54.56,
              "open": 54.59,
              "timestamp": 1789324200000,
              "volume": 2580.0
            },
            {
              "close": 54.8,
              "high": 54.95,
              "low": 54.74,
              "open": 54.8,
              "timestamp": 1789325100000,
              "volume": 2394.0
            },
            {
              "close": 54.45,
              "high": 54.89,
              "low": 54.41,
              "open": 54.8,
              "timestamp": 1789326000000,
              "volume": 3066.0
            },
            {
              "close": 54.15,
              "high": 54.5,
              "low": 54.15,
              "open": 54.45,
              "timestamp": 1789326900000,
              "volume": 2875.0
            },
            {
              "close": 54.02,
              "high": 54.22,
              "low": 54.0,
              "open": 54.16,
              "timestamp": 1789327800000,
              "volume": 2761.0
            },
            {
              "close": 54.07,
              "high": 54.11,
              "low": 53.96,
              "open": 54.02,
              "timestamp": 1789328700000,
              "volume": 2363.0
            }
          ],
          "last_price": 54.07,
          "momentum": "neutral",
          "rsi_14": 46.28,
          "structure": "neutral"
        },
        "1H": {
          "candle_count": 168,
          "candle_status": {
            "data_age_seconds": 3696,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789326000000,
            "latest_timestamp_utc": "2026-09-13T19:00:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 3600
          },
          "candles": [
            {
              "close": 70.48,
              "high": 71.4,
              "low": 69.78,
              "open": 70.88,
              "timestamp": 1788724800000,
              "volume": 15578.0
            },
            {
              "close": 71.23,
              "high": 71.67,
              "low": 70.04,
              "open": 70.48,
              "timestamp": 1788728400000,
              "volume": 16650.0
            },
            {
              "close": 71.03,
              "high": 71.27,
              "low": 69.56,
              "open": 71.24,
              "timestamp": 1788732000000,
              "volume": 16784.0
            },
            {
              "close": 71.22,
              "high": 71.61,
              "low": 70.61,
              "open": 71.03,
              "timestamp": 1788735600000,
              "volume": 16623.0
            },
            {
              "close": 69.93,
              "high": 71.51,
              "low": 69.3,
              "open": 71.19,
              "timestamp": 1788739200000,
              "volume": 17140.0
            },
            {
              "close": 69.67,
              "high": 70.32,
              "low": 68.32,
              "open": 69.93,
              "timestamp": 1788742800000,
              "volume": 17219.0
            },
            {
              "close": 71.04,
              "high": 72.36,
              "low": 69.2,
              "open": 69.67,
              "timestamp": 1788746400000,
              "volume": 17252.0
            },
            {
              "close": 69.63,
              "high": 71.06,
              "low": 69.48,
              "open": 71.04,
              "timestamp": 1788750000000,
              "volume": 17107.0
            },
            {
              "close": 69.94,
              "high": 71.05,
              "low": 69.37,
              "open": 69.63,
              "timestamp": 1788753600000,
              "volume": 17085.0
            },
            {
              "close": 67.29,
              "high": 71.35,
              "low": 67.08,
              "open": 69.94,
              "timestamp": 1788757200000,
              "volume": 17418.0
            },
            {
              "close": 68.05,
              "high": 68.75,
              "low": 67.08,
              "open": 67.29,
              "timestamp": 1788760800000,
              "volume": 17384.0
            },
            {
              "close": 67.84,
              "high": 68.07,
              "low": 66.25,
              "open": 68.05,
              "timestamp": 1788764400000,
              "volume": 17292.0
            },
            {
              "close": 67.75,
              "high": 68.02,
              "low": 67.14,
              "open": 67.84,
              "timestamp": 1788768000000,
              "volume": 16183.0
            },
            {
              "close": 67.71,
              "high": 68.63,
              "low": 67.58,
              "open": 67.75,
              "timestamp": 1788771600000,
              "volume": 15937.0
            },
            {
              "close": 68.3,
              "high": 69.08,
              "low": 67.5,
              "open": 67.71,
              "timestamp": 1788775200000,
              "volume": 16074.0
            },
            {
              "close": 67.83,
              "high": 68.42,
              "low": 67.72,
              "open": 68.31,
              "timestamp": 1788778800000,
              "volume": 14754.0
            },
            {
              "close": 68.15,
              "high": 68.21,
              "low": 67.69,
              "open": 67.83,
              "timestamp": 1788782400000,
              "volume": 14911.0
            },
            {
              "close": 67.3,
              "high": 68.4,
              "low": 67.24,
              "open": 68.16,
              "timestamp": 1788786000000,
              "volume": 16087.0
            },
            {
              "close": 66.42,
              "high": 67.21,
              "low": 65.74,
              "open": 67.21,
              "timestamp": 1788789600000,
              "volume": 17317.0
            },
            {
              "close": 64.66,
              "high": 66.42,
              "low": 64.43,
              "open": 66.42,
              "timestamp": 1788793200000,
              "volume": 17387.0
            },
            {
              "close": 65.52,
              "high": 65.76,
              "low": 64.58,
              "open": 64.64,
              "timestamp": 1788796800000,
              "volume": 16170.0
            },
            {
              "close": 65.44,
              "high": 65.93,
              "low": 65.02,
              "open": 65.52,
              "timestamp": 1788800400000,
              "volume": 15788.0
            },
            {
              "close": 63.94,
              "high": 65.51,
              "low": 63.66,
              "open": 65.44,
              "timestamp": 1788804000000,
              "volume": 15532.0
            },
            {
              "close": 64.21,
              "high": 64.4,
              "low": 63.61,
              "open": 63.94,
              "timestamp": 1788807600000,
              "volume": 15614.0
            },
            {
              "close": 64.15,
              "high": 64.78,
              "low": 63.42,
              "open": 64.21,
              "timestamp": 1788811200000,
              "volume": 15428.0
            },
            {
              "close": 64.74,
              "high": 64.95,
              "low": 64.13,
              "open": 64.15,
              "timestamp": 1788814800000,
              "volume": 13969.0
            },
            {
              "close": 63.87,
              "high": 64.83,
              "low": 63.83,
              "open": 64.74,
              "timestamp": 1788818400000,
              "volume": 16001.0
            },
            {
              "close": 62.79,
              "high": 64.03,
              "low": 62.58,
              "open": 63.87,
              "timestamp": 1788822000000,
              "volume": 16958.0
            },
            {
              "close": 63.72,
              "high": 63.88,
              "low": 62.45,
              "open": 62.79,
              "timestamp": 1788825600000,
              "volume": 17023.0
            },
            {
              "close": 64.47,
              "high": 64.64,
              "low": 63.2,
              "open": 63.72,
              "timestamp": 1788829200000,
              "volume": 16352.0
            },
            {
              "close": 63.1,
              "high": 64.62,
              "low": 63.01,
              "open": 64.47,
              "timestamp": 1788832800000,
              "volume": 16459.0
            },
            {
              "close": 62.98,
              "high": 63.57,
              "low": 62.5,
              "open": 63.1,
              "timestamp": 1788836400000,
              "volume": 16385.0
            },
            {
              "close": 62.71,
              "high": 63.08,
              "low": 62.25,
              "open": 62.98,
              "timestamp": 1788840000000,
              "volume": 16472.0
            },
            {
              "close": 63.26,
              "high": 63.42,
              "low": 62.54,
              "open": 62.71,
              "timestamp": 1788843600000,
              "volume": 16702.0
            },
            {
              "close": 63.0,
              "high": 63.91,
              "low": 62.75,
              "open": 63.27,
              "timestamp": 1788847200000,
              "volume": 16404.0
            },
            {
              "close": 62.28,
              "high": 63.02,
              "low": 61.66,
              "open": 63.0,
              "timestamp": 1788850800000,
              "volume": 16173.0
            },
            {
              "close": 61.76,
              "high": 62.48,
              "low": 61.7,
              "open": 62.28,
              "timestamp": 1788854400000,
              "volume": 16318.0
            },
            {
              "close": 62.82,
              "high": 63.06,
              "low": 61.61,
              "open": 61.76,
              "timestamp": 1788858000000,
              "volume": 16095.0
            },
            {
              "close": 62.76,
              "high": 63.53,
              "low": 62.41,
              "open": 62.82,
              "timestamp": 1788861600000,
              "volume": 15638.0
            },
            {
              "close": 63.15,
              "high": 63.62,
              "low": 62.3,
              "open": 62.74,
              "timestamp": 1788865200000,
              "volume": 15528.0
            },
            {
              "close": 63.59,
              "high": 63.65,
              "low": 62.75,
              "open": 63.15,
              "timestamp": 1788868800000,
              "volume": 15952.0
            },
            {
              "close": 62.79,
              "high": 63.7,
              "low": 61.86,
              "open": 63.59,
              "timestamp": 1788872400000,
              "volume": 16760.0
            },
            {
              "close": 63.09,
              "high": 63.77,
              "low": 62.02,
              "open": 62.77,
              "timestamp": 1788876000000,
              "volume": 17612.0
            },
            {
              "close": 64.37,
              "high": 64.96,
              "low": 62.73,
              "open": 63.08,
              "timestamp": 1788879600000,
              "volume": 17307.0
            },
            {
              "close": 63.76,
              "high": 64.92,
              "low": 63.4,
              "open": 64.36,
              "timestamp": 1788883200000,
              "volume": 17162.0
            },
            {
              "close": 62.74,
              "high": 63.97,
              "low": 62.46,
              "open": 63.76,
              "timestamp": 1788886800000,
              "volume": 16004.0
            },
            {
              "close": 61.68,
              "high": 63.24,
              "low": 61.55,
              "open": 62.74,
              "timestamp": 1788890400000,
              "volume": 15799.0
            },
            {
              "close": 61.81,
              "high": 62.23,
              "low": 61.63,
              "open": 61.68,
              "timestamp": 1788894000000,
              "volume": 15774.0
            },
            {
              "close": 61.56,
              "high": 62.21,
              "low": 61.34,
              "open": 61.81,
              "timestamp": 1788897600000,
              "volume": 15327.0
            },
            {
              "close": 61.77,
              "high": 61.96,
              "low": 61.45,
              "open": 61.55,
              "timestamp": 1788901200000,
              "volume": 13666.0
            },
            {
              "close": 62.28,
              "high": 62.75,
              "low": 61.75,
              "open": 61.77,
              "timestamp": 1788904800000,
              "volume": 15120.0
            },
            {
              "close": 62.43,
              "high": 62.63,
              "low": 61.99,
              "open": 62.28,
              "timestamp": 1788908400000,
              "volume": 15241.0
            },
            {
              "close": 63.12,
              "high": 63.42,
              "low": 62.43,
              "open": 62.43,
              "timestamp": 1788912000000,
              "volume": 15840.0
            },
            {
              "close": 62.87,
              "high": 63.19,
              "low": 62.01,
              "open": 63.12,
              "timestamp": 1788915600000,
              "volume": 15788.0
            },
            {
              "close": 61.95,
              "high": 63.06,
              "low": 61.94,
              "open": 62.87,
              "timestamp": 1788919200000,
              "volume": 15169.0
            },
            {
              "close": 62.03,
              "high": 62.67,
              "low": 61.54,
              "open": 61.95,
              "timestamp": 1788922800000,
              "volume": 15818.0
            },
            {
              "close": 64.78,
              "high": 64.93,
              "low": 62.03,
              "open": 62.03,
              "timestamp": 1788926400000,
              "volume": 17179.0
            },
            {
              "close": 64.05,
              "high": 65.0,
              "low": 63.44,
              "open": 64.78,
              "timestamp": 1788930000000,
              "volume": 16866.0
            },
            {
              "close": 65.27,
              "high": 65.99,
              "low": 63.89,
              "open": 64.05,
              "timestamp": 1788933600000,
              "volume": 16596.0
            },
            {
              "close": 65.3,
              "high": 65.66,
              "low": 64.96,
              "open": 65.27,
              "timestamp": 1788937200000,
              "volume": 15804.0
            },
            {
              "close": 65.74,
              "high": 66.2,
              "low": 64.96,
              "open": 65.3,
              "timestamp": 1788940800000,
              "volume": 15575.0
            },
            {
              "close": 64.26,
              "high": 66.31,
              "low": 64.16,
              "open": 65.74,
              "timestamp": 1788944400000,
              "volume": 16921.0
            },
            {
              "close": 65.17,
              "high": 65.25,
              "low": 64.24,
              "open": 64.26,
              "timestamp": 1788948000000,
              "volume": 16317.0
            },
            {
              "close": 65.27,
              "high": 66.09,
              "low": 64.01,
              "open": 65.17,
              "timestamp": 1788951600000,
              "volume": 16963.0
            },
            {
              "close": 64.57,
              "high": 65.64,
              "low": 64.29,
              "open": 65.27,
              "timestamp": 1788955200000,
              "volume": 15958.0
            },
            {
              "close": 63.83,
              "high": 64.99,
              "low": 63.62,
              "open": 64.57,
              "timestamp": 1788958800000,
              "volume": 16761.0
            },
            {
              "close": 64.03,
              "high": 65.14,
              "low": 63.34,
              "open": 63.83,
              "timestamp": 1788962400000,
              "volume": 17465.0
            },
            {
              "close": 62.81,
              "high": 64.63,
              "low": 62.1,
              "open": 64.03,
              "timestamp": 1788966000000,
              "volume": 16697.0
            },
            {
              "close": 64.22,
              "high": 64.6,
              "low": 62.78,
              "open": 62.81,
              "timestamp": 1788969600000,
              "volume": 16291.0
            },
            {
              "close": 64.59,
              "high": 64.89,
              "low": 64.11,
              "open": 64.22,
              "timestamp": 1788973200000,
              "volume": 15520.0
            },
            {
              "close": 63.97,
              "high": 64.64,
              "low": 63.8,
              "open": 64.59,
              "timestamp": 1788976800000,
              "volume": 14165.0
            },
            {
              "close": 61.97,
              "high": 64.3,
              "low": 61.81,
              "open": 63.97,
              "timestamp": 1788980400000,
              "volume": 15634.0
            },
            {
              "close": 62.69,
              "high": 62.85,
              "low": 61.89,
              "open": 61.96,
              "timestamp": 1788984000000,
              "volume": 15346.0
            },
            {
              "close": 61.83,
              "high": 62.8,
              "low": 61.12,
              "open": 62.69,
              "timestamp": 1788987600000,
              "volume": 13855.0
            },
            {
              "close": 58.32,
              "high": 61.89,
              "low": 58.23,
              "open": 61.84,
              "timestamp": 1788991200000,
              "volume": 16553.0
            },
            {
              "close": 58.54,
              "high": 59.46,
              "low": 58.27,
              "open": 58.32,
              "timestamp": 1788994800000,
              "volume": 15027.0
            },
            {
              "close": 58.2,
              "high": 58.9,
              "low": 57.85,
              "open": 58.58,
              "timestamp": 1788998400000,
              "volume": 16023.0
            },
            {
              "close": 56.88,
              "high": 58.35,
              "low": 56.59,
              "open": 58.2,
              "timestamp": 1789002000000,
              "volume": 16784.0
            },
            {
              "close": 58.25,
              "high": 58.34,
              "low": 56.81,
              "open": 56.88,
              "timestamp": 1789005600000,
              "volume": 16229.0
            },
            {
              "close": 57.68,
              "high": 58.29,
              "low": 57.52,
              "open": 58.25,
              "timestamp": 1789009200000,
              "volume": 15043.0
            },
            {
              "close": 57.83,
              "high": 58.26,
              "low": 57.6,
              "open": 57.68,
              "timestamp": 1789012800000,
              "volume": 14640.0
            },
            {
              "close": 57.84,
              "high": 57.96,
              "low": 57.34,
              "open": 57.83,
              "timestamp": 1789016400000,
              "volume": 14827.0
            },
            {
              "close": 57.75,
              "high": 58.04,
              "low": 56.79,
              "open": 57.84,
              "timestamp": 1789020000000,
              "volume": 15700.0
            },
            {
              "close": 56.46,
              "high": 57.76,
              "low": 55.88,
              "open": 57.75,
              "timestamp": 1789023600000,
              "volume": 16128.0
            },
            {
              "close": 56.83,
              "high": 56.99,
              "low": 56.16,
              "open": 56.46,
              "timestamp": 1789027200000,
              "volume": 15103.0
            },
            {
              "close": 56.95,
              "high": 57.3,
              "low": 56.47,
              "open": 56.83,
              "timestamp": 1789030800000,
              "volume": 14666.0
            },
            {
              "close": 57.27,
              "high": 57.68,
              "low": 56.89,
              "open": 56.96,
              "timestamp": 1789034400000,
              "volume": 15252.0
            },
            {
              "close": 57.02,
              "high": 57.8,
              "low": 57.0,
              "open": 57.27,
              "timestamp": 1789038000000,
              "volume": 14730.0
            },
            {
              "close": 56.62,
              "high": 57.68,
              "low": 55.63,
              "open": 57.02,
              "timestamp": 1789041600000,
              "volume": 16456.0
            },
            {
              "close": 56.75,
              "high": 57.03,
              "low": 56.04,
              "open": 56.62,
              "timestamp": 1789045200000,
              "volume": 17067.0
            },
            {
              "close": 56.51,
              "high": 57.17,
              "low": 56.32,
              "open": 56.75,
              "timestamp": 1789048800000,
              "volume": 16094.0
            },
            {
              "close": 56.26,
              "high": 56.53,
              "low": 55.76,
              "open": 56.51,
              "timestamp": 1789052400000,
              "volume": 15430.0
            },
            {
              "close": 55.6,
              "high": 56.31,
              "low": 54.88,
              "open": 56.26,
              "timestamp": 1789056000000,
              "volume": 16649.0
            },
            {
              "close": 56.01,
              "high": 56.63,
              "low": 55.54,
              "open": 55.6,
              "timestamp": 1789059600000,
              "volume": 15486.0
            },
            {
              "close": 56.36,
              "high": 56.46,
              "low": 55.53,
              "open": 56.01,
              "timestamp": 1789063200000,
              "volume": 14857.0
            },
            {
              "close": 55.72,
              "high": 56.39,
              "low": 55.59,
              "open": 56.36,
              "timestamp": 1789066800000,
              "volume": 14080.0
            },
            {
              "close": 56.3,
              "high": 56.43,
              "low": 55.64,
              "open": 55.72,
              "timestamp": 1789070400000,
              "volume": 12989.0
            },
            {
              "close": 55.87,
              "high": 56.38,
              "low": 55.67,
              "open": 56.3,
              "timestamp": 1789074000000,
              "volume": 11165.0
            },
            {
              "close": 55.09,
              "high": 56.29,
              "low": 55.05,
              "open": 55.87,
              "timestamp": 1789077600000,
              "volume": 13094.0
            },
            {
              "close": 54.0,
              "high": 55.36,
              "low": 53.83,
              "open": 55.09,
              "timestamp": 1789081200000,
              "volume": 16267.0
            },
            {
              "close": 54.82,
              "high": 54.93,
              "low": 53.94,
              "open": 54.01,
              "timestamp": 1789084800000,
              "volume": 14945.0
            },
            {
              "close": 54.85,
              "high": 55.34,
              "low": 54.26,
              "open": 54.81,
              "timestamp": 1789088400000,
              "volume": 14866.0
            },
            {
              "close": 55.06,
              "high": 55.3,
              "low": 54.45,
              "open": 54.85,
              "timestamp": 1789092000000,
              "volume": 15104.0
            },
            {
              "close": 55.34,
              "high": 55.4,
              "low": 54.65,
              "open": 55.06,
              "timestamp": 1789095600000,
              "volume": 14101.0
            },
            {
              "close": 55.95,
              "high": 56.25,
              "low": 55.22,
              "open": 55.33,
              "timestamp": 1789099200000,
              "volume": 15013.0
            },
            {
              "close": 55.89,
              "high": 56.11,
              "low": 55.45,
              "open": 55.95,
              "timestamp": 1789102800000,
              "volume": 13970.0
            },
            {
              "close": 55.76,
              "high": 56.01,
              "low": 55.6,
              "open": 55.89,
              "timestamp": 1789106400000,
              "volume": 13286.0
            },
            {
              "close": 55.68,
              "high": 56.33,
              "low": 55.65,
              "open": 55.76,
              "timestamp": 1789110000000,
              "volume": 12760.0
            },
            {
              "close": 55.58,
              "high": 56.02,
              "low": 55.51,
              "open": 55.68,
              "timestamp": 1789113600000,
              "volume": 13014.0
            },
            {
              "close": 54.91,
              "high": 55.63,
              "low": 54.68,
              "open": 55.58,
              "timestamp": 1789117200000,
              "volume": 13639.0
            },
            {
              "close": 54.56,
              "high": 55.1,
              "low": 54.41,
              "open": 54.91,
              "timestamp": 1789120800000,
              "volume": 14194.0
            },
            {
              "close": 54.7,
              "high": 54.81,
              "low": 54.17,
              "open": 54.56,
              "timestamp": 1789124400000,
              "volume": 14775.0
            },
            {
              "close": 57.29,
              "high": 57.33,
              "low": 54.49,
              "open": 54.7,
              "timestamp": 1789128000000,
              "volume": 16716.0
            },
            {
              "close": 58.81,
              "high": 58.95,
              "low": 56.3,
              "open": 57.28,
              "timestamp": 1789131600000,
              "volume": 17508.0
            },
            {
              "close": 57.37,
              "high": 59.4,
              "low": 56.92,
              "open": 58.82,
              "timestamp": 1789135200000,
              "volume": 17634.0
            },
            {
              "close": 56.17,
              "high": 58.36,
              "low": 55.85,
              "open": 57.38,
              "timestamp": 1789138800000,
              "volume": 17300.0
            },
            {
              "close": 56.76,
              "high": 56.98,
              "low": 55.8,
              "open": 56.17,
              "timestamp": 1789142400000,
              "volume": 16962.0
            },
            {
              "close": 56.85,
              "high": 57.1,
              "low": 56.33,
              "open": 56.76,
              "timestamp": 1789146000000,
              "volume": 15409.0
            },
            {
              "close": 55.66,
              "high": 56.91,
              "low": 55.44,
              "open": 56.86,
              "timestamp": 1789149600000,
              "volume": 16698.0
            },
            {
              "close": 56.3,
              "high": 56.39,
              "low": 55.37,
              "open": 55.67,
              "timestamp": 1789153200000,
              "volume": 15478.0
            },
            {
              "close": 56.45,
              "high": 56.81,
              "low": 56.07,
              "open": 56.3,
              "timestamp": 1789156800000,
              "volume": 14475.0
            },
            {
              "close": 55.52,
              "high": 56.75,
              "low": 55.47,
              "open": 56.45,
              "timestamp": 1789160400000,
              "volume": 13052.0
            },
            {
              "close": 55.45,
              "high": 55.83,
              "low": 55.17,
              "open": 55.52,
              "timestamp": 1789164000000,
              "volume": 13570.0
            },
            {
              "close": 56.84,
              "high": 56.96,
              "low": 55.38,
              "open": 55.46,
              "timestamp": 1789167600000,
              "volume": 14302.0
            },
            {
              "close": 57.02,
              "high": 57.23,
              "low": 56.65,
              "open": 56.82,
              "timestamp": 1789171200000,
              "volume": 14035.0
            },
            {
              "close": 56.74,
              "high": 57.2,
              "low": 56.57,
              "open": 57.02,
              "timestamp": 1789174800000,
              "volume": 13001.0
            },
            {
              "close": 56.36,
              "high": 56.91,
              "low": 56.19,
              "open": 56.74,
              "timestamp": 1789178400000,
              "volume": 12430.0
            },
            {
              "close": 56.37,
              "high": 56.52,
              "low": 55.87,
              "open": 56.36,
              "timestamp": 1789182000000,
              "volume": 12599.0
            },
            {
              "close": 56.39,
              "high": 56.58,
              "low": 56.14,
              "open": 56.37,
              "timestamp": 1789185600000,
              "volume": 11748.0
            },
            {
              "close": 56.16,
              "high": 56.43,
              "low": 56.02,
              "open": 56.39,
              "timestamp": 1789189200000,
              "volume": 11294.0
            },
            {
              "close": 55.99,
              "high": 56.4,
              "low": 55.95,
              "open": 56.16,
              "timestamp": 1789192800000,
              "volume": 11303.0
            },
            {
              "close": 56.85,
              "high": 56.98,
              "low": 55.93,
              "open": 55.99,
              "timestamp": 1789196400000,
              "volume": 12582.0
            },
            {
              "close": 56.38,
              "high": 56.85,
              "low": 56.22,
              "open": 56.85,
              "timestamp": 1789200000000,
              "volume": 11844.0
            },
            {
              "close": 56.12,
              "high": 56.45,
              "low": 55.98,
              "open": 56.38,
              "timestamp": 1789203600000,
              "volume": 11873.0
            },
            {
              "close": 56.13,
              "high": 56.39,
              "low": 56.06,
              "open": 56.12,
              "timestamp": 1789207200000,
              "volume": 10881.0
            },
            {
              "close": 56.2,
              "high": 56.27,
              "low": 56.02,
              "open": 56.13,
              "timestamp": 1789210800000,
              "volume": 9939.0
            },
            {
              "close": 56.29,
              "high": 56.58,
              "low": 55.96,
              "open": 56.2,
              "timestamp": 1789214400000,
              "volume": 11735.0
            },
            {
              "close": 56.02,
              "high": 56.48,
              "low": 55.89,
              "open": 56.29,
              "timestamp": 1789218000000,
              "volume": 12189.0
            },
            {
              "close": 56.22,
              "high": 56.46,
              "low": 55.98,
              "open": 56.02,
              "timestamp": 1789221600000,
              "volume": 12237.0
            },
            {
              "close": 56.2,
              "high": 56.51,
              "low": 56.1,
              "open": 56.22,
              "timestamp": 1789225200000,
              "volume": 11827.0
            },
            {
              "close": 55.84,
              "high": 56.26,
              "low": 55.56,
              "open": 56.2,
              "timestamp": 1789228800000,
              "volume": 11950.0
            },
            {
              "close": 55.79,
              "high": 55.92,
              "low": 55.65,
              "open": 55.84,
              "timestamp": 1789232400000,
              "volume": 11112.0
            },
            {
              "close": 55.34,
              "high": 55.79,
              "low": 55.32,
              "open": 55.79,
              "timestamp": 1789236000000,
              "volume": 11219.0
            },
            {
              "close": 54.84,
              "high": 55.48,
              "low": 54.68,
              "open": 55.34,
              "timestamp": 1789239600000,
              "volume": 11658.0
            },
            {
              "close": 54.79,
              "high": 55.09,
              "low": 54.67,
              "open": 54.84,
              "timestamp": 1789243200000,
              "volume": 10599.0
            },
            {
              "close": 54.94,
              "high": 55.06,
              "low": 54.55,
              "open": 54.79,
              "timestamp": 1789246800000,
              "volume": 10594.0
            },
            {
              "close": 54.71,
              "high": 55.06,
              "low": 54.65,
              "open": 54.94,
              "timestamp": 1789250400000,
              "volume": 9746.0
            },
            {
              "close": 54.7,
              "high": 54.85,
              "low": 54.62,
              "open": 54.71,
              "timestamp": 1789254000000,
              "volume": 10394.0
            },
            {
              "close": 54.83,
              "high": 54.96,
              "low": 54.51,
              "open": 54.52,
              "timestamp": 1789257600000,
              "volume": 11218.0
            },
            {
              "close": 54.9,
              "high": 54.99,
              "low": 54.56,
              "open": 54.83,
              "timestamp": 1789261200000,
              "volume": 11362.0
            },
            {
              "close": 54.77,
              "high": 54.92,
              "low": 54.45,
              "open": 54.9,
              "timestamp": 1789264800000,
              "volume": 10845.0
            },
            {
              "close": 54.53,
              "high": 54.91,
              "low": 54.39,
              "open": 54.77,
              "timestamp": 1789268400000,
              "volume": 12447.0
            },
            {
              "close": 55.16,
              "high": 55.46,
              "low": 54.44,
              "open": 54.53,
              "timestamp": 1789272000000,
              "volume": 12293.0
            },
            {
              "close": 56.0,
              "high": 56.1,
              "low": 55.1,
              "open": 55.16,
              "timestamp": 1789275600000,
              "volume": 11557.0
            },
            {
              "close": 55.49,
              "high": 56.02,
              "low": 55.36,
              "open": 56.0,
              "timestamp": 1789279200000,
              "volume": 11643.0
            },
            {
              "close": 55.05,
              "high": 55.75,
              "low": 55.03,
              "open": 55.47,
              "timestamp": 1789282800000,
              "volume": 11092.0
            },
            {
              "close": 53.88,
              "high": 55.08,
              "low": 53.53,
              "open": 55.05,
              "timestamp": 1789286400000,
              "volume": 14162.0
            },
            {
              "close": 54.45,
              "high": 54.54,
              "low": 53.57,
              "open": 53.89,
              "timestamp": 1789290000000,
              "volume": 14392.0
            },
            {
              "close": 54.01,
              "high": 54.56,
              "low": 53.88,
              "open": 54.45,
              "timestamp": 1789293600000,
              "volume": 12169.0
            },
            {
              "close": 53.93,
              "high": 54.3,
              "low": 53.9,
              "open": 54.01,
              "timestamp": 1789297200000,
              "volume": 11203.0
            },
            {
              "close": 53.95,
              "high": 54.15,
              "low": 53.76,
              "open": 53.93,
              "timestamp": 1789300800000,
              "volume": 11092.0
            },
            {
              "close": 53.94,
              "high": 54.24,
              "low": 53.26,
              "open": 53.95,
              "timestamp": 1789304400000,
              "volume": 12969.0
            },
            {
              "close": 54.26,
              "high": 54.54,
              "low": 53.9,
              "open": 53.96,
              "timestamp": 1789308000000,
              "volume": 12793.0
            },
            {
              "close": 53.31,
              "high": 54.29,
              "low": 53.22,
              "open": 54.26,
              "timestamp": 1789311600000,
              "volume": 12976.0
            },
            {
              "close": 54.03,
              "high": 54.08,
              "low": 53.28,
              "open": 53.31,
              "timestamp": 1789315200000,
              "volume": 12353.0
            },
            {
              "close": 54.68,
              "high": 55.0,
              "low": 54.02,
              "open": 54.03,
              "timestamp": 1789318800000,
              "volume": 12829.0
            },
            {
              "close": 54.8,
              "high": 54.95,
              "low": 54.54,
              "open": 54.68,
              "timestamp": 1789322400000,
              "volume": 10114.0
            },
            {
              "close": 54.07,
              "high": 54.89,
              "low": 53.96,
              "open": 54.8,
              "timestamp": 1789326000000,
              "volume": 11065.0
            }
          ],
          "last_price": 54.07,
          "momentum": "neutral",
          "rsi_14": 44.43,
          "structure": "bearish"
        },
        "4H": {
          "candle_count": 84,
          "candle_status": {
            "data_age_seconds": 14496,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789315200000,
            "latest_timestamp_utc": "2026-09-13T16:00:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 14400
          },
          "candles": [
            {
              "close": 41.71,
              "high": 44.25,
              "low": 40.71,
              "open": 43.6,
              "timestamp": 1788120000000,
              "volume": 58820.0
            },
            {
              "close": 41.19,
              "high": 42.43,
              "low": 40.5,
              "open": 41.71,
              "timestamp": 1788134400000,
              "volume": 54783.0
            },
            {
              "close": 42.01,
              "high": 42.26,
              "low": 40.76,
              "open": 41.19,
              "timestamp": 1788148800000,
              "volume": 46816.0
            },
            {
              "close": 44.14,
              "high": 44.43,
              "low": 41.74,
              "open": 42.01,
              "timestamp": 1788163200000,
              "volume": 53736.0
            },
            {
              "close": 44.46,
              "high": 44.65,
              "low": 42.77,
              "open": 44.14,
              "timestamp": 1788177600000,
              "volume": 62364.0
            },
            {
              "close": 45.52,
              "high": 48.44,
              "low": 44.03,
              "open": 44.46,
              "timestamp": 1788192000000,
              "volume": 67729.0
            },
            {
              "close": 44.85,
              "high": 45.77,
              "low": 44.37,
              "open": 45.54,
              "timestamp": 1788206400000,
              "volume": 51750.0
            },
            {
              "close": 45.5,
              "high": 46.06,
              "low": 44.7,
              "open": 44.85,
              "timestamp": 1788220800000,
              "volume": 57315.0
            },
            {
              "close": 46.79,
              "high": 47.43,
              "low": 45.49,
              "open": 45.5,
              "timestamp": 1788235200000,
              "volume": 58188.0
            },
            {
              "close": 45.89,
              "high": 46.8,
              "low": 44.77,
              "open": 46.79,
              "timestamp": 1788249600000,
              "volume": 58479.0
            },
            {
              "close": 44.53,
              "high": 46.28,
              "low": 44.06,
              "open": 45.89,
              "timestamp": 1788264000000,
              "volume": 61947.0
            },
            {
              "close": 43.64,
              "high": 44.57,
              "low": 42.75,
              "open": 44.53,
              "timestamp": 1788278400000,
              "volume": 59976.0
            },
            {
              "close": 43.84,
              "high": 43.98,
              "low": 43.17,
              "open": 43.64,
              "timestamp": 1788292800000,
              "volume": 45300.0
            },
            {
              "close": 42.59,
              "high": 43.92,
              "low": 41.75,
              "open": 43.84,
              "timestamp": 1788307200000,
              "volume": 55099.0
            },
            {
              "close": 42.03,
              "high": 42.82,
              "low": 41.86,
              "open": 42.59,
              "timestamp": 1788321600000,
              "volume": 49923.0
            },
            {
              "close": 41.68,
              "high": 42.19,
              "low": 41.08,
              "open": 42.03,
              "timestamp": 1788336000000,
              "volume": 54752.0
            },
            {
              "close": 42.12,
              "high": 42.7,
              "low": 41.55,
              "open": 41.69,
              "timestamp": 1788350400000,
              "volume": 47489.0
            },
            {
              "close": 42.06,
              "high": 42.6,
              "low": 41.9,
              "open": 42.12,
              "timestamp": 1788364800000,
              "volume": 48462.0
            },
            {
              "close": 42.62,
              "high": 43.5,
              "low": 42.01,
              "open": 42.06,
              "timestamp": 1788379200000,
              "volume": 46150.0
            },
            {
              "close": 42.36,
              "high": 42.97,
              "low": 42.02,
              "open": 42.62,
              "timestamp": 1788393600000,
              "volume": 47734.0
            },
            {
              "close": 42.38,
              "high": 42.9,
              "low": 42.0,
              "open": 42.36,
              "timestamp": 1788408000000,
              "volume": 47051.0
            },
            {
              "close": 43.27,
              "high": 43.4,
              "low": 42.27,
              "open": 42.38,
              "timestamp": 1788422400000,
              "volume": 46015.0
            },
            {
              "close": 47.33,
              "high": 47.46,
              "low": 42.52,
              "open": 43.27,
              "timestamp": 1788436800000,
              "volume": 52062.0
            },
            {
              "close": 46.35,
              "high": 47.35,
              "low": 45.54,
              "open": 47.33,
              "timestamp": 1788451200000,
              "volume": 59632.0
            },
            {
              "close": 47.41,
              "high": 47.61,
              "low": 45.83,
              "open": 46.36,
              "timestamp": 1788465600000,
              "volume": 54269.0
            },
            {
              "close": 51.43,
              "high": 51.66,
              "low": 46.09,
              "open": 47.42,
              "timestamp": 1788480000000,
              "volume": 63864.0
            },
            {
              "close": 49.81,
              "high": 52.86,
              "low": 48.73,
              "open": 51.41,
              "timestamp": 1788494400000,
              "volume": 69092.0
            },
            {
              "close": 52.64,
              "high": 54.58,
              "low": 49.74,
              "open": 49.81,
              "timestamp": 1788508800000,
              "volume": 69183.0
            },
            {
              "close": 52.63,
              "high": 53.72,
              "low": 49.21,
              "open": 52.64,
              "timestamp": 1788523200000,
              "volume": 59977.0
            },
            {
              "close": 55.11,
              "high": 56.44,
              "low": 52.39,
              "open": 52.63,
              "timestamp": 1788537600000,
              "volume": 69707.0
            },
            {
              "close": 62.51,
              "high": 64.17,
              "low": 55.06,
              "open": 55.1,
              "timestamp": 1788552000000,
              "volume": 68540.0
            },
            {
              "close": 66.41,
              "high": 68.73,
              "low": 61.68,
              "open": 62.48,
              "timestamp": 1788566400000,
              "volume": 71310.0
            },
            {
              "close": 68.85,
              "high": 73.8,
              "low": 66.06,
              "open": 66.41,
              "timestamp": 1788580800000,
              "volume": 55329.0
            },
            {
              "close": 67.94,
              "high": 68.5,
              "low": 65.64,
              "open": 66.04,
              "timestamp": 1788595200000,
              "volume": 64107.0
            },
            {
              "close": 68.36,
              "high": 70.83,
              "low": 67.09,
              "open": 67.94,
              "timestamp": 1788609600000,
              "volume": 70523.0
            },
            {
              "close": 67.13,
              "high": 70.44,
              "low": 66.23,
              "open": 68.36,
              "timestamp": 1788624000000,
              "volume": 67925.0
            },
            {
              "close": 65.46,
              "high": 68.58,
              "low": 64.76,
              "open": 67.13,
              "timestamp": 1788638400000,
              "volume": 63931.0
            },
            {
              "close": 68.47,
              "high": 69.49,
              "low": 65.42,
              "open": 65.45,
              "timestamp": 1788652800000,
              "volume": 67846.0
            },
            {
              "close": 70.41,
              "high": 78.68,
              "low": 68.03,
              "open": 68.47,
              "timestamp": 1788667200000,
              "volume": 70577.0
            },
            {
              "close": 67.96,
              "high": 70.64,
              "low": 65.23,
              "open": 70.39,
              "timestamp": 1788681600000,
              "volume": 68791.0
            },
            {
              "close": 66.82,
              "high": 71.2,
              "low": 66.44,
              "open": 67.96,
              "timestamp": 1788696000000,
              "volume": 68311.0
            },
            {
              "close": 70.88,
              "high": 71.55,
              "low": 66.45,
              "open": 66.82,
              "timestamp": 1788710400000,
              "volume": 68149.0
            },
            {
              "close": 71.22,
              "high": 71.67,
              "low": 69.56,
              "open": 70.88,
              "timestamp": 1788724800000,
              "volume": 65635.0
            },
            {
              "close": 69.63,
              "high": 72.36,
              "low": 68.32,
              "open": 71.19,
              "timestamp": 1788739200000,
              "volume": 68718.0
            },
            {
              "close": 67.84,
              "high": 71.35,
              "low": 66.25,
              "open": 69.63,
              "timestamp": 1788753600000,
              "volume": 69179.0
            },
            {
              "close": 67.83,
              "high": 69.08,
              "low": 67.14,
              "open": 67.84,
              "timestamp": 1788768000000,
              "volume": 62948.0
            },
            {
              "close": 64.66,
              "high": 68.4,
              "low": 64.43,
              "open": 67.83,
              "timestamp": 1788782400000,
              "volume": 65702.0
            },
            {
              "close": 64.21,
              "high": 65.93,
              "low": 63.61,
              "open": 64.64,
              "timestamp": 1788796800000,
              "volume": 63104.0
            },
            {
              "close": 62.79,
              "high": 64.95,
              "low": 62.58,
              "open": 64.21,
              "timestamp": 1788811200000,
              "volume": 62356.0
            },
            {
              "close": 62.98,
              "high": 64.64,
              "low": 62.45,
              "open": 62.79,
              "timestamp": 1788825600000,
              "volume": 66219.0
            },
            {
              "close": 62.28,
              "high": 63.91,
              "low": 61.66,
              "open": 62.98,
              "timestamp": 1788840000000,
              "volume": 65751.0
            },
            {
              "close": 63.15,
              "high": 63.62,
              "low": 61.61,
              "open": 62.28,
              "timestamp": 1788854400000,
              "volume": 63579.0
            },
            {
              "close": 64.37,
              "high": 64.96,
              "low": 61.86,
              "open": 63.15,
              "timestamp": 1788868800000,
              "volume": 67631.0
            },
            {
              "close": 61.81,
              "high": 64.92,
              "low": 61.55,
              "open": 64.36,
              "timestamp": 1788883200000,
              "volume": 64739.0
            },
            {
              "close": 62.43,
              "high": 62.75,
              "low": 61.34,
              "open": 61.81,
              "timestamp": 1788897600000,
              "volume": 59354.0
            },
            {
              "close": 62.03,
              "high": 63.42,
              "low": 61.54,
              "open": 62.43,
              "timestamp": 1788912000000,
              "volume": 62615.0
            },
            {
              "close": 65.3,
              "high": 65.99,
              "low": 62.03,
              "open": 62.03,
              "timestamp": 1788926400000,
              "volume": 66445.0
            },
            {
              "close": 65.27,
              "high": 66.31,
              "low": 64.01,
              "open": 65.3,
              "timestamp": 1788940800000,
              "volume": 65776.0
            },
            {
              "close": 62.81,
              "high": 65.64,
              "low": 62.1,
              "open": 65.27,
              "timestamp": 1788955200000,
              "volume": 66881.0
            },
            {
              "close": 61.97,
              "high": 64.89,
              "low": 61.81,
              "open": 62.81,
              "timestamp": 1788969600000,
              "volume": 61610.0
            },
            {
              "close": 58.54,
              "high": 62.85,
              "low": 58.23,
              "open": 61.96,
              "timestamp": 1788984000000,
              "volume": 60781.0
            },
            {
              "close": 57.68,
              "high": 58.9,
              "low": 56.59,
              "open": 58.58,
              "timestamp": 1788998400000,
              "volume": 64079.0
            },
            {
              "close": 56.46,
              "high": 58.26,
              "low": 55.88,
              "open": 57.68,
              "timestamp": 1789012800000,
              "volume": 61295.0
            },
            {
              "close": 57.02,
              "high": 57.8,
              "low": 56.16,
              "open": 56.46,
              "timestamp": 1789027200000,
              "volume": 59751.0
            },
            {
              "close": 56.26,
              "high": 57.68,
              "low": 55.63,
              "open": 57.02,
              "timestamp": 1789041600000,
              "volume": 65047.0
            },
            {
              "close": 55.72,
              "high": 56.63,
              "low": 54.88,
              "open": 56.26,
              "timestamp": 1789056000000,
              "volume": 61072.0
            },
            {
              "close": 54.0,
              "high": 56.43,
              "low": 53.83,
              "open": 55.72,
              "timestamp": 1789070400000,
              "volume": 53515.0
            },
            {
              "close": 55.34,
              "high": 55.4,
              "low": 53.94,
              "open": 54.01,
              "timestamp": 1789084800000,
              "volume": 59016.0
            },
            {
              "close": 55.68,
              "high": 56.33,
              "low": 55.22,
              "open": 55.33,
              "timestamp": 1789099200000,
              "volume": 55029.0
            },
            {
              "close": 54.7,
              "high": 56.02,
              "low": 54.17,
              "open": 55.68,
              "timestamp": 1789113600000,
              "volume": 55622.0
            },
            {
              "close": 56.17,
              "high": 59.4,
              "low": 54.49,
              "open": 54.7,
              "timestamp": 1789128000000,
              "volume": 69158.0
            },
            {
              "close": 56.3,
              "high": 57.1,
              "low": 55.37,
              "open": 56.17,
              "timestamp": 1789142400000,
              "volume": 64547.0
            },
            {
              "close": 56.84,
              "high": 56.96,
              "low": 55.17,
              "open": 56.3,
              "timestamp": 1789156800000,
              "volume": 55399.0
            },
            {
              "close": 56.37,
              "high": 57.23,
              "low": 55.87,
              "open": 56.82,
              "timestamp": 1789171200000,
              "volume": 52065.0
            },
            {
              "close": 56.85,
              "high": 56.98,
              "low": 55.93,
              "open": 56.37,
              "timestamp": 1789185600000,
              "volume": 46927.0
            },
            {
              "close": 56.2,
              "high": 56.85,
              "low": 55.98,
              "open": 56.85,
              "timestamp": 1789200000000,
              "volume": 44537.0
            },
            {
              "close": 56.2,
              "high": 56.58,
              "low": 55.89,
              "open": 56.2,
              "timestamp": 1789214400000,
              "volume": 47988.0
            },
            {
              "close": 54.84,
              "high": 56.26,
              "low": 54.68,
              "open": 56.2,
              "timestamp": 1789228800000,
              "volume": 45939.0
            },
            {
              "close": 54.7,
              "high": 55.09,
              "low": 54.55,
              "open": 54.84,
              "timestamp": 1789243200000,
              "volume": 41333.0
            },
            {
              "close": 54.53,
              "high": 54.99,
              "low": 54.39,
              "open": 54.52,
              "timestamp": 1789257600000,
              "volume": 45872.0
            },
            {
              "close": 55.05,
              "high": 56.1,
              "low": 54.44,
              "open": 54.53,
              "timestamp": 1789272000000,
              "volume": 46585.0
            },
            {
              "close": 53.93,
              "high": 55.08,
              "low": 53.53,
              "open": 55.05,
              "timestamp": 1789286400000,
              "volume": 51926.0
            },
            {
              "close": 53.31,
              "high": 54.54,
              "low": 53.22,
              "open": 53.93,
              "timestamp": 1789300800000,
              "volume": 49830.0
            },
            {
              "close": 54.07,
              "high": 55.0,
              "low": 53.28,
              "open": 53.31,
              "timestamp": 1789315200000,
              "volume": 46361.0
            }
          ],
          "last_price": 54.07,
          "momentum": "bearish",
          "rsi_14": 38.85,
          "structure": "bearish"
        },
        "5M": {
          "candle_count": 144,
          "candle_status": {
            "data_age_seconds": 396,
            "expected_close_timestamp_ms": 1789329600000,
            "expected_close_utc": "2026-09-13T20:00:00+00:00",
            "incomplete": false,
            "latest_timestamp_ms": 1789329300000,
            "latest_timestamp_utc": "2026-09-13T19:55:00+00:00",
            "seconds_remaining": 0,
            "stale": false,
            "status": "CLOSED",
            "timeframe_seconds": 300
          },
          "candles": [
            {
              "close": 54.92,
              "high": 55.08,
              "low": 54.91,
              "open": 55.05,
              "timestamp": 1789286400000,
              "volume": 1128.0
            },
            {
              "close": 54.88,
              "high": 54.97,
              "low": 54.88,
              "open": 54.92,
              "timestamp": 1789286700000,
              "volume": 1012.0
            },
            {
              "close": 54.81,
              "high": 54.88,
              "low": 54.8,
              "open": 54.88,
              "timestamp": 1789287000000,
              "volume": 1064.0
            },
            {
              "close": 54.66,
              "high": 54.81,
              "low": 54.65,
              "open": 54.8,
              "timestamp": 1789287300000,
              "volume": 1174.0
            },
            {
              "close": 54.68,
              "high": 54.77,
              "low": 54.65,
              "open": 54.66,
              "timestamp": 1789287600000,
              "volume": 1003.0
            },
            {
              "close": 54.32,
              "high": 54.69,
              "low": 54.3,
              "open": 54.68,
              "timestamp": 1789287900000,
              "volume": 1103.0
            },
            {
              "close": 54.16,
              "high": 54.39,
              "low": 54.0,
              "open": 54.32,
              "timestamp": 1789288200000,
              "volume": 1331.0
            },
            {
              "close": 54.06,
              "high": 54.21,
              "low": 54.01,
              "open": 54.16,
              "timestamp": 1789288500000,
              "volume": 1341.0
            },
            {
              "close": 53.61,
              "high": 54.09,
              "low": 53.53,
              "open": 54.06,
              "timestamp": 1789288800000,
              "volume": 1320.0
            },
            {
              "close": 53.93,
              "high": 53.94,
              "low": 53.6,
              "open": 53.61,
              "timestamp": 1789289100000,
              "volume": 1347.0
            },
            {
              "close": 53.87,
              "high": 53.99,
              "low": 53.8,
              "open": 53.93,
              "timestamp": 1789289400000,
              "volume": 1235.0
            },
            {
              "close": 53.88,
              "high": 53.94,
              "low": 53.79,
              "open": 53.87,
              "timestamp": 1789289700000,
              "volume": 1104.0
            },
            {
              "close": 54.21,
              "high": 54.21,
              "low": 53.87,
              "open": 53.89,
              "timestamp": 1789290000000,
              "volume": 1259.0
            },
            {
              "close": 54.14,
              "high": 54.28,
              "low": 54.11,
              "open": 54.22,
              "timestamp": 1789290300000,
              "volume": 1145.0
            },
            {
              "close": 54.14,
              "high": 54.21,
              "low": 54.05,
              "open": 54.14,
              "timestamp": 1789290600000,
              "volume": 1095.0
            },
            {
              "close": 54.18,
              "high": 54.23,
              "low": 54.08,
              "open": 54.14,
              "timestamp": 1789290900000,
              "volume": 1138.0
            },
            {
              "close": 53.98,
              "high": 54.25,
              "low": 53.92,
              "open": 54.18,
              "timestamp": 1789291200000,
              "volume": 1082.0
            },
            {
              "close": 53.7,
              "high": 54.02,
              "low": 53.69,
              "open": 54.0,
              "timestamp": 1789291500000,
              "volume": 1325.0
            },
            {
              "close": 53.67,
              "high": 53.9,
              "low": 53.57,
              "open": 53.7,
              "timestamp": 1789291800000,
              "volume": 1371.0
            },
            {
              "close": 53.84,
              "high": 54.06,
              "low": 53.67,
              "open": 53.67,
              "timestamp": 1789292100000,
              "volume": 1318.0
            },
            {
              "close": 54.14,
              "high": 54.22,
              "low": 53.82,
              "open": 53.84,
              "timestamp": 1789292400000,
              "volume": 1175.0
            },
            {
              "close": 54.35,
              "high": 54.4,
              "low": 54.04,
              "open": 54.14,
              "timestamp": 1789292700000,
              "volume": 1205.0
            },
            {
              "close": 54.48,
              "high": 54.54,
              "low": 54.23,
              "open": 54.35,
              "timestamp": 1789293000000,
              "volume": 1147.0
            },
            {
              "close": 54.45,
              "high": 54.48,
              "low": 54.37,
              "open": 54.48,
              "timestamp": 1789293300000,
              "volume": 1132.0
            },
            {
              "close": 54.49,
              "high": 54.49,
              "low": 54.36,
              "open": 54.45,
              "timestamp": 1789293600000,
              "volume": 1135.0
            },
            {
              "close": 54.53,
              "high": 54.56,
              "low": 54.38,
              "open": 54.49,
              "timestamp": 1789293900000,
              "volume": 1090.0
            },
            {
              "close": 54.44,
              "high": 54.53,
              "low": 54.38,
              "open": 54.53,
              "timestamp": 1789294200000,
              "volume": 1085.0
            },
            {
              "close": 54.34,
              "high": 54.47,
              "low": 54.33,
              "open": 54.44,
              "timestamp": 1789294500000,
              "volume": 1039.0
            },
            {
              "close": 54.32,
              "high": 54.37,
              "low": 54.25,
              "open": 54.34,
              "timestamp": 1789294800000,
              "volume": 959.0
            },
            {
              "close": 54.46,
              "high": 54.46,
              "low": 54.31,
              "open": 54.32,
              "timestamp": 1789295100000,
              "volume": 751.0
            },
            {
              "close": 54.36,
              "high": 54.47,
              "low": 54.3,
              "open": 54.46,
              "timestamp": 1789295400000,
              "volume": 896.0
            },
            {
              "close": 54.27,
              "high": 54.37,
              "low": 54.24,
              "open": 54.36,
              "timestamp": 1789295700000,
              "volume": 948.0
            },
            {
              "close": 54.07,
              "high": 54.27,
              "low": 54.03,
              "open": 54.27,
              "timestamp": 1789296000000,
              "volume": 1143.0
            },
            {
              "close": 54.13,
              "high": 54.2,
              "low": 54.05,
              "open": 54.05,
              "timestamp": 1789296300000,
              "volume": 914.0
            },
            {
              "close": 54.03,
              "high": 54.15,
              "low": 54.0,
              "open": 54.13,
              "timestamp": 1789296600000,
              "volume": 1081.0
            },
            {
              "close": 54.01,
              "high": 54.11,
              "low": 53.88,
              "open": 54.02,
              "timestamp": 1789296900000,
              "volume": 1128.0
            },
            {
              "close": 54.26,
              "high": 54.26,
              "low": 54.01,
              "open": 54.01,
              "timestamp": 1789297200000,
              "volume": 1193.0
            },
            {
              "close": 54.11,
              "high": 54.3,
              "low": 54.09,
              "open": 54.26,
              "timestamp": 1789297500000,
              "volume": 1067.0
            },
            {
              "close": 54.08,
              "high": 54.15,
              "low": 54.06,
              "open": 54.11,
              "timestamp": 1789297800000,
              "volume": 973.0
            },
            {
              "close": 54.14,
              "high": 54.26,
              "low": 54.08,
              "open": 54.08,
              "timestamp": 1789298100000,
              "volume": 1013.0
            },
            {
              "close": 54.12,
              "high": 54.15,
              "low": 54.08,
              "open": 54.14,
              "timestamp": 1789298400000,
              "volume": 857.0
            },
            {
              "close": 54.06,
              "high": 54.15,
              "low": 54.03,
              "open": 54.12,
              "timestamp": 1789298700000,
              "volume": 792.0
            },
            {
              "close": 54.15,
              "high": 54.15,
              "low": 54.04,
              "open": 54.06,
              "timestamp": 1789299000000,
              "volume": 838.0
            },
            {
              "close": 54.13,
              "high": 54.15,
              "low": 54.08,
              "open": 54.15,
              "timestamp": 1789299300000,
              "volume": 876.0
            },
            {
              "close": 54.23,
              "high": 54.25,
              "low": 54.1,
              "open": 54.13,
              "timestamp": 1789299600000,
              "volume": 912.0
            },
            {
              "close": 54.13,
              "high": 54.26,
              "low": 54.11,
              "open": 54.23,
              "timestamp": 1789299900000,
              "volume": 921.0
            },
            {
              "close": 53.96,
              "high": 54.2,
              "low": 53.93,
              "open": 54.12,
              "timestamp": 1789300200000,
              "volume": 964.0
            },
            {
              "close": 53.93,
              "high": 53.96,
              "low": 53.9,
              "open": 53.96,
              "timestamp": 1789300500000,
              "volume": 797.0
            },
            {
              "close": 53.89,
              "high": 53.94,
              "low": 53.85,
              "open": 53.93,
              "timestamp": 1789300800000,
              "volume": 989.0
            },
            {
              "close": 53.93,
              "high": 53.94,
              "low": 53.86,
              "open": 53.89,
              "timestamp": 1789301100000,
              "volume": 1012.0
            },
            {
              "close": 53.92,
              "high": 53.99,
              "low": 53.91,
              "open": 53.91,
              "timestamp": 1789301400000,
              "volume": 859.0
            },
            {
              "close": 53.97,
              "high": 53.99,
              "low": 53.9,
              "open": 53.92,
              "timestamp": 1789301700000,
              "volume": 858.0
            },
            {
              "close": 53.9,
              "high": 53.98,
              "low": 53.86,
              "open": 53.97,
              "timestamp": 1789302000000,
              "volume": 851.0
            },
            {
              "close": 53.95,
              "high": 54.05,
              "low": 53.9,
              "open": 53.9,
              "timestamp": 1789302300000,
              "volume": 758.0
            },
            {
              "close": 54.0,
              "high": 54.15,
              "low": 53.95,
              "open": 53.95,
              "timestamp": 1789302600000,
              "volume": 1042.0
            },
            {
              "close": 53.91,
              "high": 54.03,
              "low": 53.82,
              "open": 54.0,
              "timestamp": 1789302900000,
              "volume": 1035.0
            },
            {
              "close": 53.84,
              "high": 53.93,
              "low": 53.81,
              "open": 53.9,
              "timestamp": 1789303200000,
              "volume": 921.0
            },
            {
              "close": 53.78,
              "high": 53.86,
              "low": 53.76,
              "open": 53.84,
              "timestamp": 1789303500000,
              "volume": 910.0
            },
            {
              "close": 53.9,
              "high": 53.94,
              "low": 53.77,
              "open": 53.78,
              "timestamp": 1789303800000,
              "volume": 963.0
            },
            {
              "close": 53.95,
              "high": 53.95,
              "low": 53.82,
              "open": 53.9,
              "timestamp": 1789304100000,
              "volume": 894.0
            },
            {
              "close": 53.78,
              "high": 53.96,
              "low": 53.78,
              "open": 53.95,
              "timestamp": 1789304400000,
              "volume": 1064.0
            },
            {
              "close": 53.8,
              "high": 53.82,
              "low": 53.74,
              "open": 53.78,
              "timestamp": 1789304700000,
              "volume": 993.0
            },
            {
              "close": 53.8,
              "high": 53.81,
              "low": 53.77,
              "open": 53.8,
              "timestamp": 1789305000000,
              "volume": 781.0
            },
            {
              "close": 53.6,
              "high": 53.8,
              "low": 53.59,
              "open": 53.8,
              "timestamp": 1789305300000,
              "volume": 996.0
            },
            {
              "close": 53.52,
              "high": 53.63,
              "low": 53.45,
              "open": 53.6,
              "timestamp": 1789305600000,
              "volume": 1185.0
            },
            {
              "close": 53.3,
              "high": 53.54,
              "low": 53.26,
              "open": 53.52,
              "timestamp": 1789305900000,
              "volume": 1230.0
            },
            {
              "close": 53.51,
              "high": 53.55,
              "low": 53.29,
              "open": 53.3,
              "timestamp": 1789306200000,
              "volume": 1155.0
            },
            {
              "close": 53.54,
              "high": 53.6,
              "low": 53.48,
              "open": 53.51,
              "timestamp": 1789306500000,
              "volume": 986.0
            },
            {
              "close": 53.7,
              "high": 53.73,
              "low": 53.52,
              "open": 53.54,
              "timestamp": 1789306800000,
              "volume": 1062.0
            },
            {
              "close": 53.85,
              "high": 53.85,
              "low": 53.7,
              "open": 53.7,
              "timestamp": 1789307100000,
              "volume": 1143.0
            },
            {
              "close": 54.12,
              "high": 54.24,
              "low": 53.84,
              "open": 53.85,
              "timestamp": 1789307400000,
              "volume": 1280.0
            },
            {
              "close": 53.94,
              "high": 54.12,
              "low": 53.88,
              "open": 54.12,
              "timestamp": 1789307700000,
              "volume": 1094.0
            },
            {
              "close": 53.95,
              "high": 53.98,
              "low": 53.9,
              "open": 53.96,
              "timestamp": 1789308000000,
              "volume": 990.0
            },
            {
              "close": 54.11,
              "high": 54.11,
              "low": 53.93,
              "open": 53.95,
              "timestamp": 1789308300000,
              "volume": 1092.0
            },
            {
              "close": 54.25,
              "high": 54.25,
              "low": 54.05,
              "open": 54.11,
              "timestamp": 1789308600000,
              "volume": 1148.0
            },
            {
              "close": 54.3,
              "high": 54.42,
              "low": 54.19,
              "open": 54.25,
              "timestamp": 1789308900000,
              "volume": 1224.0
            },
            {
              "close": 54.36,
              "high": 54.36,
              "low": 54.26,
              "open": 54.31,
              "timestamp": 1789309200000,
              "volume": 1010.0
            },
            {
              "close": 54.33,
              "high": 54.4,
              "low": 54.3,
              "open": 54.36,
              "timestamp": 1789309500000,
              "volume": 1027.0
            },
            {
              "close": 54.25,
              "high": 54.37,
              "low": 54.2,
              "open": 54.33,
              "timestamp": 1789309800000,
              "volume": 1064.0
            },
            {
              "close": 54.41,
              "high": 54.48,
              "low": 54.22,
              "open": 54.25,
              "timestamp": 1789310100000,
              "volume": 1109.0
            },
            {
              "close": 54.38,
              "high": 54.54,
              "low": 54.35,
              "open": 54.41,
              "timestamp": 1789310400000,
              "volume": 1115.0
            },
            {
              "close": 54.35,
              "high": 54.46,
              "low": 54.28,
              "open": 54.38,
              "timestamp": 1789310700000,
              "volume": 1022.0
            },
            {
              "close": 54.27,
              "high": 54.37,
              "low": 54.24,
              "open": 54.35,
              "timestamp": 1789311000000,
              "volume": 1018.0
            },
            {
              "close": 54.26,
              "high": 54.32,
              "low": 54.17,
              "open": 54.27,
              "timestamp": 1789311300000,
              "volume": 974.0
            },
            {
              "close": 53.93,
              "high": 54.29,
              "low": 53.93,
              "open": 54.26,
              "timestamp": 1789311600000,
              "volume": 1229.0
            },
            {
              "close": 53.75,
              "high": 53.96,
              "low": 53.74,
              "open": 53.93,
              "timestamp": 1789311900000,
              "volume": 1172.0
            },
            {
              "close": 53.67,
              "high": 53.75,
              "low": 53.62,
              "open": 53.75,
              "timestamp": 1789312200000,
              "volume": 1079.0
            },
            {
              "close": 53.5,
              "high": 53.69,
              "low": 53.46,
              "open": 53.67,
              "timestamp": 1789312500000,
              "volume": 1155.0
            },
            {
              "close": 53.66,
              "high": 53.74,
              "low": 53.36,
              "open": 53.5,
              "timestamp": 1789312800000,
              "volume": 1117.0
            },
            {
              "close": 53.44,
              "high": 53.67,
              "low": 53.4,
              "open": 53.66,
              "timestamp": 1789313100000,
              "volume": 1163.0
            },
            {
              "close": 53.52,
              "high": 53.54,
              "low": 53.31,
              "open": 53.42,
              "timestamp": 1789313400000,
              "volume": 1219.0
            },
            {
              "close": 53.48,
              "high": 53.52,
              "low": 53.41,
              "open": 53.52,
              "timestamp": 1789313700000,
              "volume": 978.0
            },
            {
              "close": 53.53,
              "high": 53.57,
              "low": 53.43,
              "open": 53.48,
              "timestamp": 1789314000000,
              "volume": 895.0
            },
            {
              "close": 53.5,
              "high": 53.53,
              "low": 53.35,
              "open": 53.53,
              "timestamp": 1789314300000,
              "volume": 998.0
            },
            {
              "close": 53.41,
              "high": 53.5,
              "low": 53.34,
              "open": 53.5,
              "timestamp": 1789314600000,
              "volume": 950.0
            },
            {
              "close": 53.31,
              "high": 53.41,
              "low": 53.22,
              "open": 53.41,
              "timestamp": 1789314900000,
              "volume": 1021.0
            },
            {
              "close": 53.56,
              "high": 53.69,
              "low": 53.28,
              "open": 53.31,
              "timestamp": 1789315200000,
              "volume": 1273.0
            },
            {
              "close": 53.75,
              "high": 53.8,
              "low": 53.54,
              "open": 53.56,
              "timestamp": 1789315500000,
              "volume": 1162.0
            },
            {
              "close": 53.56,
              "high": 53.88,
              "low": 53.56,
              "open": 53.75,
              "timestamp": 1789315800000,
              "volume": 1201.0
            },
            {
              "close": 53.7,
              "high": 53.7,
              "low": 53.54,
              "open": 53.57,
              "timestamp": 1789316100000,
              "volume": 1059.0
            },
            {
              "close": 53.76,
              "high": 53.78,
              "low": 53.66,
              "open": 53.7,
              "timestamp": 1789316400000,
              "volume": 1064.0
            },
            {
              "close": 53.71,
              "high": 53.82,
              "low": 53.66,
              "open": 53.76,
              "timestamp": 1789316700000,
              "volume": 932.0
            },
            {
              "close": 53.65,
              "high": 53.74,
              "low": 53.59,
              "open": 53.71,
              "timestamp": 1789317000000,
              "volume": 898.0
            },
            {
              "close": 53.66,
              "high": 53.7,
              "low": 53.61,
              "open": 53.65,
              "timestamp": 1789317300000,
              "volume": 897.0
            },
            {
              "close": 53.88,
              "high": 53.88,
              "low": 53.66,
              "open": 53.66,
              "timestamp": 1789317600000,
              "volume": 947.0
            },
            {
              "close": 53.85,
              "high": 53.95,
              "low": 53.78,
              "open": 53.88,
              "timestamp": 1789317900000,
              "volume": 1039.0
            },
            {
              "close": 53.95,
              "high": 54.05,
              "low": 53.83,
              "open": 53.85,
              "timestamp": 1789318200000,
              "volume": 992.0
            },
            {
              "close": 54.03,
              "high": 54.08,
              "low": 53.95,
              "open": 53.95,
              "timestamp": 1789318500000,
              "volume": 889.0
            },
            {
              "close": 54.29,
              "high": 54.33,
              "low": 54.02,
              "open": 54.03,
              "timestamp": 1789318800000,
              "volume": 1079.0
            },
            {
              "close": 54.38,
              "high": 54.47,
              "low": 54.25,
              "open": 54.29,
              "timestamp": 1789319100000,
              "volume": 1198.0
            },
            {
              "close": 54.73,
              "high": 54.93,
              "low": 54.37,
              "open": 54.38,
              "timestamp": 1789319400000,
              "volume": 1325.0
            },
            {
              "close": 54.91,
              "high": 54.92,
              "low": 54.7,
              "open": 54.73,
              "timestamp": 1789319700000,
              "volume": 1189.0
            },
            {
              "close": 54.77,
              "high": 55.0,
              "low": 54.74,
              "open": 54.93,
              "timestamp": 1789320000000,
              "volume": 1176.0
            },
            {
              "close": 54.8,
              "high": 54.86,
              "low": 54.75,
              "open": 54.77,
              "timestamp": 1789320300000,
              "volume": 990.0
            },
            {
              "close": 54.61,
              "high": 54.83,
              "low": 54.57,
              "open": 54.8,
              "timestamp": 1789320600000,
              "volume": 1145.0
            },
            {
              "close": 54.58,
              "high": 54.68,
              "low": 54.53,
              "open": 54.61,
              "timestamp": 1789320900000,
              "volume": 1016.0
            },
            {
              "close": 54.48,
              "high": 54.58,
              "low": 54.43,
              "open": 54.58,
              "timestamp": 1789321200000,
              "volume": 943.0
            },
            {
              "close": 54.61,
              "high": 54.7,
              "low": 54.48,
              "open": 54.48,
              "timestamp": 1789321500000,
              "volume": 1027.0
            },
            {
              "close": 54.65,
              "high": 54.75,
              "low": 54.58,
              "open": 54.61,
              "timestamp": 1789321800000,
              "volume": 933.0
            },
            {
              "close": 54.68,
              "high": 54.76,
              "low": 54.65,
              "open": 54.65,
              "timestamp": 1789322100000,
              "volume": 808.0
            },
            {
              "close": 54.56,
              "high": 54.76,
              "low": 54.54,
              "open": 54.68,
              "timestamp": 1789322400000,
              "volume": 1068.0
            },
            {
              "close": 54.58,
              "high": 54.64,
              "low": 54.54,
              "open": 54.56,
              "timestamp": 1789322700000,
              "volume": 858.0
            },
            {
              "close": 54.63,
              "high": 54.66,
              "low": 54.55,
              "open": 54.58,
              "timestamp": 1789323000000,
              "volume": 764.0
            },
            {
              "close": 54.64,
              "high": 54.67,
              "low": 54.56,
              "open": 54.63,
              "timestamp": 1789323300000,
              "volume": 798.0
            },
            {
              "close": 54.65,
              "high": 54.73,
              "low": 54.58,
              "open": 54.64,
              "timestamp": 1789323600000,
              "volume": 810.0
            },
            {
              "close": 54.58,
              "high": 54.67,
              "low": 54.56,
              "open": 54.65,
              "timestamp": 1789323900000,
              "volume": 842.0
            },
            {
              "close": 54.68,
              "high": 54.69,
              "low": 54.56,
              "open": 54.59,
              "timestamp": 1789324200000,
              "volume": 879.0
            },
            {
              "close": 54.82,
              "high": 54.88,
              "low": 54.68,
              "open": 54.68,
              "timestamp": 1789324500000,
              "volume": 977.0
            },
            {
              "close": 54.8,
              "high": 54.82,
              "low": 54.73,
              "open": 54.82,
              "timestamp": 1789324800000,
              "volume": 724.0
            },
            {
              "close": 54.83,
              "high": 54.95,
              "low": 54.78,
              "open": 54.8,
              "timestamp": 1789325100000,
              "volume": 894.0
            },
            {
              "close": 54.86,
              "high": 54.89,
              "low": 54.82,
              "open": 54.83,
              "timestamp": 1789325400000,
              "volume": 724.0
            },
            {
              "close": 54.8,
              "high": 54.86,
              "low": 54.74,
              "open": 54.86,
              "timestamp": 1789325700000,
              "volume": 776.0
            },
            {
              "close": 54.77,
              "high": 54.89,
              "low": 54.74,
              "open": 54.8,
              "timestamp": 1789326000000,
              "volume": 940.0
            },
            {
              "close": 54.65,
              "high": 54.85,
              "low": 54.63,
              "open": 54.77,
              "timestamp": 1789326300000,
              "volume": 1070.0
            },
            {
              "close": 54.45,
              "high": 54.66,
              "low": 54.41,
              "open": 54.65,
              "timestamp": 1789326600000,
              "volume": 1056.0
            },
            {
              "close": 54.28,
              "high": 54.5,
              "low": 54.26,
              "open": 54.45,
              "timestamp": 1789326900000,
              "volume": 1099.0
            },
            {
              "close": 54.23,
              "high": 54.31,
              "low": 54.18,
              "open": 54.28,
              "timestamp": 1789327200000,
              "volume": 999.0
            },
            {
              "close": 54.15,
              "high": 54.29,
              "low": 54.15,
              "open": 54.23,
              "timestamp": 1789327500000,
              "volume": 777.0
            },
            {
              "close": 54.09,
              "high": 54.22,
              "low": 54.07,
              "open": 54.16,
              "timestamp": 1789327800000,
              "volume": 937.0
            },
            {
              "close": 54.03,
              "high": 54.12,
              "low": 54.0,
              "open": 54.09,
              "timestamp": 1789328100000,
              "volume": 963.0
            },
            {
              "close": 54.02,
              "high": 54.08,
              "low": 54.02,
              "open": 54.03,
              "timestamp": 1789328400000,
              "volume": 861.0
            },
            {
              "close": 54.03,
              "high": 54.06,
              "low": 54.0,
              "open": 54.02,
              "timestamp": 1789328700000,
              "volume": 787.0
            },
            {
              "close": 54.07,
              "high": 54.08,
              "low": 53.96,
              "open": 54.03,
              "timestamp": 1789329000000,
              "volume": 804.0
            },
            {
              "close": 54.07,
              "high": 54.11,
              "low": 54.06,
              "open": 54.08,
              "timestamp": 1789329300000,
              "volume": 772.0
            }
          ],
          "last_price": 54.07,
          "momentum": "bearish",
          "rsi_14": 34.87,
          "structure": "bearish"
        }
      }
    }
  ],
  "market_discovery": {
    "broker_instrument_count": 94,
    "candidates": [
      {
        "category": "crypto",
        "info_route_id": 452,
        "live_ask": 77254.79,
        "live_bid": 77253.6,
        "live_mid": 77254.195,
        "quote_age_seconds": 0,
        "quote_available": true,
        "quote_source": "live",
        "relative_spread_bps": 0.15403694258774897,
        "spread": 1.1899999999877764,
        "symbol": "BTCUSD",
        "tradable_instrument_id": 206
      },
      {
        "category": "crypto",
        "info_route_id": 452,
        "live_ask": 2505.44,
        "live_bid": 2504.76,
        "live_mid": 2505.1000000000004,
        "quote_age_seconds": 0,
        "quote_available": true,
        "quote_source": "live",
        "relative_spread_bps": 2.7144624965064716,
        "spread": 0.6799999999998363,
        "symbol": "ETHUSD",
        "tradable_instrument_id": 214
      },
      {
        "category": "crypto",
        "info_route_id": 452,
        "live_ask": 100.94,
        "live_bid": 100.91,
        "live_mid": 100.925,
        "quote_age_seconds": 0,
        "quote_available": true,
        "quote_source": "live",
        "relative_spread_bps": 2.972504334902268,
        "spread": 0.030000000000001137,
        "symbol": "SOLUSD",
        "tradable_instrument_id": 221
      },
      {
        "category": "crypto",
        "info_route_id": 452,
        "live_ask": 721.44,
        "live_bid": 721.43,
        "live_mid": 721.435,
        "quote_age_seconds": 0,
        "quote_available": true,
        "quote_source": "live",
        "relative_spread_bps": 0.13861262622557255,
        "spread": 0.010000000000104592,
        "symbol": "BNBUSD",
        "tradable_instrument_id": 205
      },
      {
        "category": "crypto",
        "info_route_id": 452,
        "live_ask": 1.35451,
        "live_bid": 1.35439,
        "live_mid": 1.35445,
        "quote_age_seconds": 0,
        "quote_available": true,
        "quote_source": "live",
        "relative_spread_bps": 0.8859684742893427,
        "spread": 0.00012000000000012001,
        "symbol": "XRPUSD",
        "tradable_instrument_id": 225
      },
      {
        "category": "crypto",
        "info_route_id": 452,
        "live_ask": 530.88,
        "live_bid": 530.87,
        "live_mid": 530.875,
        "quote_age_seconds": 0,
        "quote_available": true,
        "quote_source": "live",
        "relative_spread_bps": 0.18836825994802742,
        "spread": 0.009999999999990905,
        "symbol": "XMRUSD",
        "tradable_instrument_id": 224
      },
      {
        "category": "crypto",
        "info_route_id": 452,
        "live_ask": 0.1792,
        "live_bid": 0.17917,
        "live_mid": 0.17918499999999998,
        "quote_age_seconds": 0,
        "quote_available": true,
        "quote_source": "live",
        "relative_spread_bps": 1.6742472863243156,
        "spread": 3.0000000000002247e-05,
        "symbol": "XLMUSD",
        "tradable_instrument_id": 223
      },
      {
        "category": "crypto",
        "info_route_id": 452,
        "live_ask": 0.08416,
        "live_bid": 0.08411,
        "live_mid": 0.084135,
        "quote_age_seconds": 0,
        "quote_available": true,
        "quote_source": "live",
        "relative_spread_bps": 5.942829975633742,
        "spread": 4.999999999999449e-05,
        "symbol": "DOGEUSD",
        "tradable_instrument_id": 208
      },
      {
        "category": "crypto",
        "info_route_id": 452,
        "live_ask": 1085.79,
        "live_bid": 1085.06,
        "live_mid": 1085.425,
        "quote_age_seconds": 0,
        "quote_available": true,
        "quote_source": "live",
        "relative_spread_bps": 6.725476195960276,
        "spread": 0.7300000000000182,
        "symbol": "ZECUSD",
        "tradable_instrument_id": 226
      },
      {
        "category": "crypto",
        "info_route_id": 452,
        "live_ask": 54.11,
        "live_bid": 54.07,
        "live_mid": 54.09,
        "quote_age_seconds": 0,
        "quote_available": true,
        "quote_source": "live",
        "relative_spread_bps": 7.395082270290099,
        "spread": 0.03999999999999915,
        "symbol": "DASHUSD",
        "tradable_instrument_id": 207
      }
    ],
    "contains_trade_authorization": false,
    "deep_analysis_missing": 5,
    "deep_analysis_requested": 10,
    "deep_analysis_successful": 5,
    "deep_scan_completeness_note": "Symbols selected by discovery but absent from the deep-analysis export are explicitly listed here. Absence is never treated as successful analysis.",
    "deep_scan_failure_records": [
      {
        "reason": "Selected by market discovery but absent from the returned deep-analysis instrument set. This symbol is not counted as successfully analyzed.",
        "stage": "deep_multitimeframe_analysis",
        "status": "NO_DEEP_ANALYSIS_RESULT",
        "symbol": "SOLUSD"
      },
      {
        "reason": "Selected by market discovery but absent from the returned deep-analysis instrument set. This symbol is not counted as successfully analyzed.",
        "stage": "deep_multitimeframe_analysis",
        "status": "NO_DEEP_ANALYSIS_RESULT",
        "symbol": "XRPUSD"
      },
      {
        "reason": "Selected by market discovery but absent from the returned deep-analysis instrument set. This symbol is not counted as successfully analyzed.",
        "stage": "deep_multitimeframe_analysis",
        "status": "NO_DEEP_ANALYSIS_RESULT",
        "symbol": "XMRUSD"
      },
      {
        "reason": "Selected by market discovery but absent from the returned deep-analysis instrument set. This symbol is not counted as successfully analyzed.",
        "stage": "deep_multitimeframe_analysis",
        "status": "NO_DEEP_ANALYSIS_RESULT",
        "symbol": "XLMUSD"
      },
      {
        "reason": "Selected by market discovery but absent from the returned deep-analysis instrument set. This symbol is not counted as successfully analyzed.",
        "stage": "deep_multitimeframe_analysis",
        "status": "NO_DEEP_ANALYSIS_RESULT",
        "symbol": "ZECUSD"
      }
    ],
    "deep_scan_missing_count": 5,
    "deep_scan_missing_requires_review": true,
    "deep_scan_missing_symbols": [
      "SOLUSD",
      "XRPUSD",
      "XMRUSD",
      "XLMUSD",
      "ZECUSD"
    ],
    "deep_scan_output_count": 5,
    "deep_scan_output_symbols": [
      "BTCUSD",
      "ETHUSD",
      "BNBUSD",
      "DOGEUSD",
      "DASHUSD"
    ],
    "deep_scan_successful_symbols": [
      "BTCUSD",
      "ETHUSD",
      "BNBUSD",
      "DOGEUSD",
      "DASHUSD"
    ],
    "duplicate_symbols": [],
    "eligible_instrument_count": 19,
    "error": null,
    "live_quote_failure_count": 0,
    "live_quote_success_count": 19,
    "mode": "full_market_live_quote_discovery",
    "overall_scan_complete": false,
    "selected_count": 10,
    "selected_symbols": [
      "BTCUSD",
      "ETHUSD",
      "SOLUSD",
      "BNBUSD",
      "XRPUSD",
      "XMRUSD",
      "XLMUSD",
      "DOGEUSD",
      "ZECUSD",
      "DASHUSD"
    ],
    "selection_is_advisory": true,
    "selection_method": "atlas_priority_then_relative_spread_prefilter_then_existing_deep_multitimeframe_analysis",
    "shortlist_raw_count": 10,
    "shortlist_unique_count": 10,
    "timing_parent_total_ms": 11124.822,
    "timing_substages_ms": {
      "filtering_normalization_ms": 0.0,
      "other_discovery_ms": 0.0,
      "quote_retrieval_gather_ms": 11068.417,
      "resolver_spec_details_ms": 0.0,
      "shortlist_construction_ms": 0.0,
      "universe_instrument_acquisition_ms": 1289.192,
      "waits_retries_delays_ms": 0.0
    },
    "universe_asset_classes": [
      "forex",
      "index",
      "commodity",
      "crypto"
    ]
  },
  "match_trader_cross_reference": {
    "affects_tradelocker_trade_decision": false,
    "ask": null,
    "available": false,
    "bid": null,
    "error": null,
    "mapping_status": "no_tradelocker_instrument",
    "match_trader_alias": null,
    "match_trader_instrument": null,
    "role": "translation_cross_reference_only",
    "timestamp_ms": null,
    "tradelocker_instrument": null
  },
  "match_trader_sizing": {
    "account_balance": null,
    "account_currency": null,
    "account_free_margin": null,
    "advisory_only": true,
    "available": false,
    "calculated_position_size": null,
    "contract_size": null,
    "error": "Translated Match-Trader trade plan unavailable.",
    "estimated_stop_risk": null,
    "execution_authorized": false,
    "raw_quantity": null,
    "risk_amount": null,
    "risk_percent": null,
    "volume_max": null,
    "volume_min": null,
    "volume_step": null
  },
  "match_trader_translation": {
    "affects_tradelocker_trade_decision": false,
    "available": false,
    "error": null,
    "match_trader_failure_blocks_tradelocker_order": false,
    "match_trader_quote_age_seconds": null,
    "match_trader_reference_price": null,
    "match_trader_required_for_decision": false,
    "method": "relative_price_geometry_from_fresh_midpoints",
    "reference_ratio": null,
    "role": "price_cross_reference_and_order_translation_only",
    "tradelocker_reference_price": null,
    "translated_trade_plan": null,
    "translation_status": "no_frozen_trade_plan"
  },
  "persistent_alerts": {
    "active_at_export_start": [],
    "broker_order_submitted": false,
    "evaluated": [],
    "external_ai_reassessment_required": false,
    "note": "Triggered alerts require fresh external Atlas reassessment. They never authorize execution.",
    "read_only": true,
    "triggered": [],
    "triggered_count": 0
  },
  "purpose": "Atlas scan and monitor handoff for external AI review",
  "request": {
    "mode": "full_ai_review",
    "symbols": [
      "BTCUSD",
      "ETHUSD",
      "SOLUSD",
      "BNBUSD",
      "XRPUSD",
      "XMRUSD",
      "XLMUSD",
      "DOGEUSD",
      "ZECUSD",
      "DASHUSD"
    ],
    "timeframes": [
      "4H",
      "1H",
      "15M",
      "5M"
    ]
  },
  "risk_sized_execution_candidate": {
    "advisory_only": true,
    "available": false,
    "calculated_position_size": null,
    "direction": null,
    "entry": null,
    "error": null,
    "estimated_margin_requirement": null,
    "estimated_stop_risk": null,
    "execution_authorized": false,
    "instrument": null,
    "proposed_risk_percent": null,
    "raw_quantity": null,
    "risk_amount": null,
    "rr_tp1": null,
    "rr_tp2": null,
    "rr_tp3": null,
    "safe_loss": null,
    "sizing_note": "Position size is calculated only when the instrument is quoted in the account currency and broker lot metadata is available. Margin requirement is not estimated here.",
    "tp1": null,
    "tp2": null,
    "tp3": null
  },
  "rr_audit": {
    "external_ai_instruction": "Review structural_room_rr and trade-plan R:R separately. A strong structural-room metric must not override poor actual Safe-Loss-to-target R:R.",
    "geometry_metric": {
      "field": "bridge_analysis.geometry.reward_to_risk",
      "meaning": "Structural room/opportunity relative to the geometry invalidation reference. This is contextual and must not be treated as the execution trade-plan R:R.",
      "recommended_name": "structural_room_rr"
    },
    "trade_plan_metrics": {
      "fields": [
        "bridge_analysis.trade_plan.rr_tp1",
        "bridge_analysis.trade_plan.rr_tp3",
        "bridge_analysis.trade_plan.rr_tp2"
      ],
      "meaning": "Actual reward-to-risk using the final Safe Loss and the structure-derived TP1, TP3, and TP2 levels."
    },
    "validity_semantics": {
      "trade_plan_valid_does_not_mean": [
        "approved",
        "high-quality reward-to-risk",
        "actionable",
        "execution-authorized"
      ],
      "trade_plan_valid_means": "Structural trade geometry is internally coherent."
    }
  },
  "runtime_loaded_bootstrap_sha256": "84a467e807998069de9dab42584a7c2294e03ec7e7eee12d4b85e8bffa86bc9a",
  "safety": {
    "bridge_execution_disabled": true,
    "contains_execution_instruction": false,
    "contains_trade_authorization": false,
    "external_ai_may_review": true,
    "external_ai_must_reassess_current_market": true,
    "frozen_trade_plan_is_context_not_authorization": true,
    "manual_user_execution_required": true,
    "read_only": true
  },
  "scan_status": {
    "deep_analysis_failure_records": [
      {
        "reason": "Selected by market discovery but absent from the returned deep-analysis instrument set. This symbol is not counted as successfully analyzed.",
        "stage": "deep_multitimeframe_analysis",
        "status": "NO_DEEP_ANALYSIS_RESULT",
        "symbol": "SOLUSD"
      },
      {
        "reason": "Selected by market discovery but absent from the returned deep-analysis instrument set. This symbol is not counted as successfully analyzed.",
        "stage": "deep_multitimeframe_analysis",
        "status": "NO_DEEP_ANALYSIS_RESULT",
        "symbol": "XRPUSD"
      },
      {
        "reason": "Selected by market discovery but absent from the returned deep-analysis instrument set. This symbol is not counted as successfully analyzed.",
        "stage": "deep_multitimeframe_analysis",
        "status": "NO_DEEP_ANALYSIS_RESULT",
        "symbol": "XMRUSD"
      },
      {
        "reason": "Selected by market discovery but absent from the returned deep-analysis instrument set. This symbol is not counted as successfully analyzed.",
        "stage": "deep_multitimeframe_analysis",
        "status": "NO_DEEP_ANALYSIS_RESULT",
        "symbol": "XLMUSD"
      },
      {
        "reason": "Selected by market discovery but absent from the returned deep-analysis instrument set. This symbol is not counted as successfully analyzed.",
        "stage": "deep_multitimeframe_analysis",
        "status": "NO_DEEP_ANALYSIS_RESULT",
        "symbol": "ZECUSD"
      }
    ],
    "deep_analysis_missing": 5,
    "deep_analysis_missing_symbols": [
      "SOLUSD",
      "XRPUSD",
      "XMRUSD",
      "XLMUSD",
      "ZECUSD"
    ],
    "deep_analysis_requested": 10,
    "deep_analysis_successful": 5,
    "discovery_requested": 10,
    "discovery_successful": 10,
    "failed": 5,
    "overall_scan_complete": false,
    "requested": 10,
    "successful": 5,
    "underlying_batch_report": {
      "errors": {},
      "failed": 0,
      "requested": 10,
      "successful": 10
    }
  },
  "schema": "atlas-ai-bridge-scan-v2",
  "side_by_side_order": {
    "available": false,
    "execution_authorized": false,
    "manual_user_execution_required": true,
    "match_trader": {
      "alias": null,
      "available": false,
      "direction": null,
      "entry": null,
      "estimated_stop_risk": null,
      "instrument": null,
      "lot_vol": null,
      "order_type": null,
      "risk_percent": null,
      "safe_loss": null,
      "sizing_error": "Translated Match-Trader trade plan unavailable.",
      "tp1": null,
      "tp2": null,
      "tp3": null,
      "translation_status": "no_frozen_trade_plan"
    },
    "match_trader_failure_blocks_tradelocker_order": false,
    "match_trader_required_for_decision": false,
    "match_trader_role": "price_cross_reference_and_order_translation_only",
    "primary_trade_source": "TradeLocker",
    "read_only": true,
    "tradelocker": {
      "available": false,
      "direction": null,
      "entry": null,
      "estimated_stop_risk": null,
      "instrument": null,
      "lot_vol": null,
      "order_type": null,
      "risk_percent": null,
      "safe_loss": null,
      "tp1": null,
      "tp2": null,
      "tp3": null
    }
  },
  "timezone": "UTC",
  "watch_advisory": {
    "alert_policy": "fresh_structural_triggers_only",
    "alerts": [],
    "fresh_watch_conditions": [
      {
        "alert_created": false,
        "alert_gate_reason": "Fresh WATCH analysis does not expose a complete, machine-testable structural price trigger with direction, confirmation condition, cancel level, and expiry. No alert is manufactured.",
        "decision": "WATCH",
        "execution_5m": {
          "candle_confirmed": true,
          "confirmed": false,
          "reason": "5M structure shifted, but momentum/candle confirmation is incomplete.",
          "rsi_14": 49.73,
          "rsi_confirmed": false,
          "structure_shift": true
        },
        "geometry": {
          "entry_quality": "late",
          "invalidation": 76980.6,
          "reward_to_risk": 0.49,
          "risk_distance": 273.0,
          "room_to_target": 132.79999999998836,
          "target_reference": 77386.4
        },
        "instrument": "BTCUSD",
        "reason": "The setup has not earned approval under current multi-horizon evidence."
      },
      {
        "alert_created": false,
        "alert_gate_reason": "Fresh WATCH analysis does not expose a complete, machine-testable structural price trigger with direction, confirmation condition, cancel level, and expiry. No alert is manufactured.",
        "decision": "WATCH",
        "execution_5m": {
          "candle_confirmed": true,
          "confirmed": false,
          "reason": "5M momentum is aligned, but a structural trigger is still missing.",
          "rsi_14": 34.87,
          "rsi_confirmed": true,
          "structure_shift": false
        },
        "geometry": {
          "entry_quality": "acceptable",
          "invalidation": 55.0,
          "reward_to_risk": 0.91,
          "risk_distance": 0.9299999999999997,
          "room_to_target": 0.8500000000000014,
          "target_reference": 53.22
        },
        "instrument": "DASHUSD",
        "reason": "The setup has not earned approval under current multi-horizon evidence."
      }
    ],
    "historical_monitor_alerts_excluded": true,
    "note": "The Bridge may return zero recommended alerts. A price level is not an alert merely because price could reach it. Until fresh analysis exposes a fully auditable structural trigger, Atlas should decide whether any alert is warranted.",
    "quality_gate": {
      "reject_duplicate_thesis_alerts": true,
      "requires_cancel_level": true,
      "requires_confirmation_condition": true,
      "requires_expiry": true,
      "requires_explicit_trigger_price": true,
      "requires_fresh_analysis": true,
      "requires_structural_meaning": true,
      "requires_trigger_direction": true,
      "speculative_price_alerts_forbidden": true
    },
    "recommended_alert_count": 0,
    "recommended_alerts": [],
    "source": "fresh_export_analysis",
    "zero_alerts_allowed": true
  },
  "workflow_snapshot": {
    "analysis_generated_at": "2026-09-13T20:01:39.382930+00:00",
    "analysis_snapshot_id": "atlas-analysis-7d9bd951abb847f1b9e23cb24dd689d6",
    "deep_analysis_missing_symbols": [
      "SOLUSD",
      "XRPUSD",
      "XMRUSD",
      "XLMUSD",
      "ZECUSD"
    ],
    "fresh_instrument_count": 5,
    "overall_scan_complete": false,
    "previous_frozen_trade_plan": null,
    "previous_monitor_context": null,
    "previous_monitor_context_is_historical": true,
    "previous_monitor_snapshot": null,
    "previous_monitor_snapshot_is_historical": true,
    "source": "fresh_export_analysis",
    "workflow_ready": false,
    "workflow_ready_requires_complete_deep_analysis": true
  }
}
```

## Final status

```json
{
  "completed_at": "2026-09-13T20:01:39.406347+00:00",
  "created_at": "2026-09-13T19:59:45.559293+00:00",
  "error": null,
  "filename": "Atlas_AI_Scan_Challenge_2026-09-13_20-01-39_UTC.json",
  "job_id": "797cafd5e5824800983644b0275154a8",
  "nickname": "Challenge",
  "status": "READY"
}
```
