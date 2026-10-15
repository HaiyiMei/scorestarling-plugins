# Sources and how far to trust them

Read this when the user asks where a number comes from, when you cite a limit, or when you need to know
how solid an instrument's table is. Everything in the skill is our summary, in our own words, of public
documents; ABRSM, Trinity, RSL, RCM, AMEB and the Chinese boards' own documents are the authority and are
revised every few years. Nothing here copies repertoire lists, set-piece titles or scale lists. Compiled
2026-10-14; check the issue date of the syllabus before quoting a number as current.

## Contents

- How the entries are labelled
- Piano
- Strings: violin, viola, cello, double bass
- Woodwind: flute, oboe, clarinet, bassoon, saxophone, recorder
- Brass: trumpet, trombone, horn
- Guitar and ukulele
- Voice
- Drums
- Chinese instruments
- Level systems and the mappings between them
- Known gaps

## How the entries are labelled

| Label | Meaning |
| --- | --- |
| **Official** | The exam body's own document for that instrument and level |
| **Official, other board** | A different exam body's document, used for the Initial level, for a cross-check, or where the first board has no syllabus |
| **Reference** | Encyclopaedia or a maker's or teacher's reference for a physical fact (a range, a transposition) |
| **Teacher** | A teacher's, publisher's or school's page: useful, not authoritative |
| **Derived** | Computed or estimated by us from the sources above; marked in each instrument file |

An instrument file's tags (S1, S2 …, [T], [R], [D], [I]) point into that file's own Sources section. This page
is the map of those files.

ABRSM's HTML pages returned 403 to our fetchers during research; every ABRSM number was read from its
official PDF (text extracted and the key pages rendered and compared by eye). Hong Kong LCSD syllabi and
retailer copies of the same PDFs were used only to cross-check.

## Piano

| Source | Used for | Label |
| --- | --- | --- |
| ABRSM, *Piano Practical Grades syllabus 2025 & 2026*, sight-reading parameters p. 16 and scale/exam tables pp. 12–14 (PDF <https://www.abrsm.org/sites/default/files/2024-06/Piano%202025%20&%202026%20Prac%20syllabus%2020240524_access.pdf>) | Keys, time signatures, hand position and new notation features per grade (cumulative); scale speeds | Official |
| Ramoneda, Lee, Jeong, Valero-Mas, Serra, the PSyllabus paper, IEEE TASLP 33 (2025), arXiv 2403.03947; dataset Zenodo 14794592; label source pianosyllabus.com | Notes per second and piece length by ABRSM grade (1,271 recordings), aggregate percentiles only | Derived (dataset licence stated inconsistently, so no data is copied) |
| Published piece lists for Grade 1 (2025–26) | A sense of what a Grade 1 *piece* does beyond the sight-reading line | Teacher, described not copied |
| Our texture, span and leap thresholds | Hand span, left-hand pace, chord sizes, ledger lines, leaps | Derived, marked in [piano.md](instruments/piano.md) |

## Strings: violin, viola, cello, double bass

Official: ABRSM, *Bowed Strings Syllabus from 2024* (violin 70 pp, dated 11 Dec 2024; cello 71 pp, 1 Sep 2023; the
four-instrument volume 126 pp, 6 Jun 2023). Taken: the sight-reading parameter table and the keys and ranges
table (printed pp. 23–24), the scale and arpeggio box on each grade's page, and the scale speed table. Pitch
ranges are printed in Helmholtz notation and converted by us to scientific pitch (C4 = middle C); the violin and
woodwind range tables were checked against rendered page images. Viola and double bass share the same tables.
Double bass sounds an octave below written; this is a reference fact. See [violin.md](instruments/violin.md),
[viola.md](instruments/viola.md), [cello.md](instruments/cello.md),
[double-bass.md](instruments/double-bass.md) for the exact URLs.

## Woodwind: flute, oboe, clarinet, bassoon, saxophone, recorder

Official: ABRSM, *Woodwind Practical Grades Syllabus from 2022* (PDF
<https://www.abrsm.org/sites/default/files/2023-10/Woodwind%202022%20Practical%20syllabus%20(0%20ALL)%2020230911.pdf>)
and the *Woodwind Practical Grades Qualification Specification from 2026* (PDF
<https://www.abrsm.org/sites/default/files/2025-06/ABRSM%20Woodwind%20Practical%20Grades%20Qualification%20Specification%20from%202026.pdf>),
which states that scales, sight-reading and aural requirements stay the same. Taken: sight-reading parameters
(pp. 23–24), the keys and ranges table (p. 24), the scale and arpeggio tables per instrument. Official, other
board: Trinity College London, *Woodwind syllabus (from 2022)* (<https://trinitycollege.com/resource/?id=7385>):
Initial level, which ABRSM's woodwind syllabus does not have, and a cross-check. Reference: Wikipedia and woodwind
fingering guides for register breaks (clarinet break, saxophone palm keys, flute third octave). The breathing
limits are Derived: no board publishes phrase lengths.

- **Recorder.** ABRSM does examine it: a Descant (soprano) syllabus for Grades 1–5 only and a Treble (alto)
  syllabus for Grades 1–8, with the same sight-reading parameters and different keys and ranges. Descant is
  written an octave below sounding (Reference: Wikipedia, *Recorder*); ABRSM does not state whether its descant
  ranges are written or sounding, so that octave is **inferred**. Details: [recorder.md](instruments/recorder.md).
- **Oboe and bassoon.** Keys and ranges are from the same official table; the per-grade scale and technique
  lists were not reviewed. Details: [oboe.md](instruments/oboe.md), [bassoon.md](instruments/bassoon.md).
- Other instruments: [flute.md](instruments/flute.md), [clarinet.md](instruments/clarinet.md),
  [saxophone.md](instruments/saxophone.md).

## Brass: trumpet, trombone, horn

Official: ABRSM, *Brass Practical Grades Syllabus from 2023* (PDF
<https://www.abrsm.org/sites/default/files/2023-09/brass-2023-prac-syllabus-10feb23.pdf>), sight-reading
tables pp. 26–28. Official, other board: Trinity *Brass* syllabus (Initial level and a cross-check).
Reference: Wikipedia for written range and transposition (trumpet in B♭ sounds a major second lower; horn in F a
perfect fifth lower; tenor trombone in bass clef is non-transposing). ABRSM offers no Initial for brass. Brass
fatigue and breathing limits are Derived; ABRSM's slur limits for horn and the trombone slide positions are in the
instrument files but not measured by the checker. Details: [trumpet.md](instruments/trumpet.md),
[trombone.md](instruments/trombone.md), [horn.md](instruments/horn.md).

## Guitar and ukulele

- Classical guitar. Official: ABRSM *Guitar Syllabus from 2019* (still current). Taken: the sight-reading table
  (keys, time, features), scale and arpeggio positions per grade, speeds. Written pitch is an octave above
  sounding. The range is stated only to Grade 5 and is Derived from the position limits.
- Pop and rock guitar. Official, other board: Trinity College London *Rock & Pop Guitar syllabus 2018* (own-choice
  song parameters, Initial to 8) and RSL (Rockschool) *Guitar Syllabus 2018* (technical work, tempi). ABRSM has no
  rock guitar syllabus. There is no published key or range list, so the checks are lighter.
- Ukulele. ABRSM has no ukulele grades. Official, other board: RSL (Rockschool) *Contemporary Ukulele Syllabus
  Guide 2020* (a mirror of the PDF, <https://www.newschool.ie/wp-content/uploads/2020/05/RSL_Ukulele_Syllabus_Guide_2020_05May2020.pdf>;
  Debut and Grades 1–8; sight-reading parameters for Debut to Grade 5 and technical work), cross-checked with the
  London College of Music Examinations *Ukulele Syllabus 2023* (<https://lcme.uwl.ac.uk/media/qzyhfoue/ukulele-syllabus-2023.pdf>;
  chord vocabulary and time signatures). The boards are not aligned (LCM Step 1 is easier than RSL Debut), so
  "grade N" depends on the board; the profile follows RSL. RSL states a melodic compass only up to Grade 2, and
  the written octave is not stated (we assume sounding pitch in treble clef). Details: [ukulele.md](instruments/ukulele.md).

## Voice

Official: ABRSM *Singing Syllabus from 2018* (updated April 2021) for the sight-singing parameter table and the
vocal ranges printed per grade; ABRSM Singing Performance Grades. Official, other board: Trinity *Rock & Pop Vocals
2018* (range, keys, intervals, techniques) and RSL *Vocals Syllabus*. The span statistics are Derived from the
printed ranges and are biased towards treble voices; phrase lengths and breath counts are not in any source and
are our estimate.

## Drums

Official, other board: Trinity *Rock & Pop Drums syllabus 2018* (own-choice song parameters Initial–8: note values,
syncopation, time signatures, tempo, kit and beaters) and RSL (Rockschool) *Drums Syllabus 2018*. ABRSM offers no
drum-kit grades. The checks cover note values, kit size and hits at once only.

## Chinese instruments

[erhu.md](instruments/erhu.md), [guzheng.md](instruments/guzheng.md) and [dizi.md](instruments/dizi.md) each carry
their own source list. In short:

- Official (not mainland): the Hong Kong LCSD Music Office compulsory-material syllabi for each instrument
  (eight levels each; the only official numbers we found: keys or tunings per level and techniques). They say
  their pieces come partly from the CCOM (中央音乐学院) 1–6 and 7–9 books, which ties the ladders loosely together.
- Official, relayed: a 2026 CCOM overseas exam notice (via a Singapore exam centre) that confirms the subjects,
  levels 1–9 plus 演奏级 and the exam form.
- Publisher catalogues: tables of contents of the 中国音乐学院 (CCoM, levels 1–10), CCOM and 中国音协 exam books
  (etude topics per grade). Teacher: articles and vendor pages that list techniques per grade.
- No board publishes ranges, time signatures or tempi for these instruments. Ranges, meters and tempo in the
  profiles are **Derived** from instrument facts and the technique ladder; the confidence of each profile is low,
  and grade numbers are the Chinese boards' own (not mapped to ABRSM).

## Level systems and the mappings between them

Used by [levels.md](levels.md). Official: the ABRSM piano syllabus and its Simplified Chinese specifications
(vocabulary: 初级 = Initial); Trinity *Piano syllabus from 2023* (framework table, study hours); the UK Music Mark
page on equivalence of programmes of study; RCM *Piano Syllabus 2022 Edition* and RCM *Theory Examination
Equivalents* (the only cross-board table RCM publishes, theory only); University of Adelaide and UWA pages for AMEB;
the Ministry of Culture's 《社会艺术水平考级管理办法》 and its June 2026 draft revision; the 中国音协 2025 exam
subjects notice; the 上海音乐学院 2022 notice; the 上海音乐家协会 2025 piano notice (the method-book ladder per
level). Third-party copies of official notices were used for 中央音乐学院 (学琴记, 2019) and 中国音乐学院 (a 2024
summer notice relayed by the Dongguan site; the official site was down). Teacher: Chinese articles on equivalence
(Sina 2020, Toutiao 2023, Douban 2020, 学琴记 2017, pconline), which are informal, repertoire-only and contradict each
other. The PSyllabus pages (pianosyllabus.com) give a community 0–10 difficulty rating that is *not* a board
grade; they were used only as an axis.

The only official cross-links are ABRSM = Trinity (same UK framework band and study hours, not proven the same
difficulty) and RCM's theory table. Everything else in [levels.md](levels.md) below the line "working default" is
our convention and is said to be one.

## Known gaps

- No official practical equivalence between ABRSM and RCM, AMEB or the Chinese boards.
- AMEB's grade-by-grade requirements and ABRSM's own terms and licensing pages could not be fetched (HTTP 403).
- 中国音乐学院's level count for piano is 1–10 in most articles but 1–11 in one 2024 relay; unresolved.
- The Chinese short names for Trinity (三一), RCM and AMEB were not verified against the bodies' own sites.
- No public ABRSM statement on third-party use of 「英皇」 was found; the safe use is plain description of a
  level ("about Grade N"), no logos and no word like "official". Not legal advice.
- Chinese-instrument ladders: CCOM and CCoM per-grade rules could not be fetched (publisher pages blocked or absent); the
  per-grade text is teacher-level, and cross-board overlap is unclear (treat CCOM n and CCoM n as within about two grades).
- Recorder: ABRSM does not say whether its descant ranges are written or sounding; Trinity's recorder scale book was not retrieved.
- Ukulele: RSL gives no compass beyond Grade 2 and no written-octave convention; LCM set pieces are not documented.
- Estimator reliability: the checker's grade estimate is reliable to about Grade 5 for piano; above that most
  limits are left open by the sources.
