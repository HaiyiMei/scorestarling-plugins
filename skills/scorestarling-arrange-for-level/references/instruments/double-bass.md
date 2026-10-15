# Double bass: difficulty by level (ABRSM)

Read this when the target instrument is double bass. Written pitch is an octave above sounding pitch.
The script reads [profiles/double-bass.json](../profiles/double-bass.json): `check_level.py score.musicxml --instrument double-bass --grade N`.
All sources are listed in [../sources.md](../sources.md).

## Sources

- ABRSM, Practical Grades Bowed Strings syllabus from 2024 (Violin / Viola / Cello / Double Bass share one sight-reading table and one keys-and-ranges table, printed pp. 23-24), official PDF: <https://www.abrsm.org/sites/default/files/2024-12/Bowed%20Strings%202024%20Practical%20syllabus%20(1%20Violin%2020241211).pdf>. Read and cross-checked 2026-10-14.

## Table by grade

| Grade | Key signatures read (cumulative) | Range (written) | Sight-reading features, new at this grade |
|---|---|---|---|
| Initial | 1#, 2# | D3-B3 | 4 bars of 4/4 or 6 bars of 2/4; crotchets, paired quavers, crotchet rests; every note separately bowed; mf only |
| 1 | 2b, 1b, 1#, 2# | F2-B3 | 3/4; minims, four-quaver groups; f and p |
| 2 | 2b, 1b, none, 1#, 2# | E2-B3 | 8 bars; dotted minims, longer rests; simple two-note slurs; mp, hairpins |
| 3 | 2b, 1b, none, 1#, 2# | E2-B3 | accidentals within minor keys; dotted crotchet + quaver, dotted quaver + semiquaver, simple semiquaver patterns, quaver rests, ties; staccato; pizzicato at the end |
| 4 | 2b, 1b, none, 1#, 2#, 3# | E2-D4 | about 8 bars; 6/8; shifts; chromatic notes; anacrusis; hooked bowing; tenuto, accents, pause; pp, ff |
| 5 | 2b, 1b, none, 1#, 2#, 3# | E2-E4 | 8-16 bars; shifts as required; simple syncopation; arco/pizzicato changes; slowing at the end |
| 6 | 3b, 2b, 1b, none, 1#, 2#, 3# | E2-G4 | 12-16 bars; 9/8, 5/8, 5/4; triplets; a tempo after a slowing; simple chords at the end |
| 7 | 3b, 2b, 1b, none, 1#, 2#, 3#, 4# | E2-A4 | 16-20 bars; 7/8, 7/4; tenor clef |
| 8 | 4b, 3b, 2b, 1b, none, 1#, 2#, 3#, 4# | E2-C5 | 16-24 bars; 12/8; acceleration; simple ornaments; treble clef |

Key signatures are the union of the major and relative-minor keys ABRSM lists for sight-reading up to that grade (the table lists
tonics; the signature of a minor key is its relative major's). Ranges are the official sight-reading ranges converted from Helmholtz
to scientific pitch (C4 = middle C).

## Arranging implications

- Write in written pitch an octave above sounding. If the score file is at concert pitch the checker adds 12 semitones before it measures.
- Keep the part inside the grade's range and its cumulative key list; at Initial and Grade 1 that is G and D major (plus F and B-flat in half position at Grade 1).
- Bass lines already move by step and by fifth, so the easiest simplifications are: whole-note or half-note roots, a held pedal tone, root-fifth patterns in half notes; drop walking eighth-note lines to quarters below Grade 3; avoid double stops and fast shifts below Grade 6.
- Below Grade 4 avoid shifts: a melody that leaves one position needs moving down an octave or transposing to a lower key.

## Confidence and gaps

- Keys, ranges, time signatures and rhythm features: official (the sight-reading tables). The per-grade scale, arpeggio and technique lists for double bass were not reviewed, so nothing is claimed about scale speeds, bowing counts or what the set pieces ask for. Confidence: medium.
- Double-bass-specific sight-reading notes: Grade 1 may be in first or half position at the candidate's choice (keys F and B-flat are then added), Grade 2 first position only, Grade 3 half or first, Grade 4 shifts between half, first and third (at most two positions per test), Grade 6 simple chords at the end, tenor clef Grade 7, treble clef Grade 8. Initial row: keys G and D, written ranges G3-B3 and D3-F#3.
- Like the other strings, the table describes the unseen sight-reading test, which sits below the exam pieces. Pieces may touch a little beyond it; ABRSM publishes no range for pieces.
