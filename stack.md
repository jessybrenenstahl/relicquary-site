# AIM: governed autonomy, built on Relicquary

*Machine-readable Markdown of https://relicquary.com/stack.html*

# Relicquary is the core. AIM is Relicquary writ large, given hands, and the discipline to prove every move.

**Relicquary** (v0.9.0) is the runnable core: durable, local-first, receipt-bound memory **plus orchestration**: the cognitive OS an agent thinks out of. **AIM** wraps that same core in a **deterministic floor you can verify**: limits on what it may do, a receipt for what it did, and only then gives it a body and a voice.

Relicquary runs today. AIM is a working prototype; the autonomy it aims toward is research ahead of us, and we mark that line, not blur it.

relicquary · mystore runs today

\$relicquary remember mystore "decided: ship local-first"

✓ stored decision · receipt written · indexed

\$relicquary recall mystore "what did we decide?"

→ ranked, dated, explainable, from your own store

\$relicquary mcp-server

✓ listening · memory + orchestration, served over MCP

**One Rust binary** SQLite + Markdown **on your disk** **A receipt** for every mutation Your model: **local or your own provider**

01 / WHAT WE BUILD TO

## One company, one discipline.

A cognitive OS, an operator, a touch driver, a control stack, held together by three commitments that show up in the code, not just the copy.

### Sovereign by construction

Your store lives on your disk: no hosted service, no telemetry. And the model is your choice: run it fully local, or connect your own provider account (you bring the OAuth). Either way, your data and audit trail stay yours.

your machine · your files

### Bounded, not unsupervised

Exactly one action per tick, through one audited chokepoint, behind a fail-safe fence. A deterministic conscience can halt a degenerate loop. Destructive, irreversible actions are retained by the human by design.

one chokepoint · one conscience

### Receipt-bound honesty

No capability exists until a receipt backs it. If a proof didn't run, the system says so; never a green result a verifier didn't confirm. We publish honest NULLs. **A result only counts when it survives a test it could have failed.**

receipts over rhetoric

02 / THE PRODUCTS

## Start with the core.

Relicquary is the core, and it runs today. TouchLink is a virtual touchscreen driver you can use on its own, or fold into a stack, the way AIM does.

Runnable today · v0.9.0

### Relicquary: the cognitive OS for AI agents

A local-first cognitive operating system in a single Rust binary. Durable typed memory and a knowledge graph, **plus the orchestration an agent works out of** (what to do next, synthesis, handoff, continuity across sessions), all under receipt-bound governance, as SQLite and Markdown on your own disk. It's the core the rest of the stack is built from. Build it, init a store, and serve it to any MCP-compatible agent today.

[Explore Relicquary](index.html)

recall **"what did we decide about storage?"**

current

**Decision:** Ship local-first: SQLite + Markdown on the operator's own disk.

kind: *decision* trust: *verified* confidence: *0.9* edges: *supersedes ×1*

lexical (BM25).86

semantic.92

currentness.98

[](touchlink.html)

### TouchLink: a virtual touchscreen driver

Working prototype

On its own, it makes a USB touchscreen on a Mac behave like a touchscreen: taps land where you touch, and your mouse stays a mouse. Folded into a stack, it becomes a programmable control surface, the way AIM uses it to drive a workspace by touch.

Explore TouchLink

03 / THE FLAGSHIP

## AIM: an autonomous operator on a floor you can verify.

**AIM: Accurate, Immediate, Minimal; AGRO in motion.** Relicquary writ large: the cognitive core given hands and a voice, aimed at autonomy you can audit.

What sets AIM apart is its floor: a deterministic, receipt-checkable layer that decides what an autonomous agent is *allowed* to do, and proves what it *did*. The floor isn't another model second-guessing the first: **it's mechanism**. Because it's deterministic and receipt-checkable, you can verify the property rather than take it on faith.

aim · one governed tick bounded

perceiveread desktop state **+** recall prior capability

planmodel proposes **one** action · read-only sandbox

consciencedeterministic checks · halt & correct, then continue

actone audited chokepoint · behind a fail-safe fence

verifyreceipt written · no proof ran → it says so

remembercapability persisted **→** Relicquary

**How the loop is governed.** The runtime is a *perceive → plan → execute* loop. The contribution is what wraps it: deterministic limits on what the loop may do, one governed chokepoint every action passes through, and a receipt for every action it takes. A floor you can audit.

**What it's done when run, not only designed.** In real trial runs, the deterministic conscience has caught degenerate loops (fixation, no-op churn) and corrected them rather than crashing. And the capability-reuse path recalled a banked capability and re-applied it across **8 of 8 held-out trials**, on novel instances it hadn't seen. Outcomes from actual runs, each stated at its scope: the record, not a promise.

04 / THE DETERMINISTIC FLOOR

## A floor you can verify, not take on faith.

Five mechanisms, none of them another model's opinion. They hold whether or not the brain behaves.

The floor is mechanism, so it holds even when the models agree.

### FLOOR_01 · One actuation chokepoint

Exactly one place where the agent acts on the world, governed and inspectable, not scattered tool calls. A standard agent is a loop wired to many tools, with many places intent becomes effect; AIM has one. That single gate is the structural break from while-loop-plus-tools.

### FLOOR_02 · A fail-safe fence

The chokepoint sits behind a hard boundary that blocks catastrophic operations outright, independent of what the model decides. The safe state is the default; the agent is never trusted past the fence for those operations.

### FLOOR_03 · A deterministic conscience

Not a second model grading the first: rule-based checks (we call them theodicytes) that can halt the agent on fixation, on no-op churn, or on an ungrounded assertion. The judgment is mechanism, and a halt is correct-and-continue, not a crash.

### FLOOR_04 · Receipt-bound actions

Every mutation emits an append-only receipt. Actions aren't just claimed in the agent's narration; each leaves a record you can audit independently, after the fact, without trusting how the agent described what it did.

### FLOOR_05 · An untrusted-memory model

Everything the agent writes to memory is untrusted by default and carries its provenance. Trust is earned through governance, never assumed because the model said so: the same discipline that makes Relicquary's memory auditable, applied to an operator that acts.

05 / THE FULL STACK

## Relicquary, writ large.

One core, embodied. Relicquary is the cognitive OS at the center; AIM wraps it in the floor above, then gives it organs. Each part is graded for where it actually stands.

**AGRO: the soil.** The name is both an acronym and an older root: *Always Growing Recursive Optimizer*, and *agros*, cultivated ground. AGRO is the plot the cognitive core is planted in: a loop given work, fed back its own results, and tended turn after turn so capability can take root. The discipline is soil-first: nothing is harvested early. A capability is real only once it survives a held-out test it has never seen. That destination is what the present-tense work aims toward: the ambition of the stack, stated plainly, not a feature claimed today.

THE CORE

runs today · v0.9.0 · Relicquary: memory + orchestration

The cognitive OS the whole stack thinks out of: durable typed memory, a knowledge graph, recall, and the orchestration of the working loop, under receipt-bound governance. [Standalone →](index.html)

THE DRIVE

working prototype · AGRO: planning loop

Proposes one action, runs it bounded, verifies it against receipts, checkpoints, repeats. It plans; it never actuates directly.

THE BODY

working prototype · The operator substrate

The Rust substrate that runs a model as a persistent operator, and carries the one audited actuation chokepoint behind the fence.

THE CONSCIENCE

working prototype · Ultimentality: the doctrine

The bounding doctrine made executable: the deterministic detectors that halt and correct a degenerate loop. The only part that can halt.

THE HANDS

working prototype · AI Control Stack + TouchLink

How the operator touches a real machine: a local command bus of explicit, named adapters that return verifiable results, plus TouchLink's focus-preserving touch surface.

THE DRIVER

external · swappable · The brain: a hosted model

A capable frontier model drives the loop from outside, plan-only. It has no weights we can touch, so it never improves itself; it authors capability *into* AIM. Swappable by design.

06 / HOW IT GROWS

## The brain never grows. The stack accumulates.

The brain is a model whose weights we don't touch, so it never trains on your use. Capability accumulates in the stack instead. Here is exactly where it can live, and how we hold the line on what counts.

WORKS TODAY

reuse · 8/8 held-out · Reuse

Hit an obstacle whose signature it has seen, and AIM recalls the durable capability it already stored (a tool, a procedure, a receipted artifact) and re-applies it. The capability-reuse path passed all 8 of 8 held-out trials, on novel instances, not memorized ones.

OPEN FRONTIER

unbuilt · gated · Synthesis

The next phase is capability **synthesis**: authoring a genuinely new durable capability for a blocker it has **never seen**, gated behind a hard held-out test. Clearing a blocker is the entry ticket, not the verdict: a capability is real only once it passes a held-out execution on a novel instance. Model opinions don't count; only the test does.

**The stack accumulates what the brain authors:** receipt-bound capability written as it hits friction, capability that re-applies through the same governed chokepoint as any other action. In one milestone run, the operator drove a real build-repair task down to a handful of compile errors and authored the fix itself: **bounded, receipted work under governance**. The model itself does not change. DPACA: two-model cross-audit · on the roadmap

07 / THE ROAD AHEAD

## Memory you own, becoming an operator you can trust.

Every capable agent eventually hits the same wall: it forgets. We're building the other way: a foundation that remembers on your terms, governed so every move can be checked. The core runs today; the destination is an autonomous system whose every action leaves a receipt.

MOVE_01

runs today · Relicquary: memory you own

A single Rust binary, CLI and MCP, with your memory living as SQLite and Markdown on your own disk. Typed memory, a linked knowledge graph, local search and reranking; nothing routes through a model provider. Writes are untrusted by default, every mutation leaves a receipt, and it already reuses capability it has stored, demonstrated by passing 8 of 8 held-out trials on a capability it had banked before, not memorized. The foundation everything else stands on.

MOVE_02

App Store · soon · The apps: Relicquary for everyone

The same local-first core is coming to Mac and iPhone through the Apple App Store: a one-time purchase, no subscription. Your memory stays on your devices and in your hands. The durable memory that has lived on the command line becomes something anyone running capable agents can buy once and own outright.

MOVE_03

working prototype · AIM: a deterministic floor

AIM wraps Relicquary in governance. A single actuation chokepoint, a fail-safe fence, and three non-terminal conscience checks mean a questionable move is held and corrected rather than silently executed: a floor that holds even when a model is confident it's right. This is how a memory system becomes an operator you can let act: bounded, auditable, answerable for every step.

MOVE_04

on the roadmap · Cross-audit: reliability by design

DPACA puts two models in a four-eyes arrangement (one proposes, the other only approves or rejects) behind a deterministic, hash-bound publish step. Its purpose is reliability, not magic: to make it far harder for a single confident model to push a mistake through. Named here as direction, built toward acceptance gates, not something already shipping.

THE DESTINATION

open frontier · AGRO: the soil it all grows toward

AGRO is the soil: cultivated ground, *Always Growing Recursive Optimizer*. The destination is an autonomous system that can be trusted to act because every move is auditable down to the receipt. The stack accumulates receipt-bound capability: capability it can carry and reuse, with provenance attached. The hard, open frontier is capability **synthesis**: a genuinely new capability for a problem the system has never seen. That is unbuilt research, and we say so plainly. It is the work ahead, and it is the whole point. **AGRO in motion: Accurate, Immediate, Minimal.**

**Owned, local, and accountable, by construction.** Your memory stays on your hardware. The operator acts only through a chokepoint it can't route around, and it shows its work. We'd rather ship a smaller floor that holds than a larger promise that doesn't. Build on the core today; grow into the rest as it earns its place.

08 / MATURITY

## Every claim, graded.

So the credibility gradient is visible at a glance: what runs, what's prototype, what's research, what's only designed.

#### Runs today

- **Relicquary v0.9.0**: memory + orchestration, CLI + MCP
- **The deterministic floor** (chokepoint, fence, conscience), built & tested
- **Capability reuse**: 8/8 held-out

#### Working prototype

- **AGRO** planning loop
- **Operator substrate**: persistent operator + chokepoint
- **TouchLink** (one verified device)
- **AI Control Stack** (single machine)

#### Open research

- **Capability synthesis**: a new capability from a never-seen blocker; held-out test unbuilt

#### Designed, not built

- **DPACA** two-model cross-audit
- **Durable backup/restore**: memory is volatile today
- **Signed, distributable** apps & Relicquary v1.0

09 / RQ MCP LLC

## Autonomy you can actually audit.

RQ MCP LLC builds Relicquary (the local-first cognitive OS) and AIM, the governance architecture that turns it into a verifiable operator. Every capability is receipt-bound, and a result only counts when it survives a test it could have failed. The core runs today; the Mac and iPhone apps are coming to the App Store as a one-time purchase, no subscription.

> “Agents forget. Every autonomous system we ran reset to zero between sessions: repeating mistakes, losing the context it had earned, asking us to trust actions we couldn't check afterward. The conviction was simple: memory and accountability aren't features you bolt on later; they're the floor everything else stands on. So we built the floor first. The core runs today on your own machine: one binary, your disk, a receipt for every action. That's the standard I want to be held to.” Jessy Brenenstahl, Founder, RQ MCP LLC
