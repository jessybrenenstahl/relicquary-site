# Relicquary: local-first memory OS for AI agents

*Machine-readable Markdown of https://relicquary.com/index.html (content hash 159ce109)*

Memory your agents can recall,\
and the loop they run on.
===============================

Relicquary is a **local-first memory OS** for AI agents: typed memory, a knowledge graph, and explainable recall, **plus the working loop an agent runs on**. One Rust binary, your own disk, a receipt for every write.

Protocol**MCP** + CLI

Memory kinds**14** typed

Model**local** or your own

relicquary: recall · mystore demo

\$

One Rust binary, CLI + MCP · SQLite + Markdown on your disk · A receipt per mutation · Model: local or your own

01 / WHAT IT IS

## Not chat history. The memory OS your agents run on.

A reliquary is a vessel built to keep what must not be lost; Relicquary is that vessel for an agent's memory. The store is plain files you own, and the model is yours: keep it fully local on your own machine, or connect your own provider account. One honest note on durability: a first-class backup and restore path is designed, not yet built; today durability is the plain files themselves, which you can copy and version like any others.

### Local-first by design

A SQLite database plus human-readable Markdown relics, sitting in a folder on your disk. Open them, grep them, version them, and work offline. You own the store.

~/.relicquary/mystore

### Continuity across sessions

Relicquary runs the working loop, and it makes sessions continuous: `session_start` recovers stranded work and `context_pack` briefs an agent in one call, so a fresh session resumes where the last one stopped.

recall → decide → act

### Auditable, no telemetry

Every write is untrusted by default and produces a receipt: an append-only record you can read as a file. The store stays on your own disk, and nothing phones home.

receipts · trust tiers

THE WHOLE SYSTEM IS YOUR MACHINE

- 01

  ### Works offline

  Retrieval, reranking, and the store itself run on-device. No connection, no degradation of what you own.

- 02

  ### Greppable, versionable files

  Every memory mirrors to a Markdown relic you can open in any editor, grep, or commit to git. No opaque service between you and your record.

02 / EXHIBIT: RECALL

## A query becomes ranked, dated, defensible evidence.

Four stages, all on-device. The agent gets ranked results it can act on, and a reason for each one.

STAGE 01

#### Lexical · BM25

Exact-term matching over the full store catches names, IDs, and precise phrasing.

STAGE 02

#### Semantic · embeddings

On-device vector search surfaces meaning, even when the words don't match.

STAGE 03

#### Fuse, rerank + graph

Fused scores are reranked with connected-evidence and temporal-currentness signals.

STAGE 04

#### Labelled results

Each result ships with a score, a currentness label, and a why-it-ranked breakdown.

recall mystore **"what did we decide about storage?"**

current

**Decision:** Ship Relicquary local-first, SQLite + Markdown on the operator's own disk.

kind: *decision* trust: *verified* confidence: *0.9* edges: *supersedes ×1*

lexical (BM25).86

semantic.92

connected evidence.64

currentness.98

**Currentness, not just relevance.** Every result is labelled `current`, `stale`, or `superseded`, so an agent never acts on a decision that's already been overruled. Ask in natural language; get back ranked, dated, explainable memory.

03 / WHO IT'S FOR

## For agents that have to remember.

For developers and teams running MCP-capable agents (coding agents, research agents, autonomous operators) that have to pick up where they left off. Before Relicquary, every session starts from zero: the agent re-derives what it already knew, asks the same questions, and repeats mistakes it has no record of making. After, it recalls a durable, typed, receipted record of what was decided and why, cites where each piece came from, and builds on it across restarts, sessions, and tools.

- WHO_01

  ### Coding agents that keep their decisions

  The architecture call you made last week (local-first, passkeys over passwords, this library not that one) is still there next session, with the reasoning and the trail attached. The agent stops relitigating settled choices and stops reintroducing bugs you already fixed.

- WHO_02

  ### Research and operator agents that accumulate

  Long-running research and autonomous operators write findings into a typed knowledge graph (facts, entities, and the edges between them) instead of a transcript that scrolls away. Each run adds to the last, and contradictions surface instead of quietly overwriting what was true.

- WHO_03

  ### Teams that need a memory they own and can audit

  The store is SQLite and Markdown on your own disk, and every write carries a receipt. A teammate, or a different tool, can open the same record, see where each entry came from, and trust it, because nothing landed without provenance. The memory is yours to read, move, and keep.

04 / CAPABILITIES

## Structured memory, and the loop to act on it.

Memory is typed, linked, and explainable, and Relicquary orchestrates the working loop on top of it, so an agent can find the right thing, prove why it surfaced, and act on it.

### CAP_00 · THE LOOP · Orchestration, not just storage

Relicquary runs the loop an agent works out of: recall what matters, decide what's next, synthesize, hand off, keep a session moving. The orchestration is first-class, and that loop has driven **live agent sessions end to end**. [RUN 2026-06 · build-repair ↗](record.html#run-buildrepair)

next_task · synthesis · handoff · session · recall → act

### CAP_01 · Typed memory: 14 kinds

Fourteen kinds of memory object, each carrying tags, confidence, provenance, and a trust tier. No undifferentiated text blobs; every entry knows what it is.

fact · decision · task · procedure · episode · observation · contradiction · preference · entity · handoff · claim · artifact · friction · summary

### CAP_02 · Typed knowledge graph

Typed edges link memories into a graph (`supersedes`, `depends_on`, `conflicts_with`, `blocks`, `mentions`) with automatic conflict detection so stale beliefs get flagged.

supersedes · depends_on · conflicts_with · blocks · mentions

### CAP_03 · Explainable recall

Lexical BM25 fused with on-device semantic embeddings, then reranked. Results carry currentness labels and a per-result "why it ranked" breakdown, not raw text dumps.

BM25 · embeddings · rerank · currentness · why-it-ranked

### CAP_04 · Receipts for every mutation

Every mutation is recorded as an append-only receipt you can audit as a file. Approve, supersede, or forget: the history of how memory changed is always there. [REL 2026-06-10 · v0.9.0 gate ↗](record.html#rel-090)

append-only · auditable · provenance · trust tier

### CAP_05 · One store, two front doors: MCP & CLI

Agents speak the Model Context Protocol; you run `relicquary remember`, `relicquary recall`, and `relicquary mcp-server` from your terminal. One source of truth, no SDK lock-in, no SaaS daemon.

relicquary remember · relicquary recall · relicquary mcp-server

05 / THE TOOLS

## The interface is the product: 57 tools your agent calls.

Relicquary is MCP-first: not a library you wrap, a surface an agent talks to directly. One of the 57 returns the whole system: `architecture` hands an agent the reconstruction-grade spec in a single call, so it operates from understanding instead of guessing.

rememberrecallcontext_packhandoffnext_taskflag_contradictionlist_receiptsgraph_exportsession_endarchitecture

[Explore all 57 tools](tools.html) [See how they compose](tools.html#together)

06 / WHY RELICQUARY

## Memory that's yours, typed, and provable.

Agent memory is a crowded shelf. Most of it is a cloud service that holds your store, or a vector index that hands back a blob of text and calls it recall. Relicquary takes a different shape: a single binary on your own disk, memory that knows what it is, recall you can defend, and the loop your agent actually runs on. Here's where the line falls.

### VS_01 · Local-first, not a memory you rent

Unlike hosted memory services that keep your agent's knowledge in someone else's cloud, Relicquary is a single binary writing SQLite and Markdown to a folder on your own disk. No hosted service, no telemetry, nothing phoning home. The store is yours to open, grep, version, and back up, and it works offline.

### VS_02 · Typed memory and a graph, not a text-blob dump

Unlike a raw vector store that returns the nearest chunks and leaves interpretation to you, Relicquary's memory is typed across 14 kinds, linked into a knowledge graph with automatic conflict detection. Recall comes back ranked and labelled current, stale, or superseded, with a why-it-ranked breakdown, so your agent never acts on a belief that's already been overruled.

### VS_03 · MCP-native and CLI, not locked to one framework

Unlike memory baked into a single framework's SDK, Relicquary speaks the Model Context Protocol to any MCP-capable agent and answers to a clean CLI for you. One store is the single source of truth across every agent and tool: switch frameworks, run several side by side, drive it from the terminal. No SDK lock-in, no SaaS daemon.

### VS_04 · Receipt-bound, and it runs the loop

Unlike tools that are storage and nothing more, Relicquary treats every write as untrusted by default and records it as an append-only receipt you can audit as a file. And it doesn't stop at remembering: it runs the orchestration loop an agent works out of (recall, decide, synthesize, hand off), a loop that has driven live agent sessions end to end. [RUN 2026-06 · build-repair ↗](record.html#run-buildrepair)

07 / THE APPS\
Coming to the App Store

## Your memory, in your pocket.

Native macOS and iPhone apps are coming to the Apple App Store: **a one-time purchase, no subscription**. The apps are in development; the core they wrap runs today via CLI and MCP. On-device recall on your desk and your phone, no account required.

- **One-time purchase, no subscription**: buy once, yours across Mac and iPhone.
- **On-device recall**: search and surface memory locally, instantly, offline.
- **Cross-device sync**: planned for the iPhone release. [register ↗](record.html#null-sync)
- **No account required**: no sign-up, no server, no profile to harvest.

**Join the waitlist**: email [hello@relicquary.com](mailto:hello@relicquary.com?subject=Relicquary%20waitlist) and we'll tell you the moment it's live.

08 / GET IT

## The core runs today.

Relicquary v0.9.0 is in developer early access: the full core, CLI and MCP server. It builds and runs on macOS on Apple Silicon; the binary arrives by reply. [REL 2026-06-10 · v0.9.0 ↗](record.html#rel-090)

    # step 1: request access

    $ email hello@relicquary.com, subject "Relicquary early access"

    # step 2: the binary arrives with the reply

    # step 3: run it

    $ relicquary remember mystore "decided: ship local-first"

    $ relicquary recall mystore "what did we decide?"

    $ relicquary mcp-server

    {"mcpServers":{"relicquary":{"command":"relicquary","args":["mcp-server"]}}}
    # or, with Claude Code:
    claude mcp add relicquary -- relicquary mcp-server

hello@relicquary.com · subject “Relicquary early access”

PART OF SOMETHING LARGER

## Relicquary is the core of AIM.

On its own, Relicquary is the memory and the working loop your agents run on. Wired into a full stack that perceives a screen and drives a real computer, that same core becomes **AIM**, RQ MCP LLC's computer-use operator, acting on a floor you can verify. Relicquary is where it starts; AIM is what it's built into. In recorded runs, its conscience has caught and corrected degenerate loops. [RUN 2026-06 · conscience ↗](record.html#run-conscience) And its capability-reuse path went 8 of 8 on held-out trials. [RUN 2026-06 · reuse 8/8 ↗](record.html#run-reuse)

[See the full stack](stack.html) [Explore TouchLink](touchlink.html)
