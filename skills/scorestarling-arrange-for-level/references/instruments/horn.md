# French horn (in F): difficulty by level (ABRSM Brass Practical Grades from 2023; Trinity Brass from 2024 as cross-check)

**Read this when** the target instrument is horn, at any level. Numbers come from ABRSM Brass syllabus (2023); the checker reads them from [../profiles/horn.json](../profiles/horn.json): `python3 scripts/check_level.py arrangement.musicxml --instrument horn --grade N`. S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

Conventions: ALL pitches and keys below are WRITTEN pitch for horn in F, treble clef. The horn in F sounds a perfect 5th lower than written (S3), so to put a concert-pitch tune on a horn part, write it a perfect 5th higher (concert F major becomes written C major). ABRSM names scales by written key. Sounding ranges are given in brackets [D]. Scientific pitch, C4 = middle C; ABRSM prints Helmholtz (c' = C4), converted by me. "SR" = unseen sight-reading, cumulative. ABRSM's "E-flat Horn" is the tenor horn, a different instrument, and is not covered. Tags: [D] derived by me, [I] my inference, untagged = stated by source. Initial: not documented (see gaps).

## Table by grade

Columns: keys = SR new keys then scale keys; range = SR written range [sounding]; speeds = ABRSM guide, scale crotchet = N, arpeggio quaver = N.

| Grade | Keys (major / minor, written) | Time sigs (SR) | Note values and rhythms (SR) | Written range (SR) [sounding] | Technique demands | Articulation | Dynamics and other | SR length |
|---|---|---|---|---|---|---|---|---|
| Initial | not offered (ABRSM brass; Trinity horn starts at G1) | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| 1 | SR: C maj, a min. Scales: C maj, A min 1 oct (starting an octave above lowest tonic) | 4/4, 3/4 (4 bars); 2/4 (6 bars) | dotted minim, minim, crotchet, paired quavers, crotchet rest | C4-C5 [F3-F4] | Trinity SR avoids three valves together; q=50, e=66 | tongued only | f, mf | 4 bars (6 in 2/4) |
| 2 | SR: Bb maj. Scales: Bb, D maj; A, D min, 1 oct from an octave above lowest tonic | none new | four-quaver groups, dotted crotchet+quaver, minim rest, ties | Bb3-D5 [Eb3-G4] | q=56, e=72 | tongued or simple two-note slurs | mp, cresc. hairpin | 8 bars |
| 3 | SR: G maj, d min (accidentals only in minor keys). Scales: Eb maj 1 oct; G maj a 12th (from below the stave); C min 1 oct; G min 12th; chromatic from C 1 oct | 3/8 | dotted-quaver figures, simple semiquaver patterns, quaver rest | A3-D5 [D3-G4] | three valves together, slurred groups (Trinity); q=63, e=84 | three-note slurs; accents | p, dim. hairpin | 8 bars |
| 4 | SR: Eb maj, b min. Scales: Bb maj 12th; Eb maj octave and down to dominant; E, F maj 2 oct; A, Bb min 12th; F min 2 oct; chromatic G 1 oct; dom 7th F 1 oct | 6/8 | chromatic notes, anacrusis | G3-E5 [C3-A4] | q=72, e=92, 7ths q=46 | four-note slurs; tenuto | pause sign | c. 8 bars |
| 5 | SR: A, E, F maj; g, c min. Scales: A, B maj 12th; D, G maj 2 oct; C min 12th; A min octave and down; D, F# min 2 oct; chromatic F 2 oct; whole-tone F 2 oct; dom 7ths A, C; dim 7th G | none new | semibreve, simple syncopation | F3-F5 [Bb2-Bb4] | q=80, e=108, 7ths 54 | any combination of tongued and slurred | ff, pp; slowing of tempo at end | c. 8-16 bars |
| 6 | SR: D maj, f min. Scales: Db/C#, E, F#, Ab/G# maj and min 2 oct; thirds C maj 1 oct; chromatic Db, E, Ab; whole-tone D, Eb; 7ths F#, B, Db; dim 7th F# | 9/8, 5/8, 5/4; metre changes | triplet patterns, semiquaver rests (my reading of glyph) | F3-G5 [Bb2-C5] | SR includes a transposition-into-Eb section (also Trinity G6); q=104, dotted crotchet=40, 7ths 60, thirds 88 | any combination | fp, sf, subito, written cresc./dim.; swung style | c. 12-16 bars |
| 7 | SR: Ab maj, e min. Scales: B, D, Eb maj/min 2 oct; Bb maj/min 2 oct lower and upper; extended-range G maj; thirds F maj 2 oct; chromatic B, Eb, A; whole-tone E, Ab; 7ths E, G, Ab, Eb; dim 7ths B, Eb | 7/8, 7/4 | none new | F3-Ab5 [Bb2-Db5] | q=112, dotted crotchet=44, 7ths 66, thirds 100 | scales: legato-tongued / staccato / slurred | none new | c. 16-20 bars |
| 8 | SR: Db maj, bb min. Scales: C, F maj/min 2 oct; A, Bb maj/min 3 oct; extended-range E maj, D harm min; thirds Eb, A maj 2 oct; whole-tone C, Bb; 7ths F, Bb, D, Eb; dim 7ths F, A, Bb | 12/8 | triplet crotchets | E3-A5 [A2-D5] | q=126, dotted crotchet=48, 7ths 72, thirds 120; Trinity G8 SR adds simple bass clef | as G7 | acceleration; simple ornaments | c. 16-24 bars |

Concert-pitch equivalents of the SR keys [D] (written minus a perfect 5th): G1 F / d; G2 Eb; G3 C / g; G4 Ab / e; G5 D, A, Bb / c, f; G6 G / bb; G7 Db / a; G8 Gb / eb.

## What changes between neighbouring grades

- 1 to 2: slurs begin (two notes), four-quaver groups, ties, mp; range grows to Bb3-D5; Bb major.
- 2 to 3: three-note slurs, 3/8, dotted and semiquaver figures, G major and d minor; low note drops to A3 (written).
- 3 to 4: four-note slurs, 6/8, chromatic notes, anacrusis, Eb major and b minor; low G3, top E5.
- 4 to 5: slurs unrestricted, syncopation, ff/pp, sharp keys enter SR (A and E major, c and g minor); low F3, top F5.
- 5 to 6: odd metres and metre changes, triplets, fp/sf, transposition into Eb in SR; top G5.
- 6 to 8: 7/8, 7/4, 12/8, triplet crotchets, ornaments; top Ab5 then A5; low E3 at G8.

## Arranging implications

- Write horn parts a perfect 5th above concert pitch, treble clef, key signature of the written key. Check the written range against the grade ceiling (G1 C4-C5; G2 Bb3-D5; G3 A3-D5; G4 G3-E5; G5 F3-F5; G6 F3-G5; G7 F3-Ab5; G8 E3-A5).
- Concert keys that map onto early written keys: concert F or d (written C or a) is the Grade 1 home; concert Eb (written Bb) Grade 2; concert C or g (written G or d) Grade 3; concert Ab or e (written Eb or b) Grade 4.
- Slur ladder: G1 tongued only; G2 two-note slurs; G3 three-note; G4 four-note; G5+ free. Without valves only harmonic-series notes exist (S3), so a slurred leap is a lip slur; keep slurred intervals small below G5 [I].
- To go down a level: shorten slurs, cut the top (C5 at G1 rising to A5 at G8) and the bottom (C4 at G1 falling to E3 at G8) back to the grade ceiling, remove accidentals, replace semiquavers with quavers, avoid hand-stopped, muted and transposed passages (none are required below G6).
- Rhythm ladder: dotted minim/minim/crotchet/paired quavers (G1); four-quaver groups, dotted crotchet+quaver, ties (G2); dotted-quaver and semiquaver cells, 3/8 (G3); 6/8, anacrusis, chromatic notes (G4); syncopation (G5); triplets, 9/8, 5/8, 5/4 (G6); 7/8, 7/4 (G7); 12/8, triplet crotchets (G8).
- Dynamics: mf and f only at G1; add mp at G2; p at G3; ff and pp at G5.
- Tempo: scale guide is the ceiling for even quavers: crotchet 50 (G1), 56, 63, 72, 80, 104, 112, 126 (G8).
- Breath: no source gave horn phrase lengths. SR lengths (4, 6, 8 bars at G1-G3) imply short phrases; put a rest or long note every 2-4 bars for levels 1-3 [I].
- Secondary check [S4]: beginner/intermediate solo books sit between about G3 and F5 written, which matches the ABRSM G4-G5 ceiling; high A (A5) only at the top of the range.

## Confidence and gaps

- Verbatim official (S1): SR length, time signatures, rhythms, dynamics, slur limits, Eb transposition test, keys, Helmholtz ranges, scale boxes, speed guide. High.
- Derived [D]: scientific pitch, sounding ranges, concert-pitch keys. Secondary (S2 Trinity, S3, S4): valve-combination limits, bass clef at Trinity G8, general horn facts. Medium. Inferred [I]: slur and phrase advice.
- Unknown: Initial level (no board documents one); written ranges and keys of the set pieces; whether stopped or muted horn is required (not in the syllabus); extended-range scale extents (graphics on p. 20, not transcribed); hand-stopping, high-register and endurance demands per grade.

## Sources

- S1 (official, primary). ABRSM, "Practical Grades Brass Syllabus from 2023", qualification specification (updated 10 Feb 2023, 184 pp, valid until further notice; no newer brass syllabus found). https://www.abrsm.org/sites/default/files/2023-09/brass-2023-prac-syllabus-10feb23.pdf . Taken: SR parameters (pp. 26-27) including slurs by instrument and the Eb transposition test at Grades 6-8; SR KEYS (p. 27) and RANGES (p. 28) tables, read from page images; horn scale, arpeggio, 7th, chromatic, whole-tone, thirds and extended-range boxes for each grade; speed guide (p. 17, "all other brass"); "Initial Grade not available for brass"; horn accompanied pieces are published in F editions; scales named by fingering, not concert pitch.
- S2 (official, other board, cross-check). Trinity College London, "Brass Syllabus ... graded exams from December 2024" (374 pp). https://trinitycollege.com/resource/?id=8403 . Taken: French horn offered Grades 1-8 only (no Initial); SR parameter table p. 189 (three valves together not used at the lowest grades, slurred groups at G3, transposition into Eb at G6, simple bass clef at G8) and SR span table p. 190 (G6 two octaves, G7 two octaves and a semitone, G8 two octaves and a minor sixth); lip-flexibility exercise at every grade; SR set about two grades below the exam grade.
- S3. Wikipedia, "Horn (instrument)". https://en.wikipedia.org/wiki/Horn_(instrument) . Taken: horn in F sounds a fifth lower than written; double horn F/B-flat; without valves only the harmonic series is available; pitch is controlled by lip tension and valve operation; hand-in-bell changes tuning.
- S4. Colin Dorman, blog on horn solo books by level. https://colindorman.com/?p=4202 . Taken (secondary, written/sounding not stated, read as written because it matches S1): middle-school solo books rarely go above top-line F or below G below middle C; high-school books can reach high A.
- Tried and not usable: abrsm.org HTML pages (403); no ABRSM per-instrument horn PDF was needed; no source gave horn-specific breath or endurance numbers (searches returned forum posts only).
