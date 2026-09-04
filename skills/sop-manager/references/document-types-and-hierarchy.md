# Document types and hierarchy

Choose the smallest document type that matches the work. Preserve one clear primary parent.

```text
Policy or guardrail
  -> Core Process
       -> SOP
            -> Work Instruction, Checklist, Template, Script, Example, Video, or Reference
                 -> Record of completion
```

The plugin creates Core Process, SOP, Work Instruction, and Checklist drafts. Policies and records provide context but require separate authority and controls.

## Core Process

Answers: What are the major stages of an end-to-end business outcome?

Use it for work spanning roles or teams at a high level. It normally has one accountable owner, a trigger, approximately 5 to 15 outcome-led stages, major handoffs, and an objective end state. Keep button clicks, scripts, screenshots, and detailed exceptions in child documents.

## SOP

Answers: How is one repeatable workflow performed and controlled?

Use it when the source establishes a trigger, role-owned ordered steps, decisions, exception paths, outputs, completion evidence, escalation, and definition of done. Every SOP should identify one primary Core Process. Each step should retain its action, responsible role, completion condition, handoff, and supported controls.

## Work Instruction

Answers: Exactly how is one task completed?

Use it for system navigation, exact interface labels, field-entry rules, scripts, screenshots, decision branches, prohibited actions, and task-level acceptance checks. Identify the parent SOP step. A screenshot can support an instruction but should not be the only source for a critical rule.

## Checklist

Answers: What must be completed or verified at one task or gate?

Use it for a concise execution or verification list. Identify the performer, trigger, whether order matters, completion criteria, exception route, and parent SOP step.

## Child-document decision

Keep an ordinary step inside its parent. Recommend a child when the step contains numerous substeps, exact system navigation, screenshots, approved scripts, meaningful branches, specialized training, substantial resources, or details that change more frequently than the parent.

The parent still states the action, role, completion condition, and handoff. Never invent a child title or link. If the need is supported but no child exists, list only the proposed document type and reason under `Potential child document needed`.

## Multiple levels in one source

When a source contains both high-level stages and task-level mechanics, identify separate candidate documents. Do not combine a Core Process and Work Instruction into one oversized SOP. Ask which candidate the user wants first and preserve the relationships for later drafts.
