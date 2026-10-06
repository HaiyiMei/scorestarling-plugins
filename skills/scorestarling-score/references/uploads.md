# Getting a recording in: the other routes

Read this when the recording is neither a ChatGPT attachment nor a link: a file you can read
with code, a user who wants an upload link to send the file themselves, no access to the file at
all, or a local server. Choosing the transcription and following the job are steps 2 and 4 of
SKILL.md; everything here ends with following the returned `job_id` there.

| Situation | Route |
| --- | --- |
| A readable file, with code and network access (Claude, Codex) | Send the bytes yourself |
| The user wants a link to send the file themselves | An upload link for the user |
| No readable file, no code or no network | The panel |
| A local ScoreStarling server (stdio) | Its own input folder |

Every route takes the same choices as the other tools: `provider`, `bpm` only when the user gave
the tempo, and `view=jianpu` when the user wants numbered notation from the start. Files are
limited to 100 MiB.

## Send the bytes yourself

1. Get the real filename and the exact byte count of the file.
2. Call `prepare_audio_upload` with `filename`, `size` and the chosen `provider`. It returns a
   `job_id` and a one-use upload link that works for ten minutes.
3. POST the actual raw bytes once to that link, with `Content-Type: application/octet-stream`.
   Never put audio into tool arguments, and never show the upload link in the conversation.
4. Follow the `job_id` with `get_upload_status` and `wait_seconds: 20`.

HTTP 202 means the upload was accepted. After a timeout, a refusal or an unclear answer, inspect
the existing job; never POST again or prepare another upload for the same request.

### The upload helper script

The skill ships `scripts/upload_audio.py` (in this skill's folder, next to SKILL.md) for
runtimes that can run Python but would rather not write the POST themselves.

- Use the connected host's authorized `prepare_audio_upload` tool with the real filename, byte
  count and chosen provider. Its one-use upload ticket is the only capability the script needs:
  do not read environment credentials or extract tokens from another application.
- Add `size` to the ticket JSON with the exact count passed to the tool, and pass that JSON
  privately on stdin, keeping the URL out of command arguments:

  ```sh
  python scripts/upload_audio.py /path/to/audio.wav < /path/to/private-upload-ticket.json
  ```

- The script needs Python 3.11 and `httpx`, installs nothing and uses no repository imports.
  `--site` selects a trusted deployment (default `https://scorestarling.com`) or an HTTP
  loopback origin, and the ticket's upload link must be on it. It sends the raw bytes once and
  prints only the job ID and an upload-acceptance flag.
- Then follow that job with the connected `get_upload_status` tool (`wait_seconds: 20`) and
  continue as its `next_step` says. A timeout or a false acceptance flag means inspecting the
  existing job, not repeating the POST.
- Keep the ticket temporary and private, and remove the ticket file after the run.
- A runtime that provides an already-authorized tool-call function can use the script's
  `upload_audio` function instead: it also prepares the upload and polls, within a time limit,
  through that function, with no credential discovery.
- If code, dependencies or the network are unavailable, use the panel. Claude API skill
  containers cannot make this network upload; an application-side authorized tool or the panel
  has to handle it.

## An upload link for the user

When the user asks for a link to send the file themselves, call `prepare_audio_upload` without
`size`; never ask them for the byte count or the length. Give them the link with:

```sh
curl -X POST -H 'Content-Type: application/octet-stream' --data-binary @FILE LINK
```

It works once, for ten minutes. Then follow its `job_id` as usual.

## The panel

When there is no readable file, no code execution or no network access, explain what is missing
and offer `open_studio`, so the user can choose the file or record in the panel. Pass `engine`
when the instrument is known (`piano` for solo piano) so the panel preselects it. Opening the
panel starts nothing. You are not told when a panel job finishes: the panel offers the user a
button that asks you to check the new score, and `list_scores` finds the newest one.

## A local server

A local stdio ScoreStarling server reads only files already in its own `data/input` folder: use
`list_audio` and `transcribe_audio` for those. A path in your sandbox is not a path on a remote
server.
