# relicquary.com

Marketing + company site for **Relicquary** — a local memory OS for AI agents.
A product of **RQ MCP LLC**.

Static site (plain HTML/CSS, no build step). Pages:

- `index.html` — home / product landing
- `privacy.html` — privacy policy (required for the App Store + Apple Developer enrollment)
- `support.html` — support / contact / FAQ (App Store support URL)
- `assets/styles.css` — all styles
- `CNAME` — custom domain for GitHub Pages (`relicquary.com`)
- `.nojekyll` — serve files as-is on GitHub Pages

## Local preview

```bash
cd relicquary-site
python3 -m http.server 8080
# open http://localhost:8080
```

## Deploy (GitHub Pages)

1. Push this repo to GitHub.
2. Settings → Pages → Source: deploy from branch `main`, root.
3. The `CNAME` file sets the custom domain to `relicquary.com`.
4. At the DNS host for `relicquary.com`, add records pointing the apex + `www` at GitHub Pages
   (four A records to GitHub's IPs, or an ALIAS/ANAME to `<user>.github.io`), and a `www` CNAME.
   **Leave the existing `MX` records untouched** so Google Workspace email keeps working.

## Deploy (Cloudflare Pages — alternative)

Connect this repo in Cloudflare Pages, or `wrangler pages deploy .`. Add `relicquary.com` as a custom
domain; Cloudflare can also redirect `rqmcp.llc` → `relicquary.com` with a free Redirect Rule.

## Notes

- Contact address used across the site: `hello@relicquary.com` (ensure this alias routes in Google Workspace).
- `rqmcp.llc` should redirect to `relicquary.com`.
