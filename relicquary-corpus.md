# Relicquary: full site corpus

*Every content page of relicquary.com as one machine-readable Markdown document. Relicquary is a local-first memory OS for AI agents with an MCP-native surface of 57 tools; AIM is a full-stack computer-use operator built on it, acting on a verifiable floor. RQ MCP LLC.*

## Contents
- Relicquary: local-first memory OS for AI agents
- Relicquary tool catalog: 57 MCP tools
- The record: what ran, when, at what scope
- AIM: the full stack that acts, on a verifiable floor
- TouchLink: a virtual touchscreen driver
- Relicquary support
- Relicquary privacy policy
- Relicquary terms of service

---

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


---

# Relicquary tool catalog: 57 MCP tools

*Machine-readable Markdown of https://relicquary.com/tools.html (content hash 80909bba)*

# The interface is the product. 57 tools your agent calls over MCP.

Relicquary is not a library you wrap. It is a memory-and-orchestration surface an agent talks to directly, over the Model Context Protocol. Connect any MCP-compatible agent and it gets 57 verbs: remember, recall, hand off, synthesize, audit, and more. Below is every one, what it does, and why it earns its place.

[add_memory_edge](#g-graph-entities-amp-conflicts) [approve_memory](#g-lifecycle-amp-governance) [architecture](#g-the-whole-system) [capture_thought](#g-capture) [claim_synthesis](#g-synthesis) [complete_synthesis](#g-synthesis) [context_pack](#g-retrieval) [edit_memory](#g-lifecycle-amp-governance) [explain_memory](#g-retrieval) [feedback_memory](#g-lifecycle-amp-governance) [flag_contradiction](#g-graph-entities-amp-conflicts) [forget](#g-lifecycle-amp-governance) [forget_memory](#g-lifecycle-amp-governance) [get_entities](#g-graph-entities-amp-conflicts) [get_memory_edges](#g-graph-entities-amp-conflicts) [graph_export](#g-graph-entities-amp-conflicts) [handoff](#g-tasks-sessions-amp-handoff) [hybrid_search](#g-retrieval) [ingest_document](#g-wiki-documents-amp-artifacts) [lint_wiki](#g-wiki-documents-amp-artifacts) [list_artifacts](#g-wiki-documents-amp-artifacts) [list_drafts](#g-lifecycle-amp-governance) [list_receipts](#g-health-recovery-amp-audit) [list_suggestions](#g-lifecycle-amp-governance) [list_thoughts](#g-retrieval) [memory_conflicts](#g-graph-entities-amp-conflicts) [memory_export](#g-lifecycle-amp-governance) [memory_import](#g-lifecycle-amp-governance) [memory_status](#g-health-recovery-amp-audit) [next_task](#g-tasks-sessions-amp-handoff) [promote_memory](#g-lifecycle-amp-governance) [query_context](#g-retrieval) [query_memory_objects](#g-retrieval) [read_artifact](#g-wiki-documents-amp-artifacts) [read_relic](#g-wiki-documents-amp-artifacts) [rebuild_index](#g-health-recovery-amp-audit) [recall](#g-retrieval) [recall_report](#g-retrieval) [reject_memory](#g-lifecycle-amp-governance) [reliquary_status](#g-health-recovery-amp-audit) [remember](#g-capture) [remember_batch](#g-capture) [resolve_conflict](#g-graph-entities-amp-conflicts) [restore_memory_relics](#g-health-recovery-amp-audit) [retry_synthesis](#g-synthesis) [search_thoughts](#g-retrieval) [search_wiki](#g-retrieval) [session_end](#g-tasks-sessions-amp-handoff) [session_start](#g-tasks-sessions-amp-handoff) [status](#g-health-recovery-amp-audit) [suggest_memory](#g-capture) [synthesis_queue](#g-synthesis) [task_progress](#g-tasks-sessions-amp-handoff) [thought_stats](#g-health-recovery-amp-audit) [update_memory](#g-lifecycle-amp-governance) [update_thought_status](#g-lifecycle-amp-governance) [write_relic](#g-wiki-documents-amp-artifacts)

57 tools, 55 cards below: two cards each carry an alias pair (forget / forget_memory, status / reliquary_status). The count is settled by construction in [tools.json](tools.json), generated from the live schemas.

WHY MCP-FIRST

## The tools are the API.

Most memory systems ship an SDK you integrate and maintain. Relicquary ships tools an agent already knows how to call. That difference is the strength.

### No glue to wrap

Any MCP client, Claude, Cursor, or your own agent, connects and calls. Memory and the working loop are just tools it can already use. There is no adapter to write and nothing to keep in sync with a library version.

connect · call

### Every call on the record

The mutating tools write an append-only receipt, and memory is untrusted by default until governance earns it trust. The audit trail is not bolted on. It is how the tools behave, at the boundary where the agent acts.

receipts · untrusted-by-default

### Local, and your model

Retrieval and reranking run on-device, and nothing routes through a provider you did not choose. The tools operate on SQLite and Markdown files you own, so the whole surface stays inspectable.

on your disk

**One call, and the agent understands the system.** A piloting agent cannot operate what it does not understand. So Relicquary exposes its own blueprint as a tool: `architecture` returns the full, reconstruction-grade spec in a single call, the storage schema, the retrieval pipeline, governance, the complete tool catalog, and a glossary, readable section by section. An agent orienting to the system reads it once and knows how every part fits together, well enough to actually pilot the system rather than guess at it. The interface documents itself, to the agent, at runtime.

THE CATALOG

## All 56, grouped by what they are for.

The name in each card is the exact verb an agent calls. Descriptions are drawn from the live tool schemas, so this stays true as the set evolves.

### Capture

### remember · Store a typed memory

Write a fact, decision, task, procedure, or episode as a typed object, mirrored to a plain Markdown relic, with a receipt and automatic dedupe of exact and near-duplicate content. The verb an agent reaches for first.

### remember_batch · Store many at once

Capture a cluster of typed memories in one call, skipping duplicates. Saves an agent from nine round-trips when it has a batch to record.

### capture_thought · Capture, auto-typed

A lower-level capture that reads the kind from the content itself (prefix with Decision:, Fact:, Friction:, TODO:) and reindexes so it is searchable immediately.

### suggest_memory · Propose, do not commit

Stage a memory for later review instead of writing it live, so a cautious agent can surface a candidate that a promote step, or a human, later accepts or discards.

### Retrieval

### recall · The default memory lane

Ranked typed-memory retrieval, scoped per agent, project, user, or org, with connected-evidence reranking, currentness scoring, and embedding-first candidates that fall back to lexical BM25. Returns the memories with why-they-ranked explanations and any conflicts it spots.

### recall_report · Grade your own recall

Measures retrieval quality against the live store: recall@1, recall@3, MRR, stale-leak and distractor rates, worst queries. Memory quality becomes a number, not a hunch.

### explain_memory · Why did this match?

Answers "what do I know about X?" by combining recall with the matched entities and the graph edges around them, so an agent sees the reasoning behind a result, not just the result.

### query_memory_objects · Query the raw table

Fetch memory objects directly by id, kind, tag, source, or status, with no ranking. For governance and introspection over exactly what is stored.

### list_thoughts · Recent memories

List recent memories, optionally by kind or assigned agent. Quick orientation without composing a query.

### search_thoughts · Raw thought search

Lower-level search over raw memory rows, including browse-by-kind. For when you want the rows, not a ranked answer.

### hybrid_search · Semantic wiki search

Search wiki relics with local embeddings fused with BM25, falling back to lexical when the model server is unavailable.

### search_wiki · Keyword wiki search

Fast lexical keyword search over wiki pages when you already know the term.

### query_context · A cited context bundle

Builds a deterministic, cited retrieval pack for a question, lexical or hybrid. For when a model needs sourced context rather than scattered hits.

### context_pack · The startup pack

Compiles an 11-section briefing for an agent starting or resuming work: objective, constraints, canonical paths, recent decisions, open tasks, files, pitfalls, commands, receipts, conflicts, and next actions. One call to be oriented.

### Lifecycle & governance

### edit_memory · Edit in place

Rewrite a memory's content, with a receipt recording the change and its reason.

### update_memory · Change status or edges

Move a memory's status or adjust its dependency edges without rewriting the content.

### update_thought_status · Advance a claim

Set a memory's lifecycle status: active, in_progress, completed, superseded, verified, or stale.

### approve_memory · Trust a draft

Promote a draft or untrusted memory to trusted-active once it has been reviewed.

### reject_memory · Reject a suggestion or draft

Reject a pending memory suggestion, or reject a draft or untrusted memory by marking it invalid. Requires a reason, and records a receipt. The other half of governed trust: what does not earn promotion is turned away, on the record.

### promote_memory · Accept a suggestion

Turn a staged suggestion, or a draft or stale memory, into trusted-active. The accept step for the passive-capture lane.

### forget / forget_memory · Soft-delete

Mark a memory invalid, a reversible soft delete, guarded by an explicit confirm.

### feedback_memory · Rate a result

Tell the store a recalled memory was helpful, wrong, stale, or a duplicate. The signal that tunes future ranking.

### memory_export · Export the store

Write memories to a JSON or JSONL archive, with a receipt.

### memory_import · Import an archive

Load memories back from a JSON or JSONL archive.

### list_drafts · Pending review

List draft and untrusted memories waiting for approval, kept out of recall until they earn trust.

### list_suggestions · Pending suggestions

List staged suggestions by score, ready to promote or discard.

### Graph, entities & conflicts

### add_memory_edge · Link two memories

Create a typed directed edge (supersedes, depends_on, supports, invalidates, same_as, and more) between memories.

### get_memory_edges · Inspect the links

Return the typed edges around a memory before graph-expanded recall or handoff reasoning.

### get_entities · Who and what

List the file, tool, and person entities extracted from memory, with mention counts.

### graph_export · Export the graph

Emit the memory graph or the wiki-link graph as JSON, Graphviz DOT, or JSON-Canvas for visualization.

### memory_conflicts · Detected conflicts

List the conflict and scope-drift items the store flagged when new memories overlapped older ones.

### flag_contradiction · Mark a contradiction

Explicitly declare two memories in conflict, adding conflicts_with edges in both directions.

### resolve_conflict · Close a conflict

Resolve a flagged conflict, optionally naming the memory that wins and supersedes the rest.

### Wiki, documents & artifacts

### write_relic · Write a page

Create or overwrite a wiki relic, reindexed on write, with a receipt. How synthesis drafts become canonical pages.

### read_relic · Read a page

Read a relic by path: content, parsed frontmatter, outline, and memory fields, no YAML wrangling.

### ingest_document · Bring in a doc

Ingest a document body into the store, a raw copy plus a formatted source relic plus a reindex, no shell required. Bootstraps a store from project docs the agent already holds.

### lint_wiki · Wiki health

Check for duplicate titles, broken links, orphans, and TODO pages, with tag and property summaries.

### list_artifacts · List files

List the files available to the agent across raw and attachment surfaces, or all relics.

### read_artifact · Read evidence

Read a bounded slice of an artifact by path, for pulling in evidence without loading a whole file.

### Synthesis

### synthesis_queue · The work queue

List and refresh the background synthesis queue, entities, concepts, memory compaction, conflicts, and staleness, with a per-lane count so a worker knows what to claim.

### claim_synthesis · Take an item

Claim the next pending synthesis item for a worker, prioritizing source work before housekeeping.

### complete_synthesis · Finish an item

Complete a synthesis item and optionally write a draft relic, deterministic or model-generated, with receipts.

### retry_synthesis · Requeue

Return claimed or completed items to pending, one or many.

### Tasks, sessions & handoff

### next_task · What is next

Return the highest-confidence unblocked task for the next step, and optionally claim it atomically so parallel workers do not collide.

### task_progress · Where things stand

Summarize task progress: active, in-progress, completed, stale, blocked, and percent done.

### handoff · Hand off cleanly

Generate a deterministic project handoff from memory, status, and receipts, so the next agent continues without the chat history.

### session_start · Begin, and recover

Start a session and recover any stale in-progress tasks back to active, so a crashed run does not strand work.

### session_end · Close out

End a session: write a handoff, record a receipt, and return the next-task snapshot for whoever comes next.

### Health, recovery & audit

### status / reliquary_status · Is it healthy?

Inspect filesystem and SQLite health without writing. The first orientation or recovery call when something looks off.

### memory_status · Memory health

A memory-specific summary: runtime completeness, active kinds, receipt and index health.

### thought_stats · Counts and facets

Memory counts by kind, plus the top topics and people, for quick orientation.

### list_receipts · The audit trail

List the append-only governance receipts, every mutation the system made, filterable for audit.

### rebuild_index · Rebuild the index

Rebuild the SQLite index from the wiki files, backing up the old database first. Recovery when the index is damaged but the files survive.

### restore_memory_relics · Restore memory

Rebuild runtime memory rows from the durable relics after an index rebuild. Explicit recovery, never a silent repair.

### The whole system

### architecture · The whole system, one call

Returns Relicquary's full, reconstruction-grade spec as Markdown: the storage schema, the model stack, the retrieval pipeline, governance, the complete tool catalog, and a glossary, read section by section. A piloting agent can call this once and understand the entire system well enough to operate it, or to rebuild it from scratch. This is the tool that turns a memory store into something an agent can actually drive.

HOW THEY COMPOSE

## The tools are useful together, not just one at a time.

Four flows that show the catalog working as a system. Each is real: every step is a single tool call.

### FLOW · ORIENT & CONTINUE · Pick up where the last agent stopped

`session_start` recovers any stranded work, `context_pack` compiles the 11-section briefing, and `next_task` hands over the next move. The agent acts, calls `remember` for what it learned, then `session_end` writes the handoff. A fresh agent resumes with zero chat history.

### FLOW · NOTES TO KNOWLEDGE · Turn raw memory into synthesized knowledge

`capture_thought` records a raw note, `synthesis_queue` surfaces what needs synthesizing, and `claim_synthesis` with `complete_synthesis` draft canonical relics. Now `recall` returns the synthesized understanding, not just the original note.

### FLOW · UNDERSTAND, THEN PILOT · Comprehend the system before operating it

`architecture` returns the whole blueprint in one call, `status` confirms the store is healthy, `recall` pulls the relevant history, and `next_task` points at the work. The agent operates from understanding instead of assumption.

### FLOW · TRUST & REPAIR · Audit everything, recover from anything

`list_receipts` is the record of every mutation the system made. When an index is damaged, `reliquary_status` diagnoses, `rebuild_index` restores from the files, and `restore_memory_relics` rebuilds runtime memory. Nothing silent, everything recoverable.

MACHINE-READABLE

## The receipt for the catalog itself.

Every card above is prose. `tools.json` is the same catalog as data, generated from the live tool schemas: name, aliases, group, and a one-line description per tool. It settles the count by construction, and an agent can diff it between visits.

[tools.json · all 57, from the schemas](tools.json)

## Relicquary runs today.

Stand up a store, serve it over MCP, and your agent has all 57 tools, on your own disk, under your own audit.

hello@relicquary.com · subject “Relicquary early access”


---

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


---

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


---

# TouchLink: a virtual touchscreen driver

*Machine-readable Markdown of https://relicquary.com/touchlink.html (content hash 83821c11)*

**TouchLink** is the control-surface lane of **AIM** (RQ MCP LLC's full-stack computer-use operator) and a standalone macOS driver in its own right.

[AIM & the stack](stack.html)

# Touch that lands where you tap.

**TouchLink** is a virtual touchscreen driver for Mac. On its own, it makes touch behave like touch: **your touchscreen works like a touchscreen, and your mouse stays a mouse**. And because it's a virtual driver, it also folds into a larger stack as a programmable control surface, the way AIM uses it.

A working prototype, verified on real hardware. Distribution packaging comes next. macOS 13+.

touchlink verified · real panel

    plug in: your USB touchscreen
    calibrate: tap the four corners · once
    you tap: the button you meant
    it lands: right where you touched ✓
    your mouse: still works as a mouse

01 / THE PROBLEM

## macOS has no good answer for USB touchscreens.

Plug a touchscreen into a Mac and it mostly doesn't behave: your taps land on the wrong screen, in the wrong place, or just move the pointer. macOS treats a touchscreen as a mouse; TouchLink makes it behave like a touchscreen.

### Calibrated to your screen

A quick, guided four-corner tap teaches TouchLink your exact panel and layout, so from then on, your touch lands on the right spot, every time.

4-point matrix

### No kernel hacks

TouchLink runs as a menu-bar app on public macOS frameworks: `IOHIDManager` and a `CGEvent` tap. No kernel extension to break on an OS update.

IOHIDManager · CGEvent

### Right screen, every time

It corrects events for the specific display you've bound the touchscreen to, leaving your other screens untouched. The right surface gets the touch.

display-bound

02 / HOW IT WORKS

## Catch the wrong tap. Post the right one.

TouchLink watches the raw HID stream, recognises the miscalibrated event, applies your calibration, and returns a corrected native event, all on-device.

STAGE 01

#### Monitor

Reads raw USB touchscreen HID reports through `IOHIDManager`.

STAGE 02

#### Match

A `CGEvent` tap catches the miscalibrated pointer event macOS generated.

STAGE 03

#### Correct

Applies your per-device 4-point calibration matrix to the coordinates.

STAGE 04

#### Post

Returns the corrected event to the stream, and the tap lands exactly where you touched.

**On-device, by construction.** Everything happens locally on your Mac through public frameworks. TouchLink needs Input Monitoring and Accessibility permission to read raw HID and post corrected events, and nothing else.

03 / IN THE AIM STACK

## The same primitive, as a control surface.

Inside [AIM](stack.html), TouchLink is the pattern for turning a physical touchscreen into a safe driver of a virtual workspace, under the same bounded-autonomy rules as the rest of the stack.

### ROLE_01 · Observer-first

By default it observes and transforms coordinates: metadata only. No synthetic input is injected and no drivers are mutated without an explicit, approved step.

### ROLE_02 · Focus-preserving

The control-surface lane is designed to route touch into a virtual workspace without stealing focus or duplicating input; the operator's other work keeps running.

### ROLE_03 · Bounded, like the rest

Any real routing or synthetic input sits behind explicit approval: the same "no single part acts unchecked" posture that governs the whole AIM operator.

### ROLE_04 · Cross-machine, research

Extending the lane to route a Windows-owned touchscreen into a Mac workspace is on the roadmap, behind hard safety rails. Not a shipping feature today.

04 / STATUS

## A working prototype, on real hardware.

TouchLink builds, signs, launches, and passes its test suite on one real panel. [HW 2026-06 · verified ↗](record.html#hw-touchlink) Distribution packaging comes next.

Email your panel model and macOS version and we will send current-build instructions, or say “updates” to hear when packaging ships.

hello@relicquary.com · subject “TouchLink”


---

# Relicquary support

*Machine-readable Markdown of https://relicquary.com/support.html (content hash 40b13537)*

HELP · RQ MCP LLC

# Support

We're here to help.

**Email us:** <hello@relicquary.com>. We read every message and aim to reply within two business days.

## Get in touch

Whether you've hit a bug, have a question about how Relicquary works, want to request a feature, or just want to know when the Mac and iPhone apps ship, send a note to <hello@relicquary.com>. Including your operating system and app version (when applicable) helps us help you faster.

## Frequently asked

### Can I use Relicquary today?

Yes, as a developer: the v0.9.0 core (CLI plus MCP server) is in early access. Email [hello@relicquary.com](mailto:hello@relicquary.com?subject=Relicquary%20early%20access) with the subject “Relicquary early access” and the binary arrives by reply. The steps to run it are on [the overview](index.html#get).

### What is the difference between the core and the apps?

The core is the developer surface: one Rust binary serving a CLI and the MCP server, running today. The Mac and iPhone apps wrap that core for everyone else and are coming to the App Store as a one-time purchase, no subscription.

### What does the core run on?

Relicquary v0.9.0 builds and runs on macOS on Apple Silicon. TouchLink requires macOS 13 or later. App minimums will be listed on the App Store at release.

### How do agents connect?

Over the Model Context Protocol: run `relicquary mcp-server` and point any MCP-capable client at it. The one-line config is on [the overview](index.html#get), and every tool is described in [the catalog](tools.html).

### Where is my data stored?

On your own device, as a local SQLite database and Markdown files. Relicquary is local-first: your store stays on your hardware. The only thing that leaves is what you choose to send: prompts to a model provider, if you connect one. See our [Privacy Policy](privacy.html).

### Do I need an account?

No. Relicquary runs without any account or sign-up. Cross-device sync is planned for the iPhone release.

### Does it work offline?

Yes. Recall, capture, and the knowledge graph all run on-device. There is no required network connection.

### What are the system requirements?

The core runs on macOS on Apple Silicon today; TouchLink needs macOS 13+. The upcoming apps target recent versions of macOS and iOS, with exact minimums listed on the App Store at release.

### How do I export or delete everything?

Your data is plain files you control. You can export or permanently delete it at any time from within the app and your operating system's file tools.

## Company

Relicquary is built and maintained by **RQ MCP LLC**. For business or legal inquiries, email <hello@relicquary.com>.


---

# Relicquary privacy policy

*Machine-readable Markdown of https://relicquary.com/privacy.html (content hash 1a07b8c1)*

LEGAL · RQ MCP LLC

# Privacy Policy

Last updated: June 2026

**The short version:** Relicquary is local-first. Your memory data is stored on your own device and is not transmitted to us or to any third party. We do not operate a server that holds your content, and we do not sell or share your data, because we never receive it.

This Privacy Policy explains how RQ MCP LLC (“RQ MCP,” “we,” “us”) handles information in connection with the Relicquary application and the website at relicquary.com (together, the “Service”). By using the Service you agree to this policy.

## 1. Data stored on your device

Relicquary stores the memories, notes, tags, graph, and related content you create as ordinary files (a local SQLite database and Markdown files) on your own device. This content stays under your control. We have no access to it.

## 2. Information we do *not* collect

- We do not collect or store the content of your memories or files on our servers.
- We do not sell, rent, or share your personal data.
- The app does not require an account to function, and does not embed advertising or third-party trackers.

## 3. Optional sync between your devices

If you choose to enable device-to-device sync (planned for the iPhone release), your content is transferred directly between your own devices (for example over your local network, or through your personal Apple iCloud account if you opt in). When iCloud sync is used, that data is handled under [Apple's Privacy Policy](https://www.apple.com/legal/privacy/) and stored in your own iCloud account, not by RQ MCP. Sync is off unless you turn it on.

## 4. Diagnostics

The app does not send analytics or usage telemetry to us by default. If a future version offers optional, opt-in diagnostics to help us fix bugs, it will ask for your consent first and explain what is shared. Any crash reporting provided by Apple is governed by your device's system settings, which you control.

## 5. The website

relicquary.com is a static informational site. If you email us using an address listed on the site, we will receive the contents of your message and your email address, and will use them solely to respond to you.

## 6. Children's privacy

Relicquary is not directed to children under 13. As described above, the app does not collect personal information from anyone (children included), so we hold no personal data about any user, regardless of age.

## 7. Your rights

Because your data lives on your device, you can view, export, or permanently delete it at any time using the app and your operating system's file tools. If you have contacted us by email and want us to delete that correspondence, just ask.

## 8. Changes to this policy

We may update this policy from time to time; we will revise the “last updated” date above when we do.

## 9. Contact

Questions about this policy? Email <hello@relicquary.com>.\
RQ MCP LLC, the company behind Relicquary.


---

# Relicquary terms of service

*Machine-readable Markdown of https://relicquary.com/terms.html (content hash 88738d12)*

LEGAL · RQ MCP LLC

# Terms of Service

Last updated: June 2026

**The short version:** Relicquary and TouchLink are software you buy once and run on your own device. The apps are sold through the Apple App Store; Apple handles payment, billing, and refunds. There is no subscription. Your data stays local; the software is provided as-is, and RQ MCP LLC owns the software and its brand.

These Terms of Service (“Terms”) govern your use of the Relicquary and TouchLink applications and the website at relicquary.com (together, the “Service”), all provided by RQ MCP LLC (“RQ MCP,” “we,” “us”). By downloading, installing, or using the Service, you agree to these Terms. If you do not agree, do not use the Service.

## 1. Buying through the App Store

Our applications are distributed through the Apple App Store. Apple, not RQ MCP, processes your payment and handles billing, receipts, and refunds under Apple's own terms. Each app is a one-time purchase, with no subscription and no recurring charge. Where an app is offered as a universal purchase, a single purchase covers the platforms named on its App Store listing. Apple is a third-party beneficiary of these Terms and may enforce them against you.

## 2. Your license

When you buy an app, RQ MCP grants you a personal, non-exclusive, non-transferable license to install and use it on the Apple devices you own or control, as permitted by Apple's Usage Rules and these Terms. You may not copy, resell, rent, reverse-engineer, or redistribute the software except where that restriction is prohibited by law. The license is yours to use, not to own; we retain everything described in Section 5.

## 3. Local-first, and what that means for you

Relicquary stores your memories, notes, graph, and related content as ordinary files on your own device. You are responsible for that data, including backing it up and keeping your devices and any connected services (for example your own iCloud account or any model provider you connect) secure. Because your data lives on your hardware, its safety depends on your own setup. See our [Privacy Policy](privacy.html) for how information is handled.

## 4. Provided as-is; no warranty of fitness

The Service is provided “as is” and “as available,” without warranties of any kind, whether express or implied, including any implied warranties of merchantability, fitness for a particular purpose, and non-infringement, to the fullest extent permitted by law. We do not warrant that the Service will be uninterrupted, error-free, or fit for any specific use you have in mind. You use it at your own discretion and risk.

## 5. Ownership and intellectual property

RQ MCP LLC owns the Service and all intellectual property in it: the software, source code, designs, and the Relicquary, TouchLink, AIM, and RQ MCP names, logos, and marks. These Terms grant you a license to use the apps; they transfer no ownership. Your own content (the memories and files you create) remains yours. Nothing here gives us any claim to it.

## 6. Limitation of liability

To the fullest extent permitted by law, RQ MCP LLC will not be liable for any indirect, incidental, special, consequential, or punitive damages, or for any loss of data, profits, or goodwill, arising out of or related to your use of the Service. Where liability cannot be excluded, it is limited to the amount you paid for the app giving rise to the claim. Some jurisdictions do not allow these limits, so some may not apply to you.

## 7. Changes to the Service and these Terms

We may update, change, or discontinue parts of the Service, and we may revise these Terms from time to time. When we revise them, we will update the “last updated” date above. Continued use of the Service after a change means you accept the revised Terms.

## 8. Governing law

These Terms are governed by the laws of the State in which RQ MCP LLC is organized, without regard to its conflict-of-laws rules.

## 9. Security & responsible disclosure

Found a security issue? We want to hear about it. Email [hello@relicquary.com](mailto:hello@relicquary.com?subject=Security%20report) with the details: what you found, how to reproduce it, and how we can reach you. Please give us a reasonable window to investigate and ship a fix before disclosing publicly, and avoid accessing or modifying data that isn't yours while you test. We read every report and will acknowledge yours.

## 10. Contact

Questions about these Terms? Email <hello@relicquary.com>.\
RQ MCP LLC, the company behind Relicquary.
