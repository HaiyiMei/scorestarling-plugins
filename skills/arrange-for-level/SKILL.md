---
name: arrange-for-level
description: Arrange or simplify a piece for a chosen instrument at a chosen level, then check it lands there. Routes across piano, violin, viola, cello, double bass, flute, oboe, clarinet, bassoon, saxophone, recorder, trumpet, trombone, horn, classical and pop guitar, ukulele, voice, drums and the Chinese erhu, guzheng and dizi, from beginner to Grade 8 (Chinese instruments to 10), with the level as an ABRSM, Trinity, RCM, AMEB or Chinese 考级 number or in plain words (beginner, easy, 初学, 入门). Use whenever someone wants an easier, graded or "playable for my student or child" version of a piece for a particular instrument ("Grade 3 piano", "英皇五级小提琴", "尤克里里弹唱简单版", "古筝三级", "flute version for a year-two player"), wants a part fitted to a learner's level, or asks whether a score is really at some grade, even if they never say "arrange". If the instrument or the level is missing, ask one short question with options instead of guessing. Not for faithful transcriptions or for tidying a score without making it easier.
---

# Arrange a piece for an instrument at a level

This skill turns a harder piece into a version a player at a given level can really play, keeping the
tune and the harmony recognisable. It is a router: it works out *which instrument* and *which level*
from the request (asking when they are missing), loads only the reference files that apply, and
runs one shared workflow. It holds the music only. How to read the source and deliver the new score on
each platform is the ScoreStarling base skill's job (`scorestarling-score` for recordings,
`scorestarling-notation` for sheet music and files). General arranging judgement (reduction priority,
texture cards, what to ask) is in
[../scorestarling-score/references/arranging.md](../scorestarling-score/references/arranging.md) when that
skill is installed; this skill adds the instrument and the level on top of it.

## Step 1: Resolve the request

Three things decide the result. Take each from the user's words, then from the source, then ask.

| Need | Where it comes from | When it is missing |
| --- | --- | --- |
| **Instrument** (what plays the new version) | Named in the request ("for flute", "小提琴", "弹唱"); or the source is a single-instrument score and the user said "easier" without naming another | Ask, unless the source settles it |
| **Level** | A grade and its exam board ("ABRSM 3", "英皇五级", "RCM 4", "中央音乐学院三级"); plain words (beginner, easy, 初学, 入门, 进阶); or a learner description ("one year of lessons") | Ask, unless a learner description lets you pick a default (see [levels.md](references/levels.md)) |
| **Source** | The score, file, recording or title in the conversation | Ask for it; the base skill says how to read each kind |

Also note, without asking unless it changes the result: the purpose (practice, lesson, performance, an
exam), a key or length wish, and whether the user wants a piano or chord backing as well.

How the common requests resolve:

| The user says | Do |
| --- | --- |
| "Grade 3 piano version of this" | Instrument piano, ABRSM 3: go |
| 「英皇五级小提琴」 | Violin, ABRSM 5: go, and say 「约英皇五级难度」 |
| "RCM level 4 flute", 「中央音乐学院三级钢琴」 | Map the level with [levels.md](references/levels.md), say the mapping you used in one line: go |
| "My daughter plays violin, about two years" | Take the default for that description (levels.md), say it, go; offer the next level up |
| "Make this easier" with a piano score | Instrument piano; **ask the level** |
| "A beginner version" with no instrument and a band recording | **Ask the instrument**; level default Initial or 1, say so |
| "A simple version" with no instrument, no source clue and no level | **Ask both**, in one message |
| Several instruments ("for flute and cello") | One arrangement per instrument, each against its own profile |
| "Recorder version for my class" | Descant by default (the school recorder), say it; ask only if the range suggests a treble |
| 「古筝三级」「二胡五级」 | Chinese 考级 level 3 / 5 on that instrument: go, say the confidence is low; if the board matters ask 央音 / 国院 / 音协 |
| 「尤克里里弹唱，简单点」 | Ukulele, melody plus chords in C, G or F; level default Debut–Grade 1, say so |
| An instrument with no profile (harmonica, accordion, pipa …) | Say it plainly, follow [other-instruments.md](references/other-instruments.md), offer the nearest supported instrument |
| "Is this really Grade N?" | No arrangement: run the checker with `--estimate` or `--grade N` and report |

### When to ask

Ask only for what is missing *and* changes the result. Never ask what the source or the wording
already answers; never ask more than two things at once; ask in the user's language.

- One short message, the questions numbered, each with 3–4 options and one marked as the default:
  > Two quick things first: 1) Which instrument will play it: piano (default), flute, violin, something else? 2) Which level: first year (about Grade 1, default), second or third year (Grade 2–3), or past that?
- Say what the answer will do ("so I can keep it in a range she can reach"), in a few words.
- If the host cannot wait for an answer (a one-shot run, an automation), use the marked defaults and state
  them at the top of the reply, so the user can correct them.
- If the user gives an answer outside the options, take it; if it is outside this skill (an unsupported
  instrument), say so and offer the nearest one.

## Step 2: Load only what applies (progressive disclosure)

| Load | When |
| --- | --- |
| [references/levels.md](references/levels.md) | The level is in words, in a non-ABRSM system, or described by years of lessons; also to explain the mapping |
| The target instrument's file in [references/instruments/](references/instruments/) (table below) | Always, for the instrument you are arranging for. Read only that one |
| [references/other-instruments.md](references/other-instruments.md) | The instrument is not in the table |
| [references/sources.md](references/sources.md) | The user asks where a number comes from, or you cite a limit |

| Instrument (say it as the user did) | File | Checker profile | Levels | How solid |
| --- | --- | --- | --- | --- |
| piano 钢琴 | [piano.md](references/instruments/piano.md) | `piano` | Initial, 1–8 | Keys, meters, features official (ABRSM); texture and span our estimate, calibrated on 1,271 recordings |
| violin 小提琴, viola 中提琴, cello 大提琴 | [violin.md](references/instruments/violin.md), [viola.md](references/instruments/viola.md), [cello.md](references/instruments/cello.md) | `violin`, `viola`, `cello` | Initial, 1–8 | Official (ABRSM sight-reading tables) |
| double bass 低音提琴 | [double-bass.md](references/instruments/double-bass.md) | `double-bass` | Initial, 1–8 | Keys and ranges official, technique not reviewed |
| flute 长笛, clarinet 单簧管, saxophone 萨克斯 | [flute.md](references/instruments/flute.md), [clarinet.md](references/instruments/clarinet.md), [saxophone.md](references/instruments/saxophone.md) | `flute`, `clarinet`, `saxophone` | 1–8 | Official (ABRSM); breathing limits our estimate |
| oboe 双簧管, bassoon 巴松 | [oboe.md](references/instruments/oboe.md), [bassoon.md](references/instruments/bassoon.md) | `oboe`, `bassoon` | 1–8 | Keys and ranges official, technique not reviewed |
| recorder 竖笛 (descant or treble: **ask if unclear**, default descant) | [recorder.md](references/instruments/recorder.md) | `descant-recorder` (written an octave below sounding), `treble-recorder` | descant 1–5, treble 1–8 | Official (ABRSM Woodwind); descant written octave inferred |
| trumpet 小号, trombone 长号, horn 圆号 | [trumpet.md](references/instruments/trumpet.md), [trombone.md](references/instruments/trombone.md), [horn.md](references/instruments/horn.md) | `trumpet`, `trombone`, `horn` | 1–8 | Official (ABRSM Brass); slur and slide limits not measured |
| classical guitar 古典吉他 | [classical-guitar.md](references/instruments/classical-guitar.md) | `classical-guitar` | 1–8 | Keys, meters, rhythm official; range only to Grade 5 |
| pop / rock guitar 民谣、流行吉他 (acoustic or electric) | [pop-guitar.md](references/instruments/pop-guitar.md) | `pop-guitar` | Initial, 1–8 | Official (Trinity, RSL); no key or range list, so lighter checks |
| ukulele 尤克里里 | [ukulele.md](references/instruments/ukulele.md) | `ukulele` | Debut (0), 1–8 (measured to 5) | Official (RSL Rockschool, LCM cross-check); no ABRSM grades exist |
| voice 声乐、唱歌 | [voice.md](references/instruments/voice.md) | `voice` | Initial, 1–8 | Mixed boards; span and breathing partly our estimate |
| drums 架子鼓 | [drums.md](references/instruments/drums.md) | `drums` | Initial, 1–8 | Official (Trinity, RSL); note values and kit size only |
| erhu 二胡, guzheng 古筝, dizi 竹笛 | [erhu.md](references/instruments/erhu.md), [guzheng.md](references/instruments/guzheng.md), [dizi.md](references/instruments/dizi.md) | `erhu`, `guzheng`, `dizi` | 1–10 (Chinese 考级 numbers, not ABRSM) | **Low**: teacher and publisher sources; no board publishes ranges, meters or tempo |

Notes on the table: Chinese-instrument levels are the Chinese boards' own numbers (央音 1–9, 国院 1–10), never
converted to ABRSM; say the confidence is low. Dizi needs the flute key (G, D, C …) chosen first, and
erhu, guzheng and dizi players often read jianpu, so offer it. Ukulele and pop guitar arrangements are
melody plus chord symbols, strumming pattern in words.

`python3 scripts/check_level.py --list` shows every profile the script knows. An instrument that is not in
the table: read [other-instruments.md](references/other-instruments.md).

## Ground rules

- The source stays as it is. The arrangement is a new, named score beside it.
- Lower difficulty, not identity: the melody's notes and contour, the bass at each chord change and the
  hook survive. When something must go, drop inner notes, doublings and fills first, move a note by an
  octave before deleting it, and never change a melody note to silence a warning or dodge an accidental.
- The level is a ceiling on every axis at once, not an average. Fix the axes that decide most
  arrangements first: key, range, shortest note value, and how much the accompanying hand or part does.
- Say "about Grade N" / 「约英皇N级难度」. ABRSM, Trinity, RCM, AMEB and the Chinese boards are exam
  bodies whose syllabi describe what they test; none certifies a score. Never call an arrangement an
  exam piece, approved or official. If the user is preparing an exam, tell them once that exam pieces
  must come from the current syllabus list, so this is for practice and enjoyment.
- Talk in the user's words: use grade names only if the user did (or as a short aside), otherwise
  "first-year", "easy", "beginner". Title the score with the song, the instrument, the level and the key.
- An arrangement of a copyrighted song is fine for the user's own practice; ScoreStarling grants no right
  to publish or sell it.

## Step 3: The workflow

1. **Read the master.** Get the source as notation (the base skill says how). Note its key, meter, tempo,
   form (sections, repeats), the melody, one chord per bar or half bar and the hook. If the source is a
   fresh transcription nobody has checked (one made earlier in this conversation), mention once that the
   arrangement inherits its mistakes; do not guess this about a file the user brings.
2. **Decide what to keep.** The whole piece, unless it is long and the user asked for "a short version";
   then keep the best-known sections and say which bars were left out. Keep the opening and the ending.
   Reuse identical sections with plain repeat barlines (and 1st/2nd-time endings) instead of writing them
   out twice; avoid D.C., D.S. and Fine as words, which many players, exports and playback ignore.
   A section that comes back in another octave or with small variants is written out once more in the
   comfortable octave, not dropped.
3. **Choose the key and the register.** Take the instrument file's key list for the level and its range.
   Keep the original key if it is on the list and the melody fits the range; otherwise move the whole
   arrangement by one interval to the nearest listed key that keeps the melody inside the range with the
   fewest awkward notes, and say so (it changes the sound; offer the original key as a harder second
   version). A key change inside the piece moves by the same interval; if it lands outside the list,
   drop it and say so. **Transposing instruments** (clarinet and trumpet in B♭, saxophones, horn in F, guitar,
   double bass, descant recorder …): the profile ranges and keys are written pitch. Write the part as the player reads it if
   the base skill supports that; otherwise write concert pitch, say "concert pitch" and the written
   interval in the title notes, and run the checker, which shifts a concert-pitch file for you (set
   `--written-offset` for another saxophone: soprano 2, alto 9, tenor 14, baritone 21).
4. **Fit the rhythm.** Strip the rhythmic items the instrument file says arrive after the target level
   (shortest note, dotted and syncopated figures, triplets, grace notes, odd meters). Double all values
   if the source moves in sixteenths. Keep the melody's long notes long.
5. **Write the main line.** The melody, in the instrument's idiom (slurs and bowings for strings, breaths
   for winds and voice, strings and positions for guitar). For winds and voice, end each phrase with a rest or a
   breath mark: the checker counts both when it measures the longest phrase. Where the tune jumps wider than the level
   allows or runs fast, keep the landmarks (first beat of each bar, phrase ends) and fill the rest with
   steps. Single-line instruments get the melody alone; offer a simple piano or chord backing as a second
   score if the user wants one.
6. **Write the rest.** For piano: the left hand (see the piano file's ladder). For guitar: the chord
   shapes and pattern. For drums: the groove, fill and kit size for the level. For a melody instrument
   with no accompaniment, nothing. Keep contrast between sections (held notes in a verse, a fuller pattern
   in a chorus): easy pieces still have character.
7. **Check the harmony and the parts together.** Does melody plus bass still imply the chord? The notes
   that give a chord its colour (the third, a seventh, a chromatic note) must still be heard somewhere.
8. **Mark it like an edition for the level.** A tempo word and a moderate metronome mark inside the
   instrument's tempo guide, only the dynamics, articulations and markings the level reads, phrase
   marks, a few fingerings or string choices where a position changes. No more.
9. **Measure it.** When you can run code:

   ```
   python3 scripts/check_level.py arrangement.musicxml --instrument <profile> --grade <N>
   python3 scripts/check_level.py source.musicxml --instrument <profile> --estimate
   python3 scripts/check_level.py --list
   ```

   It prints ok / warn / over per check with bar numbers, and a verdict (standard library only). Fix
   every "over"; keep a "warn" only when it is deliberate and say why. `--estimate` reports the lowest
   level with nothing over and the likely level; read it as a floor, because texture and technique above
   about Grade 5 are only partly measured. `--mark out.musicxml` colours the offending notes red for a
   before/after picture. The check serves the music: never change a melody note to silence a warning; if
   the tune itself needs the leap, keep it and name it as the hard spot. When you cannot run code, go
   through the instrument file's table by hand, bar by bar. A clean check does not prove the music
   survived: A/B the result against the master for melody, bass at changes and form.
10. **Deliver and report.** Write it in the format the base skill uses (ABC with one voice per staff is
    easiest; MusicXML for a file), save it as a new score, and tell the user in a few lines: the key (and
    that it moved, if it did), what changed, what was left out, the one or two spots that may still be
    hard, and one next step (the original key, one grade up or down, a piano backing, jianpu, or
    listening to it).

## Limits to be honest about

- A level is a published syllabus table, not a stamp. Most numbers describe the unseen sight-reading
  test, which sits a little below exam pieces; they are safe-to-read limits.
- Official data is strongest for keys, meters, note values and range. Texture, hand span, leaps and
  breathing are partly our own estimates; each instrument file marks which.
- The checker measures notation, not musicianship. Cross-board equivalences are approximate and said so.
- When the learner is below the lowest level the instrument has (Initial for piano and strings, Grade 1
  for most winds), offer the five-finger or open-string version; when the source is already close to
  the target, change only what is over the line and say so.
