# Classical guitar: difficulty by level (ABRSM Guitar Grades 1-8, syllabus from 2019, still current)

**Read this when** the target instrument is classical guitar, at any level. Numbers come from ABRSM Guitar syllabus (from 2019); the checker reads them from [../profiles/classical-guitar.json](../profiles/classical-guitar.json): `python3 scripts/check_level.py arrangement.musicxml --instrument classical-guitar --grade N`. S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

## Table by grade

No Initial grade; an ungraded Prep Test precedes Grade 1 (three short tunes from memory, two pieces, the second 16-24 bars, no marks) [A1]. Sight-reading and scale tables are the only official parameter lists; pieces (3 per exam, lists A/B/C) have none, so "range" for pieces is my reading of those ceilings.

| Level | Keys | Time signatures | Note values and rhythms | Typical range (written pitch / position) | Technique demands | Other features | Sight-reading parameters |
|---|---|---|---|---|---|---|---|
| Prep (pre-G1) | unknown | unknown | unknown | unknown | tunes from memory [A1] | second piece 16-24 bars [A1] | none |
| 1 | C, G, F major; A, E minor [A1]. Scales: G, F major, A, E minor; arpeggios G major, E minor, all 1 octave | 4/4, 3/4 [A1] (a 6-bar, 2/4 line sits at foot of the G1 block; see gaps) | dotted half, half, quarter, eighth pair, quarter rests; f/p, hairpins [A1] | 1st position, written E3-G5 (sounds E2-G4) [A1][C] | thumb-only (A, E minor scales) and fingers-only scales, tirando or apoyando at choice; single line, passages for thumb alone [A1] | scale q=48 (thumb-only q=96), arpeggio dotted q=40 [A1]. [S] 1st position, single-line, little left-hand independence | 4 bars; accidentals only inside minor keys |
| 2 | adds D minor [A1]. Scales: D major, A and D minor; C major thumb-only; chromatic from A; arpeggios C, D major, A, D minor (1 oct) | 2/4 added [A1] (or G1 per layout) | adds four eighths and dotted quarter+eighth patterns, staccato, mp/mf [A1] | 1st position, written E3-G5 [A1][C]. [S] reads into 2nd position | thumb-only chromatic scale and q=112 scales; staccato [A1]. [S] multiple voices, left-hand finger independence | scale q=56, arpeggio dotted q=42 [A1] | 4-6 bars (layout ambiguous) |
| 3 | adds D major [A1]. Scales: A major, B harmonic minor (fingers), G major, E melodic minor (thumb+fingers) 2 oct; F major in sixths | 3/8 added [A1] | adds eighth rests, accents, slurs, pp, simple broken-chord patterns [A1] | 2nd position, top string to fret 5: written A5 [A1][C]. [S] reads to 5th position | thumb+fingers combined scales (thumb low octave, fingers high); broken chord G major with over-ringing; 2-oct arpeggios without over-ringing; slurs [A1]. [S] shifting, barre | scale q=66, arpeggio dotted q=44, broken chord dotted q=54, intervals q=60 [A1] | up to 8 bars |
| 4 | adds A major [A1]. Scales: B-flat major, B melodic minor, F major, F-sharp harmonic minor; chromatic from G (2 oct); G major in tenths, A harmonic minor in sixths | 6/8 added [A1] | simple semiquaver patterns, ties, chromatic notes, pause, tenuto [A1] | not stated for sight-reading beyond 2nd position [A1]. [S] to 9th position (site's own grading) | simple two-part writing, mostly open strings in one voice; dominant 7th arpeggio (1 oct); tied notes [A1]. [S] polyphony, single-string trills, stretches with shifts | scale q=80, dom/dim 7th q=72, broken chord dotted q=60 [A1] | c. 8 bars |
| 5 | adds B minor [A1]. Scales: D major, A harmonic minor (fingers, both strokes prepared), E major, G melodic minor; A major sixths, F major octaves, A melodic minor tenths; dim 7th from A | none new [A1] | anacrusis, simple syncopation, ff [A1] | up to 5th position, written C6 on top string [A1][C] | simple two-note chords inside a single voice; from G5 examiner may ask tirando or apoyando for fingers-only scales [A1]. [S] ornaments (trills, mordents, appoggiaturas), hinge/half barre, tremolo preparation | scale q=96, dom/dim 7th q=84 [A1] | c. 8-12 bars; slowing at end |
| 6 | adds B-flat major, F-sharp minor [A1]. Scales: E-flat major; C, C-sharp minors (harmonic+melodic); E major 3 oct; intervals in thirds, tenths, sixths, octaves | 9/8, 5/8, 5/4 added [A1] | triplet patterns [A1] | above 5th position, no ceiling stated [A1]. Fret 12 on top string sounds E5, written E6 [C] | three-note chords in a single voice, easily prepared partial barres, 3-octave scales; fingers-only scales tirando or apoyando [A1]. [S] portamento, artificial harmonics, campanella, tonal control | 2-oct scale q=112, 3-oct dotted q=76, arpeggio dotted q=63 [A1] | no new length (c. 8-12) |
| 7 | adds E major, G minor [A1]. Scales: A-flat, B major; D, G-sharp minor; F major/minor 3 oct; chromatic from E 3 oct | 7/8, 7/4 added [A1] | no new values stated [A1] | simple 12th-fret harmonics [A1] | four-note chords; 3-octave dominant 7th (A) and diminished 7th (E) arpeggios; capo at fret 2 or 3 allowed only for pieces with optional F-sharp tuning (G7-8) [A1][P]. [S] bass stopping, hemiola, rasgueado | 2-oct scale q=126, 3-oct dotted q=84 [A1] | c. 12-16 bars; slowing then a tempo |
| 8 | adds C minor [A1]. Scales: D-flat major; B-flat, E-flat minors; G, F-sharp major, E minor 3 oct; chromatic from F 3 oct; octave and chromatic interval scales | 12/8 added [A1] | simple ornaments [A1] | full fingerboard in pieces (unknown limit); full barres in sight-reading [A1] | full barres; 3-octave scales and arpeggios in several keys; one piece may be piano-accompanied [A1]. [S] cross-string trills, quintuplets, rest-stroke thumb, tremolo, Bartok pizzicato | 2-oct scale q=144, 3-oct dotted q=96, arpeggio dotted q=76 [A1] | c. 16-20 bars; speeding up |

## What changes between neighbouring grades

- 1 to 2: 2/4, dotted rhythms and groups of four eighths, staccato, D minor; thumb-only scales speed up.
- 2 to 3: 3/8, eighth rests, slurs/accents, 2nd position, thumb + fingers together in broken chords; D major.
- 3 to 4: 6/8, semiquavers, ties, chromatic notes, first two-part texture (open strings in one voice); A major.
- 4 to 5: anacrusis, syncopation, positions up to 5th, two-note chords, both rest- and free-stroke scales.
- 5 to 6: triplets, 9/8, 5/8, 5/4, positions above 5th, three-note chords, partial barres, 3-octave scales begin.
- 6 to 7: 7/8 and 7/4, four-note chords, 12th-fret harmonics, more 3-octave work, E major/G minor.
- 7 to 8: 12/8, full barres, ornaments, acceleration; C minor; piano-accompanied piece option.

## Arranging implications

- Write the part in treble clef sounding an octave lower than written; check written lows against the open E (written E3) [W1][W2].
- Keep keys guitar-friendly: G1-2 C, G, F, Am, Em, Dm; G3 add D; G4 add A; G5 add Bm; G6 B-flat, F-sharp minor; G7 E, Gm; G8 Cm [A1]. Open strings carry the early grades, so avoid keys with many sharps/flats before G5.
- Texture ladder: single line (G1-2, thumb alone allowed) > broken chord with thumb + fingers (G3) > two voices, one on open strings (G4) > two-note chords in one voice (G5) > three-note chords and partial barre (G6) > four-note chords (G7) > full barre (G8).
- Rhythm ceilings: G1 up to eighth pair; G2 dotted quarter+eighth; G3 eighth rests; G4 simple semiquavers, ties; G5 simple syncopation, pickup bar; G6 triplets; G7 and above compound/irregular meters (7/8, 7/4, 12/8).
- Position ceilings (sight-reading, [A1]): 1st (G1-2), 2nd (G3), up to 5th (G5), above 5th (G6). For pieces I suggest staying inside these ceilings at G1-G3 and allowing about one grade of extra position range from G4 up (inferred, not official).
- Dynamics: keep f/p (G1), add mp/mf (G2), pp (G3), ff (G5) [A1]. Tempo: use the scale speed table as an even-note ceiling (quarter at 48 G1, 66 G3, 96 G5, 144 G8 for 2-oct scales).
- Do not use a capo or altered tuning below G7; guitar-duet or piano accompaniment may be provided in G1-3 (up to 2 pieces), G4-5 (1), G8 (1 piano) [A1].
- Sight-reading lengths (4, up to 8, c. 8, c. 8-12, c. 12-16, c. 16-20 bars) are a sanity check on phrase length, not piece length.

## Confidence and gaps

- Keys, time signatures, note values, scale content, speeds, sight-reading features: verbatim official [A1]/[A2] (symbols for note values interpreted from images; "+"/"-" accidentals decoded as sharp/flat).
- Written range: computed [C] from official position limits, official only for positions; piece-level ranges and hand-stretch limits: unknown (no source). G4 position ceiling: unknown officially, only [S] (9th position, site's own scale).
- Technique demands beyond scales (barre details, tremolo, ornaments): secondary [S], medium-low confidence. [S] positions run ahead of ABRSM sight-reading ceilings (5th position at G3 vs ABRSM 2nd), consistent with pieces being harder than sight-reading but unverified.
- Gaps: no Initial level; piece length/bars unknown; the "6-bar 2/4" cell in the sight-reading table is positioned at the foot of the Grade 1 block, so whether it is Grade 1 or 2 is ambiguous (I place 2/4 at G2); "optional F-sharp tuning" for G7-8 pieces not explained in the text I read.

## Sources

- [A1] ABRSM, "Guitar Syllabus from 2019" (49 pp, valid from 1 Jan 2019 until further notice), mirror https://www.newschool.ie/wp-content/uploads/2019/09/complete_guitar_syllabus.pdf. Taken: scale/arpeggio list and speed table per grade, sight-reading parameter table (length, time, keys, features), instrument/capo rules, accompaniment/duet options, exam marks, Prep Test.
- [A2] Same document on ABRSM's own site ("Practical Music Grades Guitar Syllabus from 2019"), https://www.abrsm.org/sites/default/files/2025-05/Guitar%20Practical%20Grade%20Syllabus_0.pdf. Used to confirm [A1] is the current text (sight-reading table and speed table identical).
- [S] Classical Guitar Corner, "Classical Guitar Music Grades", https://www.classicalguitarcorner.com/classical-guitar-music-grades/. Taken: a teacher-site technique ladder per grade. It describes the site's own grading (not ABRSM's), so treat as secondary and approximate.
- [W1] Wikipedia, "Transposing instrument" https://en.wikipedia.org/wiki/Transposing_instrument: guitar sounds an octave lower than written. [W2] Wikipedia, "Classical guitar" https://en.wikipedia.org/wiki/Classical_guitar: standard tuning E2 A2 D3 G3 B3 E4, most instruments have 19 frets.
- [P] https://www.playableguitar.com/abrsm-for-guitarists.html: teacher page; only confirmed capo rule (G7-8 only). Tried and failed: ABRSM html pages and Music Teacher magazine review (403). ABRSM publishes no per-piece difficulty parameters.
- Computed [C]: written pitch ranges from the position limits in [A1] (position = fret of index finger; frets given as 4-fret spans). Open strings are written E3 A3 D4 G4 B4 E5 (sound E2-E4). Music names: UK crotchet=quarter, quaver=eighth, semiquaver=16th. "tirando" = free stroke, "apoyando" = rest stroke. ABRSM note-value symbols were read from page images.
