# Trombone: difficulty by level (ABRSM Brass Practical Grades from 2023; Trinity Brass from 2024 for Initial)

**Read this when** the target instrument is trombone, at any level. Numbers come from ABRSM Brass syllabus (2023); the checker reads them from [../profiles/trombone.json](../profiles/trombone.json): `python3 scripts/check_level.py arrangement.musicxml --instrument trombone --grade N`. S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

Conventions: tenor trombone (B-flat) read in BASS clef is non-transposing, so written = sounding; all ranges below are bass-clef, scientific pitch (C4 = middle C), converted by me [D] from ABRSM's Helmholtz notation (B-flat = Bb2, c' = C4). ABRSM also publishes a treble-clef (B-flat transposing) column in which every note is written a major 9th above sounding (British brass-band style); I list those ranges in a note under the table. Tenor clef enters sight-reading at Grade 6 (ABRSM). "SR" = unseen sight-reading, parameters cumulative. Tags: [D] derived by me, [I] my inference, untagged = stated by the source. Initial: not offered by ABRSM for brass; Trinity's Initial is used as a proxy (S2).

## Table by grade

Columns: keys = SR new keys then scale keys (bass-clef block); range = SR range (bass clef, sounding = written); speeds = ABRSM guide, scale crotchet = N, arpeggio quaver = N.

| Grade | Keys (major / minor) | Time sigs (SR) | Note values and rhythms (SR) | Written range (SR, bass clef) | Technique demands (slide, scales) | Articulation | Dynamics and other | SR length |
|---|---|---|---|---|---|---|---|---|
| Initial (Trinity S2) | SR: Bb maj (bass-clef readers), C maj (treble-clef readers); no minor listed | 2/4 | crotchet, minim, semibreve | only the span is given: a 5th [S2]; exact notes unknown | avoids 7th position and an unclear low "Bb-C" group; "straightforward slide positions"; technical work = triad, lip slur, chromatic scale | tongued only | mf, moderato | unknown |
| 1 | SR: Bb maj, c min. Scales: Bb maj, G min 1 oct (arpeggios same) | 4/4, 3/4 (4 bars); 2/4 (6 bars) | dotted minim, minim, crotchet, paired quavers, crotchet rest | Bb2-Bb3 | Bb major scale needs positions 1,2,3,4 and 6 [D]; q=44, arp e=56 | tongued only | f, mf | 4 bars (6 in 2/4) |
| 2 | SR: C, Ab maj (no new minor). Scales: Ab, C maj; G, C min 1 oct | none new | four-quaver groups, dotted crotchet+quaver, minim rest, ties | Ab2-C4 | q=48, e=63 | tongued only | mp, cresc. hairpin | 8 bars |
| 3 | SR: d min; accidentals only within minor keys. Scales: Db, D maj; Bb, D min 1 oct; chromatic from C 1 oct | 3/8 | dotted-quaver figures, simple semiquaver patterns, quaver rest | Ab2-D4 | q=56, e=76 | tongued only; accents | p, dim. hairpin | 8 bars |
| 4 | SR: Eb maj, g min. Scales: F, Db maj 1 oct; Ab maj 12th; Eb maj "octave and down to dominant"; Eb min, E min 1 oct; G min 12th; chromatic from D; dom 7th Bb | 6/8 | chromatic notes, anacrusis | G2-D4 | q=63, e=88, 7ths q=44 | tongued or simple two-note slurs; tenuto | pause sign | c. 8 bars |
| 5 | SR: F, D, Db maj; e, bb min. Scales: A, C maj 12th; F, G maj 2 oct; A, C min 12th; G min 2 oct; chromatic F 2 oct; whole-tone F; dom 7ths Bb, C; dim 7th F | none new | semibreve, simple syncopation | F#2-E4 | 7th position enters SR (Trinity S2) [S2]; q=72, e=100, 7ths 50 | as G4 | ff, pp; slowing of tempo at end | c. 8-16 bars |
| 6 | SR: G maj, eb min. Scales: C, Db/C# maj/min 12th; F, F# maj/min 2 oct; thirds Ab maj 1 oct; chromatic and whole-tone F, F#; 7ths F, F#, B; dim 7th F# | 9/8, 5/8, 5/4; changes of time signature | triplet patterns, semiquaver rests (glyph, my reading) | F2-F4 | q=96, arp dotted crotchet=40, 7ths 56, thirds 84 | any combination of tongued and slurred notes; scales tongued / legato-tongued | fp, sf, subito, written cresc./dim.; swung style; tenor clef | c. 12-16 bars |
| 7 | SR: F# maj, f min. Scales: B, D maj/min 12th; G, Ab/G# maj/min 2 oct; extended-range C maj; thirds F maj 2 oct; chromatic and whole-tone G, Ab | 7/8, 7/4 | none new | F2-F#4 | q=108, dotted crotchet=44, 7ths 66, thirds 100 | scales add staccato | none new | c. 16-20 bars |
| 8 | SR: A maj, b min. Scales: Eb maj/min 12th; E, A, B maj/min 2 oct; extended-range F# maj and F harm min; thirds F#, Ab maj; whole-tone A, Bb | 12/8 | triplet crotchets | F2-G#4 | q=120, dotted crotchet=48, 7ths 72, thirds 112 | Trinity expects a "slurred tonguing" style that imitates valve slurs [S2] | acceleration; simple ornaments; alto clef (Trinity) | c. 16-24 bars |

Treble-clef (B-flat) trombone, written ranges [S1, D]: G1 C4-C5; G2 Bb3-D5; G3 Bb3-E5; G4 A3-E5; G5 Ab3-F#5; G6 G3-G5; G7 G3-Ab5; G8 G3-A#5 (sounds a major 9th lower).
Trinity SR test span (S2): Initial and G1 a 5th; G2 a 6th; G3 an octave; G4 a 10th; G5 a 12th; G6 a 13th; G7 two octaves; G8 two octaves plus a note.

## What changes between neighbouring grades

- 1 to 2: range grows only by a tone each way (Ab2-C4); four-quaver groups, ties, minim rests, mp; keys C and Ab join. Still tongued only.
- 2 to 3: 3/8, dotted-quaver and semiquaver figures, accents, p; range to D4; still tongued only.
- 3 to 4: the big step: simple two-note slurs appear, 6/8, chromatic notes, anacrusis, tenuto; range down to G2.
- 4 to 5: 7th position and low F#2 (position 5), syncopation, ff/pp, tenor clef (Trinity), slowing at end; scales go to 2 octaves.
- 5 to 6: free mixing of slurs and tongued notes, triplets, odd metres, metre changes, tenor clef in ABRSM SR, fp/sf; top F4.
- 6 to 7 to 8: 7/8, 7/4, then 12/8, triplet crotchets, acceleration, ornaments; top F#4 then G#4; alto clef at Trinity G8.

## Arranging implications

- Write in bass clef at sounding pitch. Add tenor clef only for G6+ parts that sit above about F4; treat alto clef as G8 only.
- Range ceiling by level (SR): G1 Bb2-Bb3 (one octave); G2 Ab2-C4; G3 Ab2-D4; G4 G2-D4; G5 F#2-E4; G6 F2-F4; G7 F2-F#4; G8 F2-G#4. For levels 1-3 keep the line inside about an octave and a tone; do not go below F2 at any level (E2 = 7th position, only Trinity G5+).
- Keys (SR ladder): G1 Bb, c; G2 C, Ab; G3 d; G4 Eb, g; G5 F, D, Db, e, bb; G6 G, eb; G7 F#, f; G8 A, b. Sharp keys first appear in SR at G5 (D major, e minor); flat keys dominate before that, though scale lists already include D major (G3) and E minor (G4). Transpose a melody into Bb, F, C or Eb for levels 1-4.
- Slurs: for G1-G3 mark nothing but tongued notes (no slurs at all); G4-G5 allow only simple two-note slurs; from G6 free mixing. Do not write long slurs or lip-trill figures for low levels (Trinity requires lip-flexibility work at every grade, but ABRSM SR gives no slurs below G4).
- Rhythm ladder: dotted minim/minim/crotchet/paired quavers (G1); four-quaver groups, dotted crotchet+quaver, ties (G2); dotted-quaver and semiquaver cells, 3/8 (G3); 6/8, anacrusis (G4); syncopation (G5); triplets, 9/8, 5/8, 5/4 (G6); 7/8, 7/4 (G7); 12/8, triplet crotchets (G8).
- Tempo: the scale guide is the comfortable ceiling for even quavers (crotchet 44 at G1 up to 120 at G8); a trombone line needs slower tempi than valved brass at the same grade (valved brass guide is crotchet 50 to 126).
- Fast leaps across the slide (positions 1 to 6) are slow work: avoid quaver passages that alternate near and far positions below G4 [I].
- Breath: no official phrase-length data found. SR lengths (4, 6, 8 bars at G1-G3) and Trinity's "breath at the top of the scale" imply short phrases at low levels [I]; give a rest or a long note every 2-4 bars at G1-G3.
- To go down a level: remove slurs and ornaments, drop accidentals and sharp keys, lower the top note to the grade ceiling, replace semiquavers with quavers, remove syncopation and metre changes.

## Confidence and gaps

- Verbatim official (S1): SR length, time signatures, rhythms, dynamics, articulation per grade, tenor clef at G6, keys and Helmholtz ranges, scale boxes, speed guide. High.
- Derived [D]: scientific-pitch conversion; position counts for the Bb scale; treble-clef equivalents. Secondary (S2 Trinity, other board, SR is "two grades below"): Initial profile, 7th position at G5, alto clef at G8, test span sizes. Medium. S3 Wikipedia: slide positions, practical range. Medium.
- Unknown: positions required by the set pieces; piece ranges; exact extents of ABRSM extended-range scales; exact meaning of Trinity's "Bb-C" limit; any official phrase-length or breath figure; F-attachment demands per grade (bass trombone is Grades 6-8 only).

## Sources

- S1 (official, primary). ABRSM, "Practical Grades Brass Syllabus from 2023", qualification specification (PDF updated 10 Feb 2023, 184 pp, valid "until further notice"; I found no newer brass syllabus). https://www.abrsm.org/sites/default/files/2023-09/brass-2023-prac-syllabus-10feb23.pdf . Taken: SR parameters table (pp. 26-27: length, time signatures, rhythms, articulation by instrument, dynamics, tenor clef); SR KEYS (p. 27) and RANGES (p. 28) tables, page images read to check accidentals; trombone scale/arpeggio/7th/chromatic/whole-tone/thirds boxes for each grade (bass-clef block); trombone speed guide (p. 17); "Initial Grade not available for brass"; trombone instrument notes (bass trombone Grades 6-8 only; clefs; alto trombone allowed).
- S2 (official, other board, secondary use). Trinity College London, "Brass Syllabus, digital and face-to-face assessment, graded exams from December 2024" (374 pp). https://trinitycollege.com/resource/?id=8403 . Taken: trombone is offered Initial-Grade 8 (French horn is not offered at Initial); Initial technical work (two short exercises: triad, lip slur, chromatic scale); SR parameter table p. 189 (time signature, rhythm, dynamic, articulation, slide-position limits, clefs) and SR key and range-span table p. 190; legato-tonguing remark for trombone; lip-flexibility exercise at every grade; SR set about two grades below the exam grade.
- S3. Wikipedia, "Trombone". https://en.wikipedia.org/wiki/Trombone . Taken: seven chromatic slide positions, one semitone per position; tenor/bass trombone non-transposing, bass clef with tenor/alto/treble as options; brass-band tenor trombone is a B-flat instrument in treble clef; lowest tenor note E2 (excluding pedals); practical top F5 or conservatively D5; F attachment extends the bottom.
- Tried and not usable: abrsm.org HTML pages (403); the ABRSM extended-range scale diagrams (pp. 21/23) are graphics whose exact notes I did not transcribe; an ABRSM-independent slide-position-by-grade source was not found (searches returned beginner charts only).
