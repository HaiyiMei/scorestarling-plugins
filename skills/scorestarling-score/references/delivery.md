# Views, pages and files

Read this to show a score as numbered notation, lay out its pages, export it, or explain what an
account downloads. In a chat app, how a file reaches the user is step 7 of
[chat-hosts.md](chat-hosts.md).

- **Numbered notation** (jianpu, 简谱, "show it as numbers"): `set_notation_view` with
  `view=jianpu`; the open panel switches within a few seconds, and `view=staff` switches back. The score keeps the choice, in the workspace too, until it is
  switched back: tell the user. The view is drawn read-only from the last saved revision; your
  edits work as usual and the numbered view follows them.
- **Pages** (bars per line, where lines and pages break, fitting fewer pages, a staff too big or
  small): `edit_score` with `layout`. Notes and playback stay; the pages, PDF and panel follow.
  Read the `get_score` overview's `layout` first (each page's lines as bar ranges), then look at
  the pages with `review_score` after. Never edit `<print>`, `<scaling>` or `<system-layout>` in
  the MusicXML for this, and never send the user to MuseScore to lay out pages:
  [editing.md](editing.md#page-layout).
- **Files:** apply the requested changes first, then re-read the current revision (after a
  proposal, the one the user accepted), validate it and call `export_score` for it.

| Wanted | `format` |
| --- | --- |
| Printable sheet music | `pdf`, which follows the saved view (staff or numbered) like the panel's PDF button; `layout_pdf` for staff notation whatever the view; add `part_id` for one part, or use `format=parts` for a ZIP of every part |
| Page images | `pages` (SVG and PNG) |
| Notation software (MuseScore, Sibelius, Finale, Dorico) | `musicxml` or `mxl` (accounts with existing download access) |
| MIDI | `midi` (accounts with existing download access) |
| Listening audio | `mp3` or `wav`: the score's playback, synthesized, not the original recording |
| Numbered notation (PDF) | `jianpu` (every staff), `jianpu_melody` (the top line, usually but not always the tune) or `jianpu_fixed` (fixed do); or set the view and use `pdf` |
| ABC text to read or rewrite | `abc` (accounts with existing download access; the text also comes back in the result). To read the notes yourself, `get_score` or an editing copy |
| Music research | `mei` (accounts with existing download access) |
| Guitar TAB | `guitar_pro`, a Guitar Pro file (.gp5) with the TAB, tuning and capo (accounts with existing download access); `tab_text`, text TAB to paste in a reply |

- Jianpu is movable do in the score's key (`1=` the key; a minor key reads from its relative
  major's do). `jianpu_fixed` writes the same pitches with 1 always C and every black key marked
  (in G♭ major, b5 and b7), for players who read keys rather than degrees (固定调). Use
  `jianpu_voices` or `jianpu_fixed_voices` only when asked to show a hand's voices apart.
- Music printed without a key signature, every accidental written out, comes out as 1=C; when it
  is clearly in another key, offer `set_key` so the jianpu reads in that key. For A minor, `1=C`
  means the tonic is 6; it does not mean A major. Use full `jianpu` for both hands; check every
  staff's digits, octave dots, rhythms and key changes in the exported result. Changing the
  notation view does not simplify the music or prove multi-voice export fidelity.
- MIDI and audio need every note bound to the playing; MusicXML and PDF still export when some
  are not. Say so when it happens.
- **Downloads follow the account.** MusicXML, MXL, MIDI, Guitar Pro, ABC and MEI download on
  accounts with existing download access. Other accounts (`access.open` false in the panel and
  export results) get the PDF, page images and numbered-notation PDFs, with one small footer line ("Made with
  ScoreStarling"; mention it only if asked), and their own imported files in their original
  format. When `export_score` comes back `locked`, do not retry or work around it, and do not
  call `unlock_score` for a download: offer the PDF instead. An editing copy works on every opened score.
- A band score's original engraving (`original_pdf`, `original_scores`) is given only when the
  user asks for the original: call it the original, since it leaves out later edits, and never
  substitute it for a plain PDF request.
- Native Sibelius or Dorico files and separated stems of the original recording are not
  produced.
