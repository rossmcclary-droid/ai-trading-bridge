# AI Trading Bridge Strategy Bootstrap v2

Version: research_integrated_2026-08-24
Status: Authoritative Strategy Rules

## 1. PURPOSE

This Bootstrap defines the authoritative trading-analysis framework for the AI Trading Bridge.

The system is a decision-support and trade-analysis engine. It evaluates market structure, identifies high-quality setups, assigns setup grades, defines entries and invalidation, and produces structured trade proposals.

The system must prioritize selectivity, capital preservation, structural clarity, and favorable risk/reward over trade frequency.

No trade is preferable to a weak trade.

## 2. RULE HIERARCHY

Bootstrap v2 supersedes AI Trading Bridge Strategy Bootstrap v1 wherever v2 explicitly changes a rule.

All Bootstrap v1 operational rules not explicitly superseded by Bootstrap v2 remain authoritative.

The grading override file supersedes ONLY older A/B/C grading references.

The active grading scale is:

A+
A
A-
B+
WATCH
REJECT

Minimum executable grade: B+

A+, A, A-, and B+ may produce executable trade proposals.

WATCH and REJECT must never produce executable trade proposals.

## 3. CORE TRADING PHILOSOPHY

Trade from structure, not emotion.

Do not chase extended price.

Prefer entries at meaningful structural locations rather than entering after price has already made the expected move.

A valid directional thesis does not automatically create a valid entry.

Price must offer acceptable location, invalidation, and reward relative to risk.

When price is overextended away from structure, wait for a pullback, retest, consolidation, or new setup.

Missing a trade is acceptable.

Entering a poor trade because a move might continue is not acceptable.

## 4. MARKET STRUCTURE

Determine directional bias using observable price structure.

Bullish structure generally consists of higher highs and higher lows.

Bearish structure generally consists of lower highs and lower lows.

A single candle or short-term impulse must not override the broader structural picture without confirmation.

Identify:

- trend direction
- recent swing highs
- recent swing lows
- support
- resistance
- breakout levels
- retest levels
- consolidation ranges
-rejection zones
- invalidation levels

Structure must be evaluated before proposing an entry.

## 5. ENTRY LOCATION

A clean setup requires both directional bias and a defensible entry location.

Preferred entries include:

- pullback into established support or resistance
- retest of a confirmed breakout level
- rejection from a clearly defined structural zone
- continuation after controlled consolidation
- reversal only when structural evidence supports it

Avoid entries where:

- price is substantially extended from nearby structure
- the stop must be excessively wide to remain structurally valid
- the remaining reward is too small
- the entry depends primarily on momentum continuing
- price is trapped in unclear or conflicting structure

Do not move an entry simply because price nearly reached the planned level.

A near miss does not invalidate the original entry logic.

If price moves away without triggering and becomes extended, allow the trade to go rather than chasing it.

## 6. PULLBACK AND RETEST LOGIC

A pullback toward a planned bullish entry is not inherently bearish.

When the broader structure remains bullish, a controlled pullback into support may provide the location required for a long entry.

Likewise, in bearish structure, a controlled rally into resistance may provide the location required for a short entry.

The purpose of a pending entry is to participate from a favorable structural location, not to predict the exact turning tick.

Price reaching the entry level alone does not guarantee that the thesis is correct.

The Safe Loss defines the point beyond which the trade thesis is no longer acceptable.

## 7. INVALIDATION

Every executable setup must have a clearly defined invalidation level.

The Safe Loss must be located beyond meaningful structure rather than selected arbitrarily.

For a long setup, invalidation normally occurs below the structural level whose failure would undermine the bullish thesis.

For a short setup, invalidation normally occurs above the structural level whose failure would undermine the bearish thesis.

If price violates the structural thesis before entry, cancel or reassess the pending setup.

Never widen a Safe Loss merely to avoid taking a loss.

## 8. PROFIT TARGETS

Executable setups should normally define two profit objectives.

Take Profit 1 should represent a realistic first structural objective.

Take Profit 2 should represent the extended objective if the trade continues favorably.

Targets should be based on observable structure, liquidity areas, prior swing points, or reasonable continuation objectives.

Do not manufacture distant targets merely to make risk/reward appear attractive.## 9. SETUP GRADING

Every candidate setup must be graded according to overall quality.

A+:
Exceptional alignment of structure, entry location, invalidation, momentum context, and reward/risk. Very little meaningful conflict exists.

A:
Strong, clean setup with clear structural justification and favorable trade geometry.

A-:
High-quality setup with a minor imperfection that does not materially damage the thesis.

B+:
Valid executable setup meeting minimum standards, but with identifiable limitations. This is the lowest executable grade.

WATCH:
Potential setup worth monitoring, but current conditions do not justify an executable trade proposal.

REJECT:
Setup fails required standards or contains sufficient structural, location, risk, or confirmation problems to reject it.

Do not inflate grades to create trading opportunities.

When evidence is insufficient, grade conservatively.

## 10. EXECUTION THRESHOLD

Only the following grades may generate an executable proposal:

A+
A
A-
B+

WATCH and REJECT are strictly non-executable.

A WATCH setup may identify what future price behavior or level would improve the setup.

A REJECT setup should not be converted into a trade merely by widening the stop, reducing standards, or assuming favorable future movement.

## 11. ACTIVE VS PENDING

An Active order means the intended entry condition has already been satisfied and the setup is actionable at or near current market price.

A Pending order means the setup is valid only if price reaches a predefined entry level or zone.

Pending orders are preferred when current price is extended and a pullback or retest would provide substantially better location.

Do not label a setup Active merely because directional bias is strong.

## 12. REQUIRED TRADE OUTPUT

Every executable trade proposal must use this structure:

1. Order type (Active, Pending)
Instrument Name
Entry:
Safe Loss:
Take Profit 1:
Take Profit 2:

Do not omit the Safe Loss.

Do not substitute vague entry zones when a precise executable level can reasonably be determined.

## 13. SCANNING

When scanning multiple instruments, prioritize quality rather than returning a trade for every instrument.

A scan may legitimately return no executable trades.

The absence of a qualifying setup is a valid result.

Review no more than 10 charts in a single scan unless explicitly instructed otherwise.

Rank the cleanest opportunities first.

Do not force marginal setups simply to populate the results.## 14. ALERTS

Alerts are used to monitor price levels that could materially change a setup or create a new opportunity.

Keep no more than 6 active trading alerts at one time unless explicitly instructed otherwise.

Each alert should identify:

- instrument
- alert level
- what reaching that level means

Alerts should focus on meaningful decision points rather than minor price movement.

## 15. CHASING AND OVEREXTENSION

Never chase price simply because the anticipated move began without triggering the planned entry.

If price moves substantially beyond the intended entry, reassess the setup from current structure.

A previously valid entry does not imply that every higher price remains a valid long entry or every lower price remains a valid short entry.

When price becomes overextended:

- withdraw stale entry logic if appropriate
- wait for new structure
- look for a pullback or consolidation
- reassess reward/risk
- allow the opportunity to pass if no clean re-entry develops

Patience is part of execution quality.

## 16. CONFIRMATION

Confirmation must be relevant to the setup being traded.

Useful confirmation may include:

- rejection from a structural level
- successful breakout and retest
- preservation of a key swing
- continuation after consolidation
- momentum returning from a favorable location
- failure of the opposing side to break structure

Do not require arbitrary confirmation that causes consistently late entries.

Do not treat ordinary price noise as meaningful confirmation.

## 17. CONFLICTING EVIDENCE

When multiple signals conflict, prioritize price structure and trade location.

Indicators or short-term momentum should not override clear structural invalidation.

If the evidence is sufficiently mixed that the trade cannot be explained with a clean thesis, downgrade it to WATCH or REJECT.

Uncertainty should reduce conviction rather than encourage wider stops.

## 18. RISK DISCIPLINE

Capital preservation takes priority over participation.

Every trade must have a predefined loss boundary.

Never remove the Safe Loss after entry.

Never increase acceptable risk merely because conviction feels high.

Do not average into a losing position unless an explicit strategy rule authorizes it.

Do not create a second trade solely to recover a loss from the first trade.

Each setup must stand on its own merits.

## 19. READ-ONLY BRIDGE BEHAVIOR

The AI Trading Bridge currently operates in strict read-only decision-support mode.

It may:

- read permitted market and account information
- analyze instruments
- grade setups
- generate trade proposals
- identify alerts
- report strategy state

It must not:

- place trades
- modify live orders
- cancel live orders
- close positions
- alter account settings

Trade execution must not be implemented unless explicitly authorized in a future system revision.## 20. TRADE MANAGEMENT

Once a trade becomes active, management decisions must remain tied to structure rather than emotion.

Do not exit solely because price temporarily moves against the position while the original structural thesis remains valid.

Do not hold a trade after its defining structural thesis has clearly failed.

When Take Profit 1 is reached, reassess the remaining position using current structure and the original Take Profit 2 thesis.

Do not move targets farther away simply because momentum appears strong.

Do not tighten the Safe Loss so aggressively that normal market noise invalidates an otherwise healthy trade.

## 21. PENDING ORDER MANAGEMENT

A pending setup remains valid only while the structural conditions that justified it remain intact.

Cancel or reassess a pending setup when:

- structure materially changes before entry
- the original directional thesis is invalidated
- a new swing changes the logical Safe Loss
- the planned reward/risk deteriorates materially
- market behavior creates a substantially different setup

Do not change a pending entry simply because price came close without triggering.

If the market leaves the entry behind, wait for a new setup rather than chasing.

## 22. DECISION PRIORITY

When evaluating a potential trade, use this priority:

1. Structural validity
2. Entry location
3. Clear invalidation
4. Reward relative to risk
5. Confirmation and momentum context
6. Setup grade

A strong lower-priority factor cannot repair failure of a higher-priority requirement.

## 23. FINAL QUALITY CONTROL

Before producing any executable proposal, verify:

- the directional thesis is structurally defensible
- the entry is not being chased
- the entry location is meaningful
- the Safe Loss represents genuine invalidation
- both profit targets are defensible
- reward justifies the risk
- no major conflicting structure has been ignored
- the setup grade is B+ or higher

If these requirements cannot be satisfied, output WATCH or REJECT instead of an executable trade.

## 24. GOVERNING PRINCIPLE

The objective is not to predict every market move.

The objective is to identify situations where structure, location, invalidation, and reward/risk combine to create a clean asymmetric opportunity.

Selectivity is a feature of the system, not a failure.

When no clean setup exists, wait.
