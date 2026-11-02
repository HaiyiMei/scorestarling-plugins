# Development and releases

For installation, see the [README](../README.md#install). For the package and hosted data handling,
see [integration details](integration.md).

This public repository is the canonical source of the plugin. The private product
repository pins it as a Git submodule; backend changes do not release this package.

Run `python3 tests/check_plugin_build.py` and validate both Claude manifests before
release. `python3 scripts/build_plugin.py` builds a deterministic ZIP from the Git
index; `--source working-tree` builds tracked local changes. CI files, tests and
top-level developer scripts are excluded from the ZIP.

When the owner requests a release, update the three manifest versions (`plugin.json`, `.claude-plugin/plugin.json`,
`gemini-extension.json`), commit, and push a matching `v<version>` tag to
release. CI checks the tag and manifests, creates the GitHub ZIP release, and
advances the `release` branch only after checks pass. Claude directory submissions
track that branch, so ordinary commits to `main` do not publish a plugin update.
OpenAI directory uploads and review remain separate steps. Review videos and
reviewer credentials are supplied privately rather than included here.

## Client verification

A valid package and a passing CI run do not establish installation, OAuth, automatic skill selection
or score-panel behavior in a real client. Check these in each intended client before claiming
acceptance. A source commit, a tagged GitHub package and the version installed from a directory are
separate states. OpenAI package uploads, Claude plugin directory submissions and Claude remote MCP
connector listings have separate publication and review processes.

## Shared workflow guidance

OpenAI documents server instructions as guidance used alongside tool metadata. Its MCP
skills extension imports a static snapshot during submission through Scan Tools; it does
not fetch skills at runtime. This package does not implement that extension. See
[server instructions](https://developers.openai.com/plugins/build/mcp-server#create-the-server)
and [skill imports](https://developers.openai.com/plugins/build/skills#import-a-skill-from-mcp).

Support, terms and privacy pages are hosted by the website; changing this package does not deploy them.
