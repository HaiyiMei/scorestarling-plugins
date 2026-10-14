# Flute: difficulty by level (ABRSM)

**Read this when** the target instrument is flute, at any level. Numbers come from ABRSM Woodwind syllabus (2022, unchanged for 2026); the checker reads them from [../profiles/flute.json](../profiles/flute.json): `python3 scripts/check_level.py arrangement.musicxml --instrument flute --grade N`. S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

Pitch convention: concert flute is non-transposing, so written = sounding. Scientific pitch, C4 = middle C (ABRSM prints Helmholtz, c' = C4, c'' = C5, c''' = C6; converted by me).

## Table by grade

SR = the unseen sight-reading test (parameters are cumulative: new items shown per grade). Range = official SR range. Scale span: 1 oct, 12th, 2 oct, 3 oct from the lowest possible tonic.

| Grade | Keys (SR new maj / min; scales set) | Time sigs (SR) | Note values and rhythms (SR new) | Written range (SR; scale top [D]) | Register / fingering demands | Articulation / technique (scales) | Dynamics and other features (SR) | SR length / params |
|---|---|---|---|---|---|---|---|---|
| Initial (ABRSM: none; Trinity proxy S4) | ABRSM Prep Test only (3 short tunes from memory, 2 pieces, own-choice piece c.16-24 bars, unmarked). Trinity Initial: SR in F major; scale = first five notes of F major, G major triad | Trinity: 2/4 | Trinity: crotchets and minims | Trinity: range of a 5th (exact notes not published; unknown) | [I] first-octave notes only, centred on F4-C5 | Trinity: tongued only | Trinity: mf, moderato | Trinity: 30 s prep, "about two grades below" exam grade |
| 1 | maj G, F; min none. Scales: F, G maj; E min (any form), 1 oct | 4/4, 3/4 (4 bars); 2/4 (6 bars) | dotted minim, minim, crotchet, paired quavers; crotchet rests | E4-F5 (scales top G5 [D]) | [I] only D5-F5 of the second octave; no C4-D#4 | tongued or simple 2-note slurs; scales tongued/slurred, crotchet = 50 (quaver pairs), arpeggios quaver = 72 | f, mf | 4 bars (4/4, 3/4) or 6 bars (2/4); 30 s look-through |
| 2 | maj C; min e (natural only). Scales: C maj (from C5, 1 oct); F, G maj 12th; A min 1 oct; E min 12th | none new | groups of four quavers; dotted crotchet + quaver; tied notes; minim rests | E4-G5 (top D6 [D]) | [I] still below C6; scales touch D6 | + staccato; crotchet = 56; arpeggios quaver = 84 | mp, cresc. hairpin | 8 bars |
| 3 | maj none; min a (accidentals only within minor keys). Scales: G, B-flat maj 12th; D, F maj 2 oct; E, G min 12th; D min 2 oct; chromatic from G, 1 oct | 3/8 | dotted crotchets; simple semiquaver patterns; quaver rests | D4-C6 (top F6 [D]) | [I] first grade reaching C6 (top of 2nd octave per S6) and low D4 | + accents; crotchet = 63; arpeggios quaver = 96 | p, dim. hairpin | length not restated in table (8 bars carried from G2 [I]) |
| 4 | maj B-flat; min d. Scales: A, B-flat maj 12th; C, E-flat, G maj 2 oct; A, B min 12th; C, G min 2 oct; chromatic from D 2 oct; dom 7th in G | 6/8 | chromatic notes; anacrusis; tenuto; pause sign | D4-F6 (top G6 [D]) | [I] first entry into the third octave (D6-F6, S6): needs correct vented fingerings (S7) | + tenuto; crotchet = 72; arpeggios quaver = 108; 7ths crotchet = 54 | as G3 | c. 8 bars |
| 5 | maj D, A, E-flat; min b, g. Scales: C, D, E, A-flat, A maj; C, E, F, F#, A min (all 2 oct); chromatic from C# and F; dom 7ths A, B-flat; dim 7th on E-flat | none new | simple syncopation | C4-G6 (top A6 [D]) | [I] full low register C4 appears; third octave up to G6 | crotchet = 84; arpeggios quaver = 126; 7ths 63 | ff, pp; slowing of tempo at end | c. 8-16 bars |
| 6 | maj E, A-flat; min f#, c. Scales: D-flat/C#, D, E, F, B-flat maj and min (harmonic and melodic) 2 oct; thirds C maj 1 oct; chromatic D, E, B-flat; 7ths | 9/8, 5/8, 5/4; changes of time signature | triplet patterns; swung style; rit. then a tempo | C4-A6 (top B-flat6 [D]) | [I] A6 needs secure upper third octave | crotchet = 96; arpeggios dotted crotchet = 48; 7ths 72; thirds 88 | as G5 | c. 12-16 bars |
| 7 | maj none new; min c#, f. Scales: D-flat/C#, E-flat, G, A, B maj and min 2 oct; extended-range F maj; thirds D maj; chromatic C#, G, A, B | 7/8, 7/4 | (no new rhythmic item listed) | C4-B-flat6 (top B6 [D]) | [I] B-flat6 sits in the upper third octave (S6: third octave D6-C7), where fingerings are hardest | new names: legato-tongued / staccato / slurred; crotchet = 112; arpeggios dotted crotchet = 54; 7ths 80; thirds 100 | as G6 | c. 16-20 bars |
| 8 | maj B, D-flat. Scales: E-flat, E, F#, A-flat/G# maj and min 2 oct; C maj and min 3 oct; extended-range G maj, F harmonic min; thirds G, B-flat; whole-tone F (2 oct), C (3 oct) | 12/8 | triplet crotchets; acceleration of tempo; simple ornaments | C4-B6 (3-octave scales to C7 [D]) | [I] B6 and C7 at the very top; flute SR may use 8va sign | crotchet = 132; arpeggios dotted crotchet = 63; 7ths 96; thirds 120 | as G7; 8va sign | c. 16-24 bars |

Extended-range scale/arpeggio patterns (G7 F maj; G8 G maj, F harmonic min, G maj and F min arpeggios) run past the normal span; the exact top note is not transcribed here (unknown; see S1 p.20 graphic).

## What changes between neighbouring grades

- 1 to 2: one more tone on top (F5 to G5), C major added, ties, staccato, mp and cresc., 4-6 bars become 8.
- 2 to 3: range opens both ways (D4 low, C6 high); 3/8, semiquaver patterns, accents, p/dim.; minor-key accidentals appear.
- 3 to 4: third octave begins (D6-F6); 6/8, chromatic notes, anacrusis, tenuto, pause; B-flat major and G minor.
- 4 to 5: lowest note C4 and top G6; syncopation, ff and pp, ritardando at the end; three-flat/three-sharp keys (E-flat, A) arrive in SR; longer tests up to 16 bars.
- 5 to 6: mixed and odd metres (9/8, 5/8, 5/4, time-signature changes), triplets, swing; E and A-flat major; thirds in scales.
- 6 to 7: B-flat6 top, 7/8 and 7/4; c# and f minor; legato-tongue/staccato vocabulary; 16-20 bars.
- 7 to 8: B6 top (C7 in scales); 12/8, triplet crotchets, acceleration, ornaments, 8va; B and D-flat major.

## Arranging implications

- Use the SR range as the ceiling for a "reading-level" version: G1 E4-F5, G2 to G5, G3 D4-C6, G4 to F6, G5 C4-G6, G6 to A6, G7 to B-flat6, G8 to B6. Exam pieces are prepared, so they may stray slightly beyond (I); Trinity says its SR is about two grades below the exam grade (S4), so treat SR limits as safe-to-read, not a hard piece limit.
- To go down a grade: (1) transpose or octave-shift so the top note drops under the lower grade's ceiling; the cheapest simplification is removing third-octave notes (D6 upward) below G4; (2) avoid C4-D4 below G5/G3 and C6 below G3; (3) move to a key listed for the lower grade (G1 G/F only; G2 add C and E/A minors; G3 a; G4 B-flat/d; G5 D, A, E-flat, b, g); (4) replace semiquaver figures with quaver pairs below G3, dotted crotchet + quaver below G2, syncopation below G5; (5) drop chromatic notes below G4, 6/8 below G4, 3/8 below G3; (6) keep to 4/4, 3/4, 2/4 for G1-G2.
- To stay at grade N: do not exceed the N-row range, keep new rhythmic items (see column) to isolated spots, and keep dynamics to the grade's set (G1 f/mf only, G2 add mp, G3 add p, G5 add ff/pp).
- Slurs: G1-G2 simple two-note slurs only (S1 gives no longer-slur limit for woodwind; for G3+ unknown, [I] keep slurs to a bar or less at G1-G3).
- Breathing and phrase length ([I], no official source): SR tests are 4-8 bars at G1-G3, so write phrases of 2 bars at G1-G2 and up to 4 bars at G3-G4 with a rest or long note for a breath; G5-G6 phrases of 4-8 bars; G7-G8 8 bars or more. Keep the long fast scale-like runs (crotchet=96-132 benchmarks in S1) for G6+.
- Second-octave D and E-flat, and any third-octave note, are common weak spots (S7): at G4-G5 use stepwise approaches and avoid leaping to or trilling third-octave notes.
- Low C4/C#4 and high B6/C7 are extreme at their grades; treat G7-G8 only as the home of those notes.

## Confidence and gaps

- Keys, time signatures, rhythms, articulation, dynamics, SR length, SR range, scale spans, speeds: verbatim from official ABRSM (S1-S3), high confidence; 2022 and 2026 tables confirmed identical. Note-value glyphs were read from the rendered table (dotted crotchet vs. other symbols), moderately high.
- Scale tops [D]: calculated by me, excludes 7ths, whole-tone, thirds and extended-range; medium-high.
- Register/fingering demands: inferred ([I]) from official ranges plus S5-S7; ABRSM publishes no fingering or register statements. Medium-low.
- Initial: ABRSM has no Initial for woodwind (S1); the Initial row is Trinity (S4), different board, low-medium.
- Typical range of actual exam pieces: unknown; ABRSM publishes only SR ranges. I did not extract piece ranges from scores (not accessible).
- Breath and phrase lengths: no source; pure inference.
- Not reached: ABRSM website HTML (403); the sight-reading sample books; retailer, teacher-forum and HKEAA searches yielded no extra grade-by-grade range data.

## Sources

- S1. ABRSM, Practical Music Grades Woodwind Syllabus from 2022, Qualification Specification (official PDF, downloaded and read). https://www.abrsm.org/sites/default/files/2023-10/Woodwind%202022%20Practical%20syllabus%20(0%20ALL)%2020230911.pdf . Taken: sight-reading (SR) parameter table (length, time signatures, rhythms, articulation, dynamics) pp.23-24; SR keys and ranges table p.24; scale rules, "lowest possible tonic" rule, even-note rule, speed guide pp.16-17; "Initial Grade not available for woodwind" and Prep Test pp.160-161. Retrieved 2026-10-14.
- S2. ABRSM, Flute Syllabus from 2022 (official PDF, downloaded and read). https://www.abrsm.org/sites/default/files/2023-10/Woodwind%202022%20Practical%20syllabus%20(3%20Flute)%2020230911.pdf . Taken: scale, arpeggio, chromatic, 7th, whole-tone, thirds and extended-range requirements per grade (keys, spans, articulations); footnote that low B (foot joint) is excluded. Retrieved 2026-10-14.
- S3. ABRSM, Woodwind Practical Grades Qualification Specification from 2026 (official PDF). https://www.abrsm.org/sites/default/files/2025-06/ABRSM%20Woodwind%20Practical%20Grades%20Qualification%20Specification%20from%202026.pdf . Taken: statement that scales/arpeggios, sight-reading and aural requirements "stay the same" as the 2022 syllabus; I compared the SR keys and ranges tables and they are identical. The 2026 syllabus replaces repertoire only; 2022 pieces valid to 31 Dec 2026. Retrieved 2026-10-14.
- S4. Trinity College London, Woodwind Syllabus (qualification specs from 2022, online ed.), PDF. https://trinitycollege.com/resource/?id=7385 . Taken (secondary, a different exam board, used only as a cross-check and for the Initial level): Initial flute technical work, SR parameters, SR keys and ranges (as intervals), statement that SR is set about two grades below the exam grade. Retrieved 2026-10-14.
- S5. Wikipedia, "Flute". https://en.wikipedia.org/wiki/Flute . Taken: lowest note C4 (B3 with B foot joint); about three octaves. Retrieved 2026-10-14.
- S6. Woodwind Fingering Guide, Flute. https://www.wfg.woodwind.org/flute/index.html . Taken: octave splits B3-C#5 / D5-C#6 / D6-C7 (so the third octave starts at D6). Retrieved 2026-10-14.
- S7. Band World, "Ten things every band director should know about flutes, part 2". https://bandworld.org/magazine/index.php/ten-things-that-every-band-director-should-know-about-flutes-part-2/ . Taken: 2nd-octave D and E-flat are commonly misfingered; third-octave notes are made by venting a tone hole from the second-octave fingering; overblowing gives poor tone and pitch. Retrieved 2026-10-14.
- Tags used below: [D] derived by me from S2 with a small script (lowest tonic C4/D-flat4 etc. plus the stated span); [I] my inference from S1-S7 plus general flute knowledge; no tag = stated in S1/S2.
