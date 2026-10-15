# Trumpet: difficulty by level (ABRSM)

**Read this when** the target instrument is trumpet, at any level. Numbers come from ABRSM Brass syllabus (2023); the checker reads them from [../profiles/trumpet.json](../profiles/trumpet.json): `python3 scripts/check_level.py arrangement.musicxml --instrument trumpet --grade N`. S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

Pitch convention: ALL pitches and keys below are WRITTEN pitch for trumpet in B-flat (sounds a major 2nd lower than written, S4); ABRSM names scales by fingering, not concert pitch (D major sounds C) (S1). ABRSM's range/key tables put trumpet in one column with B-flat cornet, E-flat soprano cornet, flugelhorn and others reading treble clef, so they can only be written pitch (my reading). Scientific pitch, C4 = middle C (ABRSM prints Helmholtz, c' = C4, a-flat = A-flat3; converted by me). To write a concert-pitch tune for B-flat trumpet, transpose up a major 2nd (concert B-flat = written C, concert F = written G, concert E-flat = written F).

## Table by grade

SR = unseen sight-reading test (parameters cumulative; only new items listed). Range = official SR range, written. Scale speeds are the "all other brass" row of S1 (trumpet included).

| Grade | Keys (SR new maj / min; scales set) | Time sigs (SR) | Note values and rhythms (SR new) | Written range (SR; scale top [D]) | Register / fingering demands | Articulation / technique (scales) | Dynamics and other features (SR) | SR length / params |
|---|---|---|---|---|---|---|---|---|
| Initial (ABRSM: none; Trinity proxy S3) | ABRSM Prep Test only (3 short tunes from memory, 2 pieces, own piece c.16-24 bars, unmarked). Trinity Initial [T]: SR in C major; technical = one short exercise: major scale to the 5th, a triad, a lip slur (crotchet = 60-70) | [T] 2/4 | [T] crotchets, minims | [T] range of a 5th (exact notes unknown) | [T] three valves together not used | [T] tongued notes only | [T] mf, moderato | [T] 30 s prep; Trinity SR is about two grades below exam grade |
| 1 | maj C; min a. Scales: C maj; A min (any form), 1 oct | 4/4, 3/4 (4 bars); 2/4 (6 bars) | dotted minim, minim, crotchet, paired quavers; crotchet rests | C4-C5 (top C5 [D]) | [I] open-partial territory C4-G4-C5, few valve combinations | notes tongued only; scales tongued/slurred, crotchet = 50 (quaver pairs), arpeggios quaver = 66 | f, mf | 4 bars (4/4, 3/4) or 6 bars (2/4) |
| 2 | maj D, B-flat; min none. Scales: B-flat, D maj; A, D min, 1 oct | none new | four-quaver groups; dotted crotchet + quaver; tied notes; minim rests | B-flat3-D5 (top D5 [D]) | [I] D5 and low B-flat3 | tongued or simple two-note slurs; crotchet = 56; arpeggios quaver = 72 | mp, cresc. hairpin | 8 bars |
| 3 | min d (no new maj). Scales: E-flat, E maj; C, E min; chromatic from D, all 1 oct; accidentals within minor keys only | 3/8 | dotted crotchets; simple semiquaver patterns; quaver rests | A3-D5 (top E5 [D]) | [T] three valves together introduced; [I] low A3 | three-note slurs; accents; crotchet = 63; arpeggios quaver = 84 | p, dim. hairpin | length cell blank in table (8 bars carried [I]) |
| 4 | maj A; min e. Scales: F maj 1 oct; A-flat, B-flat maj 12th; E-flat maj 1 oct and down to the dominant; F min 1 oct; A, B min 12th; chromatic from B-flat 1 oct; dom 7th B-flat 1 oct | 6/8 | chromatic notes; anacrusis; tenuto; pause sign | A3-E5 (top F#5 [D]) | [I] F#5/E5 need firmer embouchure | four-note slurs; crotchet = 72; arpeggios quaver = 92; 7ths 46 | as G3 | c. 8 bars |
| 5 | maj E, F, E-flat; min b, c. Scales: B, C, D-flat maj 12th; G maj 2 oct; B-flat, C# min 12th; F min 1 oct and down to dominant; G min 2 oct; chromatic G 2 oct; whole-tone G 2 oct; dom 7ths C, D-flat; dim 7th G | none new | semibreve; simple syncopation | A-flat3-F#5 (top A-flat5 [D]) | [I] first 2-octave scales (G3-G5); lip slurs of any length (see articulation) | any combination of tongued and slurred notes; crotchet = 80; arpeggios quaver = 108; 7ths 54 | ff, pp; slowing of tempo at end | c. 8-16 bars |
| 6 | maj G; min f. Scales: D, E-flat maj and min 12th; G, A-flat/G# maj and min 2 oct; thirds B-flat 1 oct; chromatic and whole-tone G, A-flat; dom 7ths G, A-flat (12th), D-flat (2 oct); dim 7th G# | 9/8, 5/8, 5/4; changes of time signature | semiquaver rests; triplet patterns; swung style; rit. then a tempo | G3-G5 (top B-flat5 [D]) | SR now includes a section transposed (trumpet: into C, i.e. read as C trumpet, up a tone) (S1, S3) | crotchet = 104; arpeggios dotted crotchet = 40; 7ths 60; thirds 88 | fp, sf, subito, cresc., dim. in words | c. 12-16 bars |
| 7 | maj A-flat; min g. Scales: D-flat/C#, E maj and min 12th; A, B-flat maj and min 2 oct; extended-range D maj; thirds G maj; chromatic and whole-tone A, B-flat | 7/8, 7/4 | (none new listed) | G3-A-flat5 (top B5 [D]) | [I] upper range needs endurance; extended-range pattern goes beyond the normal span (top unknown, S2 p.21) | new names: legato-tongued / staccato / slurred; crotchet = 112; dotted crotchet = 44; 7ths 66; thirds 100 | as G6 | c. 16-20 bars |
| 8 | maj B; min c#. Scales: F maj and min 12th; F#, B, C maj and min 2 oct; extended-range A-flat maj, G harmonic min; thirds A, B-flat; chromatic F#, B, C; whole-tone B, C | 12/8 | triplet crotchets; acceleration; simple ornaments | G3-B-flat5 (scales to C6 [D]) | [I] high C6 only in scales; B-flat5 top of SR | crotchet = 126; dotted crotchet = 48; 7ths 72; thirds 120 | as G7 | c. 16-24 bars |

## What changes between neighbouring grades

- 1 to 2: top C5 to D5, low C4 to B-flat3; two-note slurs, ties, mp, cresc.; 8 bars; D and B-flat major.
- 2 to 3: low A3, 3/8, semiquavers, accents, three-note slurs, p/dim.; d minor.
- 3 to 4: top E5; 6/8, chromatic notes, anacrusis, tenuto, pause, four-note slurs; A major, e minor.
- 4 to 5: top F#5, low A-flat3; any slur combination, syncopation, ff/pp, rit.; 2-octave G scale; up to 16 bars.
- 5 to 6: top G5; 9/8, 5/8, 5/4, metre changes, triplets, swing, fp/sf; SR transposition into C.
- 6 to 7: top A-flat5; 7/8, 7/4; legato-tongue/staccato vocabulary; extended-range scale.
- 7 to 8: top B-flat5 (C6 in scales); 12/8, triplet crotchets, acceleration, ornaments; B major, c# minor.

## Arranging implications

- Write in written pitch for B-flat trumpet and pick the key from the grade list; for G1 use written C (concert B-flat) or A minor, then add D/B-flat (G2), A/e (G4), E/F/E-flat (G5).
- Range ceilings (written): G1 C4-C5, G2 B-flat3-D5, G3 A3-D5, G4 A3-E5, G5 A-flat3-F#5, G6 G3-G5, G7 G3-A-flat5, G8 G3-B-flat5. Prepared pieces may stray slightly beyond [I]; Trinity sets SR about two grades below exam grade (S3) and its range-of-test intervals are narrower: 5th (Initial, G1), 6th (G2), octave (G3), 10th (G4), 12th (G5), 13th (G6), two octaves (G7), two octaves plus a note (G8).
- Slur length is the clearest official ladder: G1 tongued only; G2 two-note slurs; G3 three; G4 four; G5 anything. To go down a grade, re-articulate long slurred phrases as tongued notes or break slurs at the grade limit. Slurs across partials are lip slurs [I]; avoid slurred leaps wider than a 5th below G4 [I].
- Keep high notes for later grades: nothing above D5 below G3, above E5 below G4, above F#5 below G5, above G5 below G7. Low notes: keep B-flat3 and below out of G1; A3 from G3; G3 from G6.
- Avoid notes needing all three valves (1-2-3, e.g. written C#4 and F#3) at G1-G2 [T, general fingering]; avoid fast chromatic runs below G4 (chromatic notes in SR from G4).
- Rhythm: minims/crotchets/quaver pairs at G1; four-quaver groups and dotted crotchet-quaver from G2; semiquavers and 3/8 from G3; 6/8 and chromatic from G4; syncopation from G5; triplets, swing, 5/8 5/4 9/8, semiquaver rests from G6; 7/8 7/4 from G7; no staccato wording appears in the brass SR table (unknown for staccato on trumpet; accents G3, tenuto G4).
- Dynamics: G1 f and mf only, G2 add mp, G3 add p, G5 add ff and pp, G6 add fp, sf.
- Breath and phrase length [I, no source]: 2-bar phrases at G1-G2, 4 bars at G3-G4, 4-8 bars from G5; give rests for embouchure rest in longer pieces; endurance is a limit for sustained notes above the staff (G5 and up) [I].
- Double/triple tonguing and flutter tonguing are not mentioned in ABRSM scale or SR requirements (S4 only says they exist); unknown whether set pieces need them.

## Confidence and gaps

- Keys, time signatures, rhythms, articulation by slur length, dynamics, SR length and range, scale spans and speeds: verbatim from official ABRSM (S1, S2); high. Note-value glyphs read from the rendered table; moderately high. Trumpet range read as written pitch by my reasoning (shared column); medium-high.
- Scale tops [D]: my calculation; excludes 7ths and extended-range; medium-high.
- Register/endurance/valve demands: ABRSM gives none; [T] Trinity and [I] inference; low-medium.
- Initial: ABRSM has none for brass; Trinity row only (other board); low-medium.
- Piece ranges per grade: unknown (not published; scores not accessible). Breath/phrase lengths: inference only.
- Not reached: ABRSM website HTML (403); SR sample books; teacher-blog and retailer searches gave no per-grade range or lip-slur data.

## Sources

- S1. ABRSM, Brass Practical Grades Syllabus from 2023, Qualification Specification (official PDF, downloaded and read; valid "until further notice"; I found no announcement of a newer ABRSM brass syllabus). https://www.abrsm.org/sites/default/files/2023-09/brass-2023-prac-syllabus-10feb23.pdf . Taken: sight-reading (SR) parameter table pp.26-27 (length, time signatures, rhythms, articulation by slur length, dynamics, transposition); SR keys p.27; SR written ranges p.28; scale rules and speed guide pp.16-17; trumpet/cornet/flugelhorn share lists p.13; SR and transposition test p.18 (Grades 6-8 SR includes a transposed section for trumpet); "Initial Grade not available for brass" p.161; Brass Prep Test pp.177-178. Retrieved 2026-10-14.
- S2. ABRSM, Trumpet, B-flat Cornet, E-flat Soprano Cornet, Flugelhorn Syllabus from 2023 (official PDF section). https://www.abrsm.org/sites/default/files/2023-10/Brass%202023%20Practical%20syllabus%20(2%20Trumpet)%2020230907.pdf . Taken: scale, arpeggio, chromatic, whole-tone, 7th, thirds and extended-range requirements per grade for B-flat trumpet (spans, articulation); extended-range graphic p.21. Retrieved 2026-10-14.
- S3. Trinity College London, Brass Syllabus (digital and face-to-face, online ed. Feb 2026), PDF. https://www.trinitycollege.com/resource?id=8403 . Taken (secondary, other board; used for the Initial level and as a cross-check): Initial trumpet technical work; SR parameters and keys/ranges for valved brass in treble clef pp.189-190; lip flexibility exercise at Grades 1-5; three valves together not used until Grade 3; SR set about two grades below the exam grade; trumpet syllabus designed for B-flat instruments. Retrieved 2026-10-14.
- S4. Wikipedia, "Trumpet". https://en.wikipedia.org/wiki/Trumpet . Taken: lowest written note F#3, standard range up to high C (C6), B-flat trumpet sounds a whole step lower, valve combinations, double/triple/flutter tonguing exist. Retrieved 2026-10-14.
- S5. Hong Kong LCSD Music Office, Trumpet syllabus. https://www.lcsd.gov.hk/en/mo/common/doc/06-tp.pdf . Taken: its scale requirements mirror ABRSM 2023 (cross-check only). Retrieved 2026-10-14.
- Tags: [D] derived by me from S2 tables with a script (lowest tonic from written F#3, stated span; excludes 7ths, whole-tone, thirds, extended-range); [I] my inference from sources plus general trumpet knowledge; [T] Trinity (S3); no tag = stated in S1/S2.
