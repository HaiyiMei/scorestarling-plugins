# Ukulele: difficulty by level (RSL/Rockschool Ukulele 2020 primary; LCM Ukulele 2023 secondary)

**Read this when** the target instrument is ukulele, at any level. Numbers come from RSL (Rockschool) Ukulele syllabus 2020, with the LCM Ukulele syllabus 2023 as a cross-check; the checker reads them from [../profiles/ukulele.json](../profiles/ukulele.json): `python3 scripts/check_level.py arrangement.musicxml --instrument ukulele --grade N`. S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

Conventions: ABRSM is not used (it has no ukulele grades; we checked only its strings, brass and woodwind syllabuses). Graded ladder used: RSL (Rockschool) Debut + Grades 1-8; LCM (University of West London) Step 1, Step 2 + Grades 1-8 as cross-check. Debut and Step 1/2 are my "Initial" equivalent [I]. Tuning assumed everywhere: standard re-entrant GCEA (G4 C4 E4 A4, string 4 = G, string 1 = A; "C" = open string 3). RSL says its syllabus "embraces the instrument's re-entrant tuning" (S1) and LCM says soprano, concert and tenor ukuleles in standard GCEA (S2). RSL notation is stave (treble clef) plus TAB (S1) but it does not state the written octave; I assume treble clef at sounding pitch [I]. Pitches are scientific pitch (C4 = middle C). Tags: [D] derived by me, [I] my inference, [LCM] from S2, untagged = RSL. "SR" = RSL sight-reading test (Debut-Grade 5 only; Grades 6-8 use a Quick Study Piece lead sheet, 3 minutes preparation, instead).

## Table by grade

Columns: keys = SR key then technical-work keys; speeds = RSL technical tempo (crotchet; Grades 4-8 in eighth notes); [LCM] = chords and time signatures from S2.

| Grade | Keys (major / minor) | Time sigs | Note values and rhythms (SR) | Range (SR, written = sounding) [D] | Technique demands (RSL tech work, [LCM] chords) | Articulation | Dynamics / other | SR length and parameters |
|---|---|---|---|---|---|---|---|---|
| Debut / Step 1-2 | SR C maj. Scales C maj, G maj, C maj pent., A min pent.; arps C, Am | [LCM] 4/4 (Step 1), +3/4 (Step 2); RSL not stated | whole, half, quarter notes | C4-E4 (C, D on string 3, E on string 2; open/first position) | open chords C F G D Am Dm (RSL); [LCM] Step 1: C F G Am; Step 2 adds Dm C7 G7; q=65 | none stated | none stated | 4 bars, q=65; or 4-bar single-note improvisation |
| 1 | SR G maj or A min. Scales C, G, F maj, A nat. min, C maj on strings 3+4; arps G, F, Dm | [LCM] 4/4, 3/4 | half and quarter notes | about C4-C5 (E-G on string 2; A-B-C on string 1; plus Debut notes) | new chords A, E, Em, Bm, G7, D7 (D, Dm repeat); [LCM] C F G A D, Am Dm Gm, C7 G7 A7 E7; q=70 | none stated | none stated | 4 bars, q=70 |
| 2 | SR D maj or Bb maj. Scales D, Bb maj, C min pent., C blues, C maj on strings 3+4; arps D, Bm, Bb, Gm | [LCM] 4/4, 3/4 | quarter notes and rests, eighth notes | about C4-C#5 (open to fret 4, strings 1-3, diatonic notes) | Bb and Gm (two fingerings each), Gmaj7, G7, Gm7, a sus-chord exercise; [LCM] adds Bb Em F#m D7 Cmaj7 Gm7; q=80 | none stated | none stated | 4 bars, q=80 |
| 3 | SR Eb maj or E min. Scales from D, Eb, E (maj, nat. min, maj/min pent.), C maj pent. campanella; arps D, Eb, E maj/min/dim | [LCM] adds 6/8 | quarter and eighth notes and rests | not stated | barre chords I IV IIm V7 VIm in D, Eb or E; diminished triads; swung muted strum in B min; [LCM] adds Bm Fm B7 Dmaj7 Gmaj7 Em7 Edim7; q=90 | campanella (scale) | swung strumming | 4 bars, q=80 |
| 4 | SR E maj or F min. Scales from Eb, E, F (maj, nat. and harm. min.), pent. across two positions, blues, one-string scales; arps incl. dom7 and min7 | [LCM] 4/4, 3/4, 6/8 | adds ties | not stated | harmonised scale in barre chords; muted chords with swung 16th strum or triple strokes; [LCM] full/partial barre, higher-position chords; q=80 (eighths) | triple strokes, muting | swung 16ths | 8 bars, q=80-90 |
| 5 | SR Ab maj or B maj. Major scale in three positions (Ab or B), harm. min. on one string, campanella C and G maj; arps Imaj7, V7, VIm7 | as G4 | adds dotted eighths and 16ths | not stated | harmonised scale (Ab or B); dom7 partial chords with 16th strum or dom7 with triple strokes; q=90 (eighths) | campanella | 16th strumming | 8 bars, q=80 |
| 6 | No SR: Quick Study Piece. Dorian, mixolydian, mel. min., chromatic scales; thirds on strings 1 and 4; campanella D nat./harm. min. | [LCM] 4/4, 3/4, 6/8 | not stated | not stated | m7b5, dim7, aug chords in two positions; Stylistic Studies group; q=100 (eighths); [LCM] G6-8 pieces use the whole range, campanella, harp harmonics, slides, slurs | campanella, slurs, slides [LCM] | stylistic | lead sheet, 3 min prep |
| 7 | Lydian, phrygian, phrygian dominant; sixths in Bb | as G6 | not stated | not stated | maj9/min9 arps; dom9, min9, maj9 chords; q=100 | as G6 | | as G6 |
| 8 | Whole-tone, diminished, altered scales | as G6 | not stated | not stated | dom7#5, b5, b9 arps; altered chords (#5, b5, #9, b9); q=100 | as G6 | | as G6 |

## What changes between neighbouring grades

- Debut to 1: key to G major / A minor, SR range grows from three notes (C4-E4) to about an octave (C4-C5); half notes only added; new chords A, E, Em, Bm and 7ths G7, D7; scale tempo q=65 to 70.
- 1 to 2: eighth notes enter SR; keys D and Bb; range to about C#5; first extended chords (maj7, m7, sus); q=80.
- 2 to 3: barre chords, diminished triads, keys Eb and E; campanella and swung strumming appear; [LCM] 6/8; q=90.
- 3 to 4: SR doubles to 8 bars, ties added; harmonic minor, blues, muted and 16th-note swung strumming; scales switch to eighth notes.
- 4 to 5: dotted eighths and 16ths in SR; scales in three positions; maj7, V7, m7 arpeggios in remote keys (Ab, B, C# minor 7).
- 5 to 6: SR replaced by a Quick Study (lead sheet); modes, melodic minor, chromatic scale, thirds; m7b5, dim7, aug chords; q=100. 6 to 8: more modes, 9th chords, then altered scales and altered chords.

## Arranging implications

- Tuning: write for re-entrant GCEA; do not put notes below C4 (the lowest sounding string) unless the player has a low-G tenor [S4]. A melody stays in C4-A5 on a soprano (S4); ceiling by grade of SR: Debut C4-E4, G1 C4-C5, G2 C4-C#5, higher unknown.
- Clef: state the clef and octave on the part; stave plus TAB is normal (S1). I assume treble clef at sounding pitch [I]. Because string 4 (G4) lies above string 3 (C4), the lowest note is C4; RSL's "C major on strings 3 and 4" (G1 and G2 technical work) is a one-octave C4-C5 line [D].
- Key ladder (SR): Debut C; G1 G, a; G2 D, Bb; G3 Eb, e; G4 E, f; G5 Ab, B. For levels up to 2 transpose into C, G, F, D or Bb (technical-work keys: C, G, F first). Prefer keys in which chords use open shapes.
- Chord ladder (RSL Debut): C F G D Am Dm; add A, E, Em, Bm, G7, D7 (G1); Bb, Gm, maj7/m7 (G2); barre forms (G3). [LCM] Step 1 is only C F G Am; add Dm C7 G7 at Step 2; Bm Fm B7 Edim7 and maj7 chords by G3.
- Rhythm ladder (RSL SR): whole/half/quarter (Debut); half/quarter (G1); eighths (G2); eighth rests (G3); ties (G4); dotted eighths and 16ths (G5). Time signatures: 4/4 only at the start, 3/4 from Step 2 [LCM], 6/8 from LCM Grade 3.
- Tempo: RSL technical tempo is the comfort ceiling for even eighths: q=65 (Debut) rising to 100 (G6-8); SR tempi are q=65-90.
- Texture: levels up to 3 are strummed chords or single-note melody (SR is single-note; improvisation is single notes). Campanella (over-ringing re-entrant notes), harp harmonics, slides and slurs belong to G3-5 technical work and G6-8 pieces [LCM, S1]; muted strumming and swung 16ths from G3-G4.
- To go down a level: cut the key to C, G, F; keep to chords C F G Am (Dm, C7, G7 at Step 2); remove barre chords, 7th extensions and diminished chords; replace eighth notes and ties by quarter notes; keep melody within a fifth to an octave from C4; avoid campanella and muting.
- Breath: not applicable.

## Confidence and gaps

- Verbatim official RSL (S1): SR lengths, rhythms, keys, tempi, compass (Debut-G2), technical lists. High for RSL. Verbatim LCM (S2): chord and time-signature tables, grade descriptors. High for LCM.
- Derived [D]: scientific-pitch ranges for Debut-G2 from the stated strings and frets. Medium. Inferred [I]: treble clef at sounding pitch; Debut/Step 1-2 as the "Initial" equivalent. S3 contradicts RSL on key order; boards are not aligned (LCM Step 1 is easier than RSL Debut), so "grade N" differs by board. Overall: medium.
- Unknown: written octave convention; compass for Grades 3-8 (RSL does not state it); tempo note value for Debut-G3 technical work; time signatures in RSL; LCM piece-level keys, ranges and tempi (set pieces not documented); fret or position numbers by grade; Trinity or ABRSM ukulele (none found); exact meaning of the RSL "root omitted" remark on a G1 chord.

## Sources

- S1 (official, primary). RSL Awards, "Rockschool Contemporary Ukulele Syllabus Guide 2020" (mirror hosted by newschool.ie, rev. May 2020; the guide's revision history runs to Apr 2020). https://www.newschool.ie/wp-content/uploads/2020/05/RSL_Ukulele_Syllabus_Guide_2020_05May2020.pdf . Taken: SR parameters per grade (duration, rhythms, key, compass, tempo, 90 s practice with backing track); technical-work lists (scales, arpeggios, chords, tempo, groups) per grade; re-entrant tuning and campanella notes; stave plus TAB; exam timings (15 min Debut to 32 min Grades 6-8).
- S2 (official, other board). London College of Music Examinations, "Ukulele Syllabus 2023" (Steps, Grades 1-8, revised 1 Jan 2025). https://lcme.uwl.ac.uk/media/qzyhfoue/ukulele-syllabus-2023.pdf . Taken: tuning/instrument statement; grade descriptors (Grades 1-2, 3-5, 6-8); chord vocabulary and time signatures for each Step and Grade; component list (rhythm study, performance melody/chords, free choice, prepared accompaniment, musicianship).
- S3 (weak, awarding body not stated in the text). TLM, "Ukulele Musical Performance Graded Exams Specification Guide, Grades 1-8". https://tlm.org.uk/wp-content/uploads/2025/03/Ukulele-Graded-Music-Exams.pdf . Taken only: scale key ladder by grade (G1 F, G major; G2 A, E major and harmonic minors; G3 Ab, Eb, G/F harmonic minor; G4 F# major) and "SR is about two grades below". It differs strongly from RSL, so I do not use it for the table.
- S4. Wikipedia, "Ukulele". https://en.wikipedia.org/wiki/Ukulele . Taken: GCEA tuning (G4 C4 E4 A4), soprano range about C4-A5 (12-15 frets), concert about C4-C6 (15-18 frets), tenor about G3-D6 (17-19 frets; low-G variants exist).
- Tried and not usable: abrsm.org HTML (403); no Trinity ukulele syllabus; RSL's FCP guidance PDF (rockschool.ameb.edu.au) found but not needed; no source gave a melodic compass beyond RSL Grade 2.
