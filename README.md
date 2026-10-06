# ScoreStarling

Turn an audio recording or sheet music into an editable score, compare it with the
original, preview musical changes, and export MusicXML, PDF, MIDI, audio, jianpu, ABC
or MEI. This plugin combines the hosted ScoreStarling MCP tools with two workflow
skills: `scorestarling-score` for recordings and `scorestarling-notation` for sheet
music, score files and music written in the chat.
It is maintained by individual developer HaiyiMei.
The OpenAI listing uses the verified developer name HAIYI MEI.

## Access and use

Sign in with a ScoreStarling account and approve the MCP connection through the
client’s OAuth flow. Each account can run two transcriptions at a time.

Ask: "Turn this attached recording into a score, open it, and help me check it." or
"Make this photo of sheet music playable and give me the MIDI."
Standard suits one instrument or voice; Piano suits solo piano, with both hands and pedal.
Uploads are limited to 50 MiB, or 120 MiB as WAV, AIFF or FLAC. Each transcription covers the account’s supported excerpt, up to five minutes.
Read `get_account_usage.max_seconds` for its current limit before starting. Any
required processing consent is requested before Pro starts. The skill checks tool results and score structure,
but listening and human review remain necessary for transcription accuracy.
Model-proposed musical edits are previews until the user accepts them.

## What connects and runs

The plugin connects only to `https://mcp.scorestarling.com/mcp`; audio uploads go to
`https://scorestarling.com`. The client's authorized MCP connection reads or changes
the signed-in user's scores and starts requested transcriptions. When Mirelo is
available and explicitly selected, the service sends the recording to that provider
within a supplier limit the server sets from the recording's length; the user sees only the credit quote.
The service's privacy policy covers Supabase/Railway storage and Sentry/PostHog
diagnostics.

ChatGPT uses its native attachment tool. For a readable local attachment, the
optional Python 3.11 upload helper requires HTTPX and network access. It receives
an explicitly prepared, one-use upload ticket on stdin, posts raw audio once to
the matching ScoreStarling origin, and reports acceptance. Status checks use the
connected host's tools. Its programmatic entry can prepare and poll through an
already-authorized tool callback. It installs nothing and reads no environment
credentials. It sends no OAuth token or cookie on the capability POST and follows
no redirects. If code or network is unavailable, use the built-in upload panel.

## Distribution and support

The portable `plugin.json` / `mcp.json` package is for ChatGPT and Codex. Claude's
`.claude-plugin/plugin.json` and `.mcp.json` reference the same skill and service.
This package does not include the backend, a local MCP server, hooks or subagents.
Actual installation and automatic skill selection must be checked in each client
before publishing. Public publication on Claude requires a public GitHub source
and a separate submission of our remote MCP connector.

A direct MCP connection receives concise initialization instructions, tool metadata and
state-dependent next steps, plus `get_workflow_guide` for recording, notation, editing, each
edit action's limits (operations) or feedback. It does not install native skills. The complete workflows remain in these two
skills; their marked MCP essentials share `apps/server/workflow_guidance.py` and are checked
by `scripts/sync_workflow_guidance.py`. After editing those shared rules, run the script with
`--write` and run `tests/mcp/check_workflow_guidance.py`.

OpenAI documents server instructions as guidance used alongside tool metadata. Its MCP
skills extension imports a static snapshot during submission through Scan Tools; it does
not fetch skills at runtime. This package does not implement that extension. See
[server instructions](https://developers.openai.com/plugins/build/mcp-server#create-the-server)
and [skill imports](https://developers.openai.com/plugins/build/skills#import-a-skill-from-mcp).

Use the hosted MCP tools for account-scoped actions and the skill for the
transcribe, review, preview, accept and export workflow. Start with an actual
chat attachment; the code upload helper and built-in upload panel are fallbacks.

- [Connection guide](https://scorestarling.com/mcp)
- [Support](https://scorestarling.com/support)
- [Privacy](https://scorestarling.com/privacy)
- [Service terms](https://scorestarling.com/terms)

The plugin files are licensed under MIT; see [LICENSE](LICENSE). This package's
license does not cover customer audio, customer scores or the hosted backend.
Support, terms and privacy pages are hosted by the website; changing this
package does not deploy them.
