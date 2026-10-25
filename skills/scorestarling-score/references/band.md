# A band transcription: instruments, rhythm, results and recovery

Read this before sending a band recording (`provider: mirelo`), when a band job waits for its
instruments, when it fails, or when the user wants a new score from a saved band result. Its
price, and the one question that goes with it, are the host's: in a chat app, "A band's price" in
step 4 of [chat-hosts.md](chat-hosts.md); in ScoreStarling's own app, the app's instructions.

## Before sending

- A band is for several instruments or drums, and it is chosen with the user.
- If a band is unavailable, read `get_account_usage.engine_status.mirelo.reason` when it is
  given. Do not assume the account lacks permission or that the service stops at two minutes.

## Steps

1. **Send** the recording with `provider: mirelo`, leaving `review_instruments` on (its default),
   and follow the job (in a chat app, steps 2 to 4 of [chat-hosts.md](chat-hosts.md)). It then
   reports `needs_review` while its instrument review is pending: stop polling the status and
   follow its `next_step`.
2. **Instruments.** Read `get_pro_instrument_review(start=false)` first. For a new upload, call
   it with `start=true` to request free instrument suggestions; this never starts the paid
   transcription. If the suggestions are not ready, the review says when to read it again.
   - Check every suggestion against the facts the user gave, any written source and what the
     recording lets you establish. You usually cannot hear the file yourself, so a list is
     grounded when the user's own description (or a written source) names the instruments and
     the suggestions agree with it. Preselected suggestions are not a complete list.
   - Confirm with `confirm_pro_instruments`: a complete list you can ground (a missing
     instrument cannot appear in the score, and a wrong one takes notes that belong elsewhere),
     or `instruments: null` for automatic parts when you cannot ground one. Automatic parts need
     no separate approval: say so in the price question. Do not make the user list the
     instruments.
   - Describe the instruments clearly heard, and those possibly heard, in plain words, never
     with agreement figures. A possibly heard instrument you left out goes into the price
     question, so the user can add it (then confirm again and quote again).
   - Rhythm choices go in `pro_options` in the same call, only as the user stated them or the
     source establishes them: `time_signature` for a known 6/8, 9/8 or 12/8 (an omitted meter
     becomes N/4; compound meters are not detected), and `tempo: "fixed"` with `bpm` only when
     the user wants one constant tempo (otherwise the tempo follows the playing; a `bpm` given
     with the upload also means a fixed tempo). Never guess an unknown meter or tempo; leave it
     out and, when the meter is unknown, add one clause to the price question that a 6/8 or 12/8
     feel is used only if they say so. Ask only about a consequential ambiguity the source
     cannot settle.
   - Do not poll or transcribe again while the review is pending. If the user stops,
     `cancel_transcription` releases its reservation.
3. **The price** comes next, with the plan you confirmed: in a chat app, "A band's price" in step 4
   of [chat-hosts.md](chat-hosts.md); in ScoreStarling's own app, the app's instructions.
4. **Follow** the same job, then review the completed score ([review.md](review.md)).

## If the user declines

- While the instruments or the price are pending, `cancel_transcription` cancels the task and
  releases its reservation. Nothing was charged; say so.
- For another choice instead (one instrument or voice, solo piano), start it as a new job from
  the same attachment or link, with that `provider`. `transcribe_music` with a `score_id` needs a
  finished or stopped score.
- Transcribing the same recording again as a band is a new task with its own price.

## After it completes

- Report the time signature and tempo from `provider_output.rhythm`, with their sources and
  warnings, in plain words.
- A band score transcribed with credits shows whole; its price is the only credits it needs.
  Downloads follow the account, as for any score ([delivery.md](delivery.md)).
- The band's notation, detection and original exports are the starting point: reuse them before
  inventing other processing, keep the original and revisions reversible, and keep what the
  service wrote apart from what you changed. Its provenance alone does not make it accurate:
  review it like any transcription ([review.md](review.md)). Listening (`review_score` with
  `check=listen`) hears the band's mix: pass `part` to check one part, such as the bass against the piano's left hand (see
  [review-tools.md](review-tools.md)).
- `provider_output.musicxml_optimized` is true only when the service reports an optimized file;
  absent or false means not optimized.
- The original engraving (`original_pdf`, the full score unless one part or tab is selected,
  with its tuning source; `original_scores`, a ZIP) shows the unedited result only. Give it only
  when the user asks for the original, call it the original, and do not present it as final
  quality.
- A guitar TAB in the originals can read an octave high (seen once): the guitar part is written an
  octave above its sound and fretted by its written pitch. Say so when you hand it over. For TAB of
  the current score, show it with `set_tablature` instead: ScoreStarling frets the pitch that sounds.

## Failures and recovery

- When `can_recover` is true, call `recover_pro_result` with the original `job_id` and follow
  the same job again. It resumes the accepted task or its saved result without a new
  transcription or reservation.
- An unknown submission stays held for manual review. Never create a replacement to recover it.
- After an ambiguous answer, inspect the same job; never start another upload or paid job, and
  retry nothing blindly.
- Say whether credits were used, refunded, held or not yet confirmed only from the tools'
  evidence; never claim zero from a failed status alone.
- Progress and the provisional note count can change, even at 96%. Review and export only the
  completed score.

## Saved results (enabled accounts only)

Only when the user explicitly wants a new score from a saved band result. The user never needs
to name internal options; explain it in ordinary words as reusing a saved result.

1. Use the original recording or `transcribe_music` with its `score_id`, with `provider: mirelo`, instrument review
   on and `replay_only: true` set when the job is created, before the first review.
2. Read `get_pro_instrument_review(start=false)` first. Its `replay_candidates` already verify
   this account, the original bytes and the decoded length. Compare every saved instrument and
   every flat `pro_options` value (tempo, meter, subdivision, timing and paper) with the
   requested choices; saved choices take precedence. Different choices need a different saved
   result. Even `start=true` stays cache-only for these jobs.
3. No matching candidate: stop and offer to open the existing score. Never start detection,
   fresh processing, a replacement or another upload, and never change the saved request.
4. Confirm the matching choices with `confirm_pro_instruments` and `replay_only: true`, then
   read the review back and check that `pro_review.replay_only` is true.
5. Keep the same excerpt length; a shorter quote needs its own matching saved result, otherwise
   stop. If a price is required, ask once for its exact credits: permission to reuse is not
   consent to pay.
6. Follow the same job and check that the completed result names `replayed_from`.
