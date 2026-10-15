# Bamboo flute (竹笛/笛子): difficulty by level (CCOM 中央音乐学院 1-9, CCoM 中国音乐学院 1-10, HK LCSD cross-check)

**Read this when** the target instrument is dizi, at any level. Numbers come from Chinese exam books and teacher texts, with the Hong Kong LCSD syllabus as the only official numbers; grade N means 国内 N 级 (ABRSM does not examine this instrument), confidence low; the checker reads them from [../profiles/dizi.json](../profiles/dizi.json): `python3 scripts/check_level.py arrangement.musicxml --instrument dizi --grade N`. S1, S2 … in the tables point to the Sources section at the end; the master list with a confidence note for each is [../sources.md](../sources.md). Compiled 2026-10-14.

## Contents

- Table by grade
- What changes between neighbouring grades
- Arranging implications
- Confidence and gaps
- Sources

Tags: [O] official/government or exam-board text; [P] publisher/bookseller catalogue (TOC, blurb); [T] teacher/vendor/school article; [R] reference work; [A] academic paper; [I] my inference (no source states it).

## Table by grade

Key convention: a flute's name is the key it plays with all holes closed = 5 (筒音作5) (S1 E-1; S9). Closed-tube note (sounding) = 5th degree of the key: C qudi G4 (S8 [A]); others by transposition [I]: Bb F4, D A4, E B4, F C5, G D5, A E5. Other 筒音 fingerings (作2, 1, 6, 3, 4) shift the tonic: tonic = tube note minus that degree (S1 [O]).

| Grade | Keys/modes & flute | Typical range (C-qudi reference [I]) | Time sigs | Note values & rhythms | Techniques introduced | Tempo | Other |
|---|---|---|---|---|---|---|---|
| 1 | 筒音作5 only; G flute implied (S1 E-1 [O]); CCoM exams allow G/A bass, bB/C/D qudi, E-A bangdi (S3 [T]) | about G4-A5 (low 5 to mid 5/6) | unknown | plain note values (S5 [T]) | posture, breath, tongued vs slurred (吐音/边音), long-tone scale (S5 [T]); etudes: each hand, hands together, high/low octave, finger agility, 4th and 5th degree (S6 [P]) | unknown | 1 etude + 1 piece (S2) |
| 2 | 筒音作5 (S1 E-2 [O]) | adds second octave, to about E6 (S5: low, middle and high registers [T]) | unknown | rhythm etude (S6 [P]) | fluent fingering, 颤音 and 打音 begin (S5 [T]); LCSD E-2: legato, 打音, 赠音, trill, long tones; etudes: long tone, rhythm, single tonguing (S6 [P]) | unknown | |
| 3 | 筒音作5 mastered; 筒音作2 introduced (one piece in 作2) (S5 [T]) | to about G6 [I] | unknown | | trills, 打音, 倚音 grace notes, half-hole fingering introduced; single, double, triple tonguing mixed (S5 [T]); etudes: 打音+叠音, single tonguing, trill (S6 [P]) | unknown | |
| 4 | 作2 fast fingering (S5 [T]); LCSD I-1 adds D qudi, 作2 scales G and C (S1 [O]) | as G3 | unknown; varied rhythms (S5) | rhythm variety | breath control, regional style; etudes: 双吐, half-hole 4, 历音, 连吐 (S6 [P]); LCSD I-1: 双吐/三吐 (S1) | unknown | solo + small piece (S5) |
| 5 | 作6 introduced (S5 [T]); LCSD I-2 adds 作1 scales D, C and F-key staff reading (S1) | to about A6 | unknown | | up/down/multiple glides 滑音, applied tonguing, strong/weak breath, double tonguing, arpeggio 琶音 (S5 [T]); LCSD I-2: 历音 up/down, 气震音 (S1) | unknown | two solo pieces (S5) |
| 6 | 作6 trained, 作1 introduced (S5 [T]) | to about A6-B6 (near upper limit, S8) | unknown | | 历音, 花舌 flutter tongue, 剁音 begins, aims at circular breathing (S5 [T]); LCSD I-3: 花舌, 垛音, 散板 free-tempo handling, southern style (S1) | unknown | scale + octave drills (S5) |
| 7 | 作3 new fingering (S5 [T]); LCSD A-1 adds 作6 scales G, C and staff transposition (S1) | full | triplets, quintuplets, septuplets at LCSD A-2 (S1) | | circular breathing (S5 [T]; S1 A-2), fast tonguing, combined glides, octave-leap staccato, 六字调 practice | unknown | |
| 8 | all fingerings; LCSD A-3 adds 作4 scales G, C (S1) | full | compound meters at LCSD A-3 (S1) | | CMA etudes: breath control, rhythm, 作2 with 4 and flat 7, high-low register, vibrato 揉音 (S7 [P]); LCSD A-3: double-tongue circular breathing (S1) | unknown | large works (S5) |
| 9 | multi-key switching exercise 多调转换 (S5 [T]) | full | unknown | | comprehensive etudes (S7 [P]); concerto movement | unknown | |
| 10 (CCoM/CMA only) | key transposition 移宫转调 etude (S7 [P]) | full | 6/8 etude (S7 [P]) | tongued notes + altered notes | leaps between 作5 and 作3, 作6, broken chords, ornate fingering (S7 [P]) | unknown | CCOM has 演奏级 instead (S2) |

Placement of LCSD levels beside mainland grades in the table above is my rough alignment [I]: E-1/E-2 ~ G1-2, I-1 ~ G4, I-2 ~ G5, I-3 ~ G6, A-1 ~ G7, A-2 ~ G7-8, A-3 ~ G8-9 (only A-2/A-3 have a footnote tie to CCOM 7-9).

HK LCSD official ladder (S1 [O]; "flute implied" column is my derivation from tube note [I]):
| Level | Scales given | Flute needed [I] | Other skills |
|---|---|---|---|
| E-1 | G key 筒音作5 | G | grip, stance, embouchure, 吐音, jianpu |
| E-2 | 筒音作5 (正宫调) | G | legato, grace notes, trill, middle/high register |
| I-1 | G and C keys with 筒音作2 | D, G | 双吐/三吐, staff reading in G, D qudi introduced |
| I-2 | D and C keys with 筒音作1 | G, F | F-key staff reading, 历音, 气震音 |
| I-3 | 作1 drills | G | D-key staff reading, 散板, 花舌, 垛音 |
| A-1 | G and C keys with 筒音作6 | A, D | transposition on staff, semitones, northern style |
| A-2 | G and C keys with 筒音作3 | E, A | triplets/quintuplets/septuplets, circular breathing |
| A-3 | G and C keys with 筒音作4 | F, Bb | compound meter, double-tongue circular breathing |

## What changes between neighbouring grades

- G1 to G2: add the high register, trills and 打音 (S5, S1 E-2).
- G2 to G3: grace-note ornaments, mixed single/double/triple tonguing, first non-5 fingering (作2) and half-holes (S5).
- G3 to G5: faster 作2, glides, double tonguing, 作6 starts (S5, S6).
- G5 to G7: 历音, 花舌, 剁音, circular breathing, 作1 and 作3 (S5).
- G8 to G10: full-range works, key changes and transposition, 6/8 and leaps (S7).
- Numbering: CCOM 1-9 + 演奏级 (S2); CCoM 1-10 + 表演文凭级, G10 added above 1-9 (S4); CMA first-set books also run to 10 (S7), 上海音协 to 10 (S6). Overlap is unclear: CCOM's 1-6 book contains pieces that CCoM files at G3-G4 (S1 footnote 5 vs S4), while one piece LCSD cites from CCOM 7-9 is CCoM G7 (S1 vs S4). Treat CCOM n and CCoM n as within about 2 grades [I].

## Arranging implications

- Pick the flute from the melody's key: at G1-G2 write in the flute's own key (筒音作5). A melody key 4th/5th away needs a different flute or 作2/作1 fingerings, which only arrive about G3-G6 (S5, S1).
- 4th degree is a cross-fingered note in 作5 (F5 on C qudi, S8); all-open gives sharp 4 (F#5). Avoid chromatics below G3; half-hole notes from G3-G4 (S5, S6).
- To go down a grade: delete 循环换气 (G6+), 花舌 and 剁音 (G6+), 气震音 and 历音 (LCSD I-2), triple/double tonguing (G3-G5), 滑音 chains (G5); replace with single tongue or slurs. Keep phrases short (breath mark every 2 bars at G1-2 [I]).
- Range: G1 inside the first octave plus a step; G2 may use the high register; do not exceed ~A6/B6 on a C qudi (S8) or about 2.25 octaves total (S10).
- Triplets/quintuplets only from about LCSD A-2; compound meters from A-3; free-tempo (散板) from I-3.
- Notation: jianpu is relative to the flute key (1=G etc., S1). Sounding pitch of undotted 1 on a C qudi is C5 [I from S8 table]; staff scores may be written an octave low (S8 sample), so state sounding vs written octave. Staff reading is taught in steps G, F, D, then transposition (S1 I-1..A-1).

## Confidence and gaps

- Fingering ladder (作5, 2, 1, 6, 3, 4) and techniques: MEDIUM-HIGH (S1 [O] agrees broadly with S5/S6/S7).
- Mainland per-grade text: MEDIUM-LOW; S5 is vendor text, board unverified. Flute key per grade: LOW (derived [I]); CCoM key families in S3 have no grade split.
- Range, time signatures: LOW; tempo: unknown (nothing found in S1-S10; no BPM in any board text).
- Not found: CCOM 笛子 1-9 per-grade rules or etude lists (publisher pages 403/absent); CCoM etude names.

## Sources

- S1 [O, Hong Kong, not mainland] LCSD Music Office 笛子必修教材 (rev. 2025-09), https://www.lcsd.gov.hk/en/mo/common/doc/faq/faq_01_syb_0301.pdf : 8 levels E-1..A-3 with scale keys + 筒音 fingering, techniques, meters; footnotes: pieces for I-2..A-2 come partly from the CCOM 笛子 1-6 book (footnote 5), pieces for A-2/A-3 partly from the CCOM 7-9 book (footnote 6).
- S2 [O] 2026年中央音乐学院海外音乐水平考级 南洋艺术学院考点简章, https://www.nafa.edu.sg/docs/default-source/corp-docs/ccom/nafa-ccom-rules-regulations-chinese.pdf : 竹笛 is a CCOM subject, grades 1-9 + 演奏级; 1 etude (may read) + 1 piece (memorised).
- S3 [T] 音乐培训学校选哪个?中国音乐学院竹笛考级培训要求有哪些? (中音阶梯), https://www.zhongyin.net.cn/news-ykwd/16810.html : CCoM 竹笛 exam rules: pieces from the second-set textbook; flute-key families G/A bass dizi, bB/C/D qudi, E/F/G/A (page prints "椰笛", evidently a typo for 梆笛); all memorised. Does not say which grade uses which family.
- S4 [P] 中国音乐学院社会艺术水平考级全国通用教材 竹笛(1-10级) (张维良, 中国青年出版社 2011), https://www.zazhi.com.cn/book/194083.html : 10 grades; 4 etudes per grade (3 at G8-9); blurb says G10 was added on top of 1-9 and some subjects have a performance diploma.
- S5 [T] 笛子考级的等级划分标准 (顺笛 flute maker site), http://www.shundi8.com/show-218.html , identical text at 中音阶梯 https://www.zhongyin.net.cn/news-ykwd/2714.html : per-grade examinee notes G1-G10 (fingering families 全按作低音5/2/6/1/3, tonguing, 剁音, 循环吸气); says it is "China Conservatory of Music" as an example; board and edition unverified (older syllabus likely).
- S6 [P] 中国竹笛考级曲集 (上海音乐家协会竹笛专业委员会, 2009), https://www.chinakaoyan.com/book/BookShow/id/89167.shtml : etude topics G1-G4.
- S7 [P] 全国笛子演奏考级作品集(第一套) (中国音协考级委员会, 人民音乐出版社 2011), https://www.chinakaoyan.com/book/BookShow/id/89193.shtml (G8-10) and .../89197.shtml (G5-7, no etude names): etude topics G8-G10.
- S8 [A] 中國笛的音準、音域與音色 (NTU, 2005 PDF), https://scholars.lib.ntu.edu.tw/bitstreams/b5a90f8b-85e5-4746-8820-78a0a35ea518/download : C-key qudi pitch table: all holes closed = G4, register zones to A6, near upper limit B6; one sample score notated an octave below sounding.
- S9 [R] 维基百科 笛子, https://zh.wikipedia.org/wiki/笛子 : bangdi F/G/A, qudi C/D/E, key named by pitch of the third hole from the bottom; technique names.
- S10 [R] Wikipedia Dizi, https://en.wikipedia.org/wiki/Dizi_(instrument) : about 2.25 octaves; bangdi sits in piccolo range, qudi a 4th/5th lower.
