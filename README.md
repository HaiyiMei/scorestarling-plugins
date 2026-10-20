# ScoreStarling

[![ScoreStarling MCP connector](https://glama.ai/mcp/connectors/com.scorestarling/scorestarling/badges/score.svg)](https://glama.ai/mcp/connectors/com.scorestarling/scorestarling)
[![Mentioned in Awesome](https://awesome.re/mentioned-badge.svg)](https://github.com/hashgraph-online/awesome-ai-plugins)

Transcribe, read, convert and edit sheet music. Move music between
sound, pictures, documents and score files. Start from an audio or video recording, a sheet-music image or PDF, MIDI, MusicXML, ABC, Guitar Pro,
numbered notation, a lead sheet or music written in chat. Create an editable,
playable score, review or preview changes, and export PDF, SVG/PNG images, MusicXML,
MIDI, Guitar Pro (.gp5), MP3/WAV audio, ABC, MEI, parts or numbered notation.

This plugin combines the hosted ScoreStarling MCP tools with two workflow skills:
`scorestarling-score` for audio/video recordings and `scorestarling-notation` for
sheet music, score files and music written in the chat.
Task skills add musical know-how on top: `scorestarling-arrange-for-level` arranges a piece for a chosen
instrument and level (piano, strings, winds, brass, recorder, guitar, ukulele, voice, drums and the Chinese
erhu, guzheng and dizi; from complete beginner to about ABRSM Grade 8), and checks the result with a
bundled script. It loads only the reference for the chosen instrument, and asks for the instrument and the
level when the request does not say.
It is maintained by individual developer HaiyiMei.
The OpenAI listing uses the verified developer name HAIYI MEI.

## Access and use

Sign in with a ScoreStarling account and approve the MCP connection through the
client’s OAuth flow. A free account runs one transcription at a time, and Plus up to five.

Ask: "Turn this attached recording into a score, open it, and help me check it." or
"Make this photo of sheet music playable and give me the MIDI."
Every new piece is a free 30-second preview; the whole piece of one instrument or voice, or of solo
piano with both hands and pedal, uses 10 credits, and a band uses 30 credits a minute.
Uploads are limited to 95 MiB. Each transcription covers the first six minutes of a recording, the
same for every account.
Read `get_account_usage.max_seconds` for its current limit before starting. A band's
price is shown, and agreed in the chat, before it starts, and so are the credits for opening a
whole piece. The skill checks tool results and score structure,
but listening and human review remain necessary for transcription accuracy.
Model-proposed musical edits are previews until the user accepts them.

Editing and listening use no credits. Downloads follow the account: MusicXML, MXL, MIDI, Guitar
Pro, ABC and MEI download on accounts with existing download access; other accounts get the PDF and
page images with a small watermark, and their own imported files in their original format.
Download access comes from active Plus or preserved historical rights; buying credits alone does not open it.
Previews can't be exported. An assistant saves its own round of edits as one version, a batch of
operations or an editing copy, which works on every opened score. When the user gives a ScoreStarling invitation
link or a beta code, the assistant redeems it in the chat (free credits, not a purchase); it offers
the user's own invitation link only when they ask to invite someone. A new user without a recording
can start from a public sample recording.

## What connects and runs

The plugin connects only to `https://mcp.scorestarling.com/mcp`; audio uploads go to
`https://scorestarling.com`. The client's authorized MCP connection reads or changes
the signed-in user's scores and starts requested transcriptions. When the user
chooses a band transcription and agrees to its price, the service sends the recording to
Mirelo, the band transcription provider, within a limit the server sets from the recording's
length; the user sees only the price in credits.
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

### Embedded-app tools and audio handling

A complete connector declaration includes these app-only tools as well as
the model-facing tools. Their MCP metadata keeps `ui.visibility` set to
`["app"]`; declaring them changes neither that visibility metadata nor the
account authorization checks.

| Tool | What it does |
| --- | --- |
| `account_preferences` | Reads or saves interface preferences for the signed-in account after verifying access to the panel’s score. It never changes notes or sends queued chat requests. |
| `begin_audio_upload` | Reserves an account-scoped upload task from file metadata and returns its single-use upload capability to the app. |
| `panel_feedback` | Saves the user's panel feedback for a score revision, including recording-sharing consent only when explicitly selected. |
| `read_notation_view` | Reads rendered numbered-notation pages for an owned score revision without changing the music. |
| `read_score_panel` | Reads the interactive panel for the current or a specified saved score revision. |
| `save_score_edits` | Saves edits the interactive panel already drew itself, in order, on the exact saved revision. |
| `score_panel_state` | Reads the current saved revision, pending preview and display preference to synchronize an existing panel. |

`begin_audio_upload` receives the filename, exact size and processing options,
not the audio itself. Its app metadata contains a ten-minute, single-use upload
URL. The panel sends the bytes to ScoreStarling over HTTPS; the service validates
the size and retains the recording with that account's task in private hosted
storage. Lossless audio may be compressed to MP3 for storage and processing.
The task then queues or waits for required instrumentation and price consent.
One-instrument and piano processing run on ScoreStarling. The selected band
workflow uses Mirelo for instrument analysis and transcription; paid transcription
waits for the required price consent. Reserving an upload does not itself send
audio to Mirelo. Playback/audio exports synthesize the saved notes rather than
create audio through a generative AI model. Retention and processing disclosures
are in the service's [privacy policy](https://scorestarling.com/privacy).

## Distribution and support

The portable `plugin.json` / `mcp.json` package is for ChatGPT and Codex. Claude's
`.claude-plugin/plugin.json` and `.mcp.json` reference the same skill and service.
This package does not include the backend, a local MCP server, hooks or subagents.
Gemini CLI reads `gemini-extension.json` at the repository root (the same remote server with OAuth,
plus the skills): `gemini extensions install https://github.com/HaiyiMei/scorestarling-plugins`.
Actual installation and automatic skill selection must be checked in each client
before publishing. Public publication on Claude requires a public GitHub source
and a separate submission of our remote MCP connector.

A direct MCP connection receives concise initialization instructions, tool metadata and
state-dependent next steps, plus `get_workflow_guide` for recording, notation, editing, each
edit action's limits (operations) or feedback. It does not install native skills. The complete workflows remain in these two
skills. The section between their `MCP ESSENTIALS` markers is generated from the same rules the
server's instructions use and is refreshed from the product repository; edit the rules there rather
than the marked section.

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

## Development and releases

This public repository is the canonical source of the plugin. The private product
repository pins it as a Git submodule; backend changes do not release this package.

Run `python3 tests/check_plugin_build.py` and validate both Claude manifests before
release. `python3 scripts/build_plugin.py` builds a deterministic ZIP from the Git
index; `--source working-tree` builds tracked local changes. CI files, tests and
top-level developer scripts are excluded from the ZIP.

Update the three manifest versions (`plugin.json`, `.claude-plugin/plugin.json`,
`gemini-extension.json`), commit, and push a matching `v<version>` tag to
release. CI checks the tag and manifests, creates the GitHub ZIP release, and
advances the `release` branch only after checks pass. Claude directory submissions
track that branch, so ordinary commits to `main` do not publish a plugin update.
OpenAI directory uploads and review remain separate steps. Review videos and
reviewer credentials are supplied privately rather than included here.
