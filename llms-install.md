# Installing ScoreStarling (for AI agents)

ScoreStarling is a hosted remote MCP server. There is nothing to clone, build or run locally, and no API key.

1. Add this server to the MCP settings (in Cline: MCP Servers → Remote Servers, or `cline_mcp_settings.json`):

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

   Keep any servers already in `mcpServers`. Do not add an `Authorization` header.

2. The first request returns 401 with OAuth metadata. The client registers itself (dynamic client
   registration), opens the browser with PKCE, and the user signs in to ScoreStarling (email or Google)
   and selects Allow. Never ask the user for a password or token in the chat.

3. Check the connection: call `get_workflow_guide` with `topic` `recording`, then `list_timbres`.
   Both are read-only and use no credits.

A voice, one instrument or solo piano is free to transcribe; a band uses credits and shows its price first.
The skills in `skills/` describe the complete workflows. Support: https://scorestarling.com/support
