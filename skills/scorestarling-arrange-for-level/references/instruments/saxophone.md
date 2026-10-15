# Saxophone: difficulty by level (ABRSM)

**Read this when** the target instrument is saxophone, at any level. Numbers come from ABRSM Woodwind syllabus (2022, unchanged for 2026); the checker reads them from [../profiles/saxophone.json](../profiles/saxophone.json): `python3 scripts/check_level.py arrangement.musicxml --instrument saxophone --grade N`. S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

Which saxophone: ABRSM candidates enter on soprano, alto, tenor or baritone; the scale list, sight-reading (SR) test and ranges are COMMON to all four, and are in WRITTEN treble-clef pitch (only the piece lists differ: E-flat list for alto/baritone, B-flat list for soprano/tenor) (S1). All pitches and keys below are WRITTEN pitch (scientific pitch, C4 = middle C; ABRSM prints Helmholtz, c' = C4, a# = A#3 = B-flat3; converted by me). Sounding pitch: soprano sounds a major 2nd below written, alto a major 6th below (S6); tenor a major 9th below and baritone an octave plus a major 6th below (standard practice, not stated in S1 or S5). ABRSM names scales by fingering, not concert pitch (S1). Default arranging target: alto saxophone (E-flat). Concert-to-written: alto up a major 6th (concert B-flat = written G, concert E-flat = written C); tenor up a major 9th, soprano up a major 2nd (concert F = written G, concert B-flat = written C).

## Table by grade

SR = unseen sight-reading test (parameters cumulative; only new items listed). Range = official SR range, written pitch, all four saxophones.

| Grade | Keys (SR new maj / min; scales set) | Time sigs (SR) | Note values and rhythms (SR new) | Written range (SR; scale top [D]) | Register / fingering demands | Articulation / technique (scales) | Dynamics and other features (SR) | SR length / params |
|---|---|---|---|---|---|---|---|---|
| Initial (ABRSM: none) | ABRSM has no Initial for woodwind; Prep Test exists for saxophone (set exercises, one set piece, an accompanied own piece, 3 aural tests, no marks; books out of print) (S1). Trinity: no Initial for saxophone (S3). Level unknown | unknown | unknown | unknown | unknown | unknown | unknown | unknown |
| 1 | maj G, F; min none. Scales: F, G maj; D min, 1 oct | 4/4, 3/4 (4 bars); 2/4 (6 bars) | dotted minim, minim, crotchet, paired quavers; crotchet rests | F4-G5 (top G5 [D]) | [I] middle of the written range only, no palm keys, no low C4/B3 | tongued or simple 2-note slurs; scales tongued/slurred, crotchet = 50 (quaver pairs), arpeggios quaver = 72 | f, mf | 4 bars (4/4, 3/4) or 6 bars (2/4) |
| 2 | maj C; min d (natural only). Scales: C maj (from C5, 1 oct); D, F maj 12th; A min 1 oct; D min 12th | none new | four-quaver groups; dotted crotchet + quaver; tied notes; minim rests | E4-A5 (top C6 [D]) | [I] still below C6 | + staccato; crotchet = 56; arpeggios quaver = 84 | mp, cresc. hairpin | 8 bars |
| 3 | min a; accidentals only within minor keys. Scales: B-flat maj (from B-flat4, 1 oct); G maj 12th; C, D maj 2 oct; B min (from B4, 1 oct); G min 12th; D min 2 oct; chromatic from G 1 oct | 3/8 | dotted crotchets; simple semiquaver patterns; quaver rests | D4-C6 (top D6 [D]) | [I] C6 reached; palm keys start at D6 (S5) | + accents; crotchet = 63; arpeggios quaver = 96 | p, dim. hairpin | length cell blank in table (8 bars carried [I]) |
| 4 | maj D; min b. Scales: A maj 1 oct; E, G maj 12th; D, E-flat maj 2 oct; F# min 1 oct; E, F min 12th; C min 2 oct; chromatic from G 12th; dom 7th in F | 6/8 | chromatic notes; anacrusis; tenuto; pause sign | C4-C6 (top E-flat6 [D]) | [I] C4 enters; E-flat6 appears only in scales (palm D/E-flat keys, S5) | + tenuto; crotchet = 72; arpeggios quaver = 108; 7ths 54 | as G3 | c. 8 bars |
| 5 | maj A, B-flat, E-flat; min e, g. Scales: A-flat, A maj 12th; B-flat, E-flat, E maj 2 oct; F, F# min 12th; B, C#, E min 2 oct; chromatic A-flat (12th), D (2 oct); dom 7ths C, A-flat; dim 7th C# | none new | simple syncopation | C4-D6 (top E6 [D]) | D6 = first SR note needing the D palm key (S5, [D]) | crotchet = 84; arpeggios quaver = 126; 7ths 63 | ff, pp; slowing of tempo at end | c. 8-16 bars |
| 6 | maj E, A-flat; min f#, c. Scales: A-flat/G#, A maj and min 12th; B, D, F maj and min 2 oct; thirds G maj 1 oct; chromatic A-flat, A (12th), D (2 oct); dom 7ths D-flat, D (12th), G (2 oct); dim 7ths A-flat, A, D | 9/8, 5/8, 5/4; changes of time signature | triplet patterns; swung style; rit. then a tempo | C4-E-flat6 (top F6 [D]) | E-flat6 needs the E-flat palm key [I] | crotchet = 96; arpeggios dotted crotchet = 48; 7ths 72; thirds 88 | as G5 | c. 12-16 bars |
| 7 | min c#, f (no new maj). Scales: F#, G maj and min 12th; C, E-flat, E maj and min 2 oct; extended-range E-flat maj; thirds D maj 2 oct | 7/8, 7/4 | (none new listed) | B3-F6 (top E6 [D]) | Low B3 and F6 (highest keyed note, S4; F palm key, S5) enter | new names: legato-tongued / staccato / slurred; crotchet = 112; dotted crotchet = 54; 7ths 80; thirds 100 | as G6 | c. 16-20 bars |
| 8 | maj B, D-flat. Scales: B, D-flat/C#, E, F maj and min 2 oct; B-flat maj and min 2.5 oct; extended-range A-flat maj, A harmonic min; thirds C, E-flat; whole-tone D, E-flat | 12/8 | triplet crotchets; acceleration; simple ornaments | B-flat3-F6 (B-flat major 2.5 oct B-flat3-F6 [D]) | Whole written compass (low B-flat key to F6); no altissimo in the SR range | crotchet = 132; dotted crotchet = 63; 7ths 96; thirds 120 | as G7 | c. 16-24 bars |

The extended-range scale/arpeggio patterns (G7 E-flat maj; G8 A-flat maj, A harmonic min and arpeggios) are set outside the normal span; their top notes are not transcribed here (unknown; see S1 p.22 graphic).

## What changes between neighbouring grades

- 1 to 2: low note drops F4 to E4, top G5 to A5; C major, ties, staccato, mp, cresc.; 8 bars.
- 2 to 3: low D4, top C6; 3/8, semiquavers, accents, p/dim.; a minor.
- 3 to 4: low C4; 6/8, chromatic notes, anacrusis, tenuto, pause; D major, b minor.
- 4 to 5: top D6 (first palm-key note); syncopation, ff/pp, rit.; A, B-flat, E-flat major; up to 16 bars.
- 5 to 6: top E-flat6; metre changes and 9/8, 5/8, 5/4, triplets, swing; E and A-flat major.
- 6 to 7: low B3, top F6; 7/8, 7/4; c# and f minors; extended-range scale.
- 7 to 8: low B-flat3; 12/8, triplet crotchets, acceleration, ornaments; B and D-flat major; 2.5-octave scales.

## Arranging implications

- Write in written pitch for the sax chosen; pick the written key from the grade list. For G1 (G or F written): alto = concert B-flat or A-flat major; tenor/soprano = concert F or E-flat major.
- Range ceilings (written): G1 F4-G5, G2 E4-A5, G3 D4-C6, G4 C4-C6, G5 C4-D6, G6 C4-E-flat6, G7 B3-F6, G8 B-flat3-F6. Prepared pieces may stray a little beyond [I]; Trinity sets SR about two grades below the exam grade (S3).
- To go down a grade: transpose the tune down or invert leaps to meet the lower ceiling; remove palm-key notes (D6, E-flat6, F6) below G5, G6, G7 respectively (S5); keep to F4-G5 for G1; avoid low C4-D4 below G4/G3 and B3/B-flat3 below G7/G8.
- Never use altissimo (above F6; S4) for any grade up to G8 SR level.
- Keys: G1 G/F only; G2 + C and d; G3 + a; G4 + D, b; G5 + A, B-flat, E-flat, e, g; G6 + E, A-flat, f#, c; G7 + c#, f; G8 + B, D-flat.
- Rhythm: minims/crotchets/quaver pairs at G1; four-quaver groups and dotted crotchet-quaver from G2; semiquavers, 3/8 from G3; 6/8 and chromatic notes from G4; syncopation from G5; triplets, swing (named for sax in S1), 5/8 5/4 9/8 from G6; 7/8 7/4 from G7.
- Articulation: G1-G2 tongued with two-note slurs only; staccato G2, accents G3, tenuto G4; slurs longer than two notes are not specified for woodwind in S1 (unknown; keep to about a bar at G1-G3 [I]).
- Breath and phrase length [I, no source]: 2-bar phrases at G1-G2, up to 4 bars at G3-G4, 4-8 bars from G5; leave fast scale-like runs (crotchet = 96-132 benchmarks in S1) for G6+.
- Tessitura differs between sizes (baritone low notes, soprano top notes) but ABRSM publishes one common written range; do not treat it as size-specific.

## Confidence and gaps

- Keys, time signatures, rhythms, articulation, dynamics, SR length and range, scale spans and speeds: verbatim from official ABRSM (S1, S2); high. Note-value glyphs read from the rendered table; moderately high.
- Scale tops [D]: my calculation; excludes 7ths and extended-range; medium-high.
- Register/fingering demands (palm keys, low keys): official ranges plus S4/S5; palm-key mapping to grades is derived; medium.
- Sounding transpositions of tenor/baritone: standard practice, not in the sources fetched; medium-high.
- Initial: none from ABRSM or Trinity for sax; unknown.
- Piece ranges per grade: unknown (not published; scores not accessible). Breath/phrase lengths: inference only.
- Not reached: ABRSM website HTML (403); SR sample books; teacher-forum searches gave no grade-specific altissimo or palm-key requirements.

## Sources

- S1. ABRSM, Practical Music Grades Woodwind Syllabus from 2022, Qualification Specification (official PDF, downloaded and read). https://www.abrsm.org/sites/default/files/2023-10/Woodwind%202022%20Practical%20syllabus%20(0%20ALL)%2020230911.pdf . Taken: SR parameters pp.23-24; SR keys and ranges (saxophone column) p.24; scale rules and speeds pp.16-17; saxophone scale/arpeggio tables per grade (Saxophone section pp.116-142); instrument rules (four saxophones, related-instrument option, E-flat and B-flat lists) p.13; "Initial Grade not available for woodwind"; Prep Test also offered for saxophone, books out of print, pp.160-161. Retrieved 2026-10-14.
- S2. ABRSM, Woodwind Practical Grades Qualification Specification from 2026 (official PDF). https://www.abrsm.org/sites/default/files/2025-06/ABRSM%20Woodwind%20Practical%20Grades%20Qualification%20Specification%20from%202026.pdf . Taken: scales, SR and aural "stay the same" as 2022; SR keys/ranges table checked identical; 2022 pieces valid to 31 Dec 2026. Retrieved 2026-10-14.
- S3. Trinity College London, Woodwind Syllabus (specs from 2022, online ed.), PDF. https://trinitycollege.com/resource/?id=7385 . Taken (secondary, other board): saxophone is offered from Grade 1 only (no Initial); SR set about two grades below the exam grade. (Its SR key list for sax differs from ABRSM's and is not used here.) Retrieved 2026-10-14.
- S4. Wikipedia, "Saxophone". https://en.wikipedia.org/wiki/Saxophone . Taken: common written range from low B-flat3 to high F6 (F#6 key on many instruments, altissimo above); same fingering across sizes; B-flat soprano/tenor, E-flat alto/baritone. Retrieved 2026-10-14.
- S5. Woodwind Fingering Guide, saxophone fingerings. https://www.wfg.woodwind.org/sax/sax_fing.html . Taken: palm keys D, E-flat, F play third-octave D to F (and F#); front F key is an altissimo alternative for F6; high F# key; side keys. Retrieved 2026-10-14.
- S6. Wikipedia, "Transposing instrument". https://en.wikipedia.org/wiki/Transposing_instrument . Taken: soprano (B-flat) sounds a major 2nd below, alto (E-flat) a major 6th below written. Retrieved 2026-10-14.
- Tags: [D] derived by me from S1 tables with a script (lowest tonic from written B-flat3, stated span; excludes 7ths, whole-tone, thirds, extended-range); [I] my inference from sources plus general saxophone knowledge; no tag = stated in S1/S2.
