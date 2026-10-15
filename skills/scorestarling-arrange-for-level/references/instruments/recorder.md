# Recorder (descant and treble): difficulty by level (ABRSM Woodwind from 2022/2026; Trinity Woodwind for Initial)

**Read this when** the target instrument is recorder (descant or treble), at any level. Numbers come from ABRSM Woodwind syllabus (2022, unchanged for 2026); the checker reads them from [../profiles/descant-recorder.json](../profiles/descant-recorder.json): `python3 scripts/check_level.py arrangement.musicxml --instrument descant-recorder --grade N` (or `--instrument treble-recorder`, whose profile is [../profiles/treble-recorder.json](../profiles/treble-recorder.json)). S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

Conventions: ABRSM does examine the recorder: its Woodwind syllabus (2022, unchanged in 2026) has a Descant (soprano) syllabus for Grades 1-5 only and a Treble (alto) syllabus for Grades 1-8. ABRSM has no Initial for woodwind; Trinity has Initial-Grade 8 for recorder. NOTATION: parts for sopranino, descant and bass are conventionally written an octave BELOW sounding pitch, treble (alto) and tenor at pitch (S4). So descant ranges below are the ABRSM printed (written) ones, and sounding = written + 1 octave [D]; treble written = sounding. We assume ABRSM prints written pitch, since its descant bottom note c' (C4) matches a written-octave-low C5 instrument [I]. Baroque fingering assumed (German not allowed by Trinity). Scientific pitch (C4 = middle C); ABRSM prints Helmholtz (c' = C4, c'' = C5, c''' = C6), converted by me. "SR" = sight-reading, parameters cumulative. Tags: [D] derived by me, [I] my inference, untagged = stated by source. "oct+dom" = scale of an octave and down to the dominant.

## Table by grade

Columns: D = descant, T = treble. Keys = SR new keys (major / minor). Range = ABRSM SR range as written; descant sounds an octave higher [D]. Speeds (ABRSM, all woodwind): scale crotchet 50, 56, 63, 72, 84, 96, 112, 132 (G1-8); arpeggio quaver 72, 84, 96, 108, 126 (G1-5), dotted crotchet 48, 54, 63 (G6-8).

| Grade | Keys | Time sigs | Note values and rhythms (SR) | Written range (SR) | Technique demands | Articulation | Dynamics and other | SR length |
|---|---|---|---|---|---|---|---|---|
| Initial (Trinity) | D: G maj | 2/4 | crotchet, minim | a 5th (notes unknown) | technical: first five notes of G or D major plus a triad, from memory, descant only; scale about 60 and triad q=120 (note value of 60 garbled in text) | tongued | mf, moderato | unknown |
| 1 | D: C, F / -. T: F, Bb / - | 4/4, 3/4 (2/4 for 6 bars) | dotted minim, minim, crotchet, paired quavers, crotchet rest | D: D4-D5 [sounds D5-D6]. T: G4-G5 | scales one octave: D: C, F maj, D min (tops F5). T: F, Bb maj, G min (top Bb5 [D]); q=50, e=72 | tongued or two-note slurs | mf only | 4 bars (6 in 2/4) |
| 2 | D: D / d. T: C / g (natural minors only) | none new | four-quaver groups, dotted crotchet+quaver, ties, minim rest | D: C4-F5. T: F4-Bb5 | first oct+dom and 12th scales (D: F oct+dom, C maj 12th; T: Bb oct+dom, F maj 12th); scale top D: A5, T: D6 [D]; q=56, e=84 | adds staccato | mf only | 8 bars |
| 3 | D: a. T: d (any minor form) | 3/8 | dotted-quaver figures, simple semiquaver patterns, quaver rest | D: C4-A5. T: F4-D6 | first chromatic scale (D: G; T: C, 1 oct); accidentals only in minor keys; top D: B5, T: E6 [D]; q=63, e=96 | adds accents | adds p | 8 bars |
| 4 | D: G / e. T: G / a | 6/8 | chromatic notes, anacrusis | D: C4-B5. T: F4-E6 | first dominant 7th (D: C; T: F, 1 oct); chromatic to a 12th; q=72, e=108, 7ths 54 | adds tenuto, pause | adds f, mp | c. 8 bars |
| 5 | D: A, Bb / b, g. T: D, Eb / e, b | none new | simple syncopation | D: C4-B5. T: F4-E6 | first 2-octave scale (D: C maj to C6; T: F maj to F6 [D]); diminished 7th; q=84, e=126, 7ths 63 | none new | cresc./dim. hairpins; slowing at end | c. 8-16 bars |
| 6 | T: A / f#, c (no descant) | 9/8, 5/8, 5/4; metre changes | triplet patterns | T: F4-F6 | oct+dom scales in B, C#/Db; 12ths in G, A, C; first thirds (F maj 1 oct); scale top G6 [D]; q=96, dotted crotchet=48, 7ths 72, thirds 88 | scales: tongued / slurred; Trinity adds acciaccaturas, turns, trills | slowing then a tempo | c. 12-16 bars |
| 7 | T: E, Ab / - | 7/8, 7/4 | none new | T: F4-G6 (excl. F#6) | extended-range Bb maj; thirds C maj; scale top Eb6 [D]; q=112, dotted crotchet=54, 7ths 80, thirds 100 | scales: legato-tongued / staccato / slurred | none new | c. 16-20 bars |
| 8 | T: - / c#, f | 12/8 | triplet crotchets | T: F4-G6 (excl. F#6) | F, Ab 2-octave scales (Ab4-Ab6, above the SR ceiling [D]); whole-tone Db, G; extended-range Eb maj and D harm. min; q=132, dotted crotchet=63, 7ths 96, thirds 120 | as G7 | ff, pp; acceleration; simple ornaments | c. 16-24 bars |

Trinity SR keys for cross-check (set about two grades below exam grade, S3): descant G Initial, G2 e, G3 D/d, G4 C, F, G5 Bb/a, G6 A/f#, G7 E, Eb/c#, G8 F#/eb; treble G1 C, G2 a, G3 G/g, G4 F, Bb, G5 Eb/d, G6 D/b, G7 A, Ab/f#, G8 B/ab. Trinity SR time signatures: 2/4 Initial, 4/4 G1, 3/4 G2, 6/8 G5, 3/8 G6, 9/8 G7, 2/2 and changing metre G8. Trinity SR span: Initial a 5th, G1-2 an octave, G3-4 a 12th, G5-6 two octaves, G7-8 full range. Trinity SR articulation: tongued (Initial), slurs (G2), accidentals (G3), staccato, accents, tenuto (G4), acciaccaturas, turns, trills (G6).

## What changes between neighbouring grades

- 1 to 2: descant bottom drops from D4 to C4 (top F5); treble top Bb5 (bottom F4); four-quaver groups, ties, staccato; first minor key (natural); first 12th scales.
- 2 to 3: top A5 (descant) / D6 (treble); 3/8, dotted and semiquaver figures, accents, p; any minor form; first chromatic scale.
- 3 to 4: top B5 / E6; 6/8, anacrusis, chromatic notes, tenuto, pause, f and mp; first dominant 7th. Descant range stops growing here (B5 at G4 and G5).
- 4 to 5: syncopation, hairpins, slowing at end; A and Bb major, D and Eb major; first 2-octave scale; diminished 7th. Last descant grade.
- 5 to 6 (treble only): top F6, odd metres, triplets, metre changes; scales reach B and C#/Db major and minor; first thirds.
- 6 to 8: 7/8, 7/4, then 12/8, triplet crotchets, acceleration, ornaments, ff/pp; SR range tops at G6 while scales reach Ab6 at G8.

## Arranging implications

- Say which recorder. DESCANT: write an octave below sounding (stave C4-B5 for sounding C5-B6). TREBLE: write at sounding pitch. Ceilings by grade (written): descant G1 D4-D5, G2 C4-F5, G3 C4-A5, G4-G5 C4-B5; treble G1 G4-G5, G2 F4-Bb5, G3 F4-D6, G4-G5 F4-E6, G6 F4-F6, G7-G8 F4-G6 (no F#6 required).
- Key ladder (SR): descant G1 C, F; G2 D, d; G3 a; G4 G, e; G5 A, Bb, b, g. Treble G1 F, Bb; G2 C, g; G3 d; G4 G, a; G5 D, Eb, e, b; G6 A, f#, c; G7 E, Ab; G8 c#, f. For levels 1-3 transpose into C or F (descant) or F or Bb (treble); keep accidentals out until G3 (minor keys only), chromatic notes until G4.
- Fingering cost: recorders play chromatics by cross-fingering, so sharps and flats are more demanding than on keyed woodwinds [I]; the syllabus keeps accidentals out of SR until G3 (S1) and Trinity until G3 (S3).
- Articulation ladder: G1 tongued or two-note slurs only; staccato G2; accents G3; tenuto and pause G4; ornaments (acciaccaturas, turns, trills) enter Trinity SR at G6. Dynamics: mf only at G1-G2; p G3; f and mp G4; hairpins G5; ff and pp only at G8. Recorder dynamics grow more slowly than other woodwinds in the same table (S1), and blowing harder sharpens pitch (S4): keep marked dynamics modest and gentle at low levels.
- Rhythm ladder: dotted minim/minim/crotchet/paired quavers (G1); four-quaver groups, dotted crotchet+quaver, ties (G2); dotted-quaver and semiquaver cells, 3/8 (G3); 6/8, anacrusis (G4); syncopation (G5); triplets, 9/8, 5/8, 5/4, metre changes (G6); 7/8, 7/4 (G7); 12/8, triplet crotchets (G8). Trinity Initial is only crotchets and minims in 2/4.
- Tempo: the scale guide is the ceiling for even quavers (crotchet 50 at G1 to 132 at G8); keep G1-G2 pieces slow enough for clean finger changes.
- Breath: recorder needs very little air (S4); running out is common and breath should fall at musical points (S5, weak). No official phrase length: give a rest or long note every 2-4 bars at G1-G3 [I].
- Descant for the first five grades (ABRSM ends there); at Trinity Initial the piano accompaniment can be moved down a 5th to let a treble player take the descant part (S3).
- To go down a level: cut range to the lower grade's ceiling, remove slurs longer than two notes, staccato, accents, tenuto, ornaments; replace dotted and semiquaver figures with quavers; remove accidentals; transpose to C or F (descant) or F or Bb (treble); remove syncopation and metre changes; use only mf.

## Confidence and gaps

- Verbatim official (S1, same as S2): SR length, time signatures, rhythms, recorder dynamics, articulation, keys, Helmholtz ranges, scale boxes, speeds. High. Trinity (S3) SR table and keys read from page images: high for Trinity, but the grade spacing differs from ABRSM (SR set two grades below).
- Derived [D]: scientific pitch, sounding pitch for descant, scale tops (lowest-tonic rule: treble lowest F4, descant written lowest C4). Medium-high. Notation octave (S4 plus ABRSM consistency) medium; ABRSM does not state whether its descant ranges are written or sounding.
- Unknown: set-piece ranges and keys; exact extended-range scale notes (graphics); Trinity scales (book not retrieved); Initial SR range notes; ABRSM Initial (none exists); sopranino, tenor, bass demands; official phrase or breath figures; recorder-specific difficulty of thumb-hole and high-register fingerings by grade.

## Sources

- S1 (official, primary). ABRSM, "Woodwind Practical Grades Qualification Specification from 2026" (163 pp, valid from 1 Jan 2026). https://www.abrsm.org/sites/default/files/2025-06/ABRSM%20Woodwind%20Practical%20Grades%20Qualification%20Specification%20from%202026.pdf . Taken: recorder rules (pp. 10-11: separate syllabuses, descant only G1-5, related-instrument options), scale rules and speed guide (pp. 13-15), SR parameters (p. 21: includes recorder-specific dynamics), SR keys and ranges (p. 22, page image read), Descant (from p. 23) and Treble (from p. 33) scale boxes, SR prep time 30 s. States that scales, SR and aural stay as in 2022.
- S2 (official, previous edition). ABRSM, "Practical Music Grades: Woodwind Syllabus from 2022" (168 pp). https://www.abrsm.org/sites/default/files/2023-10/Woodwind%202022%20Practical%20syllabus%20(0%20ALL)%2020230911.pdf . Used to check: I text-diffed the descant and treble scale boxes and the SR keys and ranges against S1: identical except page references.
- S3 (official, other board). Trinity College London, "Woodwind Syllabus ... graded exams from 2022" (340 pp). https://trinitycollege.com/resource/?id=7385 . Taken: recorder Initial-Grade 8; recorder rules (descant or treble at Initial-G5, both at G6-8, technical work on descant at Initial and on treble at G6-8, Initial piano part may be transposed down a 5th for treble); Initial technical work (p. 108); SR parameter table (p. 173) and SR keys and test span (pp. 174-175, page images read); SR is set about two grades below the exam grade.
- S4. Wikipedia, "Recorder (musical instrument)". https://en.wikipedia.org/wiki/Recorder_(musical_instrument) . Taken: notation octave (sopranino, soprano, bass an octave below sounding; alto and tenor at pitch), lowest notes (soprano C5, alto F4), baroque vs German fingering, "very little air pressure" needed, blowing harder sharpens a note and much harder overblows, range of a baroque recorder about two octaves and a tone.
- S5 (weak). Recorder Jen blog, breath tag. https://recorderjen.co.uk/tag/breath/ . Taken (via a search summary, page not read in full): running out of breath is normal; breathe at musical points. Low confidence.
- Tried and not usable: abrsm.org HTML (403); Trinity's "Recorder Scales, Arpeggios & Exercises from 2017" (the book holding the technical work) not retrieved, so Trinity scales are known only from the syllabus text.
