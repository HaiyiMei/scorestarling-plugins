# Bassoon: difficulty by level (ABRSM)

Read this when the target instrument is bassoon. Written pitch equals sounding pitch (bass clef, tenor clef for high notes).
The script reads [profiles/bassoon.json](../profiles/bassoon.json): `check_level.py score.musicxml --instrument bassoon --grade N`.
All sources are listed in [../sources.md](../sources.md).

## Sources

- ABRSM, Practical Grades Woodwind syllabus from 2022 (unchanged for 2026: the 2026 specification says sight-reading and scale requirements stay the same), keys and ranges table p. 24, sight-reading parameters pp. 23-24, official PDF: <https://www.abrsm.org/sites/default/files/2023-10/Woodwind%202022%20Practical%20syllabus%20(0%20ALL)%2020230911.pdf>. Read 2026-10-14.

## Table by grade

| Grade | Key signatures read (cumulative) | Range (written) | Sight-reading features, new at this grade |
|---|---|---|---|
| 1 | 1b, 1# | G2-G3 | 4 bars of 4/4 or 3/4, or 6 bars of 2/4; dotted minim, minim, crotchet, paired quavers, crotchet rests; tongued or simple two-note slurs; f, mf |
| 2 | 1b, none, 1# | E2-B3 | 8 bars; four-quaver groups, dotted crotchet + quaver, ties, minim rests; staccato; mp, crescendo hairpin |
| 3 | 1b, none, 1# | E2-C4 | 3/8; dotted crotchets, simple semiquaver patterns, quaver rests; accents; p, diminuendo hairpin; accidentals only within minor keys |
| 4 | 1b, none, 1#, 2# | D2-F4 | about 8 bars; 6/8; chromatic notes, anacrusis, tenuto, pause |
| 5 | 3b, 2b, 1b, none, 1#, 2#, 3# | C2-G4 | 8-16 bars; simple syncopation; ff, pp; slowing at the end |
| 6 | 4b, 3b, 2b, 1b, none, 1#, 2#, 3#, 4# | Bb1-A4 | 12-16 bars; 9/8, 5/8, 5/4, changes of time signature; triplets; swung style; rit. then a tempo |
| 7 | 4b, 3b, 2b, 1b, none, 1#, 2#, 3#, 4# | Bb1-Bb4 | 16-20 bars; 7/8, 7/4 |
| 8 | 5b, 4b, 3b, 2b, 1b, none, 1#, 2#, 3#, 4#, 5# | Bb1-C5 | 16-24 bars; 12/8; triplet crotchets; acceleration; simple ornaments |

Key signatures are the union of the major and relative-minor keys ABRSM lists for sight-reading up to that grade (the table lists
tonics; the signature of a minor key is its relative major's). Ranges are the official sight-reading ranges converted from Helmholtz
to scientific pitch (C4 = middle C).

## Arranging implications

- Keep the part inside the grade's range and its cumulative key list. Grade 1 is G and F major, a long way inside the instrument's compass (G2-G3).
- Bassoon phrases need breaths like other winds: the script uses an estimate of the longest phrase without a breath (profiles/bassoon.json, breath_s).
- Remove the top-register phrases first when going down a grade; the written range grows by about a third per grade at the top and by a fourth at the bottom at Grades 1-3.

## Confidence and gaps

- Keys, ranges, time signatures and rhythm features: official (the sight-reading tables). The per-grade scale and technique lists for bassoon were not reviewed, so nothing is claimed about scale speeds, register or fingering demands, or clefs used per grade. Confidence: medium.
- ABRSM has no Initial grade for bassoon. The table describes the unseen sight-reading test, which sits below the exam pieces.
