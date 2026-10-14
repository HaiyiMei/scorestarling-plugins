# Guzheng (古筝): difficulty by level (CCOM 中央音乐学院 1-9, CCoM 中国音乐学院 1-10, HK LCSD cross-check)

**Read this when** the target instrument is guzheng, at any level. Numbers come from Chinese exam books and teacher texts, with the Hong Kong LCSD syllabus as the only official numbers; grade N means 国内 N 级 (ABRSM does not examine this instrument), confidence low; the checker reads them from [../profiles/guzheng.json](../profiles/guzheng.json): `python3 scripts/check_level.py arrangement.musicxml --instrument guzheng --grade N`. S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

Tags: [O] official/government or exam-board text; [P] publisher/bookseller catalogue (TOC, blurb, printed rules); [T] teacher/school/website article; [R] reference work; [A] academic paper; [I] my inference (no source states it).

## Table by grade

Tuning note: standard 21-string zheng in D = D major pentatonic, 5 notes per octave, D2-D6 sounding (S8, S10); 4th and 7th degrees only by left-hand pressing 按音 (S5, S9). Parts are not transposed [I].

| Grade | Keys/modes & tuning | Typical range | Time sigs | Note values & rhythms | Techniques introduced | Tempo | Other |
|---|---|---|---|---|---|---|---|
| 1 | D tuning only, pentatonic (S1 E-1 [O]) | whole 21 strings are taught from the start (S1); melody likely D3-B5 [I] | unknown | basic rhythm patterns (S5 [T]) | 勾托抹托, 劈, 大撮/小撮, 花指, 揉弦, 上滑音 (S5 [T]); etudes: 勾托, 撮弦, 抹托, 花指, 托劈, 上滑音 (S3 [P]); simple two-hand pieces | unknown | jianpu reading (S1) |
| 2 | D; 按音 of 4 and 7 begins (S5 [T], etude 按音4、7 in S6) | as G1, left hand adds lower notes [I] | unknown | | 四点, 双手轮抹, 左手按变音, 上下滑音, 双手勾托+撮弦 (S3, S5); thumb small joint (S5); LCSD E-2: 大撮/小撮 + basic pressed slides (S1 [O]) | unknown | sight-reading and rhythm drills (S1) |
| 3 | D; accurate 4 and 7, tuning-by-ear (S5 [T]) | up to about B5/D6 [I] | unknown | | 摇指 incl. 短摇; 轮指 (3- and 4-finger) (S5 [T]); CCoM etudes: 花指+刮奏 glissando, 变音, 按音 (S3 [P]); LCSD I-1: basic 摇指, left-hand plucking, two-hand arpeggio (S1) | unknown | |
| 4 | D; modal piece 轻六调 (S6 [T]) | as G3 | unknown | syncopation, 32nd-note rhythms (S5 [T]) | 琶音, 分解和弦, relaxed even 摇指 (S5); CCoM etudes: 摇指, 琶音, 双手轮抹, 和音, 分指 (S3 [P]); 短摇 etude (S6); LCSD I-2: 扫摇, 双手轮抹, 泛音 (S1) | unknown | sight-reading stressed (S5) |
| 5 | D; D to G transposition appears at LCSD I-3 (S1 [O]; grade mapping [I]) | up to about D6 [I] | unknown | | singing 摇指, 快四点, left/right independence (S5); CCoM etudes: left-hand plucking, 双撮, 扫摇 (S3); LCSD I-3: 短摇 (S1) | unknown | regional styles and fingerings begin (S5) |
| 6 | special tunings 特殊定弦 (S5 [T]); 重六调 in CCoM piece (S3 [P]) | as G5 | unknown | | tone-colour control, left-hand 韵味, Shandong thumb-small-joint 托劈, Henan big-joint 托劈, 剔托 octaves (S5 [T]) | unknown | dynamics contrast (S5) |
| 7 | G key (LCSD A-1, S1 [O]; its pieces are from the CCOM 7-9 book, exact grade [I]); 重六调 in CCOM piece (S4) | up to about D6 and beyond [I] | unknown | | 短摇/长摇/扫摇/八度摇/多弦摇, 快四点, fast 分指 (S5 [T]); CCOM/CCoM etudes: 双撮, triplet two-hand arpeggios, 右手摇指+左手琶音, small polyphony, fast 轮抹 (S3, S4) | unknown | |
| 8 | C key (LCSD A-2, S1; mapping [I]); accidentals and key changes, styles of Shandong, Henan, Chaozhou, Hakka, Zhejiang (S5 [T]) | full range [I] | unknown | 加花变奏 ornamented variation (S5) | 快速双撮, 复调, 长摇指 (S3, S4 [P]); staff sight-reading (S5, S1 A-2); 三指轮/四指轮 etudes (S6) | unknown | strength, endurance, speed (S5) |
| 9 | F key (LCSD A-3, S1; mapping [I]) | full range | unknown | | fast descending two-hand arpeggios, 摇指+琶音, polyphony (S3 [P]); 长轮/短轮 etudes (S6); efficient fast movement (S5) | unknown | modern techniques, fast finger sequences (S1 A-3) |
| 10 (CCoM/CMA only) | 活三五调 piece (S6 [T]) | full | unknown | | 小撮, 摇指 + left-hand broken chords, fast 托劈, 点指/轮抹 (S3 [P]) | unknown | CCOM has 演奏级 instead (S2) |

## What changes between neighbouring grades

- G1 to G2: single-note melodies become two-hand with 四点, 轮抹, pressed notes 4 and 7 (S5).
- G2 to G3: first 摇指 (short) and 轮指, glissando 刮奏, accurate 4 and 7 (S3, S5).
- G3 to G4: arpeggios and broken chords, steadier 摇指, syncopation and 32nd notes (S5).
- G4 to G6: faster 四点, left-hand independence, regional styles, special tunings (S5).
- G7 and up: full tremolo family, polyphony, key changes, staff sight-reading (S3, S4, S5).
- Numbering: CCOM 1-9 + 演奏级 (S2); CCoM 1-10 + 表演文凭级 (S3; its dizi/erhu blurbs say G10 was added on top of an earlier 1-9 scheme); 上音 1-10 (S7). Cross-board overlap is not clean: one Tibet-themed piece is CCoM G7 (S3) but in CCOM's 1-6 book (S1 footnote 3), another Shaanxi piece is G7 in both (S3, S4). Treat CCOM n and CCoM n as within about 2 grades [I].

## Arranging implications

- Default pitch set is D E F# A B; anything else needs 按音 (up to a minor third, S9). Below G2, remap 4 and 7 to neighbouring pentatonic notes; G3 allow occasional 4/7 on weak beats; G8+ allow accidentals and key changes.
- Keys: D for G1-G5 (S1 E-1..I-2, D to G transposition at I-3); G, C, F keys only at LCSD A-1..A-3, whose pieces come from the CCOM 7-9 book, so about G7-G9 [I]. Retuning means moving bridges; do not change key mid-piece below G8.
- To go down a grade: remove 摇指 below G3 (use repeated plucks or ringing long notes), no 刮奏 below G3, no 轮指 below G3, no 快四点 below G5, no octave tremolo/多弦摇 below G7, no polyphony or two independent moving lines below G7.
- Texture ladder: G1-2 melody right hand with sparse left-hand support; G3 left-hand fills; G4-6 broken chords and arpeggios; G7+ independent lines.
- Rhythm: keep 8ths/quarters at G1-3; syncopation and 32nds only from G4 (S5).
- Notation: jianpu is the main format for low grades (S1 E-1 teaches jianpu; staff reading arrives LCSD A-2 / CMA G8). If staff: grand staff, right hand top, left hand bottom (S9); written at sounding pitch [I]. Jianpu 1=D with low 1 (two dots) = D2, middle = D4 (I derived from D2-D6 21-string layout).
- The right hand plays to the right of the bridges, the left hand presses on the left side (S9): keep left-hand notes to the bass/accompaniment and pressed notes, and leave 4 and 7 unpressed when both hands are busy.

## Confidence and gaps

- Per-grade techniques: MEDIUM-HIGH (S3 etude topics [P] and S5 hints [T] agree; S1 [O] consistent: 摇指 at I-1/G3, 扫摇 at I-2/G4-5, 大撮 at E-2/G1-2).
- Keys: HIGH for D tuning and G/C/F ladder (S1), LOW for exactly which mainland grade each key arrives (mapping [I]).
- Range per grade: LOW; nothing states it. Time signatures: unknown; tempo: unknown. Tried: LCSD, CCOM/CCoM TOC pages, search for 速度/♩=.
- CCOM G1-6 etude topics not found online (only CCoM's); S5/S6 board is unnamed (likely the national "amateur" 1-10 book; search snippet also claimed a 9-grade 中国音协 vs 10-grade 民管学会 split, not verified).
- Zhihu pages with per-grade technique tables were blocked (HTTP 403).

## Sources

- S1 [O, Hong Kong, not mainland] LCSD Music Office 古箏必修教材 (rev. 2012-01), https://www.lcsd.gov.hk/en/mo/common/doc/faq/faq_01_syb_0206.pdf : 8 levels E-1..A-3, key per level, techniques, scale spans; footnotes say E-1..I-3 pieces come from the CCOM 古筝 1-6 book and A-1..A-3 pieces from the CCOM 7-9 book.
- S2 [O] 2026年中央音乐学院海外音乐水平考级 南洋艺术学院考点简章, https://www.nafa.edu.sg/docs/default-source/corp-docs/ccom/nafa-ccom-rules-regulations-chinese.pdf : CCOM grades 1-9 + 演奏级; exam = 1 etude (may read) + 1 piece (memorised).
- S3 [P] 中国音乐学院社会艺术水平考级全国通用教材 古筝 (second set, 林玲 ed.), TOCs: https://www.chinakaoyan.com/book/BookShow/id/89165.shtml , .../89173.shtml (G1-6), .../89192.shtml (G7-9), .../89196.shtml (G10 + diploma) : etude topics per grade, design blurb (G1-2 folk miniatures; from G3 traditional + created pieces; amateur, not a conservatory syllabus).
- S4 [P] 中央音乐学院海内外考级曲目 古筝(7-9 + 演奏级), https://www.chinakaoyan.com/book/BookShow/id/196882.shtml and .../89170.shtml : etude topics G7-G8.
- S5 [T] 古筝一至十级的考级提示与要求 (guzhengw.cn, 2013), http://www.guzhengw.cn/html/44-2/2554.htm : one hints block per grade 1-10 (board not named).
- S6 [T] same hints reposted: 古筝考级演奏中,有哪些标准与要求? (sohu/音教艺术网, 2018) https://www.sohu.com/a/228339012_156373 ; and 中音阶梯 古筝考级怎么考 https://www.zhongyin.net.cn/news-ykwd/2149.html : confirms S5 wording and adds an etude-topic list per grade (board not named): 按音4/7 at G2, 短摇 at G4, 扫摇 at G7, 三指/四指轮 at G8, 长轮/短轮 at G9; piece titles mention 轻六调 (G4), 活三五调 (G10); theory exam needed for G8.
- S7 [P] 古筝考级曲集 (上海音乐学院出版社, 2003), https://www.chinakaoyan.com/book/BookShow/id/89188.shtml : 10 levels, 1-4 初 / 5-7 中 / 8-10 高; 2 pieces per exam; G5-7 add theory + ear tests, required to enter G8-10.
- S8 [A] Sinin et al., Acoustics of the Guzheng, BioResources 21(2) 2026, https://bioresources.cnr.ncsu.edu/resources/acoustics-of-the-guzheng-chinese-plucked-zither/ : 21 strings from D2 (73.41 Hz, string 21) to D6 (1174.7 Hz, string 1); notes D E F# A B each octave.
- S9 [R] Orchid Ensemble, Compose for the zheng, https://www.orchidensemble.com/instruments/compose-for-the-zheng/ : grand staff (right hand upper, stems up), up to 4 notes per hand, slides/bends up to a minor third, tremolo 摇, 轮, 扫 notation.
- S10 [R] 维基百科 古箏, https://zh.wikipedia.org/wiki/古箏 : 21-string tuning is D major pentatonic; right/left-hand technique names.
