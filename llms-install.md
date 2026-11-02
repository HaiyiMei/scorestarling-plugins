# Installing ScoreStarling (for AI agents)

Choose the user's client before changing configuration. Use the [client installation instructions](README.md#install)
for ChatGPT, Codex, Claude, Claude Code or Gemini CLI. They include the ChatGPT directory link and
stable-branch commands for Claude Code and Gemini CLI. A package installation includes bundled skills;
a direct MCP connection provides hosted tools and workflow guidance without installing native skills.

## Direct MCP connection

ScoreStarling is a hosted remote MCP server. There is no local server to build or run and no
ScoreStarling API key. Do not add a second connection if the user already installed the plugin.

### Codex

If ScoreStarling is not available in the plugin directory, use Codex's MCP connection:

```sh
codex mcp add scorestarling --url https://mcp.scorestarling.com/mcp
codex mcp login scorestarling
```

Complete sign-in in the browser. See [OpenAI's MCP guide](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
for client configuration and OAuth.

### Cline and other MCP clients

In Cline, add a remote server through MCP Servers or merge this entry into `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "scorestarling": {
      "type": "streamableHttp",
      "url": "https://mcp.scorestarling.com/mcp"
    }
  }
}
```

Keep servers already in `mcpServers`. Other clients use their own configuration format; use the same
server URL with Streamable HTTP and OAuth. Do not add an `Authorization` header manually.

### Sign in and check the connection

The first unauthenticated request returns 401 with OAuth metadata. The client follows that metadata,
opens the browser with PKCE, and the user signs in to ScoreStarling (email, Google or Apple) and
selects Allow. Never ask the user for a password or token in the chat.

Check the connection by calling `get_workflow_guide` with `topic` `recording`, then `list_timbres`.
Both are read-only and use no credits. Do not start a transcription as a connection test.

## Start the requested task

A transcription or sheet-music reading covers the whole piece and uses the account's existing credits
when it first opens (30 seconds or less is free); make a free 30-second preview (`preview=true`) only
when the user asks for one. A band's exact price, and opening the rest of a preview, need the user's
agreement first. Read the account's current limits from `get_account_usage`.

The skills in `skills/` describe the complete workflows. For connection and audio handling, see
[integration details](docs/integration.md). Support: https://scorestarling.com/support
