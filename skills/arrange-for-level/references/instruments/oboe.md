# Oboe: difficulty by level (ABRSM Woodwind Practical Grades, syllabus from 2022 and 2026)

**Read this when** the target instrument is oboe, at any level. Numbers come from ABRSM Woodwind syllabus (2022, unchanged for 2026); the checker reads them from [../profiles/oboe.json](../profiles/oboe.json): `python3 scripts/check_level.py arrangement.musicxml --instrument oboe --grade N`. S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

Conventions: oboe is non-transposing, written = sounding, treble clef (S4). Pitches are scientific pitch, C4 = middle C; ABRSM prints Helmholtz (c' = C4, a# = A#3 = Bb3), converted by me [D]. "SR" = unseen sight-reading test, parameters cumulative; SR "range" is the span the test may use. ABRSM scales are always even notes and "from the lowest possible tonic" unless the box says otherwise. Tags: [D] derived by me from ABRSM numbers (lowest oboe note Bb3), [I] my inference, untagged = stated by source. Initial: not offered for oboe by ABRSM ("Initial Grade not available for woodwind") nor by Trinity (oboe starts at Grade 1).

## Table by grade

Columns: keys = SR new keys then scale keys; range = SR range; scale top = highest note any scale/arpeggio reaches [D]; speeds = ABRSM guide, scale crotchet = N, arpeggio quaver = N.

| Grade | Keys (major / minor) | Time sigs (SR) | Note values and rhythms (SR) | Written range (SR) | Technique demands (scales, register) | Articulation | Dynamics and other | SR length |
|---|---|---|---|---|---|---|---|---|
| Initial | not offered | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| 1 | SR: G, F maj (no minor). Scales: F, G maj; D min, 1 oct | 4/4, 3/4 (4 bars); 2/4 (6 bars) | dotted minim, minim, crotchet, paired quavers, crotchet rest | D4-D5 | scale top G5 [D]; q=50, e=72 | tongued or simple two-note slurs; scales tongued/slurred | f, mf | 4 bars (6 in 2/4) |
| 2 | SR: C maj, d min (natural form only). Scales: C maj 1 oct from the octave above lowest tonic; D, F maj 12th; A min 1 oct; D min 12th | none new | four-quaver groups, dotted crotchet+quaver, minim rest, ties | D4-G5 | scale top C6 [D]; q=56, e=84 | adds staccato | mp, cresc. hairpin | 8 bars |
| 3 | SR: a min (accidentals only in minor keys). Scales: Bb maj 1 oct (octave above lowest tonic); D, G maj 12th; C maj 2 oct; B min 1 oct (octave above); E, G min 12th; chromatic from G 1 oct | 3/8 | dotted-quaver figures, simple semiquaver patterns, quaver rest | D4-B5 | first 2-octave scale (C4-C6); top D6 [D]; q=63, e=96 | adds accents | p, dim. hairpin | 8 bars |
| 4 | SR: D maj, e min. Scales: A maj 1 oct; E, G maj 12th; D, Eb maj 2 oct; F# min 1 oct; E, F min 12th; C min 2 oct; chromatic G 12th; dom 7th F 2 oct | 6/8 | chromatic notes, anacrusis | C4-C6 | top Eb6 [D]; q=72, e=108, 7ths 54 | adds tenuto | pause sign | c. 8 bars |
| 5 | SR: A, Bb, Eb maj; b, g min. Scales: Ab, A maj 12th; Bb, Eb, E maj 2 oct; F, F# min 12th; B, C#, D min 2 oct; chromatic Ab 12th, D 2 oct; dom 7ths Bb, Ab; dim 7th C# | none new | simple syncopation | C4-D6 | low Bb3 reached by Bb scale [D]; top E6 [D]; q=84, e=126, 7ths 63 | none new | ff, pp; slowing of tempo at end | c. 8-16 bars |
| 6 | SR: E, Ab maj; f#, c min. Scales: G, Ab/G#, A maj/min 12th; B, C maj/min 2 oct; thirds F maj 1 oct; chromatic G, A, C; 7ths C, D, F; dim 7ths G, A, C | 9/8, 5/8, 5/4; metre changes | triplet patterns | B3-E6 | B major 2 oct starts on B3 [D]; q=96, dotted crotchet=48, 7ths 72, thirds 88 | scales still tongued/slurred | slowing then a tempo | c. 12-16 bars |
| 7 | SR: c#, f min (no new major). Scales: F#, Ab/G# maj/min 12th; D, E, F maj/min 2 oct; extended-range G maj; thirds C maj 2 oct; chromatic F#, Ab, D, E | 7/8, 7/4 | none new | Bb3-E6 | top F6 [D]; q=112, dotted crotchet=54, 7ths 80, thirds 100 | scales: legato-tongued / staccato / slurred | none new | c. 16-20 bars |
| 8 | SR: B, Db maj (no new minor). Scales: B, Db/C#, Eb, F maj/min 2 oct; Bb maj/min 2.5 oct; extended-range Ab maj, D harm min; thirds D, Eb 2 oct; whole-tone D, F | 12/8 | triplet crotchets | A#3 (=Bb3)-F6 | Bb scale Bb3-F6 [D]; q=132, dotted crotchet=63, 7ths 96, thirds 120 | as G7 | acceleration; simple ornaments | c. 16-24 bars |

## What changes between neighbouring grades

- 1 to 2: top G5 (was D5) but still D4 at the bottom; four-quaver groups, ties, staccato, mp; C major and d minor.
- 2 to 3: top B5, 3/8, dotted and semiquaver cells, accents, p; first 2-octave scale.
- 3 to 4: bottom drops to C4, top C6; 6/8, chromatic notes, anacrusis, tenuto, pause; D major and e minor.
- 4 to 5: top D6; sharp-heavy keys (A, Bb, Eb major; b, g minor), syncopation, ff/pp, slowing at the end; longer 12-bar-ish tests (8-16 bars).
- 5 to 6: bottom B3, top E6 (the extreme registers open up); 9/8, 5/8, 5/4, metre changes, triplets.
- 6 to 7: low Bb3; 7/8, 7/4; c# and f minor. 7 to 8: top F6; 12/8, triplet crotchets, acceleration, ornaments; B and Db major.

## Arranging implications

- Write in concert pitch, treble clef (no transposition). Ceiling by level (SR range): G1 D4-D5; G2 D4-G5; G3 D4-B5; G4 C4-C6; G5 C4-D6; G6 B3-E6; G7 Bb3-E6; G8 Bb3-F6.
- Keep the three lowest notes (Bb3, B3, C4) out of anything below Grade 4 (C4), Grade 6 (B3) and Grade 7 (Bb3); keep the line above C6 only for G5+ (D6) and E6/F6 for G6+.
- Key ladder (SR): G1 G, F; G2 C, d; G3 a; G4 D, e; G5 A, Bb, Eb, b, g; G6 E, Ab, f#, c; G7 c#, f; G8 B, Db. For G1-G3 transpose into F, G, C, d or a.
- Articulation ladder: G1 tongued or two-note slurs only (no longer slurs, no staccato marks); staccato G2; accents G3; tenuto, pause G4; slowing at end G5. Avoid wide slurred leaps at low levels: leaps are harder to keep legato (S4) [I].
- Rhythm ladder: dotted minim/minim/crotchet/paired quavers (G1); four-quaver groups, dotted crotchet+quaver, ties (G2); dotted-quaver and semiquaver cells, 3/8 (G3); 6/8, anacrusis, chromatic notes (G4); syncopation (G5); triplets, 9/8, 5/8, 5/4, metre changes (G6); 7/8, 7/4 (G7); 12/8, triplet crotchets (G8).
- Dynamics: f/mf only at G1; mp G2; p G3; ff/pp G5. Tempo: scale guide is the ceiling for even quavers (crotchet 50 at G1 to 132 at G8).
- Breath: oboe uses little air and stale air is the usual problem (S5, S6): give a clear exhale-and-inhale point at every phrase end, mark breaths, and avoid many long phrases in a row, especially high. Long phrases are physically possible, so rests exist for the player's air, not for lack of it; for levels 1-3 give a rest or long note every 2-4 bars [I].
- To go down a level: cut the range to the lower grade's ceiling, remove staccato/accents/tenuto, shorten slurs to two notes, replace dotted and semiquaver figures with quavers, drop accidentals and transpose into G/F/C, remove syncopation and metre changes.

## Confidence and gaps

- Verbatim from official ABRSM (S2, confirmed identical with S1 for oboe): SR length, time signatures, rhythms, dynamics, articulation, keys, Helmholtz ranges, scale boxes, speeds. High.
- Derived [D]: scientific pitch; lowest-tonic, scale tops and spans (assume lowest oboe note Bb3 and the "lowest possible tonic" rule). Medium-high. Trinity (S3) is only a cross-check (different grade spacing). S4-S6 are secondary (Wikipedia, teaching sites): medium.
- Unknown: Initial profile (none exists); set-piece ranges, keys and rhythms (not published in the syllabus; lists not copied); exact notes of the extended-range scales (graphics, p. 19); reed, half-hole or high-note (altissimo) fingering demands per grade; official phrase-length figures.

## Sources

- S1 (official). ABRSM, "Practical Music Grades: Woodwind Syllabus from 2022", qualification specification, 168 pp (rebranded Sep 2023). https://www.abrsm.org/sites/default/files/2023-10/Woodwind%202022%20Practical%20syllabus%20(0%20ALL)%2020230911.pdf . Taken: SR parameters, SR keys and ranges, oboe scale boxes (compared with S2).
- S2 (official, primary). ABRSM, "Woodwind Practical Grades Qualification Specification from 2026", 163 pp, valid from 1 Jan 2026 until further notice. https://www.abrsm.org/sites/default/files/2025-06/ABRSM%20Woodwind%20Practical%20Grades%20Qualification%20Specification%20from%202026.pdf . Taken: SR parameter table and KEYS/RANGES table (printed pp. 21-22, page images read), scale rules (even notes, lowest tonic, legato slurs, breath place free) and speed guide (pp. 13-15), the oboe grade boxes (Oboe Syllabus from p. 67), "Initial Grade not available for woodwind", oboe note (Grade 8 one piece may be on cor anglais). States scales, SR and aural stay the same as 2022; I checked this by text-diffing the oboe scale boxes and the SR keys/ranges: identical except page references. 2022 pieces valid to 31 Dec 2026.
- S3 (official, other board, cross-check). Trinity College London, "Woodwind Syllabus ... graded exams from 2022" (340 pp). https://trinitycollege.com/resource/?id=7385 . Taken: oboe offered Grades 1-8; SR parameter table p. 173 (articulation: slurs and accidentals G2, staccato G4, accents and tenuto G5, pause G6) and SR test span (octave G1-G2, 12th G3-G4, two octaves G5-G6, full range G7-G8); SR set about two grades below the exam grade.
- S4. Wikipedia, "Oboe". https://en.wikipedia.org/wiki/Oboe . Taken: music for the standard oboe is written in concert pitch; usual range Bb3 to about G6, common tessitura C4 to Eb6; double reed; semi-automatic octave keys; cross-intervals (leaps) are harder to play cleanly and legato.
- S5. oboehelp.com, "Breathing". https://oboehelp.com/breathing/ . Taken: young players often hold too much stale air; exhale at phrase ends before inhaling; with careful management very long phrases are possible, but not many in a row; long high-register phrases can cause dizziness.
- S6. M. Isaac Ripple, "Beginning Exercises for the Developing Oboist", Bandworld Magazine, 7 Feb 2025. https://bandworld.org/magazine/?p=7180 . Taken: the oboe needs consistent support but not a lot of air; mark inhale and exhale points in the music; exhale-first breathing exercises.
- Tried and not usable: abrsm.org HTML pages (403); no oboe-specific reed or finger-by-grade source found.
