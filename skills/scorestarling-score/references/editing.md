# Changing a score: edited copies, previews, marks and specific fixes

Read this with step 6 of SKILL.md when a change needs more than one `edit_score` operation, when
you add printed marks or reduce a part to one line, and for specific fixes. The live tool schema
and `get_workflow_guide(topic="operations")` list every operation's fields and limits.

## In place, always

Every change to an existing score stays in that score as its next revision, with its recording
comparison, open panel, comments and undo history. Never make a new score to change one:
`create_score`, `transcribe_attachment`, `transcribe_link` and `transcribe_again` make separate
scores without that history. Make a new score only when the user asks for one, such as an
arrangement ([arranging.md](arranging.md)) or another transcription.

## One operation: edit_score

`edit_score(score_id, revision, operation)` applies one operation at the exact current revision;
stale revisions and unknown note or mark IDs are refused. It takes effect at once and `undo`
reverts it. Read note IDs, staves, voices and marks with `get_score` (filter by `measure`,
`part_id` or `note_ids`), and re-read after each change: re-engraving, moving staves, scaling
note values, rewriting the rhythm and re-beating replace note IDs.

## An edited copy: revise_score

For anything else, or many changes at once (moving notes between voices, deleting a misheard voice, correcting many pitches, adding missed notes, ties, beams, rhythm
spelling, a shifted passage):

1. Before the first file fetch in the conversation, tell the user in one line that the chat may
   ask to allow it, and that allowing ScoreStarling for the conversation stops further asks.
2. `export_score` with `format=editing_copy` for the current revision, once for the whole round
   (the changes you are about to save or preview together). It is the score's MusicXML for your
   own edits: it works on every score without unlocking and is saved back into the same score, so
   it is not a download for the user. Never present it as one or link it as a file; when the user
   asks for a MusicXML file, that is a download (SKILL.md step 7), which a free score only gives
   once it is unlocked.
3. Make every change in that copy, keeping each note's `id` attribute.
4. Save it once with `revise_score` (the file as an attachment, or the text as `musicxml`),
   giving the revision it was exported from. `preview=true` saves it as a suggestion the user
   applies or discards in the panel instead.
5. Re-read IDs with `get_score`, `review_score` the result, and say in plain words what changed.
   If `revise_score` refuses, it says what differs: fix the file and save again.

How the copy plays back: a kept note keeps its played timing whatever its written rhythm, staff
or voice; a changed pitch plays at the new pitch; a removed note stops sounding; a note without
an existing `id` is added to the playing where it is written, inside the recording's length.
Parts stay the same. Without the exported IDs, only notation changes that keep every pitch are
accepted.

One export serves one save. When notation-only fixes and proposed note changes both need the
copy, save the notation-only fixes first, then export the new revision for the preview.

If you cannot fetch or edit the file, use single operations for what they can express (a
`preview_score_edit` with `fill_rest` for a missed note in a rest, `delete_notes`, `set_pitch`)
and say plainly what is left undone and why.

## Requests and proposals

- What the user asked for, broad or exact (including a broad correction or arrangement goal), is
  applied directly within that goal, without asking again for each ordinary edit. That includes
  removing notes the request covers (tidying the hands drops doubled and stray notes): save it as
  a new version and say what you removed; undo restores the previous one.
- A panel message can list several numbered requests, each with its own note IDs: apply them in
  order, each on the current revision.
- What you propose on your own goes into a preview: `preview_score_edit` (one operation; every
  action except undo and redo) or `revise_score` with `preview=true`. Explain its scope,
  `review_score` the preview, and say what improves and what gets worse. A preview changes
  nothing until the user accepts it; then call `apply_score_preview` with its ID and base
  revision. `discard_score_preview` drops one. The panel's Apply and Discard ask the user; in chat,
  say that the score shown is the suggestion, without citing tool rules.
- Up to five previews can wait on one revision, but applying one makes the others stale: put
  related changes into one preview.
- On a stale revision, re-read `get_score` and reconsider the proposal against the new score
  rather than repeating it silently.
- A request to review is not permission to delete plausible voices.

## Printed marks

Printed marks are objects of their own, as in a notation program: tempo and expression words
(rit., a tempo), rehearsal marks (A, A6), metronome marks, dynamics, hairpins and fermatas, each
with an ID in `get_score` `marks`. Use `add_mark`, `update_mark`, `move_mark` and `delete_mark`
when the user asks for a mark, or when one text is doing two jobs, instead of rewriting the
score.

Example: a section "A6" where the music returns to tempo is two marks on the same note, printed
stacked, never one text "A6 · a tempo":
`{"action":"add_mark","kind":"rehearsal","note_id":"n…","text":"A6"}` and
`{"action":"add_mark","kind":"words","note_id":"n…","text":"a tempo"}`. An ABC `"^A6"` arrives
as words; `update_mark` with `kind: "rehearsal"` makes it the boxed section label.

Only dynamics change playback (as `set_dynamic` does). A metronome mark is printed only: say
that playback keeps the recording's tempo. Jianpu exports carry the same marks.

## One note at a time

When the user explicitly asks for a one-note-at-a-time melody, `reengrave` with `line: "single"`
keeps one note at a time on one staff and removes the other notes from playback too (undo brings
them back), without transcribing again. It is a reduction of the music, not a way of showing it.
A part still named after the piano becomes Melody. It suits a single-part recording only.

- Merely naming a voice, a violin or a flute does not authorize removing real simultaneous
  notes, and a `single_line` suggestion is `voices: 1`, not this.
- Apply an already requested reduction with `edit_score`; preview one you propose with
  `preview_score_edit`.
- The user can do the same in Score settings › Layout, which also offers one staff with chords,
  two piano staves and the shortest note. Other simplifications are arrangements
  ([arranging.md](arranging.md)).

## Specific fixes

**Pitch and octave.** Use real selected note IDs with `transpose` or `set_pitch`. Distinguish
written from sounding pitch for transposing instruments. When the user names only a letter
("should be an E"), take the nearest note of that name and say the exact pitch you wrote (E5,
E♭5) so they can correct it; ask only when the key leaves it truly unclear.

**Meter, pickup and beat level.**
- Inspect the current settings first. Preview `set_meter` (one time signature for the whole
  score) or `rebar_pickup` with a confirmed pickup length in quarter-note beats; `rebar_pickup`
  moves every bar line. `set_pickup` only marks a first bar that is already partial.
- Never infer a pickup length from an underfull bar alone. A solo-piano score's pickup was
  estimated from the playing: change it with clear source evidence, and ask only when the
  downbeat stays unclear.
- Notes that look halved or doubled may mean the beat level is off. A slow ballad whose
  sixteenths came out as eighths under a doubled tempo mark needs `scale_note_values` with
  `factor` 0.5 (halve every value); a quick waltz written in sixteenths at half its tempo needs
  2 (double). Preview it. The tempo mark changes with the values and the playing stays; a
  solo-piano score finds its time signature and bar lines again. Then check the meter and the
  first downbeat against the source.
- A 6/8 song written as 3/4 (the same bar length) only needs `set_meter`.

**A different pulse.** `rewrite_rhythm` changes a steady recording's note values and bar lines
together at an explicit quarter-note `bpm`, `beats` and `beat_type`, without inference or
credits. It keeps the played notes, controls, pitch bends and comparison playback, with MIDI
rounding below 0.1 ms. Check its availability in the review and the source evidence: tracked or
changing tempo, pickups, imported sheet music, and marks or tuplets it cannot keep are refused.
Do not apply an uncalibrated candidate merely because it ranks first; preview new
interpretations and re-read IDs afterwards.

**A wrong tracked beat.** A solo-piano score follows the beat the Piano engine tracked, and
`rewrite_rhythm` refuses it. When that beat is wrong (a swung piece read as 3/4 at 150 where it
swings in 4/4 at about 130, a tempo off by 4:3, bars starting off the beat), `rebeat` writes it
again: `bpm` (quarter notes), `beats`, `beat_type`, `downbeat` (the second a bar starts: the
start of the note there, from `get_score`) and, for swing, `swing` (the share of each beat its
first eighth takes; 2/3 for a triplet feel), so long-short pairs print as even eighths. The beats
follow the playing from that downbeat, so a player's drift is kept and the printed tempo is what
they played; notes before it make a pickup. Every note keeps its time and hand. Choose the
downbeat where the returning phrase starts, apply it, then read the score again: the phrases
should now start at the same place in their bars.

**Quantized rhythm.** Compare onsets, durations and the supplied tempo. `set_duration` corrects
a supported note length but changes playback note-offs, so it is not notation-only cleanup;
`rebeam` changes grouping only; `reengrave` with `grid: "8th"` rewrites the whole performance on
a coarser grid. When a timing repair is unsupported, explain it rather than inventing an
operation or starting another transcription without the user's authorization.

**A shifted passage.** When one passage sits a beat or two off while the rest is right, write it
at its proper place in the edited MusicXML copy and save it with `revise_score` (a preview,
since it changes how the music reads), checking the bar lengths around it. `rebar_pickup` would
move every bar line.

**Hands and staves.** `set_staff {note_ids, staff, clef?}` moves played notes of a part on two
staves to the other hand's staff (1 upper, right hand; 2 lower, left hand), as one notation edit:
every note keeps its ID, pitch, start and length, so the playing and the IDs you hold stay valid.
"Give the accompaniment to the left hand" is one call with the accompaniment's IDs (read them from
`get_score`; a chord can move in part, a tied note moves with its whole tie, a tuplet moves whole).
For a passage over many bars, name where the notes are instead of listing IDs:
`select {measures: "1-28", voice?, below?, above?, part_id?}` takes the other staff's sounding
notes in those bars, only in that voice and strictly below or above those MIDI pitches when given
(C5 = 72). Read one bar with `get_score` first to see which voice the accompaniment is in, or which
pitch separates it from the melody; the preview or the result's count shows what moved.
Rests under the moved notes are covered, rests are written where a hand is left empty, and voices,
stems and beams are set again in the bars touched. Leave `clef` out unless the user names a clef:
`auto`, the default, gives the receiving hand the treble or bass clef its notes read in wherever it
then holds one line (it was resting, or the moved notes continue its own), and the old clef returns
after them. An accompaniment from middle C up, such as K. 545's, reads in the treble clef, as
Mozart wrote it; a low one keeps the bass clef. `keep` leaves clefs alone, `treble` or `bass` sets
one. It is refused for a part on one staff and for a slur or tuplet it would split (select the whole
phrase). Preview it when the user asked to look first. Never repitch or delete notes to imitate a
staff move. For a video, `watch_score` the bars first: each frame lists the notes struck there with
their ID and staff, so a note in the other hand can be moved by its ID.

**Guitar TAB.** TAB is a setting of the score, not a second score: `set_tablature {part_id?, view,
tuning?, capo?, strings?}` shows a guitar, bass or ukulele part with TAB under the staff (`both`),
as TAB alone (`tab`) or not (`off`), and the panel, PDF, parts and MusicXML follow; the notes and
playback never change. Pass the tuning the user names (a preset such as `drop_d` or `dadgad`, or
the open strings from the lowest, `["D2","A2","D3","G3","B3","E4"]`) and the capo fret; a Pro part
already starts from the tuning its supplier's TAB named. `strings: "lowest"` (the default) writes
each note at its lowest fret, as notation apps do; `"hand"` keeps the hand in one position when
the user asks for fewer shifts or an easier fingering. For one note, `set_string {note_ids, string}`
plays it on another string at the same pitch (string 1 is the top line, high e; `null` returns it
to the rule) and `set_fret {note_ids, string, fret}` writes a fret, which changes the pitch to the
one that fret plays. `get_score` lists each note's `string` and `fret`; `tab_issue` marks a note no
string can play as written (below the lowest string, above the top fret, or more notes at once than
strings), and validation lists those bars: tell the user rather than moving notes on your own. When
the user wants TAB in the conversation, `export_score` `tab_text` (with `part_id` for one part)
returns plain-text TAB to paste.

Re-engraving operations (`reengrave`, `rebeat`, `scale_note_values`) write the
notation again from the playing. Printed words, rehearsal and metronome marks, dynamics, hairpins
and fermatas go with the played notes they stand on and keep their IDs (one between notes goes to
the nearest played note); chord symbols and tuplets still block them. `rewrite_rhythm` refuses
printed marks.

**Voices.** Move notes between voices in the edited MusicXML copy; `edit_score` has no operation
for it.

**Tuplets, swing, grace notes, arpeggios, ties, slurs and pedal.** Write them in the edited
MusicXML copy. Never flatten genuine tuplets.

**Notes not bound to the playing.** Inspect validation and the note mapping before editing
playback. `repair_bindings` repairs only unambiguous links. Do not guess MIDI bindings or align
audio precisely from `notation_estimate` times. MusicXML and PDF may still export; MIDI and
audio need complete bindings. Report what stays unresolved, in plain words ("some notes can't be
edited one by one yet").

## What no operation does

Nothing edits the played onsets and offsets freely or the local tempo map. A global voice cap or
rhythm grid cannot replace local editing, and duration edits have chord, binding and rhythm
restrictions. Report a gap in plain words without inventing action names or destructive
workarounds.

## Another transcription of the same recording

When a recording was transcribed as the wrong instrument ("it's a piano"), and the user agrees,
call `transcribe_again` with the score ID and the right `provider`: it makes a new score from
the same recording, the first score stays, and nothing is uploaded again. Follow its job like an
upload; a band still needs its price question. Never use it merely to fix notation. Sheet music
and notation imports have no recording to transcribe again.

## Rebuilding music from ABC

Rewriting a passage or a whole score as ABC and calling `create_score` makes a new score. Use it
only when the user wants a new score (an arrangement) or the first reading is unusable, not to
correct a transcription you can edit in place.

- Keep the original draft, and say that the result is a new score.
- Compare every pitch and rhythm change between the new and the old score against the source,
  with the bars before and after. For a draft read from a PDF or an image, check against
  enlarged original pages: clef, key, staff position, accidentals, grace notes and ties.
- Check that the coverage and the markings survived; a rewrite is a new reconstruction, not
  proof that every detail of the source came through.
- A valid structure, or a model calling the result corrected, does not prove fidelity. Until the
  changes are checked, report the remaining uncertainty rather than complete accuracy.
