# Viola: difficulty by level (ABRSM Bowed Strings Practical Grades, syllabus from 2024)

**Read this when** the target instrument is viola, at any level. Numbers come from ABRSM Bowed Strings syllabus from 2024; the checker reads them from [../profiles/viola.json](../profiles/viola.json): `python3 scripts/check_level.py arrangement.musicxml --instrument viola --grade N`. S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

Conventions: viola is non-transposing (written = sounding). Alto clef is the default clef (C4 on the middle line); ABRSM first puts treble clef into the sight-reading test at Grade 6 (S1). Pitches are scientific pitch, C4 = middle C. ABRSM prints ranges in Helmholtz notation (c = C3, c' = C4); I converted them [D]. "SR" = the unseen sight-reading test; its parameters are cumulative. Tags: [D] derived by me from official numbers; [I] my inference from official data plus general viola knowledge; untagged = stated by ABRSM.

## Table by grade

Columns: keys = SR new keys (cumulative) then scale/arpeggio keys; range = SR range; speeds = ABRSM scale guide (crotchet = N) and arpeggio guide.

| Grade | Keys (major / minor) | Time sigs (SR) | Note values and rhythms (SR) | Written range (SR) | Technique demands (positions, scales) | Articulation / bowing | Dynamics and other | SR length |
|---|---|---|---|---|---|---|---|---|
| Initial | SR: G, D maj. Scales: G, D maj 1 oct from open strings; A min a 5th from bottom A | 4/4 (4 bars); 2/4 (6 bars) | crotchet, paired quavers, crotchet rest | G3-C4 or D4-G4 (two alternative ranges as printed) | 1st position only; scales q=42 even notes or long tonic | all notes separately bowed | mf | 4 or 6 bars |
| 1 | SR: none new (G, D). Scales: G, D, A nat min 1 oct; C maj 2 oct; arpeggios same (C 2 oct) | adds 3/4 (4 bars) | adds minim, four-quaver groups | G3-D5 | 1st position; 2-oct C major still fits 1st position [I]; q=48, arpeggio e=96 | scales separate or 2 quavers/bow; arpeggios separate bows | adds f, p | 4 bars |
| 2 | SR: C maj, A min (natural form only). Scales: F, Bb maj; C, G min (open-string starts) 1 oct; C, D, Eb maj 2 oct | none new | adds dotted minim, minim rest | C3-D5 | still 1st position; q=54, e=108 | simple two-note slurs | adds mp, cresc./dim. hairpins | 8 bars |
| 3 | SR: F, Bb, Eb maj; d, g, c min (any minor form); accidentals only inside minor keys. Scales: Db, Ab, A maj 1 oct; Eb, G maj and D, G min 2 oct; chromatic from open G 1 oct | none new | dotted crotchet+quaver, dotted quaver+semiquaver, simple semiquaver patterns, quaver rest, ties | C3-E5 (top of 1st position with 4th finger [I]) | 1st position; arpeggios 3 notes/bow possible; q=58, e=112 | staccato; pizzicato (at end) | none new | 8 bars |
| 4 | SR: A maj (no new minor). Scales: Db, E, F, A maj; C, E, F min 2 oct; dominant 7ths F (from open C) and G (from bottom D) 1 oct; chromatic from D and A 1 oct | 6/8 | chromatic notes, anacrusis | C3-G5 (needs 3rd position [I]) | first shifts: 1st and 3rd positions only; q=63, e=116 | hooked bowing, tenuto, accents, pause sign | adds pp, ff | c. 8 bars |
| 5 | SR: E, Ab maj; e, f# min. Scales: F, A, Bb maj and D, E, F#, A min 2 oct; C maj and C min 3 oct; 7ths Eb, F, G; dim 7ths from open C and G; chromatic C, D, Eb 2 oct | none new | simple syncopation | C3-A5 | shifts as required to cover the range; q=72, arpeggio dotted crotchet=40 | arco/pizzicato changes; simple chords (at end) | slowing of tempo at end | c. 8-16 bars |
| 6 | SR: f min (no new major). Scales: Db/C#, F#, Ab/G# maj and min 2 oct; C, D maj and min 3 oct; dim 7ths; chromatic 2 oct; first double stops (broken sixths, Eb maj 1 oct) | 9/8, 5/8, 5/4; changes of time signature | triplet patterns | C3-A5 | q=84; double-stop q=84 | slurs up to 7 notes/bow in scales | rit. then a tempo; treble clef appears | c. 12-16 bars |
| 7 | SR: b, c# min. Scales: F, G, Bb maj/min 2 oct; D, Eb maj/min 3 oct; broken sixths C and Eb; broken octaves G | 7/8, 7/4 | none new | C3-B5 | q=96; double-stop q=96 | left-hand pizzicato | none new | c. 16-20 bars |
| 8 | SR: B, Db maj. Scales: A, B maj/min 2 oct; Db/C#, Eb, E maj/min 3 oct; parallel octaves G maj and C min 1 oct; parallel sixths Ab maj 2 oct; broken thirds Eb maj 2 oct | 12/8 | none new listed | C3-C6 | q=112; parallel double stops q=66 | simple ornaments | acceleration of tempo | c. 16-24 bars |

## What changes between neighbouring grades

- Initial to 1: minims, four-quaver groups, 3/4, f and p; still 1st position and separate bows; scales gain a natural minor (A) and a 2-octave C major.
- 1 to 2: first slurs (two notes), dotted minim, mp and hairpins; sight-reading doubles to 8 bars; C and G minor scales and Bb/F majors join.
- 2 to 3: dotted figures, semiquavers, ties, staccato, pizzicato; Bb and Eb major; range tops out at E5 (all of 1st position).
- 3 to 4: biggest jump: 6/8, chromatics, anacrusis, hooked bows and the first shift (1st to 3rd); range to G5; pp and ff.
- 4 to 5: shifts anywhere, syncopation, arco/pizz changes, a closing chord, 3-octave C scales; range to A5.
- 5 to 6: triplets, odd metres (9/8, 5/8, 5/4), metre changes, treble clef, first double-stop scales; range unchanged (A5).
- 6 to 7: 7/8 and 7/4, left-hand pizzicato, B5; more double stops. 7 to 8: 12/8, ornaments, acceleration, top C6, parallel octaves and sixths.

## Arranging implications

- Treat the SR range as the ceiling for a "level N" tune: G1 G3-D5, G2 C3-D5, G3 C3-E5, G4 C3-G5, G5-G6 C3-A5, G7 C3-B5, G8 C3-C6. Repertoire may stray slightly beyond (unknown, see gaps), so stay inside for a safe arrangement.
- Stay in 1st position (no shifts written) to reach Grade 3 level; allow one shift between 1st and 3rd position at Grade 4; free shifting only from Grade 5 [I from S1 SR rule].
- Initial-1: keys G, D, C; crotchets, minims, quaver pairs; separate bows; mf (add f/p at G1); 4-6 bar phrases. Add two-note slurs and mp/hairpins at G2; add dotted rhythms, semiquaver runs, ties, staccato at G3; chromatic notes, anacrusis, hooked bows at G4.
- To go down a level: remove slurs longer than two notes, then all slurs; replace dotted and semiquaver figures by quavers; drop accidentals; transpose into G, D or C major; cut range to the grade ceiling; delete chords, double stops, pizzicato and treble-clef passages (none before G5/G6).
- Key ladder by grade for the tune's key: G, D (Initial/G1); C, a (G2); F, Bb, Eb, d, g, c (G3); A (G4); E, Ab, e, f# (G5); f (G6); b, c# (G7); B, Db (G8). Keys beyond the grade's list are not forbidden but are above SR level.
- Alto clef for the whole part up to Grade 5; use treble clef only for notes above about A5 at G6+ [I; ABRSM only says treble clef enters SR at G6].
- Dynamics: do not mark below mf at Initial; no pp/ff before G4. Tempo: use the scale-speed guide as the comfortable ceiling for even quavers (q=42 at Initial up to q=112 at G8).
- Strings have no breath limit; phrase length is bow length: keep separate-bow or two-quavers-per-bow patterns at G1-G2; long slurs (6-7 notes) only G6+ (scale slurs 7 notes/bow at G6-G8).

## Confidence and gaps

- Verbatim from official ABRSM (S1, cross-checked S2): SR length, time signatures, rhythms, dynamics, articulations, positions, clef, keys, Helmholtz ranges, scale boxes, speed guide. High confidence.
- Derived [D]: scientific-pitch conversion of ranges (Helmholtz c = C3, c' = C4, c'' = C5). Inferred [I]: which position each range implies; "2-oct C major fits 1st position"; treble-clef rule of thumb.
- Unknown: ranges, positions and clefs actually printed in the set pieces (not published in the syllabus; repertoire lists deliberately not copied); Initial grade sample pieces; a second board's viola profile (Trinity strings spec not retrievable). Time signatures list only those newly introduced; 2/4, 3/4, 4/4 stay in use.
- Table cells "none new" mean the cumulative SR list adds nothing at that grade.

## Sources

- S1 (official, primary). ABRSM, "Practical Music Grades: Bowed Strings Syllabus from 2024", all-instruments qualification specification, 126 pp, dated 6 Jun 2023, valid from 1 Jan 2024 until further notice. https://www.abrsm.org/sites/default/files/2023-09/bowed-strings-2024-practical-syllabus-20230606.pdf . Taken: SR parameter table (length, time signatures, note values, dynamics, bowing, positions, clefs); SR KEYS and RANGES tables (viola column); the viola scale/arpeggio/7th/chromatic/double-stop box for every grade; viola scale speed guide; rules (even notes or long tonic, memory, lowest possible tonic, vibrato remark). Page images rendered and read to check glyphs. States that scales, SR and aural requirements "stay the same as the preceding syllabus".
- S2 (official text, mirror). ABRSM "Viola syllabus from 2024" (viola-only extract, 20 pp) as hosted by Caswell's Strings. https://caswells-strings.co.uk/wp-content/uploads/2025/07/ABRSM-Viola-syllabus-from-2024.pdf . Used only as a cross-check: all 161 lines of the viola scale boxes are text-identical to S1.
- S3. Wikipedia, "Viola". https://en.wikipedia.org/wiki/Viola . Taken: open strings C3 G3 D4 A4; music "primarily uses the alto clef", treble clef for higher passages; players use half position and most commonly third position.
- Tried and not usable: abrsm.org HTML pages return 403; us.abrsm.org returns 502 via proxy; guessed viola-only PDF paths on abrsm.org return 404; Trinity strings syllabus resource ids 8741/8742 return empty files; Hong Kong LCSD viola syllabus (https://www2.lcsd.gov.hk/en/mo/common/doc/faq/faq_syb_0402.pdf) is a local scheme that lists scales only, no positions or clefs, so nothing taken. No second graded board for viola was needed for the table.
