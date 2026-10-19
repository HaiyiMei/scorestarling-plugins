# Refinement rounds: preserve evidence, reduce repeated work

Use this for substantial corrections within the user's goal, or to audit a frozen result.
Keep the musical judgment in [good-score.md](good-score.md) and operation contracts in
[editing.md](editing.md); this reference explains how to organize the work efficiently.

## Contents

- [Choose a round](#choose-a-round)
- [Use the right editing surface](#use-the-right-editing-surface)
- [Handle added notes and timing](#handle-added-notes-and-timing)
- [Prepare only needed dependencies](#prepare-only-needed-dependencies)
- [Verify three representations](#verify-three-representations)
- [Deliver and audit immutable files](#deliver-and-audit-immutable-files)
- [Measure the next run](#measure-the-next-run)

## Choose a round

Start from the current project/revision, the user's corrections, and source evidence. Keep the
draft and edit the same project. If the user freezes it, restrict work to reads and separate
audit artifacts; report newly found discrepancies without silently fixing them.

Identify the few musical decisions that control the rest: source performance versus arrangement,
phrase boundaries and actual variations, pulse/pickup, voices and hands. Read complete phrases;
use source listening/video evidence at disputed attacks. A texture hypothesis directs checking,
not note generation: never complete a figure solely because the neighboring bars repeat it.
Do not force a melody into the top note, all accompaniment into one rhythmic value, or every
return into identical notation. Preserve real rests, syncopation, inner voices and changes of texture.

Keep a compact change ledger: location, existing ID when available, proposed change, supporting
source span, conflicting evidence and status. Separate confirmed corrections from unresolved
leads. Group changes that share a stable base revision and can be verified together. Make the
round large enough to avoid a save per cosmetic detail, but small enough to isolate a failure.
This is a decision aid, not a mandatory long sequence of tool calls.

Reuse existing provider originals, reviews and local artifacts. A second transcription is an
optional source of independent evidence only when needed and authorized, not a prerequisite or
a response to a slow editing API. Record its original job ID, parameters and result; after an
uncertain paid response, read that job before any retry. Do not equate model agreement with truth.

## Use the right editing surface

Prefer the connected MCP for reads, supported edits, revision ownership and exports. Read the
live operation limits once per relevant capability; cached prose is not a new endpoint. Use
local code only for gaps such as editing a MusicXML copy or comparing returned artifacts.

| Needed change | Choose and verify |
| --- | --- |
| One supported operation, or a supported passage selector | Use `edit_score`; pass the current revision and inspect the returned changes. |
| A passage that came in late or early | One `shift_time` from its first struck note; never note by note. |
| Up to 30 supported note, rhythm, hand/voice, tie, beam or stem edits that belong together | One `edit_score` `batch`: one version, all or none; inspect the returned changes. |
| More than a batch holds, or notation no operation writes | Edit one current `editing_copy`, preserve retained IDs, and save a coherent round with `revise_score`. |
| Only written duration changes | Change MusicXML; retained notes keep their performed timing. Do not promise changed MIDI releases. |
| Played releases | Check `set_duration` limits. A note ID array can represent a contiguous tied note or complete chord, not arbitrary distinct onsets. |
| Unsupported played onset/local tempo changes | Report the gap. Do not invent an action, delete/recreate retained events, or modify storage to imitate support. |

`edit_score`'s `batch` saves several operations as one version, a file revision batches
notation changes no operation writes, and some selectors already handle a passage. Conversely,
an array parameter does not prove independent events can be edited in one call. Estimate the required serial saves before a long
duration loop, explain the expected wait, and reconsider whether notation-only changes suffice
for the user's goal. If releases really must change, preserve starts/pedal and use the supported
operation; do not shorten every note merely to clear validation.

Serialize dependent writes. Use each successful returned revision for the next write, and
re-read IDs/settings when an operation regenerates them or the result is uncertain. Batch
independent reads and immutable exports where the host permits. Do not interleave another
writer with a running edit loop. A rejected save creates no confirmed revision; a timeout has
unknown outcome until the same project/request is inspected.

## Handle added notes and timing

Keep existing note IDs for the same events; allocate new, collision-free IDs for genuinely new
events and tie segments. Never reuse a temporary counter namespace from an earlier generated
file without checking the authoritative current IDs. Count sounding attacks separately from
MusicXML note heads and tie continuations.

Check the current binding/timing behavior before inserting many notes into rewritten bars.
Retained IDs preserve played times, while additions are located from written positions and
retained performance anchors. Changing the printed meter or phrase grid does not necessarily
replace the MIDI tempo map. Nearby retained tie continuations can also refer to an earlier
attack. A same-pitch overlap error may therefore be a placement error, not an extra source note.

Inspect the actual source onset, MIDI ticks/tempo map, same-pitch neighbors and note-offs.
Check new-versus-new as well as new-versus-retained collisions. Do not blindly retry, delete the
new note, erase IDs, or shorten the whole accompaniment to make a save pass. Choose the smallest
supported correction and verify the resulting MIDI against its intended source time.

A temporary timing representation followed by final notation can preserve staged events in a
file revision, but is not a general onset-editing API or a default shortcut. Use such a script
only when the exposed reconciliation behavior is understood, the source times are supported,
retained events stay unchanged, and every inserted event can be checked after saving. Bound
and label intermediate revisions; preserve the draft and inspect the final score before delivery.
If these conditions cannot be established, report the unsupported timing correction. Do not ship
a song-specific staging script as a generic transcriber.

## Prepare only needed dependencies

Inspect the existing runtime before installing anything. Use the project's locked environment
when working in a repository; otherwise isolate authorized missing packages in the task workspace.
Load an XML parser for XML work, a MIDI parser only for performance comparison, and a PDF renderer
only for page proof. Do not bootstrap a server, clone historical projects, download inference
models, or build a test framework to make reversible score edits. Keep task artifacts outside
tracked source and record dependency versions for scripts actually run.

Before a long round, confirm the tools and local readers needed to finish it are usable. Install
only the missing dependency that blocks authorized work. Do not run supplier inference or a paid
model just to verify a script or claim the workflow is faster.

## Verify three representations

**Source and performance.** Check changed attacks against the recording, including soft/repeated
notes and neighboring phrases. Compare retained MIDI pitch, onset, release, velocity and controls
as appropriate to the requested changes. For additions, measure actual exported MIDI onset
error against the chosen source target; this checks the write, not whether the target was right.
Document uncertain source notes and any pedal/articulation approximation.

**Musical structure.** Re-read affected phrases and the complete resulting form, not just a
sample. Check pickup, bar sums, cross-bar ties, voice continuity, hand allocation, repeated-section
variants, coverage and binding completeness. Explain event-count deltas from retained/deleted/
added events; do not use a smaller note count or clean validation as an accuracy score.

**Printed output.** Inspect every exported page, dense passages and page turns. Check accidentals,
not only pitch numbers: MusicXML `pitch/alter` controls pitch, while a renderer may need an explicit
`accidental` to print the sign. A natural pitch against a sharp/flat key signature needs a visible
cancellation unless the current staff/bar state already supplies it. Follow that state through
voices, octaves, key changes and ties; verify the rendered glyph against XML and playback. Do not
patch one visible symbol without checking its musical scope. Check clefs, stems, beams, ties,
expression, clipping and ledger lines. Structural validity does not establish PDF/XML agreement.

Prefer notation layout controls to manual PDF rearrangement. If a delivery-only PDF layout is
necessary, preserve whole vector systems, label its derivation from the saved revision, and check
all resulting pages for clipped high/low notes, accidentals, measure numbers and tie ends. Do not
reuse fixed crop coordinates from another piece, or imply the project's PDF has the same pagination.

## Deliver and audit immutable files

Pin every export to the saved revision the user accepted. Keep a manifest linking project ID,
score revision, format, local byte count/hash, delivery file/version ID and post-delivery hash.
Use the host's actual file tools and any applicable delivery skill; do not invent download links
or treat a local path or prepared panel as proof of receipt. Preserve the original run record
when adding corrections.

When bytes change during delivery, read the pinned delivered file/version back through the
authorized host tool. Compare content before attributing the change to metadata or signing.
For local artifacts, the read-only helper performs the comparison without accounts or networking:

```sh
python3 scripts/compare_artifacts.py BEFORE AFTER
python3 scripts/compare_artifacts.py BEFORE.pdf AFTER.pdf --pdf --require-same-content
```

Resolve the script relative to this skill directory. The basic mode uses only Python's standard
library. PDF mode additionally needs an available PyMuPDF installation; it fails clearly if absent.
It records hashes, whether the original bytes remain a prefix, page geometry, extracted text and
all-page raster equality at 144 dpi. A complete comparison returns zero; `--require-same-content`
returns nonzero for different content. Neither mode establishes musical correctness or verifies
signature trust. Do not call a byte-changing PDF “identical”; distinguish rendered content from
file identity and document any delivery-added signature/provenance data separately.

Record tool/skill provenance at execution time: exact skill URI plus captured content hash or
release commit when exposed, script hash, tool arguments/results with secret URLs and credentials
excluded, source audio hash only when authorized bytes or an authoritative hash are available.
Never substitute a URL hash for an audio hash, a supplier output hash for an input hash, a current
skill snapshot for its historical version, or an application job ID for a supplier request ID.
Mark unavailable evidence as unknown. Keep private case IDs, recording links and customer files
out of a public skill package; store historical cases separately from blind evaluation inputs.

## Measure the next run

Report source accuracy, print readability and playability separately. Preserve the user's
acceptance and any remaining uncertainty; a good-looking PDF is not proof of complete fidelity.
Track wall time, observed provider time, serial saves, rejected requests, dependency setup and
verification time when exposed. Keep provider credits, product credits and model tokens separate;
tool-output token counts are not model billing. Do not fill missing counters with zero.

Treat fewer avoidable exports, coherent bulk revisions and earlier capability checks as proposed
efficiency improvements. Measure them on a fresh authorized piece with the same quality checks
before claiming a speedup. Do not benchmark against a historical case whose answers the agent
has already seen, or spend credits solely to validate the skill.
