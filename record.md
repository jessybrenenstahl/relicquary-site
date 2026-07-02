# The record: what ran, when, at what scope

*Machine-readable Markdown of https://relicquary.com/record.html (content hash 9335065b)*

THE RECORD

# What ran, when, at what scope.

One rule: entries are appended and dated, never edited. Each entry states its own scope. What has not run is listed too. Everything this site claims about behavior resolves to an entry on this page.

## 01  Releases

2026-06-10

### Relicquary v0.9.0, Crystallization

runs today

The core in its current shape: one Rust binary serving CLI and MCP, typed memory mirrored to Markdown relics, the knowledge graph, hybrid explainable recall, receipts on every mutation, and a supervised local model runtime that restarts a crashed model lane instead of failing for the life of the process.

**The gate this release passed:** formatting clean, 341 of 341 tests green, the 16-case memory evaluation suite at 16 of 16, and a live verification on real hardware in which one model lane was force-killed mid-session, recall kept working in degraded mode, and the supervisor respawned the lane.

scope: one machine, macOS on Apple Silicon, built from source · versioning note: a legacy v1.0 git tag from 2026-05-13 predates this line and is a historical mislabel; it is retained as immutable history and supersedes nothing

2026-07-02

### Tool surface verified at 57

drift-check green

The MCP tool catalog was re-derived from the binary's own schema output and its generated documentation, with the repository drift check passing. The count is **57 tools**. Earlier copy on this site said 56 and omitted `reject_memory`; both are corrected as of this entry, and [tools.json](tools.json) is now generated from the same schema output so the count is settled by construction.

scope: schema-derived count, verified against source on the date above

## 02  Recorded runs

AIM trial runs on a real machine, re-typed here from the recorded sessions. No screenshots are shown because none were retained; what follows is the record as kept, at the scope stated.

2026-06

### The conscience caught degenerate loops, and corrected them

working prototype

In live operator runs, the deterministic conscience detected degenerate loops the model itself did not notice: fixation (re-attempting one failing move) and no-op churn (activity without progress). The checks are non-terminal: the run was halted at the check, corrected, and continued, rather than crashing or running the loop blind.

scope: prototype operator, single machine, supervised runs, June 2026

2026-06

### Capability reuse: 8 of 8 held-out trials

working prototype

A durable capability was authored by hand and banked in the store with its obstacle signature. The trials tested the **reuse path**: given a novel instance the system had not seen, could it recall the banked capability by signature and re-apply it through the governed chokepoint? It did, in 8 of 8 held-out trials.

**What this does not show:** the capability was hand-authored, not synthesized by the system. Authoring a genuinely new capability for a never-seen blocker is the open research line in the register below.

scope: 8 held-out trials on novel instances, single machine, June 2026 · tests reuse, not synthesis

2026-06

### A real build-repair run

working prototype

Given a failing real build as its mission, the operator perceived the failure output, drove the task down to a handful of compile errors, and authored the fix itself, acting through the audited chokepoint with a receipt per move. This is the run behind the sentence "bounded, receipted work under governance" on the stack page.

scope: one milestone run, real codebase, single machine, supervised, June 2026

## 03  Hardware verification

2026-06

### TouchLink on a real panel

verified · real panel

The TouchLink driver builds, signs, launches, and passes its test suite on one physical USB touchscreen panel attached to a Mac: taps land where the finger touches, across displays, while the mouse stays a mouse.

scope: one panel model, one Mac, macOS 13+ · distribution packaging not yet built

## 04  What has not run

The register of things this site does not claim, kept next to the things it does.

open

### Capability synthesis

unbuilt · open research

Authoring a genuinely new durable capability for a blocker the system has never seen. Unbuilt. It will be graded only by a held-out execution test on a novel instance, and that test does not exist yet.

status: the open frontier; no claim until the test passes

open

### DPACA two-model cross-audit

designed, not built

One model proposes, a second only approves or rejects, behind a deterministic hash-bound publish step. Designed for reliability. Not built.

status: on the roadmap, toward acceptance gates

open

### Durable backup and restore

designed, not built

A first-class backup and restore path for the store. Designed, not built. Today durability is the plain files themselves: SQLite and Markdown you can copy, version, and snapshot with ordinary tools.

status: gates any paid artifact; graded runs-today only when a restore drill passes in CI

open

### Cross-device sync

planned, not built

Synchronizing a store between Mac and iPhone. Planned for the iPhone release. Not built, and not claimed anywhere else on this site.

status: planned for the iPhone release

Want the underlying receipts for an entry, or to build on the core the record describes? Email and name the entry.

[Get developer early access](mailto:hello@relicquary.com?subject=Relicquary%20early%20access)

hello@relicquary.com · subject “Relicquary early access”
