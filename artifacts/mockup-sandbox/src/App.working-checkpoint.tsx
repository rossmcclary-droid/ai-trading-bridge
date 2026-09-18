import { useState } from "react";

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

type TradingSummary = {
  account: string;
  requested: number;
  successful: number;
  failed: number;
  errors: Record<string, string>;
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
