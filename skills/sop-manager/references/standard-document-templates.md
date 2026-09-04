# Standard document templates

Use the lean base below. State each idea once and omit non-applicable conditional fields instead of filling the draft with placeholders.

```text
<DOCUMENT TITLE>

Document type: <Core Process | SOP | Work Instruction | Checklist>
Status: Draft: Human Review Required
Process owner: <role or TBD: confirm with process owner>
Primary parent: <supported parent or TBD>
Compliance review: <Not indicated | Needed: human determination required>

CONTROL METADATA: INCLUDE ONLY WHEN CONFIRMED OR NEEDED
Document ID | Version | Effective date | Approver | Last reviewed | Next review

PURPOSE
<Why the document exists and the desired outcome>

SYSTEMS AND ACCESS: INCLUDE WHEN NEEDED
<Systems, permissions, inputs, and prerequisites>

<STAGES | PROCEDURE | INSTRUCTIONS | CHECKLIST>
1. <ACTION-ORIENTED TITLE> [<RESPONSIBLE ROLE>]
   Task breakdown: <only for multi-action work>
   Done when: <meaningful supported completion condition>
   Handoff: <when responsibility changes>
   Decision / exception: <when a branch or control exists>
   Existing resources: <only when evidenced>
   Existing child document: <only when evidenced>
   Visual: <only for screenshot-dependent work>

DEFINITION OF DONE
<Objective completion criteria>

RELATED DOCUMENTS
<Existing linked documents or No related document is linked yet>

EXCEPTIONS AND ESCALATION: INCLUDE WHEN SUPPORTED
<Failure condition, escalation role, and corrective path>

QUESTIONS FOR APPROVER
<No more than five high-impact questions>

REVISION AND APPROVAL
Revision summary: <what was created or changed>
Approval record: Pending human review
```

## Core Process rendering

- Use `STAGES` as the main section.
- Use approximately 5 to 15 outcome-led stages.
- Show major ownership changes and handoffs.
- Keep execution mechanics in linked SOPs or Work Instructions.

## SOP rendering

- Use `PROCEDURE` as the main section.
- Lead each step with a concise action title.
- Show the responsible role after the title when supported.
- Keep simple steps self-contained.
- Include expected result, decision, exception, control, handoff, or completion evidence only when supported.

## Work Instruction rendering

- Use `INSTRUCTIONS` as the main section.
- Preserve exact interface labels and supported warnings.
- Use visual slots with subject, placement, and `Redaction required: Yes`.
- End with a task-level acceptance check.

## Checklist rendering

- Use `CHECKLIST` as the main section.
- Use short verb-led or verification items.
- State whether order matters.
- End with completion and exception gates.

## Conditional modules

Add only when relevant and supported: timing or service levels; definitions; troubleshooting; quality checks or KPIs; RACI or cross-team handoffs; training; vendor dependency; fallback procedure; data classification; access restrictions; automation opportunities; upstream or downstream impact; and compliance-controlled fields.

## Compliance review module

Place this in Audit View when review appears necessary:

```text
COMPLIANCE REVIEW: HUMAN DETERMINATION REQUIRED
Apparent risk or prohibited outcome: <observed or TBD>
Preventive control: <observed or TBD>
Verification evidence: <observed or TBD>
Exception or corrective action: <observed or TBD>
Required record: <observed or TBD>
Retention rule: <observed or TBD; never invent>
Compliance reviewer: <role or TBD>
Approval evidence: Pending
```

This routes human review. It does not make a legal or compliance determination.
