# Clarinet: difficulty by level (ABRSM)

**Read this when** the target instrument is clarinet, at any level. Numbers come from ABRSM Woodwind syllabus (2022, unchanged for 2026); the checker reads them from [../profiles/clarinet.json](../profiles/clarinet.json): `python3 scripts/check_level.py arrangement.musicxml --instrument clarinet --grade N`. S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

Pitch convention: ALL pitches and keys below are WRITTEN pitch for clarinet in B-flat (sounds a major 2nd lower; a clarinet in A, also allowed by ABRSM per S1, sounds a minor 3rd lower [general knowledge, not in S1]; same written parts). ABRSM names scales by fingering, not concert pitch (D major on B-flat clarinet sounds C). Scientific pitch, C4 = middle C (ABRSM prints Helmholtz, a = A3, c' = C4; converted by me). To write a concert-pitch tune for B-flat clarinet, transpose up a major 2nd (concert F major = written G major, concert B-flat = written C).

## Table by grade

SR = unseen sight-reading test (parameters cumulative; only new items listed). Range = official SR range, written.

| Grade | Keys (SR new maj / min; scales set) | Time sigs (SR) | Note values and rhythms (SR new) | Written range (SR; scale top [D]) | Register / fingering demands | Articulation / technique (scales) | Dynamics and other features (SR) | SR length / params |
|---|---|---|---|---|---|---|---|---|
| Initial (ABRSM: none; Trinity proxy S3) | ABRSM Prep Test only (tunes from memory, 2 pieces, own piece c.16-24 bars, unmarked). Trinity Initial: SR in C major; first five notes of C major scale, D minor triad | Trinity: 2/4 | Trinity: crotchets, minims | Trinity: range of a 5th (exact notes unknown) | [I] chalumeau register only; exact notes unknown | Trinity: tongued only | Trinity: mf, moderato | Trinity: 30 s prep |
| 1 | maj G, F; min none. Scales: F, G maj; A min, 1 oct | 4/4, 3/4 (4 bars); 2/4 (6 bars) | dotted minim, minim, crotchet, paired quavers; crotchet rests | A3-A4 (top A4 [D]) | Chalumeau plus throat tones (G4-A4); no register key (S4, S5, S8) | tongued or simple 2-note slurs; scales tongued/slurred, crotchet = 50 (quaver pairs), arpeggios quaver = 72 | f, mf | 4 bars (4/4, 3/4) or 6 bars (2/4) |
| 2 | maj C; min a (natural only). Scales: B-flat maj 1 oct; F, C maj 12th; D min 1 oct; A min 12th | none new | four-quaver groups; dotted crotchet + quaver; tied notes; minim rests | F3-B-flat4 (top G5 [D]) | SR still avoids the break; but scales/arpeggios to a 12th (C4-G5) already cross it [D] | + staccato; crotchet = 56; arpeggios quaver = 84; chromatic not yet | mp, cresc. hairpin | 8 bars |
| 3 | min d; accidentals only within minor keys. Scales: A, D maj 12th; G, B-flat maj 2 oct; B, D min 12th; G min 2 oct; chromatic from G 1 oct | 3/8 | dotted crotchets; simple semiquaver patterns; quaver rests | F3-G5 (top B-flat5 [D]) | First SR range that crosses the break (B4 onward, register key; S4, S6) | + accents; crotchet = 63; arpeggios quaver = 96 | p, dim. hairpin | length cell blank in table (8 bars carried [I]) |
| 4 | maj B-flat; min g. Scales: E-flat maj 12th; F, A, C, D maj 2 oct; C min 12th; A, B, D min 2 oct; chromatic from F 2 oct; dom 7th in C | 6/8 | chromatic notes; anacrusis; tenuto; pause sign | F3-B-flat5 (top D6 [D]) | Upper clarion in SR; D6 (first altissimo note) appears only in scales [D] | + tenuto; crotchet = 72; arpeggios quaver = 108; 7ths 54 | as G3 | c. 8 bars |
| 5 | maj D, A, E-flat; min e, b. Scales: E, G, A-flat, B-flat, E-flat maj; F, F#, G, C, C# min (all 2 oct); chromatic A, C; dom 7ths D, F; dim 7th G | none new | simple syncopation | E3-D6 (top E-flat6 [D]) | Lowest note E3 and first altissimo note D6 (above C6, S4) in SR; tongued upper-clarion notes can sound undertones (S7) | crotchet = 84; arpeggios quaver = 126; 7ths 63 | ff, pp; slowing of tempo at end | c. 8-16 bars |
| 6 | maj E, A-flat; min f#, c. Scales: A-flat/G#, B, C, D maj and min 2 oct; E maj and min 3 oct; thirds B-flat maj 1 oct; chromatic G#, D (2 oct), E (3 oct); dom 7ths C#, G (2 oct), A (3 oct); dim 7ths G#, D, E | 9/8, 5/8, 5/4; changes of time signature | triplet patterns; swung style; rit. then a tempo | E3-E-flat6 (3-octave scales E3-E6 [D]) | [I] altissimo up to E-flat6 | crotchet = 96; arpeggios dotted crotchet = 48; 7ths 72; thirds 88 | as G5 | c. 12-16 bars |
| 7 | min c#, f (no new maj). Scales: F#, A, B-flat, D-flat/C# maj and min 2 oct; F maj and min 3 oct; extended-range C maj; thirds G maj 2 oct | 7/8, 7/4 | (none new listed) | E3-E6 (top F6 [D]) | [I] E6 near the top of practical altissimo | new names: legato-tongued / staccato / slurred; crotchet = 112; dotted crotchet = 54; 7ths 80; thirds 100 | as G6 | c. 16-20 bars |
| 8 | maj B, D-flat. Scales: B, C, E-flat maj and min 2 oct; F#, G maj and min 3 oct; extended-range A maj, E harmonic min; thirds D (2 oct), F (3 oct); whole-tone D-flat (2 oct), E (3 oct) | 12/8 | triplet crotchets; acceleration; simple ornaments | E3-F6 (top G6 [D]) | [I] F6/G6 secure altissimo | crotchet = 132; dotted crotchet = 63; 7ths 96; thirds 120 | as G7 | c. 16-24 bars |

## What changes between neighbouring grades

- 1 to 2: top A4 to B-flat4 (still no break), F3 below; C major; ties, staccato, mp, cresc.; 8 bars.
- 2 to 3: SR crosses the break (to G5); 3/8, semiquavers, accents, p/dim.
- 3 to 4: top B-flat5, 6/8, chromatic notes, anacrusis, tenuto, pause; B-flat major, G minor.
- 4 to 5: low E3 and altissimo D6 enter; syncopation, ff/pp, rit.; up to 16 bars.
- 5 to 6: 9/8, 5/8, 5/4, metre changes, triplets, swing; E and A-flat major; 3-octave scales (E3-E6).
- 6 to 7: 7/8, 7/4; c# and f minors; extended-range scale; E6.
- 7 to 8: F6 top; 12/8, triplet crotchets, acceleration, ornaments; B and D-flat major.

## Arranging implications

- Write in WRITTEN pitch and choose the written key from the grade list; for concert-pitch material transpose up a major 2nd first (concert F to written G for G1, concert B-flat to written C for G2).
- SR range ceilings: G1 A3-A4, G2 F3-B-flat4, G3 F3-G5, G4 to B-flat5, G5 E3-D6, G6 to E-flat6, G7 to E6, G8 to F6. Prepared pieces can exceed these a little [I]; Trinity sets SR about two grades below the exam grade (S3).
- Lowest-effort way down a grade: remove the break crossing (keep the tune at or below B-flat4 for G1-G2 level; A4 max at G1) by transposing the whole tune down or inverting leaps (S4, S5). If a crossing must stay, make it a single, prepared, slurred step with a rest before it [I]; the 12th jump low G to D5 is the classic fault zone (S6).
- Keep altissimo (D6 up) out below G5 and sustained E-flat6 and above out below G6; avoid loud, tongued entries on upper clarion notes at lower grades (S7).
- Low E3/F3: keep F3 for G2+ and E3 for G5+ in SR terms; below that stay at A3 or higher for G1.
- Keys: G1 only G and F major (concert F and E-flat on B-flat clarinet); G2 adds C and A minor; G3 d; G4 B-flat/g; G5 D, A, E-flat/e, b; G6 E, A-flat/f#, c; G7 c#, f; G8 B, D-flat. A clarinet (allowed per S1; written a minor 3rd above concert, general knowledge) can give friendlier written keys for sharp concert keys [I].
- Rhythm: below G3 keep to minims, crotchets, quaver pairs; dotted crotchet-quaver from G2; semiquavers from G3; syncopation from G5; triplets, swing, 5/8 5/4 9/8 from G6.
- Articulation: G1-G2 mostly tongued with two-note slurs only (S1 gives no longer-slur limit for woodwind; unknown, keep slurs to a bar or less at G1-G3 [I]).
- Breath and phrase length [I, no source]: 2-bar phrases at G1-G2, up to 4 bars at G3-G4, 4-8 bars from G5; leave long fast runs (crotchet = 96-132 benchmarks in S1) for G6+.

## Confidence and gaps

- Keys, time signatures, rhythms, articulation, dynamics, SR length and range, scale spans and speeds: verbatim from official ABRSM (S1, S2); high. Note-value glyphs read from the rendered table; moderately high.
- Scale tops [D]: my calculation; excludes 7ths and extended-range; medium-high.
- Register demands (break, altissimo, throat tones): official ranges plus secondary teaching sources S4-S8; the register boundaries differ slightly between sources (S4 chalumeau top B-flat4; S5 separates F#4 and throat tones); medium.
- Initial: ABRSM has none for woodwind; Trinity row only; low-medium.
- Piece ranges per grade: unknown (ABRSM publishes no piece ranges; piece scores not accessible). Breath/phrase lengths: inference only.
- Not reached: ABRSM website HTML (403); SR sample books; teacher-blog searches for grade-specific break/altissimo requirements returned nothing usable.

## Sources

- S1. ABRSM, Practical Music Grades Woodwind Syllabus from 2022, Qualification Specification (official PDF, downloaded and read). https://www.abrsm.org/sites/default/files/2023-10/Woodwind%202022%20Practical%20syllabus%20(0%20ALL)%2020230911.pdf . Taken: sight-reading (SR) parameter table pp.23-24; SR keys and ranges table p.24; scale rules and speed guide pp.16-17; clarinet scale/arpeggio tables per grade (Clarinet section pp.84-101); clarinet in B-flat or A allowed; "Initial Grade not available for woodwind"; Prep Test pp.160-161. Retrieved 2026-10-14.
- S2. ABRSM, Woodwind Practical Grades Qualification Specification from 2026 (official PDF). https://www.abrsm.org/sites/default/files/2025-06/ABRSM%20Woodwind%20Practical%20Grades%20Qualification%20Specification%20from%202026.pdf . Taken: scales, SR and aural "stay the same" as 2022; SR keys/ranges table checked identical; 2022 pieces valid to 31 Dec 2026. Retrieved 2026-10-14.
- S3. Trinity College London, Woodwind Syllabus (specs from 2022, online ed.), PDF. https://trinitycollege.com/resource/?id=7385 . Taken (secondary, other board): Initial clarinet technical work and SR (C major, range of a 5th), SR set about two grades below exam grade. Retrieved 2026-10-14.
- S4. Wikipedia, "Clarinet". https://en.wikipedia.org/wiki/Clarinet . Taken: written range E3-C7; chalumeau E3 to B-flat4, clarion B4 to C6, altissimo above C6. Retrieved 2026-10-14.
- S5. clarinet-now.com, "Clarinet range". https://www.clarinet-now.com/clarinet-range.html . Taken: throat tones = open G to B-flat (G4-B-flat4); clarion starts at B4. Retrieved 2026-10-14.
- S6. clarinet-now.com, "Crossing the break". https://www.clarinet-now.com/crossing-the-break.html . Taken: break crossing needs the left-thumb register key; typical faults (insufficient air support, thumb not over key, chin movement, squeaks). Retrieved 2026-10-14.
- S7. Bret Pimentel, "Avoiding clarinet undertones: published techniques". https://bretpimentel.com/avoiding-clarinet-undertones-published-techniques/ . Taken: undertones occur on tongued attacks in the upper clarion (about written G to C above the staff). Retrieved 2026-10-14.
- S8. Hong Kong LCSD Music Office, Clarinet syllabus 2025 (ABRSM-based local syllabus). https://www.lcsd.gov.hk/en/mo/common/doc/02-cl.pdf . Taken: its Grade E1 scales are "F, G majors; A minor (one octave, in the chalumeau register)", corroborating that ABRSM G1 stays below the break. Retrieved 2026-10-14.
- S9. Wikipedia, "Transposing instrument". https://en.wikipedia.org/wiki/Transposing_instrument . Taken: B-flat clarinet sounds a major 2nd lower. Retrieved 2026-10-14.
- Tags: [D] derived by me from S1 tables with a script (lowest tonic from written E3, stated span; excludes 7ths, whole-tone, thirds, extended-range); [I] my inference from sources plus general clarinet knowledge; no tag = stated in S1/S2.
