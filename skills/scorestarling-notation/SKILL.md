---
name: scorestarling-notation
description: Turns written music into an editable, playable ScoreStarling score and converts music between forms. Sources include notation visible in video frames, a photo, scan or PDF of printed music, jianpu (numbered notation), a lead sheet or chord chart, a MusicXML, MIDI, ABC or Guitar Pro file, or music typed, described or written in the chat. Outputs include MIDI, audio, PDF, MusicXML, Guitar Pro, ABC, MEI and jianpu. Use it whenever music arrives as notation rather than by listening to a recording, and when writing music on request.
---

# Sheet music and notation to a score

A score made here is a normal ScoreStarling project: it plays back, takes the same edits
(`edit_score`) and exports to PDF, images, audio and, on accounts with existing download access,
the editable formats (MusicXML, MIDI, Guitar Pro, ABC, MEI; see Converting). Music read from a
video's notation follows the section below; music transcribed by listening follows the
`scorestarling-score` skill.

**Where you work decides the conversation.** In a chat app with the ScoreStarling MCP connection
(ChatGPT, Claude, Codex, Gemini), read [references/chat-hosts.md](references/chat-hosts.md) before
the first tool call: how a file reaches the server, what the score panel shows, a preview's
price, saved results and how files reach the user. In ScoreStarling's own app, the app's
instructions say those things, and they win where they differ from this skill.

## Notation visible in a video

The goal is the requested editable score in ScoreStarling from one user request. Decide from accessible
source evidence whether to read notation or transcribe the performance; the video file type alone does
not decide. `check_link` provides initial context; `watch_link` can return actual frames without a score ID.
Choose useful times, crops and any authorized image-processing steps yourself. A cover is not evidence
of the whole video. Screenshots or a PDF may help you work, but are not required intermediate deliverables.

When notation is readable, follow its changing systems, avoid copying overlapping bars twice, write the
notes, rhythms and marks with `create_score`, and compare the saved score against the source. A sheet in a
video is a strong lead, not proof: it may be simplified, from another arrangement or out of step with the
playing. Look the piece up and check the sheet against the recording and what you find, as "Putting it
together" in the `scorestarling-score` skill's `references/research.md` describes. If inspected
frames show no notation, continue with audio transcription.

A sheet that scrolls or turns with the playing is the performer's own score. Read it whether the user asks
for the piece or for "this version": it already holds the rhythm, voices, spelling and bar lines that a
transcription would have to rebuild, and correcting an audio draft toward it bar by bar costs many edits
and leaves split voices and ties. Then check it against the recording: a transcription of the same link,
started when the request covers it and it fits the free preview (otherwise offered in one line), shows
where the playing differs, and only those bars change. Make the audio the base only when the user
explicitly asks to transcribe the performance by ear, when the sheet covers little of what is played, or
when it clearly does not match the playing; keep the sheet as the reference for the bars it shows. An
explicit request to transcribe the actual performance takes precedence over reading the printed score.

Distinguish unreadable images from failed access: for blurred, cropped or incomplete notation, inspect
another useful time or region. If the source cannot be fetched, do not repeat the same failing download
with different crop settings. Explain what is unavailable and request the video file or clear screenshots;
offer audio transcription as an alternative if audio is accessible, without silently changing an original-score
request. Missing frames do not establish that no score exists, and unreadable bars must not be invented.
Once the source is usable, finish the score in the same turn rather than asking the user to request import again.

## Choose the way in

| What the user has | Do this |
| --- | --- |
| A clean PDF or flat scan of printed music, especially piano or several pages | Send it to the server's sheet-music reader as you would a recording; it takes about 30–50 seconds a page |
| A phone photo, a lead sheet with chord symbols, jianpu, handwriting or a single short page | Read it yourself, write ABC ([references/abc.md](references/abc.md)) and call `create_score` |
| A MusicXML, MXL, MIDI, ABC or Guitar Pro (.gp, .gpx, .gp3–.gp5) file | Send it as it is (Guitar Pro keeps its TAB); a short ABC text can also go straight to `create_score` |
| Music typed or described in the chat, or music you compose or arrange on request | Write ABC and call `create_score` |

These defaults come from measured readings (docs/sheet-music.md in the ScoreStarling
repository). On clean printed pages the reader was as accurate as the best assistants and much
faster. On a real piano page exported from Sibelius it agreed with the assistant's reading on
93.5% of notes and was right in 8 of the 10 bars where they differed. It cannot read jianpu, it
lost the bar structure of a lead sheet, and it read phone photos badly. Strong assistants read
melodies, lead sheets, jianpu and chorales almost perfectly. Dense piano photos stayed hard for
everyone, so read those bar by bar and check carefully. When the user offers both a photo and
a PDF of the same music, upload the PDF.

Uploaded sheet music and score files are read, not transcribed: the recording check, the engine
choice and tempo detection do not apply. A score file (MusicXML, MIDI, Guitar Pro, ABC) or
notation text is free; a PDF or photo read is a piece like any other (a free 30-second preview, then
10 credits for the whole). A tempo the user gives
(`bpm`) sets playback for a score that marks none. Follow the job until it finishes,
then do what its `next_step` says.

## Reading the music yourself

1. Look at the whole page first: title, composer, key signature, time signature, tempo mark,
   instruments, number of systems and bars, repeats, pickup. Write them down.
2. Write ABC bar by bar, one line per printed system, with a `%` comment naming its first bar
   number, so you can check it against the page. Copy every accidental the page shows; like
   staff notation, an ABC accidental lasts to the end of its bar, so a later note in the same
   bar written without one keeps it. Count ledger lines from a known note (middle C sits on the
   first ledger line below the treble staff and above the bass staff).
3. Check each bar's beats add up to the time signature, except a pickup and the bar that
   completes it.
4. Call `create_score` with the ABC and the title. Its `warnings` list notation it could not
   read and bars whose lengths do not match the time signature.
5. Call `review_score` and compare its picture with the source bar by bar: pitches,
   accidentals, octaves (bass notes especially), rhythms, ties, tuplets, chord symbols, key
   and time signatures. The picture lays bars out differently from the page, so compare by
   bar number and zoom in with `measures` (`"9-12"`).
6. Fix what differs: `edit_score` for a few notes, with operations such as
   `{"action": "set_pitch", "note_ids": ["<id from get_score>"], "pitch": 62}`, `set_duration`,
   `delete_notes`, `add_chord_tone` or `set_clef`; for many errors, correct the ABC, call
   `create_score` again, then `trash_score` the first attempt. Change a note only where you can
   count its line or space in the source; a note that merely looks higher or lower than in the
   review picture is not enough. In a test on a blurry photo, corrections made by comparing
   shapes turned four right notes wrong. Corrections that make the score match its source are
   part of what the user asked for, so apply them directly rather than as previews. Tell the
   user which bars you were unsure of; when the source is too blurry to count lines, ask for a
   sharper, straight-on photo or a PDF rather than guessing.

For jianpu, `1=C`-style keys give the tonic: map the digits to scale degrees in that key,
dots above or below to octaves, underlines to eighths and sixteenths, dashes to held beats.

## After an upload is read

The imported result is an editable starting score. Preserve the source and reversible
revisions; the goal is faithful, clear, playable notation, not merely a passing validator.
The status says how many bars, parts and notes were read. Call `review_score` and compare its
picture with the original page (the user's file, or ask them to share a picture when you have
none). The reader's typical slips: a missed natural or courtesy accidental, a doubled note in
a chord, a lost tie, and text it cannot read. Correct them with `edit_score` and say what you
changed. If the reader failed or most bars are wrong (a photo, jianpu, handwriting), read the
page yourself as above. `review_score` does not compare the source automatically;
`doubtful_notes` is unavailable for notation imports, which says nothing about accuracy.
Use [the review reference](../scorestarling-score/references/good-score.md) as conditional
checks, not rules that override written opening rests, syncopation, inner voices or ornaments.

Apply clear source corrections and reversible edits within the user's stated goal directly.
When the user asks for faithful or playable music, finish clear source-supported fixes before
ending the turn; listing known missed notes or ties and waiting for another prompt leaves
that request unfinished. Keep corrections in the same score, as "Change the score in place" in the
`scorestarling-score` skill describes: `edit_score` for single operations, or a `batch` of up to 30
note, rhythm, voice and bar edits saved as one version; otherwise an edited copy of the current
revision, keeping note ids, saved with `revise_score`, which also adds missed notes and removes
misread ones. Reconstruct ABC as a new score only when the
first reading is unusable; preserve the draft, check the replacement and say it is a new score.
Ask one specific question only when the source leaves a consequential musical choice unclear.
A new arrangement or interpretation outside that goal needs the user's acceptance before it
is applied. Keep a faithful master when making a learner version. `edit_score` has no grace-note, arpeggio, swing or pedal entry (voices,
staves, tuplets, ties, slurs, beams, stems and a shifted passage are operations); write those in
an edited copy and save it with `revise_score`. Do not invent
actions or reengrave an import to bypass that limit. If rewriting ABC, verify coverage and supported markings
before replacing a version; do not discard the first attempt until the replacement is checked.
Inspect all exported pages, compare changed bars with the written source and audition
playback when available; report uncertainty and unverified exports explicitly.

## Preserve and audit source corrections

For PDF/OCR drafts, prefer source-supported local edits over replacing correctly read music.
Keep the original draft. If missing notes or ties require a `create_score` replacement, compare
**all** pitch and rhythm changes between the new and old scores against enlarged original pages.
Check clef, key, staff position, accidentals, grace notes and ties, with the preceding and following
bars. A structurally valid score or a model calling it “corrected” is not proof of source fidelity.
Until those changes have been checked, report the remaining uncertainty rather than complete accuracy.

## Converting

Once a score exists, `export_score` gives every other form of it. The formats, what each account
downloads and numbered notation are in the `scorestarling-score` skill's
[references/delivery.md](../scorestarling-score/references/delivery.md).

Transpose with `edit_score` `transpose_score` (an interval such as `M2` or `-m3`) so the score,
playback and exports stay consistent; change the playback instrument with `set_timbre`. To
arrange or simplify music, read the score with `get_score` (or its editing copy), write the new
ABC yourself (or a MusicXML file, passed as `file`) and `create_score` the new version; the
original score stays as it is. An `abc` export works only on accounts with existing download
access; to read the notes yourself, use `get_score` or the editing copy. For arrangements read [the arranging reference](../scorestarling-score/references/arranging.md).

## Limits

Repeats play once, as written. Playback uses the score's first tempo and any later tempo marks;
without one it plays at 100 quarter notes per minute. Scores from notation are not re-engraved
(re-engraving rebuilds notation from playback); edit their notes instead. Up to ten minutes of
music per score, 95 MiB per file and twelve pages per PDF. Drum tracks in a MIDI file get a drum
staff after the pitched parts.
