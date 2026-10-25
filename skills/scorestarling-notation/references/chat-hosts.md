# In a chat app: sheet music and score files over the ScoreStarling tools

Read this first when you are a chat app (ChatGPT, Claude, Codex, Gemini) with the ScoreStarling
MCP connection and the music arrives as notation. Starling, the assistant inside ScoreStarling,
stops here: its own instructions cover the conversation. The method (the way in, reading, checking and
correcting the music) is in [SKILL.md](../SKILL.md). The "Shared MCP essentials" at the end are
the server's own rules in compact form, the same for every host, written with the internal tool
names that stay out of replies.

- **Sending a file.** Upload sheet music and score files like a recording: `transcribe_music`
  with the attachment or a link to the file, `prepare_audio_upload`, or the panel. Skip
  `check_recording`. Follow the job with `get_upload_status`
  (`wait_seconds: 20`) until it finishes, then do what its `next_step` says.
- **The panel.** `create_score`'s `panel_prepared: true` means the result includes prepared panel
  data. Reuse it; do not call `open_score` again in the same request unless the user/host reports
  a display failure or a new user request explicitly asks to reopen it. Preparation does not
  prove visibility.
- **Previews.** The user's own score file or notation text shows whole; a PDF or photo read shows its
  first 30 seconds until paid for. If a score tool
  refuses because only a free 30-second preview shows, its message names the exact credits: ask
  the user in one line whether to open the whole piece for exactly that many, as use of credits the
  account already has, not a purchase. Only after a clear yes call `unlock_score` with that number
  and `consent: true`, then read the score again. A preview can't be exported.
- **Files.** Use the host's attachment if it appears; otherwise point to the prepared panel's
  Download menu. Do not paste or reconstruct signed download URLs in chat. Never offer purchases,
  plans or checkout links, even when asked.
- **Proposals.** Preview a new arrangement or interpretation outside the user's goal and apply it
  only after its acceptance.

## Reuse an existing score or saved result

When the user says “reuse the existing result” or “do not start new processing”, first
use `list_scores` and open it once with `open_score` unless this request already returned its
prepared panel. Opening a finished score needs no upload, audio check
or new transcription. Do not ask for information already recorded in that score.

Only if the user explicitly wants a **new score from a saved Pro result**, use the original
recording or `transcribe_music` with its `score_id`, with `provider: mirelo`, instrument review enabled and
`replay_only: true` **at creation**, before the first review. This is available only to enabled
replay accounts. Never require the user to say internal parameter names.

Read `get_pro_instrument_review(start=false)` first. Match the complete historical
`instruments` and flat `pro_options`, including tempo, meter, subdivision, timing and paper;
the candidates already verify this account, original bytes and decoded duration. Different
choices need a different saved result. If no candidate matches, stop and offer to open the
existing score. Do not start fresh detection, processing or another upload.

Confirm matching choices with `confirm_pro_instruments(replay_only=true)`, then read back
the saved guard. If a quote is required, ask once for consent to its exact product credits;
permission to reuse is not payment consent. Keep the same excerpt length; a shorter quote needs its
own matching saved result. Follow the same job and verify the completed
result includes `replayed_from`. Explain this as reusing a saved result, in ordinary language.

<!-- BEGIN MCP ESSENTIALS (generated; edit the source, not this block) -->
## Shared MCP essentials

Use the connected host's authorized tools and respect its file, network and approval boundaries. Guidance grants no account access, upload consent, supplier spending or acceptance of a proposal. Never invent file references, expose upload capabilities or discover credentials.

Use existing ScoreStarling entitlements only. Never offer credit purchases, new subscriptions, upgrades or checkout links in chat, even if asked. Explain limits and covered excerpts. With a zero or insufficient band balance, already-open scores remain viewable and editable; account-permitted PDF and audio exports remain available.

When the user says reuse the existing result or do not start new processing, first list_scores; open_score once if no panel result was already prepared for this score/request. do not upload, check_recording or transcribe_music merely to reopen a score. Only for an explicitly requested new score from a saved Pro result, use the original upload or transcribe_music with its score_id, provider=mirelo, review_instruments=true and replay_only=true from creation (enabled replay accounts only). Read get_pro_instrument_review(start=false) first. replay_candidates verify this owner, original bytes and decoded length; compare every historical instrument and flat pro_options with the requested choices. No matching candidate means stop and offer the existing score; never start detection, fresh processing or a replacement. Confirm matching complete choices with replay_only=true, then read back pro_review.replay_only=true. Keep the same excerpt length; a shorter quote needs its own matching saved result, otherwise stop. If a quote is required, ask once for its exact product credits; reuse permission is not payment consent. Follow the same job and verify completed.replayed_from. Explain saved-result reuse in plain words; the user does not need to name internal fields.

panel_prepared=true confirms prepared data, not visibility. Reuse the returned panel (an upload or transcription panel becomes the score); call open_score again only for a reported display failure or a request to reopen, or once if this conversation returned no score/upload panel.

Video links: inspect actual frames before choosing a source; watch_link provides times/crops without a score_id. Read visible notation with create_score and review against the source; otherwise transcribe audio when no notation is visible or the performance is explicitly requested. Missing or blurry frames do not prove absence: seek readable evidence or report the limitation, never invent bars. Finish the requested score in ScoreStarling. The notation skill explains the complete video-reading workflow.

Sheet music and score files (PDF/images, MusicXML/MXL, MIDI, ABC, Guitar Pro with its TAB) use the same upload paths but are read, not audio-transcribed: skip check_recording; no engine choice, tempo detection or provider fee applies. Use local for their upload route. Clean PDFs/flat scans suit the reader. For phone photos, handwriting, jianpu or lead sheets, read the source and write ABC with create_score; also use create_score for music typed/described/composed in chat. Prefer a PDF when both are given.

Poll get_upload_status(job_id, wait_seconds=20) in this turn until terminal; never reupload or finish with an ID or request to keep waiting. Give brief plain progress. HTTP 202 is acceptance, not completion. Inspect the original job after ambiguous responses; never blindly retry a mutation or paid job. On failed/needs_review follow can_recover/next_step: pending instruments and quotes need explicit approvals; recover_pro_result resumes the same accepted Pro task; otherwise stop for review. Quota estimates are not billing receipts.

After reading or create_score, call review_score and compare its page picture with the source bar by bar: pitches, accidentals, octaves, rhythms, ties, key/meter and chord symbols (measures="9-12" zooms in). For a playable/faithful score, correct clear misreadings before finishing; do not merely list errors and wait for another user prompt. Keep corrections in this score: edit_score for supported changes, otherwise a MusicXML copy (note ids kept) saved with revise_score, which also adds missed notes. If only an ABC reconstruction can repair the reading, preserve the draft and compare the replacement with the source and playback. Prefer source-supported local edits to preserve correctly read music. If create_score replaces a draft, compare every new-versus-old pitch/rhythm change against enlarged original pages: clef, key, staff position, accidentals, grace notes, ties and neighbouring bars. Preserve the draft. Validation and a model calling it corrected do not prove fidelity; unverified changes remain uncertain, so do not declare complete accuracy. Change notes only where the source supports them, never by comparing shapes alone; report uncertain bars and ask for a clearer source when needed. Do not reengrave notation imports from playback. bpm supplies playback tempo when needed; report the score/file tempo or the 100 BPM fallback, never a detected audio tempo.

A provider result is an editable starting score, not a publication-ready verdict. Reuse the provider's available detection, notation and original exports before inventing replacement processing. Keep the original and reversible revisions. Work toward accurate, clear, playable notation: check coverage, instrument assignment, pitches, rhythm, meter, voices, clefs, ties and spacing against the recording or written source. Inspect every exported page, including page turns and dense passages. Use get_score, review_score (with its checks), previews and edit_score for evidence-based corrections within the user's request; no guessed deletions or merges. Structural checks and MIDI hashes do not prove musical accuracy. Choose style/texture hypotheses from full phrases and source evidence: opening rests, offbeat harmony, three voices, crossing hands, ornaments, swing and rubato can be genuine; no fixed rhythm ratios or left-hand eighth-note template. Separate performance, structure, notation and authorized arrangements. Keep a faithful master for learner reductions. Say what was actually listened to and what remains uncertain; report accuracy, readability and playability separately. Pro is powered by Mirelo: its original PDFs (original_pdf is the full score unless one part or tab is selected, with tuning source; original_scores the ZIP) engrave the unedited result only, exclude later edits (then call them the original) and are not a claim of final quality.

set_staff moves played notes of a two-staff part to the other hand's staff as a notation edit: ids, pitches, timing, ties and playback stay, the receiving hand's clef follows its notes (leave clef out unless the user names one), and it refuses a part on one staff or part of a tuplet or slur. For a passage over many bars give select {measures "1-28", voice?, below?/above? MIDI} instead of note_ids: it takes the other staff's notes there (read one bar with get_score first to see which voice the accompaniment is). Re-engraving operations (reengrave, rebeat, scale_note_values) keep printed marks on the notes they stand on, with their IDs; chord symbols and tuplets still block them. edit_score has no swing/grace/arpeggio/pedal entry (voice, tie, slur, tuplet, beam, stem and shift_time are operations): write those in a MusicXML copy and save it with revise_score (kept notes keep their played timing; new pitches, removed and added notes reach playback). Score-based revisions follow the new notation; original performances remain evidence. Legacy operations do not edit performance onsets/offsets freely or one passage's tempo map (rebeat replaces a solo-piano score's whole beat, swing included). set_duration changes playback note-offs; rebeam only changes grouping; global voice/grid options cannot replace local editing. Read live schemas and operation restrictions. Report unsupported corrections without inventing actions or destructive workarounds. ABC reconstruction needs source comparison and representation checks. Inspect all exported pages and audition changed passages when possible; structural validation, MIDI preservation and cleaner pages do not prove musical accuracy.

get_score provides current revision and IDs. edit_score applies one operation to an existing score; revise_score saves its edited copy with note IDs, recording comparison, panel and undo history retained. create_score: arrangement; source_score_id inherits media by default; original stays. Requested corrections, removals included, save undoable versions whose results identify changes. Panel numbered requests are ordered edits. preview_score_edit or revise_score(preview=true) leaves proposed changes pending; the panel offers Apply/Discard. apply_score_preview commits the specific preview accepted by the user. Stale revisions are rejected.

When document_model.playback_basis=score, notation defines the notes, rhythm and sound; original MIDI is historical evidence, never a write constraint. include_source=true reads its original pitches/events separately. Preserve user_modified_fields during automatic refinement; an explicit user request may replace those decisions. Score seconds do not locate the recording: listen/watch by bars uses recording alignment and reports gaps. set_recording_alignment repairs one measure/visit with user-confirmed recording-second anchors. adopt_score creates an owner-requested score-playback migration as a new revision, preserving legacy history and its hashed MIDI reference.

Say only what tool results show: an edit is made when its result lists it; an error or "Nothing changed" means not, so say so. Say how bars are written (clefs, key, notes) from get_score or review_score text, not a picture or the opening settings; if the user disputes it, reread those bars.

Structural validation does not prove transcription accuracy; doubtful_notes are leads to listen to, not a verdict. Score-based MIDI/audio exports compile the selected notation; legacy MIDI/audio exports require complete performance bindings. On an account without existing download access (access.open false) MusicXML, MIDI, Guitar Pro, ABC and MEI are refused with locked=true and PDFs carry a small footer line; never unlock_score for a download. A preview (30 seconds) needs unlock_score, with explicit consent to its exact credits, before anything else. Use a host-presented attachment; otherwise the prepared panel Download menu for the requested format. Never paste/reconstruct download_url in chat. A ResourceLink does not prove receipt. A plain PDF request uses format=pdf and follows the saved view, like Download; do not silently substitute Mirelo's original PDF. Use original_pdf only when requested and label it as the original. Audio exports are synthesis, not original stems. reference_midi downloads preserved initial/historical performance evidence, not the current score or a supplier original; it covers the whole score and obeys the MIDI download entitlement.

Show a score as staff or jianpu (简谱: jianpu 1=key, jianpu_fixed 1=C 固定调, jianpu_melody) with set_notation_view: the score keeps it, the prepared panel and Download PDF follow; without a prepared panel result, open_score once with notation; before it exists, pass view to the tool making it. export_score takes the same names; jianpu_voices only if asked for a hand's voices apart.

Guitar TAB (六线谱, also bass and ukulele) is a score setting, not a view: edit_score set_tablature (view both puts TAB under the staff, tab shows TAB only; tuning and capo as the user says; strings hand when they want fewer hand shifts), then the panel, PDF and MusicXML show it. set_string moves a note to another string at the same pitch; set_fret writes a fret on a string. export_score tab_text returns text TAB to paste in your answer; guitar_pro is a Guitar Pro file (.gp5) with the TAB, tuning and capo, for Guitar Pro, TuxGuitar or Songsterr. TAB adds no credits.

Call send_feedback once only after the user explicitly expresses an opinion of a result, with their own words as a non-empty comment and the revision they judged. Never supply your own rating or solicit one. Feedback grants no consent to share the recording.
<!-- END MCP ESSENTIALS -->
