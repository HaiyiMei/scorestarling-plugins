# Review tools: what they show and how to act on it

Read this with step 5 of SKILL.md: how to read each tool's evidence, how to weigh what
`listen_score` reports and what `watch_score` shows, how to use the ready suggestions, and how to
check tempo, meter and the first downbeat. What a good score of this piece looks like is in [good-score.md](good-score.md).

None of these tools checks the notes against the recording for you. Everything they report is a
lead to check, and an empty or unavailable result proves nothing about accuracy.

## review_score

`review_score(score_id, revision?, measures?, image=true, text=false)` reads one saved revision
(or a preview's revision) and changes nothing.

- `measures` selects up to 16 bars in the score's own bar numbers ("5-8", "17-32"). Without it
  the picture is the first page and the text covers the whole score up to a size limit.
- `image=true` (the default) adds the page picture; the read pass turns it off with
  `image=false`.
- `text=true` adds a second block, the score as text: "Score as text, bars A-B.", then a line
  for each bar ("bar 9 (4/4)", with "(pickup, 2.5 beats)" when the bar is short) and a line for
  each staff listing its attacks ("upper staff: 1 D4, 1.5 E4+G4, 3 A2 held 2 (tied on: …)", or
  "rest" when the staff has nothing). Beats are counted in quarter notes from 1, `+` joins notes
  struck together, `held N` marks a note held for N beats, and "tied on" names notes continuing
  from the bar before. When the score is longer than the limit, the text ends with "More bars:
  request measures A-B."; the structured result has the same in `bars_text` (`measures`,
  `more`). Read it by role (tune, figure, bass), not by pitch or by staff alone.

It returns:

- `summary`: bars, notes, parts and clefs, the meter and tempo, and `rhythm`, which says where
  bar 1 starts and how the rhythm reads; for a band score also `provider_rhythm`.
- `suggestions`: ready operations for key, clef, ledger lines, voices, staff layout and
  register, and rhythm advice (codes `rhythm` and, for a band score, `pro_rhythm`). A suggestion
  is a lead; see "Suggestions" below.
- `structure`: the same findings as `validate_score` (bar lengths, voices and chords, notes not
  bound to the playing). A clean structure does not mean the notes are right.
- `doubtful_notes`: confidence leads from the one-instrument transcription only. They are
  unavailable for solo piano, band scores and sheet-music imports, and an empty list does not
  mean the score is accurate.
- `source_note_evidence`: at most six cached, independent pitch or voicing leads for detected
  single lines, each linked to an unchanged current note ID and a span of the recording. Inspect
  that passage of the original yourself before correcting anything; quiet, short or ornamental
  real notes get flagged too.
- `source_rhythm_analysis`: candidate meters and downbeats from the recording. Their scores and
  gaps are not calibrated, and the right meter may be missing.
- `reengrave`, `rewrite_rhythm` and `rebeat`: whether each is available, and why not (`rebeat` is
  available exactly where a tracked piano beat turns `rewrite_rhythm` away).
- `expression`: each bar's timing and loudness, for tempo and dynamics marks ("Expression marks
  from the recording" in good-score.md). It measures timing and level, not notes.
- The picture, when `image` is on: the first page, or the bars in `measures`. Judge it as an
  engraver would.

## listen_score

`listen_score(score_id, measures, revision?)` only reads: at most 16 bars or 45 seconds, about a
second of server work, and no credits. A second transcription engine hears that stretch of the
score's own recording again. Per bar and beat it returns:

- `heard_not_written`: heard, but not in the score; often a missed note.
- `written_not_heard`: in the score, but not heard; sometimes an extra or wrong note, sometimes
  just a soft or quick one.
- `heard_as_overtone`: heard as a partial of a written note; usually ignore it.
- `heard_written_share` and a reading note on how to take the result.

It is not available for written music (sheet music, MusicXML or MIDI imports) or for scores with
several parts: it then returns `available: false` with a reason. Rely on reading and looking
instead, and name the bars for the user's ear.

How to use it:

- Spend it where it decides something: the passages where the read pass found a return on
  another beat, a broken figure or stray notes. A few calls are usually enough; it does not
  replace reading every bar.
- Weigh each lead against the score's own patterns. A note heard where a figure has a gap, at
  the pitch the figure predicts, is strong support for a missed note. A written note that was
  not heard and also fits no line supports an extra note. A note heard beside a figure that
  already has its note there, or one that fits no line, is often an echo, an overtone or a note
  an octave away: only one of the two transcriptions hears it, and a clear-looking attack does
  not confirm it.
- A return written on another beat is a question of the beat grid, which these leads do not
  settle: count the accompaniment's pulse ("Returning phrases" in good-score.md).
- Leads are never verdicts: quiet, short or ornamental real notes can go unheard. A change to
  notes still goes through a preview unless the user asked for corrections.

## watch_score

`watch_score(score_id, measures?, seconds?, frames?, columns?, crop?, revision?)` only reads and uses
no credits. For a score made from a video (an uploaded video, or a YouTube, Bilibili or other video
page) it returns one picture of frames from that video, left to right then down, and per frame its
bar, beat, time and the written notes struck just before it (`struck`: staff, name, ID).

- `measures`: up to 16 bars ("5-8"). The frames land just after attacks, when the key or string is
  down and the hand still on it, spread over the bars; `frames` sets how many (1 to 16, default 8).
  `seconds` asks for exact times in the recording instead.
- `columns` (1 to 4): fewer columns show each frame larger. `crop` is `[left, top, right, bottom]`
  as fractions of the frame: `[0, 0.5, 1, 1]` keeps its lower half, where a keyboard often is.
- A video page's pictures are fetched again from the site the first time (a few seconds) and kept
  for an hour. A recording without pictures (audio, or a link from before links were kept)
  returns `available: false` with a reason. Never fetch the video yourself.

How to use it:

- Spend it on what pictures settle: which hand plays a note (the staff it belongs on), crossing
  hands, an octave figure split between the hands, a guitarist's position, who of a band plays a
  line. Compare each frame's `struck` notes with where the hands are: a note listed on the lower
  staff while only the right hand moves is probably on the wrong staff.
- Pitches come from listening, not from pictures: a frame does not show which key sounded.
- Say what the frames showed and what they could not ("the left hand is out of view in bars 9-12").

## Suggestions

- A suggestion's label is not an approval: read the operation it would run.
- Apply only source-supported cleanup that keeps the playing (key, clef, voices, an empty
  staff). After a transcription, this notation-only cleanup is part of the review; changes to
  notes stay previews unless the user asked for corrections. A key estimate or a voice-count
  heuristic alone is not enough: keep genuine inner voices, crossings and the key the user
  stated.
- The `single_line` suggestion supplies `reengrave` with `voices: 1`, not `line: "single"`.
  `line: "single"` deletes notes and can shorten held notes in playback: never add it on your
  own, and never take an instrument name (a voice, a violin, a flute) as permission to discard
  simultaneous notes. If a requested melody reduction warrants it, explain the affected notes;
  otherwise preview it as a new proposal ("One note at a time" in [editing.md](editing.md)).
- `reengrave` without `line` or `program` keeps the playing and replaces the notation (`line`
  and `program` change the sound too): earlier clef, beam and spelling edits are redone and some
  note IDs change. Omitted options reuse the saved choices, so inspect those before claiming the
  playback is unchanged. It is unavailable with chord symbols, for example, and after a pickup
  unless the solo-piano transcription found it.
- Order: settle the instrument and layout first (`program`, `staff_split`, `voices`, an
  authorized melody reduction), then the key (`key`, at sounding pitch), then the rhythm grid
  (`grid`), and only then single notes. Merge the supported `reengrave` options into one call,
  then set clefs.
- After each change, re-read the changed note IDs with `get_score`, validate, and compare the
  revision before continuing; `undo` restores the one before.

## Tempo, meter and the first downbeat

- The tempo was supplied by the user or detected; a detected tempo is an estimate. Compare it
  with `source_rhythm_analysis`, the score's own phrases and any written source, call it an
  estimate in the report, and ask the user to check it by ear when it matters.
- A solo-piano transcription also places the time signature (4/4, 3/4, 6/8 or 12/8), a pickup
  and the bar lines from the playing. Compare `source_rhythm_analysis` candidates with complete
  phrases, opening rests and the source; their ranking is not calibrated, and the right meter
  may be missing.
- A band score's time signature and tempo come from `provider_output.rhythm`; report them with
  their warnings.
- A suggestion with the code `rhythm` means the bar lines may not follow the playing. Tell the
  user what it found and make "where do you feel the first downbeat?" your one question; for a
  solo piano transcribed as one instrument, offer solo piano, which places bar lines from the
  playing.
- Rhythm ratios are candidate evidence. Opening rests, offbeat bass and chord changes,
  syncopation and dense sixteenths can all be real.
- Notes that read at half or double the felt speed: offer `scale_note_values` (free, keeps the
  playing). Another explicit quarter-note tempo and meter: `rewrite_rhythm`, when the review
  says it is available. Never start another transcription merely to change notation. The
  operations are in "Meter, pickup and beat level" in [editing.md](editing.md).
- A meter, tempo or bar lines that keep every played note are part of the score the user asked
  for: apply them once the returning phrases settle them, and say what changed (undo restores it).
  A single shifted passage is a preview ("A shifted passage" in [editing.md](editing.md)). When
  the evidence does not settle a reading, ask the one question.
- When a solo-piano score's tracked beat is itself wrong (swing or a triplet feel read as straight
  beats, a tempo off by 4:3, bars starting off the beat), `set_meter` only regroups the wrong
  beats: `rebeat` writes it again on the beat the phrases show ("A wrong tracked beat" in
  [editing.md](editing.md)), then review the result.
- A 6/8 or 12/8 score marks and reports its tempo in dotted quarters.

## Listening with the user

You cannot hear the panel's playback. When a decision needs an ear, name the bars and what to
listen for, and ask the user to compare the recording with the score's playback in the panel; if
the host cannot play audio at all, say so. Stop when the remaining questions need the user's ear
or taste.

## When you finish a round of corrections the user asked for

- Look at every page the user will read or receive, not only the first picture ("The page" in
  good-score.md), and check the changed passages against the recording: `listen_score` on those
  bars where it is available, and the user's ear.
- Report accuracy, readability, playability and, for a learner, suitability separately. Never
  invent a quality score.
- Say which revision you checked, what you actually compared, and what is still uncertain.
