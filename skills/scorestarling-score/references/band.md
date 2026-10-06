# A band transcription: instruments, price, recovery and saved results

Read this before sending a band recording (`provider: mirelo`), when a band job waits for
instruments or a price, when it fails, when the user asks about credits or a short balance, or
when they want a new score from a saved band result.

To the user this is "a band (uses credits)" and its "price", which is always a number of
credits, never money. The service behind it is credited only by the short line "Powered by
Mirelo", added as written when you ask the user to agree to a price, and nowhere else. Never
show the service's own credits or limits, and never ask for a credit cap: the server sets each
task's limit from the length it may transcribe.

## Before sending

- A band is for several instruments or drums, and it is chosen with the user. When they asked
  for the band, the whole song or a full score, that is the choice; when only the recommendation
  suggests it, ask first in one line that it uses credits and that the price comes before
  anything starts.
- It is the only choice that uses credits: 40 a minute of the account's existing credits. One
  instrument or voice and solo piano are free.
- Read `get_account_usage`. If the account has prices and no credits available for a band, say
  so before sending and offer the free choices instead.
- The excerpt is the shorter of the length limit and what the balance covers. The length limit
  is five minutes for invited accounts and accounts holding purchased credits, otherwise two;
  `check_recording`, `get_account_usage` (`max_seconds`) and the upload result (`max_seconds`,
  `excerpt`) give it. Tell the user before it starts when the recording is longer.
- If a band is unavailable, read `get_account_usage.engine_status.mirelo.reason` when it is
  given. Do not assume the account lacks permission or that the service stops at two minutes.
- Mention cost only for a band, or when `get_account_usage` shows a limit. Estimates are not
  billing receipts.

## Steps

1. **Send** the recording as in steps 2 and 3 of SKILL.md with `provider: mirelo`, leaving
   `review_instruments` on (its default), and follow the job. It then reports `needs_review`
   while its instrument review is pending: stop polling the status and follow its `next_step`.
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
     `cancel_pro_review` releases its reservation.
3. **Price.** When `get_upload_status` reports `product_quote.phase=pending`, call
   `get_transcription_quote` with the `job_id`: it gives the exact credits for the decoded
   length and the complete choices you confirmed. Ask once, in the user's language: the length
   it covers, the exact credits as use of credits the account already has (not a purchase), and
   the plan (the instruments or automatic parts, and any rhythm choice), then "Powered by
   Mirelo". For example (made up): "A band score of the first 3:00 (piano, bass and drums) uses
   120 of your credits. Shall I start? Powered by Mirelo."
   - Only after the user's explicit yes, call `confirm_transcription_quote` with the unchanged
     `quote_id` and credits and `consent: true`.
   - Until then the user may still change the choices: confirm again and quote again, and ask
     again for the new price. An expired price or changed input needs a fresh quote. An upload's
     estimate is not consent.
   - Nothing is transcribed or reserved before the yes.
   - An account without prices gets one question about starting instead of the price.
4. **Follow** the same job (SKILL.md step 4), then review the completed score (step 5).

## A short or empty balance

When the balance does not cover the whole excerpt, the quote's `affordable` is the longest
excerpt from the start that it does cover. Offer it rather than stopping, as the one price
question: call `get_transcription_quote` again with `seconds` set to that length (free; nothing
is reserved), then ask with that quote's exact credits, saying what the whole recording would
need and what is left out. For example (made up): "The whole 3:30 needs 140 credits and you have
100. Those cover the first 2:30 (vocals, guitar, bass and drums) for 100 credits; the last
     minute is left out. Shall I start the first 2:30? Powered by Mirelo." A yes to that exact
     offer is the consent for that quote; another length needs a new quote and a new question.

If no excerpt is covered, explain that a band transcription is not available now; opening
existing scores, sheet music and score files, editing and downloads all still are, and so are
the free choices.

Never offer credit purchases, subscriptions, upgrades, top-ups or checkout links, even when the
user asks to buy, and never show money prices, plans or packs. In reply to a request to buy, say
that purchases are not available here, with no link. If asked how credits work,
https://scorestarling.com/credits documents them neutrally; it is not a way to get more credits.

## If the user declines

- While instruments are pending, `cancel_pro_review` releases the reservation; while the price
  is pending, `cancel_transcription_quote` cancels it. Nothing was charged; say so.
- For a free choice instead (one instrument or voice, solo piano), start it as a new job from
  the same attachment or link, with that `provider`. `transcribe_again` works only from a
  completed score.
- Transcribing the same recording again as a band is a new task with its own price.

## After it completes

- Report the time signature and tempo from `provider_output.rhythm`, with their sources and
  warnings, in plain words.
- The band's notation, detection and original exports are the starting point: reuse them before
  inventing other processing, keep the original and revisions reversible, and keep what the
  service wrote apart from what you changed. Its provenance alone does not make it accurate:
  review it like any transcription (SKILL.md step 5). `listen_score` does not work for scores
  with several parts.
- `provider_output.musicxml_optimized` is true only when the service reports an optimized file;
  absent or false means not optimized.
- The original engraving (`original_pdf`, the full score unless one part or tab is selected,
  with its tuning source; `original_scores`, a ZIP) shows the unedited result only. Give it only
  when the user asks for the original, call it the original, and do not present it as final
  quality.

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

1. Use the original recording or `transcribe_again`, with `provider: mirelo`, instrument review
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
