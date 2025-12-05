PTDT-OS v3.0 — Safety State Machine Specification (Public Reference)
This document defines the official PTDT-OS safety state machine.
Every domain and every kernel step must pass through these states.
This is the “constitution” of the entire system.
1. Overview
PTDT-OS enforces a unified safety state machine across all domains (ROAD, AI, QUANTUM, BRAIN, ROBOTICS, BIOSAFETY, AUTONOMY, ANY FUTURE DOMAIN).
The state machine ensures:
• deterministic transitions
• predictable throttling behavior
• consistent global veto conditions
• cross-domain alignment
• auditability in post-mortem analysis
All PTDT implementations (vendor or open-source) must conform to this.
2. The Four States
STATE 0 — SAFE
The system is operating within nominal divergence bounds.
Throttling = 1.0 (full capability).
No cross-domain alarms.
STATE 1 — CAUTION
Divergence rising beyond expected envelope.
Throttling = 0.4 to 0.8 depending on domain rules.
Operator awareness required.
System logs elevated.
STATE 2 — DANGER
Divergence exceeds safe operating window OR derivative spike detected.
Throttling = 0.1 to 0.4.
Autonomy may be partially suspended.
If multiple domains enter DANGER simultaneously, the kernel considers escalation.
STATE 3 — CATASTROPHIC
Irreversible threshold.
Immediate GLOBAL VETO.
Throttling = 0.0.
All domains enter safe state.
Cryptographically signed event emitted.
Human intervention mandatory.
3. State Transition Rules
SAFE → CAUTION
If delta >= safe_threshold
OR delta_rate >= caution_derivative
OR anomaly_score triggers caution signal.
CAUTION → DANGER
If delta >= danger_threshold
OR delta_rate >= panic_derivative
OR cross-domain conflict detected.
DANGER → CATASTROPHIC
If delta >= catastrophic_threshold
OR delta_rate >= catastrophic_derivative
OR domain reports structural failure
OR kernel detects inconsistent temporal trajectories.
CAUTION → SAFE
If delta returns below caution threshold
AND derivative stabilizes
AND no anomalies remain.
DANGER → CAUTION
If delta drops significantly
AND derivative negative for sustained period
AND operator acknowledges.
CATASTROPHIC → SAFE
Never automatic.
Requires explicit cryptographically signed human reset.
4. Global Veto Triggers
Catastrophic divergence (delta >= 0.95).
Derivative spike beyond catastrophic bound.
Cryptographic failure or tampering detection.
Kernel reports inconsistent Merkle chain.
Multiple domains reporting DANGER simultaneously.
Domain crash, silence, or malformed report.
Operator manual override.
Each veto is cryptographically signed and stored in the immutable PTDT-OS ledger.
5. Kernel Integration Requirements
Every domain adapter must produce:
delta (float)
delta_rate (float)
state (enum)
throttle (float)
timestamp (float)
optional meta fields
Kernel must:
aggregate states
determine global worst-case
compute global throttle
update Merkle root
enforce veto conditions
emit signed event
6. Deterministic Behavior Guarantees
No silent transitions
No ambiguous states
No probabilistic veto
No unsupervised recovery from catastrophic
Every event cryptographically signed
Every step forward-chained via Merkle hashing
Every domain treated as first-class, equal-weight safety source
7. Required for Certification
This state machine spec is part of:
PTDT-OS Safety Standard
Vendor Certification Audit
Regulatory Submission Package
Interoperability Requirements
PTDT-Kernel Compliance Tests




Any vendor building a PTDT adapter MUST implement this exact state machine definition.
