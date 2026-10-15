# Erhu (二胡): difficulty by level (CCOM 中央音乐学院 1-9, CCoM 中国音乐学院 1-10, HK LCSD cross-check)

**Read this when** the target instrument is erhu, at any level. Numbers come from Chinese exam books and teacher texts, with the Hong Kong LCSD syllabus as the only official numbers; grade N means 国内 N 级 (ABRSM does not examine this instrument), confidence low; the checker reads them from [../profiles/erhu.json](../profiles/erhu.json): `python3 scripts/check_level.py arrangement.musicxml --instrument erhu --grade N`. S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

Tags: [O] official/government or exam-board text; [P] publisher/bookseller catalogue (TOC, blurb, printed exam rules); [T] teacher/school/association web article; [R] reference work; [low] generic non-exam article; [I] my inference (not stated by any source).

## Table by grade

Tuning note: the erhu is always D4/A4 (S9, S10). Syllabi name the "定弦" by jianpu key: 1-5 = D key, 5-2 = G key, 2-6 = C, 6-3 = F, 4-1 = A, 3-7 = Bb (S1 [O]); this is the same physical tuning, only the key changes.

| Grade | Keys/modes & tuning | Typical range | Time sigs | Note values & rhythms | Techniques introduced | Tempo | Other |
|---|---|---|---|---|---|---|---|
| 1 | D, G first-position 7-note scales (S6 [T]); CCOM also F (S3 [P]); 1-octave scale from open string (S1 [O]) | about D4-F5 [I from S1, S11] | unknown; 2/4, 4/4 [S11 low] | accurate note values; dotted rhythms, front/back 16ths (S3 [P]) | slurred vs separate bow 连弓/分弓, string crossing, 3rd/4th-finger pitch correction, little finger; first position only, relaxed tone (S3 [P], S6 [T]) | unknown (beginner 60-80 [S11 low]) | all memorised; blurb says do not skip grades (S3) |
| 2 | D, G; F upper/middle-position etude (S5 [P]) | about D4-F5, a bit higher in middle position [I] | unknown; 2/4, 4/4 [low] | syncopated bow, held notes, 16th groups (S3 [P]) | first shifting 换把, stable upper/middle-position pitch (S6 [T]); fast bow, 连顿弓, alternating bow, "11 string-crossing patterns" (S3, S5 [P]) | unknown | G1-3 etudes open with scale + finger-spacing (S3 [P]) |
| 3 | adds C (first-position c-key etudes, S5 [P]) | to about G5 [I from S11] | + 3/4 [S11 low] | two-hand coordination, finger-sequence patterns (S5 [P]) | comfortable shifting among upper/middle/lower positions; start of 揉弦 vibrato and 滑音 slides (S6 [T]); trill 颤音 etude (S5 [P]) | unknown | three vibrato etudes in S5 show vibrato is a G3 focus |
| 4 | adds Bb (upper-position intonation, Bb pentatonic) (S5 [P], S6 [T]) | to about G5 [I] | unknown | mixed rhythms (S5 [P]) | clean short/fast bows with spring, full-bodied long bows (S6 [T]); fast alternating fingers, fast shifting, 垫指滑音 slide etude (S5, S8 [P]) | unknown | pieces complete and fluent (S6 [T]) |
| 5 | C dynamics etude, D 溜手 (S6 [T], S5 [P]) | to about D6 [I from S11] | compound meter appears around here [I from S1 I-3] | octaves, fast large leaps (S5 [P]) | 跳把 jump shifts with secure pitch (S6 [T]); fast 7-note shifting, string crossing with held fingers, octave etude (S5 [P]) | unknown (fast bow 120-160 for intermediate [S11 low]) | first required piece, others optional (S6 [T]) |
| 6 | pentatonic and D major study (S5 [P]) | to about D6 [I] | unknown | triplet string crossing, syncopated bow (S6 [T], S5 [P]) | fast shifting, jump shifts, inner/outer string changes 里外换弦; wrist vibrato good, press/slide vibrato 压揉/滑揉 begin (S6, S7 [T]); fast-bow (快弓) etude (S5 [P]) | unknown | ~2 years of weekly lessons to reach G6 (S7 [T]) |
| 7 | chromatic (semitone) scales added (S5 [P]) | to about D6-G6 [I] | unknown | regional-style ornament rhythms | regional ornaments: slides, 滑揉, 花指 trills, third-interval trills 三度颤音 (S7 [T]); violin-study transcriptions (S5 [P]) | unknown | CCOM sight-reading starts at G7 (S4 [P]) |
| 8 | D, G, F, C, Bb, A, Eb in all positions (LCSD A-2/A-3, S1 [O]; grade mapping [I]); a Kreutzer D major study sits at LCSD A-2 (S1) | to about G6+ [I] | unknown | fast phrases with accents, dynamics (S7 [T]) | fast shifting/crossing with varied fingerings; style and "韵味" (S6, S7 [T]) | "快慢自如" qualitative (S7 [T]) | |
| 9 | all keys; fixed-pattern string-crossing etude (S6 [T]) | to G6+ (max A7, S9) | unknown | | all techniques fluent; transcribed violin ballade-type works (S7 [T]) | unknown | |
| 10 (CCoM, CMA only) | | | | | concert etude, concerto movements (S5, S6 [T]) | unknown | CCOM has 演奏级 instead (S2 [O]) |

HK LCSD official progression (S1 [O]; mapping to mainland grades is [I], from overlapping pieces: E-1/E-2 ~ G1-2, I-1 ~ G3-4, I-2/I-3 ~ G5-6, A-1 ~ G6-7, A-2 ~ G8, A-3 ~ G9-10):
| Level | Keys and scale span | Positions / techniques |
|---|---|---|
| E-1 | D (1-5 strings), G (5-2): 1 octave scale + arpeggio | first position only, jianpu reading, basic bowing and finger placing |
| E-2 | D, G first position | 3rd/4th-finger intonation, sequence patterns, four-finger first-position accuracy |
| I-1 | D, G in positions 1/3/5; F in positions 2/4 (1 octave) | shifting, basic 揉弦, 快弓 and 顿弓 |
| I-2 | + C (1.5 octaves); D, F, G all positions | consolidate vibrato and fast bow; first transposition drills |
| I-3 | + A major scale | fast bow + shifting; compound-meter (複拍子) rhythm |
| A-1 | A, Bb (up to 1.5 octaves) | natural harmonics 自然泛音, fast arpeggios, 滑音 |
| A-2 | + Eb (2 octaves); A, Bb consolidated | two-hand coordination, string crossing, finger spans, fast arpeggio |
| A-3 | C, D, Eb, F, G, A, Bb in all positions; A and Bb over 2 octaves | fast arpeggios and large leaps; piece analysis |

## What changes between neighbouring grades

- G1 to G2: still first position, but shifting to the middle position, syncopation and short fast bows arrive (S3, S6).
- G2 to G3: vibrato and slides start; three positions used; C key and trills appear (S5, S6).
- G3 to G4: Bb key, cleaner fast/short bows, finger-pad slides, quicker alternating fingers (S5, S6, S8).
- G4 to G5/G6: jump shifts, octaves, large leaps, inner/outer string changes; pressed and sliding vibrato (S5, S6, S7).
- G6 to G7+: regional ornaments, chromatic scales, sight-reading (CCOM), then transcriptions and concertos (S4, S5, S7).
- Numbering: CCOM = 1-9 + 演奏级 (S2); CCoM = 1-10 + 表演文凭级, G10 added on top of 1-9 (S5); the national amateur books (S6) and 上海音协 (S8) also use 1-10. Piece overlap shows no stable conversion: a Liu Tianhua march piece is CCoM G5 (S5) but sits in CCOM's 7-9 book (S1 footnote 3), while all four LCSD E-level pieces are in CCOM's G1 list (S3) and two of them also in CCoM G1 (S5). Treat CCOM n and CCoM n as within about 2 grades of each other [I].

## Arranging implications

- Pitch window: strings are D4 and A4, so nothing below D4; physical limit about A7 (S9). For G1-2 stay about D4-F5; G3-4 to about G5; G5-6 to about D6; go above D6 only at G7+ (ranges [I]).
- Keys by grade: D and G for G1-2 (S6); add F (S3) and C by G3; Bb by G4; A and Eb only for G6+ (S1 I-3..A-2); avoid keys with more than 3 sharps (none appear in any syllabus found).
- To go down a grade: drop shifts above the middle position, remove 揉弦 requirement (write long notes plain), turn 16th runs into 8ths, replace slides/ornaments with plain notes, avoid string alternation every note.
- Staying playable at grade N: only one string change per bar at G1-2; keep melodic stepwise in the same position; accidentals outside the key need extra finger-spacing work (no source gives a grade for chromatics except G7 chromatic scales in S5), so avoid below G6.
- Do not write harmonics (S1 A-1), fast arpeggios, third trills or jump shifts below G5-G7.
- Notation: students read jianpu first (S1 E-1); give key as "1=D (定弦 1-5)". The erhu is non-transposing, so staff notation is at sounding pitch [I]. Provide bow marks (推/拉) and fingerings at G1-3.

## Confidence and gaps

- Keys and positions by level: HIGH for LCSD levels (official), MEDIUM for mainland grades (publisher TOCs + teacher text, board of S6/S7 unnamed).
- Technique introduction order: MEDIUM-HIGH (S1, S3, S5, S6 agree on vibrato at about G3, shifting at about G2).
- Range per grade: LOW; no source states it. Derived from S1 scale spans, S9 limits and the weak S11. Tried: Baidu Baike (not fetchable), LCSD, CCOM pages.
- Time signatures: LOW (compound meter only from S1 I-3; S11 low). Tempo: unknown; no board number found (tried CCOM/CCoM pages, search for 速度 ♩=).
- CCOM 3-9 per-grade etude lists and exam rules by grade not found online; the 2004 rules (S4) may be outdated (2026 overseas uses 1+1, S2).

## Sources

- S1 [O, Hong Kong, not mainland] LCSD Music Office 二胡必修教材 (rev. 2023-09), https://www.lcsd.gov.hk/en/mo/common/others/faq/imts/faq_01_syb_0101.pdf : 8 levels E-1..A-3 (plus X-1/X-2): keys, positions, techniques, scale spans; its footnotes draw pieces from the CCOM 二胡 1-6 and 7-9 books.
- S2 [O] 2026年中央音乐学院海外音乐水平考级 南洋艺术学院考点简章, https://www.nafa.edu.sg/docs/default-source/corp-docs/ccom/nafa-ccom-rules-regulations-chinese.pdf : CCOM grades 1-9 + 演奏级; exam = 1 etude (may read) + 1 piece (memorised; 18+ may read).
- S3 [P] 考级曲目--二胡(1-6级) (CCOM Press 2004), https://www.chinakaoyan.com/book/BookShow/id/89283.shtml : etude topics G1-G2, blurb (G1-3 etudes open with scale/finger-spacing; warns against skipping grades).
- S4 [P] 中央音乐学院海内外考级曲目二胡(1-6) rules text, https://www.chinakaoyan.com/book/BookShow/id/89194.shtml : 2 etudes + 2 pieces per exam; sight-reading from G7 (8-12 bars, 2-3 grades lower); G4+ needs previous certificate.
- S5 [P] 中国音乐学院社会艺术水平考级全国通用教材 二胡(第二套 1-6), https://www.chinakaoyan.com/book/BookShow/id/89168.shtml : 10 grades + 表演文凭级; etude topics G1-G6; blurb (chromatic scales and violin-etude transcriptions from G7).
- S6 [T] 全国二胡(业余)考级要求及曲目 (jyerhu.com, 2013), http://www.jyerhu.com/ehpx/show.asp?id=13 : one requirement line per grade 1-10 (board not named; 10-grade system).
- S7 [T] 二胡考级:二胡演奏业余考级基本要求 (中音阶梯 school, reposting notes on 中国二胡考级曲集, 上海音乐出版社), https://www.zhongyin.net.cn/news-ykzx/696.html : G6-G10 level essays.
- S8 [P] 二胡考级曲集 1-10 (上海音乐家协会, 2006), https://www.chinakaoyan.com/book/BookShow/id/89200.shtml : etude topics G2-G4 (换把, 两手配合, 垫指滑音), 初/中/高 split.
- S9 [R] Wikipedia Erhu, https://en.wikipedia.org/wiki/Erhu : strings D4 (inner) / A4 (outer); max range D4-A7, usual about 2.5 octaves.
- S10 [R] 维基百科 二胡, https://zh.wikipedia.org/wiki/二胡 : modern tuning d'/a' (fifth); technique names.
- S11 [low] 针对不同学习阶段二胡选曲与难度选择建议 (sohu), https://m.sohu.com/a/923763876_121123854/ : stage ranges, meters, tempo guesses. Not an exam source; weak corroboration only.
- S12 [T] 央音二胡考级全攻略 (sohu), https://www.sohu.com/a/942875518_121123854 : domestic CCOM format (prepare 2+2, examiner draws 1+1; 音基 needed).
