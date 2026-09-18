import { useEffect, useState } from "react";

type Order = {
  order_type: string;
  instrument: string;
  entry: number;
  safe_loss: number;
  take_profit_1: number;
  take_profit_2: number;
  grade: string;
  reason: string;
};

type Alert = {
  instrument: string;
  alert_level: number;
  meaning: string;
  alert_type: string;
  grade: string;
  state: string;
  bias: string;
};

type WatchItem = {
  instrument: string;
  grade: string;
  decision: string;
  state: string;
  bias: string;
  reason: string;
};

type TopCandidate = {
  instrument: string;
  score: number;
  grade: string;
  decision: string;
  state: string;
  bias: string;
  current_price: number | null;
  entry_quality: string;
  invalidation: number | null;
  target_reference: number | null;
  reward_to_risk: number | null;
  extension: string;
  "5m_confirmed": boolean;
  next_conditions: string[];
  satisfied_conditions: string[];
  reason: string;
};

type PendingSetup = {
  instrument: string;
  direction: string;
  status: string;
  entry_reference: number;
  safe_loss: number;
  tp1: number;
  tp2: number;
  rr_tp1: number | null;
  rr_tp2: number | null;
  requirements_remaining: string[];
  requirements_satisfied: string[];
};

type TradingSummary = {
  account: string;
  requested: number;
  successful: number;
  failed: number;
  errors: Record<string, string>;
  top_candidate: TopCandidate | null;
  pending_setup: PendingSetup | null;
  executable_orders: Order[];
  alerts: Alert[];
  watchlist: WatchItem[];
};

function Card({
  title,
  children,
}: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <section
      style={{
        background: "#151515",
        border: "1px solid #303030",
        borderRadius: 18,
        padding: 18,
      }}
    >
      <div
        style={{
          fontSize: 13,
          letterSpacing: 1,
          color: "#8f8f8f",
          marginBottom: 14,
        }}
      >
        {title}
      </div>
      {children}
    </section>
  );
}

function BiasBadge({ bias }: { bias: string }) {
  const bullish = bias === "bullish";
  const bearish = bias === "bearish";

  return (
    <span
      style={{
        borderRadius: 999,
        padding: "5px 9px",
        fontSize: 12,
        background: bullish
          ? "#14351f"
          : bearish
          ? "#3a1717"
          : "#292929",
        color: bullish
          ? "#8fe0a5"
          : bearish
          ? "#ffaaaa"
          : "#bbb",
      }}
    >
      {bias.toUpperCase()}
    </span>
  );
}

export default function App() {
  const [data, setData] = useState<TradingSummary | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [lastScan, setLastScan] = useState("");
  const [autoRefresh, setAutoRefresh] = useState(false);
  const [testState, setTestState] = useState<
    "LIVE" | "WATCH" | "PENDING" | "EXECUTABLE"
  >("LIVE");

  useEffect(() => {
    if (!autoRefresh) return;

    const timer = window.setInterval(() => {
      scanChallenge();
    }, 60000);

    return () => window.clearInterval(timer);
  }, [autoRefresh]);

  async function scanChallenge() {
    setLoading(true);
    setError("");

    try {
      const response = await fetch(
        "/api/scan/Challenge/trading-summary"
      );

      if (!response.ok) {
        throw new Error(`Scan failed: HTTP ${response.status}`);
      }

      const result: TradingSummary = await response.json();

      setData(result);
      setLastScan(new Date().toLocaleTimeString());
    } catch (err) {
      setError(
        err instanceof Error ? err.message : "Unable to run scan."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main
      style={{
        minHeight: "100vh",
        background: "#090909",
        color: "#f5f5f5",
        fontFamily: "system-ui, sans-serif",
        padding: "22px 16px 48px",
      }}
    >
      <div
        style={{
          maxWidth: 760,
          margin: "0 auto",
          display: "grid",
          gap: 16,
        }}
      >
        <header>
          <div
            style={{
              fontSize: 13,
              color: "#8d8d8d",
              letterSpacing: 0.8,
            }}
          >
            LIVE MARKET SCANNER
          </div>

          <h1
            style={{
              margin: "5px 0 0",
              fontSize: 30,
            }}
          >
            AI Trading Bridge
          </h1>
        </header>

        <Card title="ACCOUNT">
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              gap: 16,
            }}
          >
            <div>
              <div style={{ fontSize: 22, fontWeight: 700 }}>
                Challenge
              </div>
              <div
                style={{
                  color: "#8d8d8d",
                  marginTop: 4,
                }}
              >
                TradeLocker · Read-only
              </div>
            </div>

            <div
              style={{
                padding: "7px 11px",
                borderRadius: 999,
                background: "#14351f",
                color: "#8fe0a5",
                fontSize: 13,
              }}
            >
              Connected
            </div>
          </div>
        </Card>

        <button
          onClick={scanChallenge}
          disabled={loading}
          style={{
            border: 0,
            borderRadius: 15,
            padding: "17px 18px",
            fontSize: 17,
            fontWeight: 750,
            background: loading ? "#343434" : "#f2f2f2",
            color: loading ? "#aaa" : "#111",
          }}
        >
          {loading ? "Scanning markets..." : "Scan Challenge"}
        </button>

        <button
        onClick={() => setAutoRefresh((current) => !current)}
        style={{
          border: "1px solid #303030",
          borderRadius: 12,
          padding: "12px 14px",
          background: autoRefresh ? "#102517" : "#151515",
          color: autoRefresh ? "#8fe0a5" : "#c7c7c7",
          fontSize: 14,
          fontWeight: 700,
        }}
      >
        Auto-refresh: {autoRefresh ? "ON · every 60s" : "OFF"}
      </button>

      {loading && (
          <div
            style={{
              textAlign: "center",
              color: "#999",
              fontSize: 13,
            }}
          >
            Reading live 4H · 1H · 15M · 5M market data
          </div>
        )}

        {!loading && lastScan && (
          <div
            style={{
              textAlign: "center",
              color: "#888",
              fontSize: 13,
            }}
          >
            Last scan: {lastScan}
          </div>
        )}

        {error && (
          <Card title="ERROR">
            <div style={{ color: "#ff9d9d" }}>{error}</div>
          </Card>
        )}

        {data && (
          <>
            <Card title="TEST HARNESS">
            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(4, 1fr)",
                gap: 8,
              }}
            >
              {(["LIVE", "WATCH", "PENDING", "EXECUTABLE"] as const).map(
                (state) => (
                  <button
                    key={state}
                    onClick={() => setTestState(state)}
                    style={{
                      border: "1px solid #303030",
                      borderRadius: 10,
                      padding: "10px 6px",
                      background:
                        testState === state ? "#2b2b2b" : "#121212",
                      color:
                        testState === state ? "#ffffff" : "#8d8d8d",
                      fontSize: 11,
                      fontWeight: 700,
                    }}
                  >
                    {state}
                  </button>
                )
              )}
            </div>

            <div
              style={{
                marginTop: 9,
                color: "#777",
                fontSize: 11,
              }}
            >
              UI simulation only. Does not change backend state or place trades.
            </div>
          </Card>

          <Card title="TRADING STATE">
            {testState === "EXECUTABLE" ||
            (testState === "LIVE" && data.executable_orders.length > 0) ? (
              <div
                style={{
                  padding: "14px",
                  borderRadius: 14,
                  background: "#102517",
                  border: "1px solid #275a36",
                }}
              >
                <div
                  style={{
                    fontSize: 24,
                    fontWeight: 850,
                    color: "#8fe0a5",
                  }}
                >
                  EXECUTABLE
                </div>

                <div
                  style={{
                    marginTop: 6,
                    color: "#b9d8c1",
                    lineHeight: 1.45,
                  }}
                >
                  A setup has earned trade approval. Review the
                  executable order below.
                </div>
              </div>
            ) : testState === "PENDING" ||
              (testState === "LIVE" && data.pending_setup) ? (
              <div
                style={{
                  padding: "14px",
                  borderRadius: 14,
                  background: "#251f10",
                  border: "1px solid #5a4927",
                }}
              >
                <div
                  style={{
                    fontSize: 24,
                    fontWeight: 850,
                    color: "#e7c58a",
                  }}
                >
                  PENDING SETUP
                </div>

                <div
                  style={{
                    marginTop: 6,
                    color: "#d8c7a7",
                    lineHeight: 1.45,
                  }}
                >
                  {testState === "PENDING"
                    ? "SIMULATION LONG is armed and waiting for confirmation."
                    : `${data.pending_setup?.instrument} ${data.pending_setup?.direction} is armed but still waiting for remaining confirmation.`}
                </div>
              </div>
            ) : (
              <div
                style={{
                  padding: "14px",
                  borderRadius: 14,
                  background: "#151515",
                  border: "1px solid #303030",
                }}
              >
                <div
                  style={{
                    fontSize: 24,
                    fontWeight: 850,
                    color: "#bcbcbc",
                  }}
                >
                  WATCH
                </div>

                <div
                  style={{
                    marginTop: 6,
                    color: "#8d8d8d",
                    lineHeight: 1.45,
                  }}
                >
                  No trade is armed. Continue monitoring the strongest
                  candidates and alerts.
                </div>
              </div>
            )}
          </Card>

          {(testState === "PENDING" || testState === "EXECUTABLE") && (
            <Card title="SIMULATED ORDER TICKET">
              <div
                style={{
                  padding: "16px",
                  borderRadius: 14,
                  border: "1px solid #333",
                  background: "#101010",
                }}
              >
                <div
                  style={{
                    color: "#777",
                    fontSize: 11,
                    fontWeight: 800,
                    letterSpacing: 1,
                    marginBottom: 14,
                  }}
                >
                  TEST DATA · NOT A LIVE ORDER
                </div>

                <div
                  style={{
                    display: "grid",
                    gridTemplateColumns: "1fr 1fr",
                    gap: 10,
                  }}
                >
                  {[
                    ["ORDER TYPE", testState === "PENDING" ? "Pending" : "Active"],
                    ["INSTRUMENT", "SIMULATION"],
                    ["ENTRY", "100.00"],
                    ["SAFE LOSS", "99.00"],
                    ["TAKE PROFIT 1", "100.75"],
                    ["TAKE PROFIT 2", "101.50"],
                  ].map(([label, value]) => (
                    <div
                      key={label}
                      style={{
                        padding: "12px",
                        borderRadius: 10,
                        border: "1px solid #292929",
                      }}
                    >
                      <div
                        style={{
                          color: "#777",
                          fontSize: 10,
                          marginBottom: 6,
                        }}
                      >
                        {label}
                      </div>

                      <div
                        style={{
                          color: "#f2f2f2",
                          fontSize: 17,
                          fontWeight: 800,
                        }}
                      >
                        {value}
                      </div>
                    </div>
                  ))}
                </div>

                <div
                  style={{
                    marginTop: 14,
                    padding: "10px",
                    borderRadius: 9,
                    background: "#281313",
                    color: "#d99a9a",
                    fontSize: 12,
                    lineHeight: 1.4,
                  }}
                >
                  Simulation only. These prices must never be used as a
                  trading instruction.
                </div>
              </div>
            </Card>
          )}

          <Card title="SCAN STATUS">
              <div style={{ fontSize: 18, fontWeight: 700 }}>
                {data.successful}/{data.requested} markets scanned
              </div>
              <div
                style={{
                  marginTop: 5,
                  color: "#8d8d8d",
                }}
              >
                {data.failed === 0
                  ? "All requested markets returned successfully."
                  : `${data.failed} market scan(s) failed.`}
              </div>
            </Card>

            {data.top_candidate && (
              <Card title="TOP CANDIDATE">
                <div
                  style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    gap: 12,
                  }}
                >
                  <div>
                    <div
                      style={{
                        fontSize: 24,
                        fontWeight: 800,
                      }}
                    >
                      {data.top_candidate.instrument}
                    </div>

                    <div
                      style={{
                        marginTop: 5,
                        color: "#8d8d8d",
                        fontSize: 13,
                      }}
                    >
                      {data.top_candidate.state} · {data.top_candidate.grade}
                    </div>
                  </div>

                  <BiasBadge bias={data.top_candidate.bias} />
                </div>

                <div
                  style={{
                    marginTop: 16,
                    display: "flex",
                    alignItems: "baseline",
                    gap: 8,
                  }}
                >
                  <div
                    style={{
                      fontSize: 34,
                      fontWeight: 850,
                    }}
                  >
                    {data.top_candidate.score}
                  </div>

                  <div
                    style={{
                      color: "#777",
                      fontSize: 13,
                    }}
                  >
                    candidate score
                  </div>
                </div>

                <div
                  style={{
                    marginTop: 18,
                    display: "grid",
                    gridTemplateColumns: "1fr 1fr",
                    gap: 10,
                  }}
                >
                  {[
                    ["Price", data.top_candidate.current_price],
                    ["Entry quality", data.top_candidate.entry_quality],
                    ["Invalidation", data.top_candidate.invalidation],
                    ["Target", data.top_candidate.target_reference],
                    ["R:R", data.top_candidate.reward_to_risk],
                    ["Extension", data.top_candidate.extension],
                  ].map(([label, value]) => (
                    <div
                      key={String(label)}
                      style={{
                        background: "#101010",
                        border: "1px solid #2b2b2b",
                        borderRadius: 12,
                        padding: 11,
                      }}
                    >
                      <div
                        style={{
                          color: "#777",
                          fontSize: 11,
                          textTransform: "uppercase",
                          letterSpacing: 0.7,
                        }}
                      >
                        {label}
                      </div>

                      <div
                        style={{
                          marginTop: 5,
                          fontWeight: 700,
                          fontSize: 15,
                        }}
                      >
                        {value ?? "—"}
                      </div>
                    </div>
                  ))}
                </div>

                <div
                  style={{
                    marginTop: 14,
                    padding: "10px 12px",
                    borderRadius: 12,
                    background: data.top_candidate["5m_confirmed"]
                      ? "#102517"
                      : "#251b10",
                    color: data.top_candidate["5m_confirmed"]
                      ? "#8fe0a5"
                      : "#e7c58a",
                    fontSize: 13,
                  }}
                >
                  5M confirmation:{" "}
                  {data.top_candidate["5m_confirmed"]
                    ? "Confirmed"
                    : "Not confirmed"}
                </div>

                {(() => {
                  const blockers: string[] = [];

                  if (data.top_candidate.entry_quality === "late") {
                    blockers.push("late entry");
                  }

                  if (
                    data.top_candidate.reward_to_risk !== null &&
                    data.top_candidate.reward_to_risk < 1
                  ) {
                    blockers.push("weak R:R");
                  }

                  if (!data.top_candidate["5m_confirmed"]) {
                    blockers.push("5M not confirmed");
                  }

                  if (
                    data.top_candidate.extension === "extended" ||
                    data.top_candidate.extension === "highly_extended"
                  ) {
                    blockers.push("price extended");
                  }

                  if (data.top_candidate.state === "transitioning") {
                    blockers.push("multi-horizon transition");
                  }

                  if (blockers.length === 0) {
                    return null;
                  }

                  return (
                    <div
                      style={{
                        marginTop: 12,
                        padding: "11px 12px",
                        borderRadius: 12,
                        background: "#221313",
                        border: "1px solid #482020",
                        color: "#ffb0b0",
                        fontSize: 13,
                        lineHeight: 1.45,
                      }}
                    >
                      <strong>Why not a trade?</strong>
                      <div style={{ marginTop: 4 }}>
                        Blocked by: {blockers.join(" · ")}
                      </div>
                    </div>
                  );
                })()}

                {data.top_candidate.next_conditions.length > 0 && (
                  <div
                    style={{
                      marginTop: 12,
                      padding: "12px",
                      borderRadius: 12,
                      background: "#161616",
                      border: "1px solid #303030",
                    }}
                  >
                    <div
                      style={{
                        fontSize: 13,
                        fontWeight: 800,
                        marginBottom: 8,
                      }}
                    >
                      What needs to happen?
                    </div>

                    <div
                      style={{
                        display: "grid",
                        gap: 7,
                        color: "#d0d0d0",
                        fontSize: 13,
                        lineHeight: 1.45,
                      }}
                    >
                      {data.top_candidate.next_conditions.map((condition) => (
                        <div key={condition}>• {condition}</div>
                      ))}
                    </div>
                  </div>
                )}

                {data.top_candidate.satisfied_conditions.length > 0 && (
                  <div
                    style={{
                      marginTop: 12,
                      padding: "12px",
                      borderRadius: 12,
                      background: "#102017",
                      border: "1px solid #21452d",
                    }}
                  >
                    <div
                      style={{
                        fontSize: 13,
                        fontWeight: 800,
                        color: "#8fe0a5",
                        marginBottom: 8,
                      }}
                    >
                      Already satisfied
                    </div>

                    <div
                      style={{
                        display: "grid",
                        gap: 7,
                        color: "#b8d8c0",
                        fontSize: 13,
                        lineHeight: 1.45,
                      }}
                    >
                      {data.top_candidate.satisfied_conditions.map(
                        (condition) => (
                          <div key={condition}>✓ {condition}</div>
                        )
                      )}
                    </div>
                  </div>
                )}

                <div
                  style={{
                    marginTop: 14,
                    color: "#c4c4c4",
                    lineHeight: 1.5,
                  }}
                >
                  {data.top_candidate.reason}
                </div>

                <div
                  style={{
                    marginTop: 12,
                    color: "#777",
                    fontSize: 12,
                  }}
                >
                  Ranking indicates attention priority, not trade approval.
                </div>
              </Card>
            )}

            <Card title="PENDING SETUP">
              {data.pending_setup ? (
                <div>
                  <div
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      alignItems: "center",
                      gap: 12,
                    }}
                  >
                    <div>
                      <div
                        style={{
                          fontSize: 22,
                          fontWeight: 800,
                        }}
                      >
                        {data.pending_setup.instrument}
                      </div>

                      <div
                        style={{
                          marginTop: 4,
                          color: "#8d8d8d",
                          fontSize: 13,
                        }}
                      >
                        {data.pending_setup.direction} · {data.pending_setup.status}
                      </div>
                    </div>
                  </div>

                  <div
                    style={{
                      marginTop: 16,
                      display: "grid",
                      gridTemplateColumns: "1fr 1fr",
                      gap: 10,
                    }}
                  >
                    {[
                      ["Entry", data.pending_setup.entry_reference],
                      ["Safe Loss", data.pending_setup.safe_loss],
                      ["TP1", data.pending_setup.tp1],
                      ["TP2", data.pending_setup.tp2],
                      ["R:R TP1", data.pending_setup.rr_tp1],
                      ["R:R TP2", data.pending_setup.rr_tp2],
                    ].map(([label, value]) => (
                      <div
                        key={String(label)}
                        style={{
                          background: "#101010",
                          border: "1px solid #2b2b2b",
                          borderRadius: 12,
                          padding: 11,
                        }}
                      >
                        <div
                          style={{
                            color: "#777",
                            fontSize: 11,
                            textTransform: "uppercase",
                          }}
                        >
                          {label}
                        </div>

                        <div
                          style={{
                            marginTop: 5,
                            fontWeight: 700,
                          }}
                        >
                          {value ?? "—"}
                        </div>
                      </div>
                    ))}
                  </div>

                  {data.pending_setup.requirements_remaining.length > 0 && (
                    <div
                      style={{
                        marginTop: 12,
                        color: "#d8b27b",
                        fontSize: 13,
                        lineHeight: 1.5,
                      }}
                    >
                      {data.pending_setup.requirements_remaining.map((item) => (
                        <div key={item}>○ {item}</div>
                      ))}
                    </div>
                  )}

                  {data.pending_setup.requirements_satisfied.length > 0 && (
                    <div
                      style={{
                        marginTop: 12,
                        color: "#8fe0a5",
                        fontSize: 13,
                        lineHeight: 1.5,
                      }}
                    >
                      {data.pending_setup.requirements_satisfied.map((item) => (
                        <div key={item}>✓ {item}</div>
                      ))}
                    </div>
                  )}
                </div>
              ) : (
                <div>
                  <div
                    style={{
                      fontSize: 20,
                      fontWeight: 700,
                    }}
                  >
                    None armed.
                  </div>

                  <div
                    style={{
                      marginTop: 6,
                      color: "#8d8d8d",
                      lineHeight: 1.5,
                    }}
                  >
                    The top candidate has not yet produced valid trade geometry.
                  </div>
                </div>
              )}
            </Card>

            <Card title="EXECUTABLE ORDERS">
              {data.executable_orders.length === 0 ? (
                <div>
                  <div
                    style={{
                      fontSize: 20,
                      fontWeight: 700,
                    }}
                  >
                    No trade yet.
                  </div>
                  <div
                    style={{
                      color: "#8d8d8d",
                      marginTop: 6,
                    }}
                  >
                    No setup currently meets the executable threshold.
                  </div>
                </div>
              ) : (
                <div style={{ display: "grid", gap: 12 }}>
                  {data.executable_orders.map((order) => (
                    <div
                      key={order.instrument}
                      style={{
                        border: "1px solid #275a36",
                        background: "#102517",
                        borderRadius: 14,
                        padding: 15,
                      }}
                    >
                      <div
                        style={{
                          fontSize: 20,
                          fontWeight: 800,
                          marginBottom: 10,
                        }}
                      >
                        {order.instrument}
                      </div>

                      <div>Entry: {order.entry}</div>
                      <div>Safe Loss: {order.safe_loss}</div>
                      <div>Take Profit 1: {order.take_profit_1}</div>
                      <div>Take Profit 2: {order.take_profit_2}</div>
                    </div>
                  ))}
                </div>
              )}
            </Card>

            <Card title={`ALERTS · ${data.alerts.length}`}>
              {data.alerts.length === 0 ? (
                <div style={{ color: "#999" }}>No active alerts.</div>
              ) : (
                <div style={{ display: "grid", gap: 12 }}>
                  {data.alerts.map((alert) => (
                    <div
                      key={`${alert.instrument}-${alert.alert_level}`}
                      style={{
                        border: "1px solid #303030",
                        borderRadius: 14,
                        padding: 15,
                        background: "#101010",
                      }}
                    >
                      <div
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                          alignItems: "center",
                          gap: 10,
                        }}
                      >
                        <div
                          style={{
                            fontSize: 20,
                            fontWeight: 800,
                          }}
                        >
                          {alert.instrument}
                        </div>

                        <BiasBadge bias={alert.bias} />
                      </div>

                      <div
                        style={{
                          fontSize: 27,
                          fontWeight: 800,
                          marginTop: 12,
                        }}
                      >
                        {alert.alert_level}
                      </div>

                      <div
                        style={{
                          color: "#aaa",
                          marginTop: 6,
                          lineHeight: 1.45,
                        }}
                      >
                        {alert.meaning}
                      </div>

                      <div
                        style={{
                          marginTop: 10,
                          color: "#727272",
                          fontSize: 12,
                        }}
                      >
                        {alert.state} · {alert.grade}
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </Card>

            <Card title={`WATCHLIST · ${data.watchlist.length}`}>
              {data.watchlist.length === 0 ? (
                <div style={{ color: "#999" }}>
                  No additional markets waiting for confirmation.
                </div>
              ) : (
                <div style={{ display: "grid", gap: 12 }}>
                  {data.watchlist.map((item) => (
                    <div
                      key={item.instrument}
                      style={{
                        border: "1px solid #303030",
                        borderRadius: 14,
                        padding: 15,
                        background: "#101010",
                      }}
                    >
                      <div
                        style={{
                          display: "flex",
                          alignItems: "center",
                          justifyContent: "space-between",
                          gap: 10,
                        }}
                      >
                        <div
                          style={{
                            fontSize: 20,
                            fontWeight: 800,
                          }}
                        >
                          {item.instrument}
                        </div>

                        <BiasBadge bias={item.bias} />
                      </div>

                      <div
                        style={{
                          marginTop: 8,
                          color: "#8d8d8d",
                          fontSize: 13,
                        }}
                      >
                        {item.state} · {item.decision}
                      </div>

                      <div
                        style={{
                          marginTop: 10,
                          color: "#c7c7c7",
                          lineHeight: 1.5,
                        }}
                      >
                        {item.reason}
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </Card>
          </>
        )}
      </div>
    </main>
  );
}
