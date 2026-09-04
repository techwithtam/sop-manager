# Field, evidence, and review guide

## Evidence statuses

- `Observed`: stated or visibly supported by an identified source.
- `Inferred`: a plausible interpretation that needs confirmation.
- `Missing`: required for safe or complete execution but not supplied.
- `Conflicting`: credible sources disagree or one source contradicts itself.

Every normative instruction must be supported by Observed evidence. Inferred, Missing, and Conflicting items stay outside the clean procedure.

## Atomic extraction

For each material fact capture:

- source ID or short source name;
- speaker or author when known;
- page, timestamp, heading, step, or other location;
- a short exact excerpt or faithful visual observation;
- normalized fact;
- evidence status; and
- affected draft field or step.

Do not infer execution order from conversation order. Do not silently resolve contradictions. Preserve uncertain terminology and offer a marked candidate for confirmation.

## Field meanings

- `Process owner`: one role accountable for the document.
- `Responsible role`: role performing a particular stage or step.
- `Primary parent`: one controlling Core Process or SOP step.
- `Trigger`: event or condition that starts the work.
- `Scope`: included and excluded conditions, people, systems, or cases.
- `Done when`: step-level observable completion condition.
- `Definition of done`: objective completion condition for the whole document.
- `Output or record`: produced item or retained completion evidence.
- `Control`: action that prevents, detects, or corrects an unwanted result.
- `Approver`: authorized human role that accepts the draft outside the plugin.

## Questions for the approver

Ask no more than five questions in Review View. Prioritize missing facts that affect safety, ownership, sequence, completion, controls, exceptions, or approval. Combine related gaps. Do not block a useful draft for low-impact metadata.

Use `TBD: confirm with process owner` only when the field must remain visible. Omit non-applicable fields.

## Compact review note

Report:

- source coverage and any source limitations;
- missing and conflicting information;
- inferences excluded from the clean draft;
- optional improvements kept outside the procedure;
- possible child documents;
- privacy result; and
- compliance-review status.

## Evidence Appendix for Audit View

Use a table with these columns:

| Draft location | Normalized fact | Status | Source | Location | Evidence excerpt | Reviewer decision |
| --- | --- | --- | --- | --- | --- | --- |

Keep excerpts short enough to establish traceability. Redact prohibited data. Never fabricate an excerpt or location. If a source cannot be quoted safely, describe the redacted evidence type and explain the limitation.

## Revision behavior

When the user supplies a correction, treat it as new evidence. Revise only affected fields and steps, preserve unresolved conflicts, and summarize the change. Never overwrite an Approved or Published record. Create a new draft or follow the organization's controlled revision process.
