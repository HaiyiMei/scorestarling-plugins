---
name: piano-grade-1
description: Arrange a piano piece or song down to about ABRSM Grade 1 difficulty (约英皇一级难度) as a new two-hand score a first-year pianist can really play, then check it lands there. Use whenever someone wants a Grade 1, 英皇一级, 一级, first-year, beginner or easy piano version of a piece, a transcription or a score file, wants a piece their child or student can play after six months to a year of lessons, or asks whether an arrangement is really Grade 1 level, even if they never say "arrange". Not for faithful transcriptions or for cleaning up a score without making it easier.
---

# Arrange a piano piece at about Grade 1

A Grade 1 pianist reads at most one sharp or flat, counts quarters, halves and pairs of eighths, plays
hands together with the left hand mostly one note at a time, and moves the hand a few times per
phrase. This skill turns a harder piece into that, keeping the tune and the harmony recognisable.
It holds the music only: how to read the source and deliver the new score on each platform is the
ScoreStarling base skill's job (`scorestarling-score` for recordings, `scorestarling-notation` for
sheet music and files). General arranging judgement (what the source is, reduction priority,
texture cards) is in [../scorestarling-score/references/arranging.md](../scorestarling-score/references/arranging.md)
when that skill is installed; this skill is the Grade 1 target on top of it.

The full profile with its sources is in [references/grade-1.md](references/grade-1.md). Read it
before the first arrangement in a conversation; the table below is the short form.

| Axis | About Grade 1 |
| --- | --- |
| Key | C, G or F major; A or D minor (E minor, one sharp, is the edge: Grade 2 keys start there) |
| Meter | 2/4, 3/4 or 4/4; keep a song's 6/8 only if it stays in plain dotted-quarter and quarter-eighth figures |
| Rhythm | Whole, half, dotted half, quarter, pairs of eighths, rests; an occasional dotted quarter + eighth and tie. No sixteenths, triplets or grace notes |
| Right hand | The melody, one note at a time; an occasional two-note interval at a cadence |
| Left hand | One note at a time in quarters or slower; simple patterns (held bass, root–fifth, 1-5-3 in a waltz); an occasional two-note fifth or sixth. No three-note chords |
| Span and moves | Each hand mostly in a five-finger position, a few moves per phrase, no stretch beyond a sixth, no leap over an octave between connected notes (after a rest or a long note the hand has time to move) |
| Reading | Treble clef RH, bass clef LH, no clef changes, no 8va, at most one ledger line |
| Extras | No pedal needed; p, mp, mf, f, hairpins, slurs, staccato are fine |
| Length | Usually 8–40 bars; a song keeps its form, with repeat signs where sections repeat |

## Ground rules

- The source stays as it is. The arrangement is a new, named score beside it.
- Lower difficulty, not identity: the melody's notes and contour, the bass at each chord change
  and the hook survive. When something must go, drop inner notes, doublings and fills first,
  move a note by an octave before deleting it, and never "fix" a melody note to dodge an
  accidental.
- Say "about Grade 1" / 「约英皇一级难度」. ABRSM is a trademark and its grades are a syllabus,
  not a stamp: never call an arrangement an ABRSM piece, exam piece or approved, and if the user
  is preparing an exam, tell them once that exam pieces must come from the current syllabus list,
  so this is for practice and enjoyment.
- An arrangement of a copyrighted song is fine for the user's own practice; ScoreStarling grants
  no right to publish or sell it.

## Workflow

1. **Read the master.** Get the source as notation (the base skill says how). Note its key,
   meter, tempo, form (sections, repeats), the melody line, one chord per bar or half bar, and the
   hook. If you know the source is a fresh transcription nobody has checked yet (one made earlier
   in this conversation, say), mention once that the arrangement inherits its mistakes; do not
   guess this about a file the user brings.

2. **Decide what to keep.** The whole piece, unless it is long and the user asked for "a short
   version"; then keep the best-known sections and say which bars were left out. Keep the
   opening and the ending (intro, coda, the last cadence): they are what makes it sound finished.
   Reuse identical sections with plain repeat barlines (and 1st/2nd-time endings) instead of
   writing them out twice; avoid D.C., D.S. and Fine as words, which many players, exports and
   playback ignore. A section that comes back in another octave or with small variants is written
   out once more in the comfortable octave, not dropped.

3. **Choose the key.** Keep the original key if it already has at most one sharp or flat.
   Otherwise transpose the whole arrangement to the Grade 1 key that keeps the melody inside about
   C4–G5 with the fewest moves (usually the nearest of C, G or F major, or A or D minor), and say so: it
   changes the sound, so offer the original key as a harder second version. A key change inside
   the piece moves by the same interval; if it lands on a key with more than one accidental, drop
   it and say so.

4. **Fit the rhythm.** If the source moves in sixteenths, double every note value (2/4 → 4/4, ♩
   → 𝅗𝅥, tempo halved in feel) so the shape of the rhythm survives as eighths and quarters. Turn
   triplets into eighth pairs or a quarter-eighth pattern, drop grace notes and trills, and turn
   syncopations across a beat into on-beat notes unless the syncopation is the hook (then keep one
   simple version of it). Keep the melody's long notes long.

5. **Write the right hand: the melody.** One line, top voice of the source. Place it in an octave
   that sits around C4–G5. Where the tune jumps more than an octave or runs fast, keep the
   landmarks (first beat of each bar, phrase ends) and fill the rest with steps.

6. **Write the left hand: bass and harmony, slowly.** At each chord change choose one note,
   usually the root, sometimes the third or fifth when it makes a smoother line, inside one
   five-finger position around C3–C4 for as long as possible. Then give it one pattern per section
   from the ladder below, and keep the left hand still when the right hand has eighths.

   | Section feel | Grade 1 left hand |
   | --- | --- |
   | Calm, slow, one chord per bar | Whole or dotted-half bass note |
   | Steady, two chords per bar | Half notes, root then root or fifth |
   | Waltz, minuet, 3/4 | Dotted half, or bass on 1 then a held fifth/sixth on 2 |
   | Driving or broken-chord source (Alberti, 16th arpeggios, 8th pop patterns) | Quarters: 1-5-1-5 or 1-5-3-5 within a fifth, never faster |
   | Cadence or chorus lift | One two-note fifth or sixth, or a bass in octave-lower register |

   Keep a little contrast between sections (held notes in a verse, quarters in a chorus): Grade 1
   pieces still have character.

7. **Check the harmony and the hands together.** Play the two lines in your head bar by bar: does
   melody + bass still imply the chord (a bare fifth under a melody third is fine; a bass that
   clashes with a held melody note is not)? The notes that give a chord its colour (the third, a
   seventh, a chromatic note such as a diminished seventh's or a borrowed E♭ in C) must still be
   heard in one of the hands; over a held bass, give them to the right hand. Are both hands ever
   moving in eighths at once? Is any move faster than the beat before it allows?

8. **Mark it like a Grade 1 edition.** A tempo word and a moderate metronome mark, dynamics
   (p, mp, mf, f), phrase slurs, a few finger numbers on the first note of each new hand position.
   No pedal marks. Keep the title short enough for one line.

9. **Measure it.** When you can run code, run
   `python3 scripts/grade1_check.py arrangement.musicxml` (standard library only). It prints ok /
   warn / over per check with bar numbers. Fix every "over"; keep a "warn" only when it is
   deliberate and say why (for example a song that needs 48 bars). The check serves the music,
   not the other way round: never change a melody note or its octave inside a phrase only to
   silence a warning; if the tune itself needs the leap, keep it and name it as the hard spot.
   When you cannot run code, go through the table above by hand, bar by bar. A clean check does
   not prove the music survived: A/B the result against the master for melody, bass at changes
   and form.

10. **Deliver and report.** Write it in the format the base skill uses (ABC with two voices, one
    per staff, is the easiest to write and ScoreStarling reads it directly; MusicXML for a file).
    Save it as a new score titled in plain words with the song, the
    level and the key, e.g. "Clementine — Easy piano (about Grade 1), C major", in the user's
    language. Tell the user in a few lines: the key (and that it moved, if it did), what changed
    in each hand, anything left out, the one or two spots that may still be hard, and one next
    step (the original key, a Grade 2 version, jianpu, or listening to it).

## When the source is already close

If the check says the source is about Grade 1 already, say so and change only what is over the
line; do not rewrite a good easy piece. If the user's learner is below Grade 1 (Initial, a few
months), offer the five-finger version instead: both hands in one position, hands mostly taking
turns, quarters and halves only.
