# Instruments without a graded profile

Read this when the instrument is not in the table in SKILL.md: harmonica, melodica, ocarina, accordion,
organ, harp, mandolin, banjo, xylophone, pipa, euphonium, tuba, an electronic keyboard, or anything else. No exam
board we found publishes level tables for these in a form that gives numbers, so this skill does not pretend
to know them. It still helps: it borrows the limits that carry over, takes the physical facts from the
instrument itself, and says so.

## Contents

- What to tell the user
- Which profile to borrow
- Facts to get from the instrument
- Worked example: diatonic harmonica
- Checking the result
- When to say no

## What to tell the user

One short line at the top of the reply, in the user's language, before the music:

> There is no published level table for harmonica, so I borrowed the beginner limits for rhythm and phrase
> length from flute Grade 1 and fitted the notes to a C diatonic harmonica. Treat the level as a guess; tell
> me if it is too hard or too easy.

- Say what was borrowed and what was taken from the instrument. Do not name a grade as if it were official.
- Offer the nearest supported instrument as a second version (flute or recorder for a blown melody
  instrument, piano for a keyboard-like one, guitar for a plucked chord instrument).
- Ask the player's real level in plain terms (months played, which method book or songs), because the
  grade borrowed from another instrument is only a starting point.

## Which profile to borrow

Pick the supported instrument whose *playing problem* is closest, not whose name is closest. Borrow only
what carries over: meters, shortest note value, dotted and syncopated rhythm, phrase length, tempo guide,
number of notes at once.

| Instrument | Borrow | Because |
| --- | --- | --- |
| Harmonica (diatonic), melodica, ocarina, tin whistle, 口琴, 口风琴, 陶笛 | `flute`, or `descant-recorder` for a beginner | One breath-driven line; phrase length and rhythm limits transfer |
| Accordion, organ, keyboard or synthesiser, harp, 电子琴, 手风琴 | `piano` | Two-hand texture, hand span and left-hand pace transfer; look up the left hand separately for accordion bass buttons |
| Xylophone, glockenspiel, marimba, vibraphone, hand bells, 木琴 | `piano` right hand | Single mallet line at a beginner level; no pedal, no sustained notes, so keep the notes short |
| Mandolin, banjo, bouzouki, 曼陀林 | `violin` for the line, `pop-guitar` or `ukulele` for chords | Violin tuning for mandolin; a chord part works as for guitar |
| Pipa, ruan, liuqin, yangqin, gu qin and other plucked or struck 民乐 | `classical-guitar`, or `guzheng` for the Chinese grade ladder | A plucked line with fingered positions; use the instrument's own range |
| Suona, sheng, xiao, hulusi, 唢呐, 笙, 箫, 葫芦丝 | `dizi` for Chinese grade numbers, or `flute` | One breath-driven line; take the key and range from the instrument |
| Huqin family other than erhu (gaohu, banhu, zhonghu), 高胡, 板胡 | `erhu` | Same bowing and fingering idiom; the range differs, so read it from the instrument |
| Euphonium, baritone horn, tuba, 上低音号, 大号 | `trombone` (bass clef, non-transposing), or `trumpet` for cornet and flugelhorn | Brass phrase length and rhythm; read the range from the instrument |
| Sopranino or bass recorder (written an octave below sounding), tenor recorder | `descant-recorder` (sopranino, bass) or `treble-recorder` (tenor) | Same family and fingering; the written-octave convention differs, see recorder.md |
| Anything with several voices at once (choir, hand-bell ensemble) | `voice` per part | One profile per part |

Say which profile you borrowed in the reply.

## Facts to get from the instrument

The profile can not tell you these, so ask the user or use what you reliably know, and mark anything you
are not sure of:

- Which model (key, number of holes or strings, tuning, a diatonic or chromatic one).
- The notes the instrument can actually play, and the range a beginner uses comfortably.
- Whether it transposes (written against sounding pitch).
- What it can not do (sustained notes on a xylophone; two adjacent notes at once on a diatonic harmonica;
  fast repeated notes on a bowed or blown instrument).

If you do not know, ask one short question rather than guess: a wrong note on a real instrument is worse
than a question.

## Worked example: diatonic harmonica

From general knowledge of the standard Richter layout, not from an exam board: a 10-hole diatonic
harmonica in C plays these notes, blow and draw, with the usual bends not counted (scientific pitch, C4 =
middle C):

| Hole | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Blow | C4 | E4 | G4 | C5 | E5 | G5 | C6 | E6 | G6 | C7 |
| Draw | D4 | G4 | B4 | D5 | F5 | A5 | B5 | D6 | F6 | A6 |

- A complete C major scale lies in holes 4 to 7: C5 D5 E5 F5 G5 A5 B5 C6. A beginner version fits there.
- F4 and A4 do not exist without a bend, so a lower octave line avoids them.
- Only one key, C major (and its modes), is available straight. A tune in another key has to be moved to C.
  Arrange in C, in a range of about C5–C6 for a beginner, with long notes and clear breaths between phrases.
- Borrow: Grade 1 flute for meters, note values and breathing.

## Checking the result

Run the checker with the borrowed profile and tell it to leave out what does not apply:

```
python3 scripts/check_level.py arrangement.musicxml --instrument flute --grade 1 --ignore range,key
```

`--ignore` turns the named checks into information only. Check the range and key by hand against the facts
above. Say in the reply that the check was against a borrowed profile.

## When to say no

- The user wants a part for an instrument you can not describe at all (a rare folk instrument): say so and
  offer the nearest supported instrument, or ask for the range and tuning.
- The user wants the part to match an exam syllabus for an instrument whose syllabus we did not read: say
  that the exam body's own book is the source, and offer an arrangement for practice at a stated difficulty.
