# AIM: the full stack that acts, on a verifiable floor

*Machine-readable Markdown of https://relicquary.com/stack.html (content hash fe0085e8)*

# Relicquary is the core. AIM is the full stack that acts on it.

**Relicquary** (v0.9.0) is the runnable core: durable, local-first, receipt-bound memory **plus orchestration**, the memory OS an agent thinks out of. **AIM** is the full stack around it: an operator that perceives the screen, plans, and drives a real computer, everything it knows drawn from that memory. Every action it takes passes through a **floor you can verify**.

Relicquary runs today. AIM is a working prototype, graded part by part in the maturity map below: what runs, what is prototype, what is still research. We mark the line, we do not blur it.

relicquary · mystore runs today

\$relicquary remember mystore "decided: ship local-first"

✓ stored decision · receipt written · indexed

\$relicquary recall mystore "what did we decide?"

→ ranked, dated, explainable, from your own store

\$relicquary mcp-server

✓ listening · memory + orchestration, served over MCP

One Rust binary · SQLite + Markdown on your disk · A receipt for every mutation · Your model: local or your own provider

01 / THE RECORDED RUNS

## What it has done when run, before any architecture.

Three entries from the record: real trial runs on a real machine, each stated at its own scope. The full dated ledger, including what has not run, is [the record](https://relicquary.com/record.html).

RUN · 2026-06

supervised runs · The conscience caught degenerate loops

In live runs, the deterministic conscience detected fixation and no-op churn the model did not notice, and corrected the run rather than crashing it. [entry ↗](https://relicquary.com/record.html#run-conscience)

RUN · 2026-06

8 held-out trials · Capability reuse: 8 of 8

A hand-authored, banked capability was recalled by obstacle signature and re-applied on novel held-out instances, 8 of 8. Reuse, not synthesis; the entry says exactly which. [entry ↗](https://relicquary.com/record.html#run-reuse)

RUN · 2026-06

one milestone run · A real build-repair run

Given a failing real build, the operator drove the task down to a handful of compile errors and authored the fix itself, through the audited chokepoint, with a receipt per move. [entry ↗](https://relicquary.com/record.html#run-buildrepair)

02 / WHAT WE BUILD TO

## One company, one discipline.

A memory OS, an operator, a touch driver, a control stack, held together by three commitments that show up in the code, not just the copy.

### Sovereign by construction

Your store lives on your disk: no hosted service, no telemetry. And the model is your choice: run it fully local, or connect your own provider account (you bring the OAuth). Either way, your data and audit trail stay yours.

your machine · your files

### Bounded, not unsupervised

Exactly one action per tick, through one audited chokepoint, behind a fail-safe fence. A deterministic conscience can halt a degenerate loop. Destructive, irreversible actions are retained by the human by design.

one chokepoint · one conscience

### Receipt-bound honesty

No capability exists until a receipt backs it. If a proof didn't run, the system says so; never a green result a verifier didn't confirm. We publish honest NULLs. **A result only counts when it survives a test it could have failed.**

receipts over rhetoric

03 / THE PRODUCTS

## Start with the core.

Relicquary is the core, and it runs today. TouchLink is a virtual touchscreen driver you can use on its own, or fold into a stack, the way AIM does.

Runnable today · v0.9.0

### Relicquary: the memory OS for AI agents

A local-first memory OS in a single Rust binary: the working loop included. Durable typed memory and a knowledge graph, **plus the orchestration an agent works out of** (what to do next, synthesis, handoff, continuity across sessions), all under receipt-bound governance, as SQLite and Markdown on your own disk. It's the core the rest of the stack is built from. Build it, init a store, and serve it to any MCP-compatible agent today.

[Explore Relicquary](https://relicquary.com/index.html) [The 57 tools](https://relicquary.com/tools.html)

recall **"what did we decide about storage?"**

current

**Decision:** Ship local-first: SQLite + Markdown on the operator's own disk.

kind: *decision* trust: *verified* confidence: *0.9* edges: *supersedes ×1*

lexical (BM25).86

semantic.92

currentness.98

[](https://relicquary.com/touchlink.html)

### TouchLink: a virtual touchscreen driver

Working prototype

On its own, it makes a USB touchscreen on a Mac behave like a touchscreen: taps land where you touch, and your mouse stays a mouse. Folded into a stack, it becomes a programmable control surface, the way AIM uses it to drive a workspace by touch.

Explore TouchLink

04 / THE FLAGSHIP

## AIM: a full computer-use operator on a floor you can verify.

**AIM: Accurate, Immediate, Minimal; AGRO in motion.** The full stack: an operator that perceives the desktop, plans, and acts on a real computer, drawing everything it knows from Relicquary, on a floor you can audit.

AIM drives a real computer, so every action it takes passes through its floor: a deterministic, receipt-checkable layer that decides what the operator is *allowed* to do, and proves what it *did*. The floor isn't another model second-guessing the first: **it's mechanism**. Because it's deterministic and receipt-checkable, you verify the property rather than take it on faith.

aim · one governed tick bounded

    perceive: read desktop state + recall prior capability
    plan: model proposes one action · read-only sandbox
    conscience: deterministic checks · halt & correct, then continue
    act: one audited chokepoint · behind a fail-safe fence
    verify: receipt written · no proof ran → it says so
    remember: capability persisted → Relicquary

**How the loop is governed.** The runtime is a *perceive → plan → execute* loop. The contribution is what wraps it: deterministic limits on what the loop may do, one governed chokepoint every action passes through, and a receipt for every action it takes.

05 / THE DETERMINISTIC FLOOR

## A floor you can verify, not take on faith.

Five mechanisms, none of them another model's opinion. They hold whether or not the brain behaves.

The floor is mechanism, so it holds even when the models agree.

FLOOR_01

#### One actuation chokepoint

Exactly one place where the agent acts on the world, governed and inspectable, not scattered tool calls. A standard agent is a loop wired to many tools, with many places intent becomes effect; AIM has one. That single gate is the structural break from while-loop-plus-tools.

FLOOR_02

#### A fail-safe fence

The chokepoint sits behind a hard boundary that blocks catastrophic operations outright, independent of what the model decides. The safe state is the default; the agent is never trusted past the fence for those operations.

FLOOR_03

#### A deterministic conscience

Not a second model grading the first: rule-based checks (we call them theodicytes) that can halt the agent on fixation, on no-op churn, or on an ungrounded assertion. The judgment is mechanism, and a halt is correct-and-continue, not a crash.

FLOOR_04

#### Receipt-bound actions

Every mutation emits an append-only receipt. Actions aren't just claimed in the agent's narration; each leaves a record you can audit independently, after the fact, without trusting how the agent described what it did.

FLOOR_05

#### An untrusted-memory model

Everything the agent writes to memory is untrusted by default and carries its provenance. Trust is earned through governance, never assumed because the model said so: the same discipline that makes Relicquary's memory auditable, applied to an operator that acts.

Grades: the floor components are built and tested; the operator lanes around them are a working prototype.

06 / THE FULL STACK

## Relicquary, writ large.

One core, embodied into an operator that acts. Relicquary is the memory OS at the center; AIM adds the parts that let it perceive and drive a real machine, with the floor between every intent and the world. Each part is graded for where it actually stands.

**AGRO: the soil.** The name is both an acronym and an older root: *Always Growing Recursive Optimizer*, and *agros*, cultivated ground. AGRO is the plot the core is planted in: a loop given work, fed back its own results, and tended turn after turn so capability can take root. The discipline is soil-first: nothing is harvested early. A capability is real only once it survives a held-out test it has never seen. That destination is what the present-tense work aims toward: the ambition of the stack, stated plainly.

THE CORE

runs today · v0.9.0 · Relicquary: memory + orchestration

The memory OS the whole stack thinks out of: durable typed memory, a knowledge graph, recall, and the orchestration of the working loop, under receipt-bound governance. [Standalone →](https://relicquary.com/index.html)

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

07 / THE ROAD AHEAD

## The brain never grows. The stack accumulates.

The brain is a model whose weights we don't touch, so it never trains on your use. Capability accumulates in the stack instead: what that means today, and where it goes.

WORKS TODAY

reuse · 8/8 held-out · Reuse

Hit an obstacle whose signature it has seen, and AIM recalls the durable capability it already stored (a tool, a procedure, a receipted artifact) and re-applies it. The capability-reuse path passed 8 of 8 held-out trials on novel instances. [RUN 2026-06 · reuse 8/8 ↗](https://relicquary.com/record.html#run-reuse)

OPEN FRONTIER

unbuilt · gated · Synthesis

The next phase is capability **synthesis**: authoring a genuinely new durable capability for a blocker it has **never seen**, gated behind a hard held-out test. Clearing a blocker is the entry ticket, not the verdict: a capability is real only once it passes a held-out execution on a novel instance. Model opinions don't count; only the test does.

THE APPS

App Store · Relicquary for everyone

The same local-first core, on Mac and iPhone, bought once and owned outright. Status and details live in one place: [the apps](https://relicquary.com/index.html#apps).

CROSS-AUDIT

on the roadmap · DPACA: reliability by design

Two models in a four-eyes arrangement (one proposes, the other only approves or rejects) behind a deterministic, hash-bound publish step. Its purpose is reliability: to make it far harder for a single confident model to push a mistake through.

THE DESTINATION

open frontier · AGRO: the soil it all grows toward

The destination is an autonomous system that can be trusted to act because every move is auditable down to the receipt. The stack accumulates receipt-bound capability it can carry and reuse, with provenance attached; the hard, open frontier is synthesis. It is the work ahead, and it is the whole point. **AGRO in motion: Accurate, Immediate, Minimal.**

**Owned, local, and accountable, by construction.** Your memory stays on your hardware. The operator acts only through a chokepoint it can't route around, and it shows its work. We'd rather ship a smaller floor that holds than a larger promise that doesn't.

08 / MATURITY

## Every claim, graded.

So the credibility gradient is visible at a glance: what runs, what's prototype, what's research, what's only designed. The floor components are built and tested; the operator lanes around them are a working prototype. Each line links to its dated entry in [the record](https://relicquary.com/record.html).

#### Runs today

- **Relicquary v0.9.0**: memory + orchestration, CLI + MCP [entry ↗](https://relicquary.com/record.html#rel-090)
- **The deterministic floor** (chokepoint, fence, conscience), built & tested
- **Capability reuse**: 8/8 held-out [entry ↗](https://relicquary.com/record.html#run-reuse)

#### Working prototype

- **AGRO** planning loop
- **Operator substrate**: persistent operator + chokepoint
- **TouchLink** (one verified device) [entry ↗](https://relicquary.com/record.html#hw-touchlink)
- **AI Control Stack** (single machine)

#### Open research

- **Capability synthesis**: a new capability from a never-seen blocker; held-out test unbuilt [entry ↗](https://relicquary.com/record.html#null-synthesis)

#### Designed, not built

- **DPACA** two-model cross-audit [entry ↗](https://relicquary.com/record.html#null-dpaca)
- **Durable backup/restore**: memory is volatile today [entry ↗](https://relicquary.com/record.html#null-backup)
- **Signed, distributable** apps & Relicquary v1.0

09 / RQ MCP LLC

## Autonomy you can actually audit.

RQ MCP LLC builds Relicquary (the local-first memory OS) and AIM, the full stack that turns it into a computer-use operator you can audit. Every capability is receipt-bound, and a result only counts when it survives a test it could have failed.

> “Agents forget. Every autonomous system we ran reset to zero between sessions: repeating mistakes, losing the context it had earned, asking us to trust actions we couldn't check afterward. The conviction was simple: memory and accountability aren't features you bolt on later; they're the floor everything else stands on. So we built the floor first. The core runs today on your own machine: one binary, your disk, a receipt for every action. That's the standard I want to be held to.” Jessy Brenenstahl, Founder, RQ MCP LLC

hello@relicquary.com · subject “AIM” for the recorded-run evidence, or to build on the stack
