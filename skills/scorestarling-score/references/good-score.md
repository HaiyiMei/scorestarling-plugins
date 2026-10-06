# What this piece is, and what a good score of it looks like

Read this once in a conversation before judging a transcription (step 5 of SKILL.md), and come
back to an entry when a passage raises its question. It is musical judgment, not a list of tool
calls: [review-tools.md](review-tools.md) explains the tools' evidence, and
[editing.md](editing.md) the operations.

The service's output is a starting point; the goal is accurate, clear, playable notation that a
person has reviewed. Musical conventions suggest explanations to test; they never establish what
a particular recording contains. The user's source, the edition they want and their feedback
come first. For a score read from sheet music, the written source is the evidence instead of the
recording. Every example here is made up.

Keep four things apart: performance events (attacks, releases, pedal and microtiming), musical
structure (beat, phrase, harmony and voices), notation, and an arrangement the user asked for.
Compare full phrases and repeated sections, not isolated note density, and keep plausible
alternatives when the evidence is uncertain.

## First: what is this recording, and what does the user want?

Faithful means faithful to the player on this recording, so decide what the recording is before
judging any passage:

- **An original piano piece, or a pianist's own performance:** the score is what the pianist
  played.
- **Someone's piano cover of a song** (common on Bilibili and YouTube): the cover's notes, not
  the original song's. Many covers of one song are equally valid, so never correct a cover
  toward the record or toward another cover ([Pop2Piano](https://arxiv.org/abs/2211.00895)
  models many arranger styles for one song).
- **A band or produced track:** no single piano part exists. The band choice writes each
  instrument's part; any piano version is an arrangement.
- **A voice or one melodic instrument:** the melody. Chords or an accompaniment are additions.
- **A guitar, alone or with a voice:** the guitar's part in guitar notation (a treble clef
  sounding an octave lower, melody stems up and bass stems down, tablature optional); a piano
  version is an arrangement ([guitar octave clef](https://musescore.org/en/node/330700)).
- **An orchestra, a film cue or a choir:** the parts; a piano version is a reduction.

Then decide what the user wants. A note-for-note score (还原版, 扒谱, "exactly as played", 原谱) is the
faithful transcription with every note of both hands, delivered first. A lead sheet, an easier
version, a piano version of a band, 弹唱 or two-hand jianpu are arrangements: separate, named
scores made on request, after it ([arranging.md](arranging.md); [Sheet Music Direct, arrangement
types](https://blog.sheetmusicdirect.com/2018/09/piano-arrangements-explained.html)). The
faithful transcription stays the master: never edit it toward an arrangement, and never
"correct" it toward a familiar pattern. This is the old distinction between descriptive and
prescriptive notation ([Seeger, 1958](https://academic.oup.com/mq/issue/XLIV/2)).

## What a texture tells you to check

Recognizing a texture tells you where to look and which regularity to test; it never tells you
what to write, and when the recording disagrees, the recording wins. Describe each section's
texture to yourself in a few words, layer by layer from the top (made up: "verse: tune in the
right hand over broken chords in eighths; chorus: tune in octaves over octave bass and chords";
[Couturier et al., 2022](https://archives.ismir.net/ismir2022/paper/000061.pdf)), then test what
that texture predicts:

- **A steady accompaniment figure** (broken chords, an Alberti bass, a rocking 6/8 figure, a
  stride or boogie left hand): every bar of the passage should carry the figure's attacks. A gap
  is a lead for a missed note; a figure that changes at a cadence or a new section can be real
  ([Hutchinson, accompanimental
  textures](https://musictheory.pugetsound.edu/mt21c/AccompanimentalTexture.html)).
- **A bass at each chord change:** the bass should arrive with each change of harmony, which pop
  songs often anticipate by an eighth.
- **Block chords and pads:** the chord's notes should start together on the texture's rhythm;
  spread attacks may be a rolled chord, and a missing third changes the chord.
- **A tune with returning phrases:** each return should start on the same beat with the same
  rhythm, unless the music clearly varies it ("Returning phrases" below).
- **Independent voices** (a chorale, a fugue, a choir): each voice should continue with its own
  entries, rests and held notes. A choir is written with soprano and alto on the treble staff
  and tenor and bass on the bass staff, stems up and down ([OMT,
  SATB](https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_(Gotham_et_al.)/01%3A_Fundamentals/1.19%3A_Roman_Numerals_and_SATB_Chord_Construction)).
- **Swing:** long-short pairs across many beats, written as straight eighths with a swing mark;
  real triplets stay triplets.
- **Compound meter:** whole sections dividing every beat in three, with the bass on dotted
  quarters, suggest 6/8 or 12/8 rather than 4/4 full of triplets; a few triplets in 4/4 do not
  ([OMT, compound
  meter](https://viva.pressbooks.pub/openmusictheory/chapter/compound-meters-and-time-signatures/)).
- **A waltz:** one strong beat in three, the bass on beat 1. A hemiola (two groups of three
  across bars) is real and keeps its bar lines.
- **Latin grooves:** [bossa nova](https://en.wikipedia.org/wiki/Bossa_nova) is not swung and is
  often written in 2/4; a [montuno](https://en.wikipedia.org/wiki/Guajeo) lines up with its
  clave (2-3 or 3-2), so flag the clave's direction rather than guess it.
- **A band:** drums belong to their own part; a backbeat on 2 and 4 is evidence for the beat
  level.

Texture often changes by section (a fuller chorus, octaves, a new figure): compare a passage
with its own section's returns. In a transcription the tune can sit in the left hand or an inner
voice, and the top note is not necessarily the tune: a cover's chorus often doubles the tune in
octaves or puts octave hits above it, so follow the verse's contour and register ([OMT, popular
music](https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_(Gotham_et_al.)/07%3A_Popular_Music)).

## Explanations for a passage

Each entry gives the evidence that supports it, what contradicts it, the supported action and
how to verify. None is a default for every piece: a pop ballad, a chorale, a fugue and a stride
left hand are written differently. Most pieces need at least "Returning phrases", "Beat level,
meter and pickup", "Broken chords and repeated patterns", "Hands, voices and staves" and "The
page". Notation-only fixes are made directly; note changes are applied when the user asked for
corrections and otherwise proposed as a preview (SKILL.md step 5).

1. **Melody and accompaniment.** Look for a recurring melody and harmony pattern heard across a
   phrase. An eighth-note left-hand accompaniment under a right-hand melody is one example, not
   a default: block chords, syncopation, a left-hand melody and changes of texture are
   counterexamples. Consider supported voice and staff layout, clef and beam changes; replacing
   an accompaniment pattern is an arrangement. Verify the actual rhythm, melody and fills,
   including section changes.

2. **Independent voices.** Look for separate melodic continuations, entries and releases.
   Simultaneous chord tones alone do not establish independent voices, and crossing voices do
   not exchange their identities. Two voices per staff is not a musical maximum: treat
   `reengrave` `voices` as a candidate, not permission to lose an inner line. Check each line's
   continuity, rests and held notes, and reassign voices in the edited MusicXML copy
   ([counterpoint](https://musictheory.pugetsound.edu/mt21c/SpeciesCounterpoint.html)).

3. **Hands, voices and staves.** In overlapping registers or cross-staff figures, judge
   continuity, reach and the time available between attacks. Middle C is not a hand boundary,
   and the treble staff does not mean the right hand. In melody and accompaniment, assign by
   role, not pitch: the melody is usually the right hand's, and broken accompaniment chords that
   climb above middle C (to E♭4, say) stay in the left hand. When each hand plays one note per
   eighth and one hand already has its agreed note on an eighth, an extra note on that same
   eighth belongs to the other hand, whatever a pitch split says. The audio may not settle which
   hand plays what. Move notes between staves in the edited MusicXML copy, never by repitching
   to imitate a staff move. Verify the sounding pitches and a playable allocation, and present
   uncertain hand choices as a proposed fingering ([keyboard
   notation](https://lilypond.org/doc/v2.24/Documentation/notation/common-notation-for-keyboards)).

4. **Broken chords and repeated patterns.** Hear several cycles before assuming a pattern. An
   ascending arpeggio is not necessarily an Alberti bass, and a cadence can genuinely vary a
   repeated figure. `rebeam` may clarify grouping; `fill_rest`, `add_chord_tone` or `set_pitch`
   belong only at source-supported places. Check the attack order, real variants and harmonic
   changes, and never fill notes from a generic template. Once the user or the recording
   confirms a single-note broken-chord texture (one note per hand per eighth, no dyads), a note
   only one transcription hears beside the figure is usually an echo or an octave or harmonic
   ghost, however clear its attack looks. When deciding which notes to keep or add, prefer notes
   both transcriptions agree on (the score and `listen_score`'s second engine), then the bar's
   own pattern. A gap in a steady eighth figure is usually a missed attack, not a rest: propose
   filling it from the bar's own pattern (preferring the same half bar, since the harmony often
   changes mid-bar), first where `listen_score` heard a note, and mark positions where nothing
   was heard as less certain. A bar holding only its bass is one held note, not a bass plus
   stray eighths ([arpeggiated
   accompaniments](https://musictheory.pugetsound.edu/mt21c/ArpeggiatedAccompaniments.html)).

5. **Swing and syncopation.** Compare long-short timing over several beats, and check straight
   sections and real tuplets. Jazz does not always swing, and swing is not a fixed triplet
   ratio. Keep offbeat attacks. `rebeam` changes grouping only, and a global grid cannot express
   every swing or tuplet passage; swing marks and tuplets are written in the edited MusicXML
   copy. Verify a readable beat grouping and the retained performance timing rather than pushing
   attacks onto strong beats ([swing
   rhythms](https://viva.pressbooks.pub/openmusictheory/chapter/swing-rhythms/)).

6. **Rubato and rolled chords.** Follow phrase-level slowing and recovery, and sequential
   attacks; tell a flexible pulse from a free passage. Rubato does not imply a new meter. A
   section's first note is often held long and phrase ends are held freely: keep the parallel
   phrase's bars and let the tempo map take the extra time, rather than inserting or dropping
   beats. An even grid spreads a slowed repeat ending's few attacks across the bar: when they
   sit further apart than the grid's notes, copy the parallel bar's rhythm. Rolled chords need
   not become tiny notes and rests, or simultaneous attacks. Inspect a supported quantization
   preview against the original. Nothing edits the local tempo map or free rhythm; an arpeggio
   sign goes in the edited copy, and a held phrase end can carry a printed fermata (`add_mark`),
   which does not change playback. Verify phrase timing and attack order; changing the whole
   tempo is no substitute for local timing corrections ([played and notated
   durations](https://www.steinberg.help/r/dorico-se/6.2/en/dorico/topics/key_editor/key_editor_notes_duration_played_notated_c.html)).

7. **Short notes and apparent false detections.** Check for an audible attack, the pitch,
   repeated passages and an A/B of the original against the score's playback. A short or quiet
   note can be a real ornament or a musical ghost note rather than a model error; confidence
   only decides what to inspect first, and confidence from one model must not be borrowed for
   another. Delete or repitch specific notes only with evidence; keep uncertain notes or propose
   alternatives. Verify that real ornaments survive: a lower note count is not evidence of
   correctness ([Basic Pitch outputs](https://github.com/spotify/basic-pitch)).

8. **Pedal, key release and decay.** Check pedal events, repeated attacks and harmony changes.
   Acoustic decay, key release and notated duration are different quantities; an overlap alone
   proves neither a held voice nor an unwanted note. `set_duration` changes the played note-off
   too, so never present it as notation-only cleanup; a written length changed in the edited
   MusicXML copy keeps the played timing, and pedal marks are written there as well. Verify
   repeated attacks and held voices both in playback and on the page ([piano transcription
   model](https://arxiv.org/abs/2010.01815)).

9. **Beat level, meter and pickup.** Compare accents, the bass and harmony, and phrase
   boundaries across phrases. Syncopation, anticipation and hemiola can contradict a beat-one
   guess; an opening rest can be real, and an underfull first bar is not automatically a pickup.
   No universal tie-per-note or sixteenth-note ratio decides correctness. Use
   `scale_note_values` for an evidenced half or double reading of the whole score, `set_meter`
   for the grouping and `rebar_pickup` for a confirmed pickup length. Re-read IDs, then verify
   the timing, the first downbeat and later bars ([rhythmic
   notation](https://musictheory.pugetsound.edu/mt21c/CommonRhythmicNotationErrors.html)).

10. **Returning phrases.** A returning phrase (a repeated verse, the tune an octave higher)
    usually keeps its rhythm. Line the occurrences up and count the accompaniment's steady pulse
    between melody notes: when one sits half a beat or a beat off and its bars run unusually
    short or long, the beat grid drifted, not the player, so write it like the others. Keep the
    differences the pulse confirms or that change pitch (fills, pickups, a slowed final
    cadence). Aligning can also put every occurrence on the wrong beat (say, three returns
    written two beats late in a section that starts on beat 1): count the accompaniment's own
    pulse from its first attack to place the section's first note, and match the parallel
    section the user confirmed. When it stays unclear where the pulse stops, make that your one
    question. `rebar_pickup` moves every bar line; a single shifted passage is rewritten in the
    edited MusicXML copy ("A shifted passage" in [editing.md](editing.md)). Verify each
    occurrence's first downbeat and bar lengths by ear.

11. **Key, modulation and jianpu.** Use cadences, the bass, melodic direction and sustained
    tonal centres; fewer accidentals alone cannot decide the spelling, major or minor, or a
    modulation. Accidentals that persist through a section after a new dominant seventh mean a
    new key the signature misses: confirm it from the accidentals that recur and from where that
    dominant resolves. Songs, anime and J-pop songs especially, often change key into the chorus
    (often by a third) or at the last chorus ([Li 2026, anime-song
    modulation](https://www.mtosmt.org/issues/mto.26.32.1/mto.26.32.1.li.html)). `set_key`
    changes the key signature (notation only); `transpose_score` changes pitch. Full `jianpu`
    keeps every staff; `jianpu_melody` takes the top line, which may not carry the melody;
    `jianpu_fixed` writes every staff in 1=C fixed do (固定调), each black key marked. In the key,
    a minor uses its relative major's do: `1=C` with 6 as the tonic. Inspect each staff's
    digits, octave dots, rhythms, key changes and multi-voice output; do not assume the export
    loses nothing ([tonicization and
    modulation](https://musictheory.pugetsound.edu/mt21c/TonicizationVersusModulation.html)).

12. **Learner arrangements.** Use the learner's actual difficulty, comfortable reach, rhythms
    and target tempo. Jianpu does not make the music easier to play, and two beginners can need
    different changes. Keep the faithful master and make a clearly named arrangement as a new
    score within the authorized goal ([arranging.md](arranging.md)). Explain removed or revoiced
    material, and verify the retained melody, important bass and recognizable rhythm through the
    learner's listening or playing.

13. **The page.** Inspect every page the user will read or receive, and every dense passage:
    vertical alignment, rhythmic spacing, beams, rests, accidentals, clefs, continuation ties,
    headings, part labels and page turns. Equal spacing is not the goal. Ledger lines may
    suggest another clef, but frequent clef changes or moved notes can make reading worse. Check
    the instrument's range, transposition and reach instead of declaring an octave-span limit;
    the octave notation of a bass guitar or double bass is not a rule for every bass instrument.
    Use supported clef, beam and heading edits, and never change the music to hide a layout
    defect. Report engraving limits that remain. The [MOLA preparation
    guidelines](https://mola-inc.s3.eu-west-1.amazonaws.com/files/mola3/MOLA-Guidelines-for-Music-Preparation.pdf)
    support performer-oriented preparation and independent proofreading; their orchestral part
    conventions are not universal phone or jianpu layout rules.

14. **Expression marks from the recording.** When the user asks for tempo or dynamics marks,
    read `review_score`'s `expression`. Timing: a phrase end running about a quarter slower
    (stretch about 1.25) is rit., nearer 1.15 poco rit., with a tempo where the next section
    resumes; 1.5 or more is a fermata candidate on that bar's held note. A phrase end's held bar
    often measures short because the player moves on early: read the last two bars together.
    Leave beat-level rubato inside phrases unmarked; a section's long first note is not a
    fermata. When `timing` says the bars follow one fixed tempo, the bars cannot show slowing:
    compare the written rhythms of repeated phrases instead. Dynamics: compare sections'
    `level_db`; about 3 dB between sections is one step (mp to mf), and a steady fall or rise
    over several bars that are not held is a hairpin. Held bars read decay, and levels depend on
    the mix, so propose dynamics as a preview and let the user's ear decide. Apply clear timing
    evidence with `add_mark` when the user asked for marks.

## Keeping a record

For each correction, note the bars and note IDs, what you observed, the evidence for and
against, the change, its effect on playback, how to undo it and what you actually checked. These
notes make the report precise and let the user judge the change by ear.
