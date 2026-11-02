# Integration details

For installation and first requests, see the [README](../README.md#install).
This document describes the package, agent workflows and hosted data handling.

## Files and bundled skills

It starts from an audio or video recording, a sheet-music image or PDF,
MIDI, MusicXML, ABC, Guitar Pro, numbered notation, a lead sheet or music written in chat, and exports
PDF, SVG/PNG images, MusicXML, MIDI, Guitar Pro (.gp5), MP3/WAV audio, ABC, MEI, parts or numbered
notation.

This plugin combines the hosted ScoreStarling MCP tools with two workflow skills:
`scorestarling-score` for audio/video recordings and `scorestarling-notation` for
sheet music, score files and music written in the chat.
Task skills add musical know-how on top: `scorestarling-arrange-for-level` arranges a piece for a chosen
instrument and level (piano, strings, winds, brass, recorder, guitar, ukulele, voice, drums and the Chinese
erhu, guzheng and dizi; from complete beginner to about ABRSM Grade 8), and checks the result with a
bundled script. It loads only the reference for the chosen instrument, and asks for the instrument and the
level when the request does not say.

The portable `plugin.json` / `mcp.json` package is for ChatGPT and Codex. Claude's
`.claude-plugin/plugin.json` and `.mcp.json` reference the same skills and service.
Gemini CLI reads `gemini-extension.json` at the repository root. This package does not include the
backend, a local MCP server, hooks or subagents.

## Agent workflows

A direct MCP connection receives concise initialization instructions, tool metadata and
state-dependent next steps, plus `get_workflow_guide` for recording, notation, editing, each
edit action's limits (operations) or feedback. It does not install native skills. The recording and
notation skills contain the complete base workflows. The section between their `MCP ESSENTIALS` markers
is generated from the same rules the
server's instructions use and is refreshed from the product repository; edit the rules there rather
than the marked section.

Read the account's own upload size, recording coverage (`max_seconds`) and concurrency
(`active_limit`) from `get_account_usage`. Use the hosted MCP tools for account-scoped actions and
the skills for the transcribe, review, preview, accept and export workflow. Start with an actual
chat attachment; the code upload helper and built-in upload panel are fallbacks.

An assistant saves its own round of edits as one version, a batch of
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
| `cancel_pro_review` | Cancels a held band instrument review for a panel opened before `cancel_transcription` took this over. |
| `cancel_transcription_quote` | Cancels a held band price for a panel opened before `cancel_transcription` took this over. |
| `listen_score` | Hears up to 16 bars of a score's own recording again, for hosts that listed it before `review_score` took this over (`check=listen`). |
| `panel_feedback` | Saves the user's panel feedback for a score revision, including recording-sharing consent only when explicitly selected. |
| `read_notation_view` | Reads rendered numbered-notation pages for an owned score revision without changing the music. |
| `read_score_panel` | Reads the interactive panel for the current or a specified saved score revision. |
| `save_score_edits` | Saves edits the interactive panel already drew itself, in order, on the exact saved revision. |
| `score_panel_state` | Reads the current saved revision, pending preview and display preference to synchronize an existing panel. |
| `transcribe_again` | Transcribes a score's recording again as a new score, for the panel's Transcribe again and panels opened before `transcribe_music` took this over. |
| `transcribe_attachment` | Makes a new score from an attached file, for panels opened before `transcribe_music` took this over. |
| `transcribe_link` | Makes a new score from a public link, for panels opened before `transcribe_music` took this over. |
| `validate_score` | Lists a saved revision's structural issues, for hosts that listed it before `review_score` took this over (`check=structure`). |
| `watch_score` | Shows frames of a video-based score's own video, for hosts that listed it before `review_score` took this over (`check=watch`). |

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
