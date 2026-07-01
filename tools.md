# Relicquary tool catalog: 56 MCP tools

*Machine-readable Markdown of https://relicquary.com/tools.html*

# The interface is the product. 56 tools your agent calls over MCP.

Relicquary is not a library you wrap. It is a memory-and-orchestration surface an agent talks to directly, over the Model Context Protocol. Connect any MCP-compatible agent and it gets 56 verbs: remember, recall, hand off, synthesize, audit, and more. Below is every one, what it does, and why it earns its place.

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

## Relicquary runs today.

Stand up a store, serve it over MCP, and your agent has all 56 tools, on your own disk, under your own audit.
