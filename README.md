# ScoreStarling

[![Install in ChatGPT](https://img.shields.io/badge/ChatGPT-Install%20plugin-000000)](https://chatgpt.com/plugins/plugin_asdk_app_6ac3484e9e408191bcd88bf7ea90a67e)
[![ScoreStarling MCP connector](https://glama.ai/mcp/connectors/com.scorestarling/scorestarling/badges/score.svg)](https://glama.ai/mcp/connectors/com.scorestarling/scorestarling)
[![Mentioned in Awesome](https://awesome.re/mentioned-badge.svg)](https://github.com/hashgraph-online/awesome-ai-plugins)
[![Mentioned in Awesome](https://awesome.re/mentioned-badge.svg)](https://github.com/punkpeye/awesome-remote-mcp-servers)

ScoreStarling is an all-in-one AI sheet music assistant. Ask for anything to do with sheet music:
transcribe a song, read a PDF or photo, add chords, change the key, make it easier, turn it into guitar
TAB or numbered notation (jianpu) or arrange it for your instrument. Every change lands on a real score
you can hear, fix and download.

## Install

Choose your client below, then sign in with a ScoreStarling account and allow access when prompted.
ScoreStarling runs on a hosted service; you do not need a local server or a ScoreStarling API key.

| Client | Install |
| --- | --- |
| ChatGPT | Open [ScoreStarling in the plugin directory](https://chatgpt.com/plugins/plugin_asdk_app_6ac3484e9e408191bcd88bf7ea90a67e), select **Install plugin**, then connect your account. [Steps with pictures](https://scorestarling.com/mcp#chatgpt). |
| Codex | Open the plugin directory (`/plugins` in the CLI) and search for **ScoreStarling**. If it is not listed for your account, use the [direct MCP connection](llms-install.md#codex). |
| Claude | Add a [custom connector](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) with the server URL `https://mcp.scorestarling.com/mcp`, then connect your account. |
| Claude Code | Install from this repository's marketplace with the [commands below](#claude-code). |
| Gemini CLI | Install this repository as an extension with the [command below](#gemini-cli). |
| Cline and other MCP clients | Follow the [direct MCP connection guide](llms-install.md#direct-mcp-connection). |

### Claude Code

Run these commands in a Claude Code session:

```text
/plugin marketplace add HaiyiMei/scorestarling-plugins#release
/plugin install scorestarling@scorestarling
```

### Gemini CLI

Run this command in your terminal, then restart the Gemini CLI session:

```sh
gemini extensions install https://github.com/HaiyiMei/scorestarling-plugins --ref release
```

The commands above use the stable `release` branch. Installing this package includes its bundled
skills; a direct MCP connection provides the hosted tools and workflow guidance without installing
native skills. See [files, skills and integration details](docs/integration.md).

## Try it

- "Turn this attached recording into a score, open it, and help me check it."
- "Make this photo of sheet music playable and give me the MIDI."

A transcription can contain pitch, rhythm or notation errors. Listen and review the result;
the skill's checks do not establish transcription accuracy. Proposed musical edits stay in preview
until you accept them.

## Credits and downloads

A transcription or sheet-music reading covers the whole piece and uses credits the account already
holds when it first opens (30 seconds or less is free); the assistant says so as it starts. You can
ask to try a free 30-second preview first. A band's exact price, and opening the rest of a preview,
are agreed in the chat before any credits are used. Nothing is sold in ChatGPT or Claude.

Editing and listening use no credits. Downloads follow the account: MusicXML, MXL, MIDI, Guitar Pro,
ABC and MEI download on accounts with existing download access; other accounts get the PDF and page
images with a small watermark, and their own imported files in their original format. Download access
comes from active Plus or preserved historical rights; buying credits alone does not open it.
Previews cannot be exported. [Plans, credits and limits](https://scorestarling.com/pricing).

## Privacy and access

The connection can read or change the signed-in user's scores and start requested transcriptions.
Recordings and scores are processed and stored by the hosted ScoreStarling service. A band
transcription sends the recording to Mirelo after the required agreement to its price.
See the [privacy policy](https://scorestarling.com/privacy) and
[connection and audio-handling details](docs/integration.md#what-connects-and-runs).

## Versions and development

`main` contains development source. The `release` branch and
[GitHub Releases](https://github.com/HaiyiMei/scorestarling-plugins/releases) contain tagged packages.
Directory installations use the version offered by that directory. Each directory has its own
publication and update process; check its available version separately from GitHub Releases.
See [development and releases](docs/development.md) for checks and publication steps.

## Support

- [Connection guide](https://scorestarling.com/mcp)
- [AI installation guide](llms-install.md)
- [Support](https://scorestarling.com/support)
- [Service terms](https://scorestarling.com/terms)

Maintained by individual developer HaiyiMei; the OpenAI listing uses the developer name HAIYI MEI.
The plugin files are licensed under [MIT](LICENSE). That license does not cover customer audio,
customer scores or the hosted backend.
