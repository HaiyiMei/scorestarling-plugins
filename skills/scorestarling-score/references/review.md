# Reviewing a transcription: read, listen, watch, look, proof

Use this to review a transcription: in a chat app after every one ([chat-hosts.md](chat-hosts.md),
step 5), and anywhere the user asks how one came out or wants it checked or corrected. Each pass
has its own evidence; decide what to change from it as "What a change needs" in
[SKILL.md](../SKILL.md) says. What a good score of the piece looks like is in
[good-score.md](good-score.md); how to weigh each check's evidence and use the ready suggestions,
in [review-tools.md](review-tools.md). Review and edits use no credits.

## 1. Read

Read [good-score.md](good-score.md) once in the conversation
if you have not. Call `review_score` with `text=true` and `image=false`. Besides the summary and
the ready suggestions, it returns the score as text: "Score as text, bars A-B.", then a line for
each bar (`bar 9 (4/4)`, with `(pickup, 2.5 beats)` when the bar is short) and a line for each
staff listing its attacks, such as `upper staff: 1 D4, 1.5 E4+G4, 3 A2 held 2`. Each attack is
its beat, counted in quarter notes from 1, and its pitch; `+` joins notes struck together,
`held N` marks a note held for N beats, `(tied on: …)` names notes continuing from the bar
before, and `rest` marks a staff with nothing in that bar. When the text ends with "More bars:
request measures A-B.", call `review_score` again with those `measures`, `text=true` and
`image=false`, until you have read every bar. Then write yourself these working notes (they are
not the reply), giving places as bar:beat (9:3 is bar 9, beat 3):

1. Work out what the piece is: the instruments and texture, who plays what, the meter, the
   sections and phrase lengths, and which phrases return. No texture or hand layout is a
   default; the piece's own returning phrases and figures are your main reference.
2. List every bar:beat where each phrase starts and returns. Mark a return that starts on
   another beat, or with another rhythm, than the others.
3. Follow each staff's figure bar by bar (a steady stream of eighths, a bass note at each
   change, a repeated chord rhythm) and note where it breaks off.
4. Note the notes that fit no line: not the tune, not the figure, not the bass.
5. Note where bar 1 starts and whether the opening is a pickup.

Keep the notes short and concrete. A made-up example: "Returns: opening phrase at 1:1, 17:1,
25:3 (the others start on beat 1). Breaks: lower-staff eighths stop at 6:3-4 and 22:2. Strays:
A3 in the upper staff at 6:3, where the lower figure stops (maybe its note on the wrong staff)."
What this pass finds is musical: changes to notes or rhythm need the user's acceptance unless
they asked for them, and notes move between staves only with evidence ("What a change needs" in
[SKILL.md](../SKILL.md)).

## 2. Listen

Call `review_score` with `check=listen` and `measures` on the few passages whose
problems from the read pass matter most, at most 16 bars or 45 seconds each. It only reads, takes about a second
and uses no credits. A second transcription engine hears that stretch of the score's own
recording again and returns, per bar and beat, `heard_not_written` (often a missed note),
`written_not_heard` (sometimes an extra or wrong note, sometimes just a soft or quick one) and
`heard_as_overtone` (a partial of a written note: usually ignore it), with `heard_written_share`
(yours for weighing the leads, never a figure for the user) and a reading note. Use it to confirm or rule out what the read pass found, weighing each lead
against the score's own patterns: a note heard in a figure's gap, at the pitch the figure
predicts, supports a missed note; a stray that fits no line and was not heard supports an extra
note; a return on another beat is a question of the beat grid, which the accompaniment's own
pulse settles ("Returning phrases" in good-score.md). These are leads, never verdicts, and note
changes still need the user's acceptance; [review-tools.md](review-tools.md)
says how to weigh them. For written music (sheet music, MusicXML or MIDI imports) it returns
`available: false` with a reason: then rely on reading and looking, and name the bars for the
user's ear. With several parts it hears their mix; pass `part` to check one part.

## 3. Watch (a video)

When the recording is a video (an uploaded video, or a YouTube, Bilibili or
other video page), some questions are plain to see and hard to hear: which hand plays the top note
of an octave figure, where hands cross, who of a band plays a line. Call `review_score` with
`check=watch` and `measures` (up to 16 bars) on the bars where hands, staves or parts are in doubt. It returns one
picture of frames, each just after an attack and labelled with its bar, beat and time, and per frame
the written notes struck there (staff, name, ID), so a note on the wrong staff shows as a hand that
isn't where the score puts it. Ask for fewer `columns` to see each frame larger, and `crop` to the
keyboard or the fretboard (`[0, 0.5, 1, 1]` is the lower half). A video page's pictures are fetched
again the first time, which takes a few seconds; never fetch the recording or its video yourself
(yt-dlp, a browser): `review_score` hears and watches the score's own. What a frame shows is
evidence for staves and hands; pitches still come from listening. Act on it: `set_staff` the notes
the frames show in the other hand (their struck IDs), one call per staff, and name the bars; a
question about how a passage is played is answered with its bars and what the frames show, then
that change.

## 4. Look

Call `review_score` with its page picture: the first page (no `measures`), then
every further 16 bars from the first bar that page does not show (`measures`, in the score's bar
numbers, such as "17-32"). Judge each page as an engraver would: clefs and ledger lines,
spelling, beams, voices and stems, rests, ties, collisions, spacing and labels. Inspect each
suggested operation before using it, as "Suggestions" in
[review-tools.md](review-tools.md) says.

## 5. Proof

After changes, look at the pages as the user will read them: `review_score`
pictures of the new revision (or of the preview), every page after a round of changes, or the
pages a local fix touched. Check that each fix landed and nothing got worse (collisions, clef
changes, broken ties, bar lengths). Run `review_score` with `check=structure` on a saved
revision (for a preview, read the `structure` in its review), and undo whatever made it worse.
