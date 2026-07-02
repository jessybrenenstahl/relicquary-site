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
