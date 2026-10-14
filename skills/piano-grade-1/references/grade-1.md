# About Grade 1: the profile, its sources and worked moves

Read before the first Grade 1 arrangement in a conversation. Everything here is our summary, in
our own words, of public syllabus documents and published Grade 1 pieces; ABRSM's own documents
are the authority, and they change every two years.

## Contents

- Where the profile comes from
- The profile, axis by axis
- Neighbouring levels
- Worked moves (source pattern → Grade 1 version)
- Self-check by hand

## Where the profile comes from

- **ABRSM Piano Practical Grades syllabus 2025 & 2026, sight-reading parameters** (pages 15–16).
  The table adds elements grade by grade and they carry upwards. Up to Grade 1: keys C, G, F major
  and A, D minor; 2/4, 3/4, 4/4; any five-finger position; dotted halves, eighths and rests;
  slurs, accents, staccato; p, mp, mf, f and hairpins; occasional accidentals in minor keys. Grade 2
  adds D major, E and G minor, hands together, dotted quarter + eighth, ties. Grade 3 adds
  positions outside five fingers, two-note chords in either hand and simple sixteenth patterns.
  Sight-reading tests sit below the level of the pieces at the same grade.
  <https://www.abrsm.org/sites/default/files/2024-06/Piano%202025%20&%202026%20Prac%20syllabus%2020240524_access.pdf>
- **Grade 1 scales** in the same syllabus: C major hands together; G, F major and A, D minor hands
  separately. These are the keys a Grade 1 hand knows.
- **Published Grade 1 pieces** (2025–26 lists, e.g. Köhler's Melody in F with broken-chord left
  hand, Handel's Fireworks Minuet arranged with shifting positions, a folk song with the melody
  passing to the left hand, film and pop arrangements): pieces play hands together, the left hand
  is mostly single notes or simple broken chords in quarters, hand positions move a few times per
  piece, dotted rhythms and ties appear, pedal is at most optional.

So the profile is pitched at Grade 1 *pieces*: a little above the Grade 1 sight-reading line,
around the Grade 2 sight-reading line for rhythm (dotted quarter, ties) and hands together.

## The profile, axis by axis

| Axis | Comfortable | Occasional | Above Grade 1 |
| --- | --- | --- | --- |
| Key signature | 0 or 1 accidental | — | 2 or more (D major is Grade 2) |
| Accidentals | Raised 7th in minor | A chromatic passing note or two per piece | Many, or chromatic lines |
| Meter | 2/4, 3/4, 4/4 | Plain 6/8, 3/8 | Changing meters, 5/4, 7/8 |
| Values | 𝅝 𝅗𝅥. 𝅗𝅥 ♩ ♫ and rests | ♩. ♪, ties | ♬ sixteenths, triplets, dotted eighths, grace notes |
| RH texture | Single melody line | Two-note interval at a cadence | Chords of three, two voices in one hand |
| LH texture | Single notes, quarters or slower | Two-note fifth/sixth; a bar of eighths | Chords of three, Alberti in eighths, wide arpeggios |
| Span in one hand | Within a fifth | Sixth | Seventh, octave |
| Leaps in a line | Steps, thirds, fourths, fifths | Sixth to octave, prepared | Over an octave between connected notes (a new phrase after a rest or long note may start anywhere) |
| Range | RH ~C4–G5, LH ~C3–C4 | One ledger line | Clef changes, 8va, two ledger lines |
| Hand positions | Five-finger, a move per phrase | A few moves per 8 bars | Constant moves, crossing |
| Hands together | One hand moves while the other holds | Both in quarters | Both in eighths for long |
| Tempo | ♩ = 60–112 | Up to ~132 | Faster |
| Pedal | None | Optional | Required |
| Length | 8–40 bars (about a minute) | Longer song form with repeats | — |

`scripts/grade1_check.py` measures these axes with the same thresholds.

## Neighbouring levels

- **Initial / pre-grade:** five-finger position per hand, hands mostly separate, quarters and
  halves, C major or D minor. Offer it when the learner has played for only a few months.
- **Grade 2:** D major, E and G minor; hands together throughout; dotted quarter + eighth, ties;
  a bit more left-hand movement. The natural "next version".
- **Grade 3:** positions outside five fingers, two-note chords in either hand, simple sixteenth
  patterns, B♭ and E♭ major.

## Worked moves

Made-up examples, written as bar contents.

- **Sixteenth arpeggios (Bach-prelude style), one chord per bar** → RH: the chord's top notes as a
  slow melody, e.g. `E4 half, F4 half` or the figure's top note per beat in quarters; LH: the bass
  as a whole note. Or double values: a bar of 16ths becomes two bars of eighths, kept to one
  five-finger shape.
- **Alberti bass in eighths (C–G–E–G)** → LH quarters C3–G3 (1-5) or a whole-note C3; never Alberti
  in eighths at Grade 1.
- **Pop LH broken chords 1-5-8-10 in eighths** → LH half notes root then fifth, or a whole-note
  root; in the chorus quarters 1-5-1-5 within a fifth.
- **RH melody in octaves or with chord tones under it** → the top note only.
- **Melody jumping an octave for the chorus** → keep it in the same octave as the verse, or move
  the whole phrase, never half a phrase.
- **Syncopated melody (pushed an eighth early)** → put the note on the beat, except the one
  signature push of the hook, written as eighth–quarter–eighth.
- **Triplet melody** → two eighths, or quarter + eighth pair, keeping the first note on the beat.
- **Six flats (G♭ major)** → down a tritone to C, or up a semitone to G; pick the one that keeps the
  melody around C4–G5.
- **Waltz LH bass + two chords (oom-pah-pah)** → dotted-half bass, or bass on 1 and a two-note
  fifth on 2 held to the end of the bar.

## Self-check by hand

Go bar by bar and answer: Is any value shorter than an eighth? Does any hand have three notes at
once? Does the LH have eighths for more than a bar at a time? Is any jump wider than an octave?
Is any stretch wider than a sixth? Does any note need two ledger lines? Does the signature have
more than one accidental? Then sing the RH: is it still the tune? Play RH + LH bass: are the
chords still heard?
