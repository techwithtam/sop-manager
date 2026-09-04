# Synthetic example: Work Instruction pattern

This fictional example demonstrates exact labels, branching, and acceptance checks. Never reuse its process facts.

```text
UPDATE A TRAINING SESSION STATUS

Document type: Work Instruction
Status: Draft: Human Review Required
Process owner: Training Coordinator
Primary parent: Close a completed training session

SYSTEMS AND ACCESS
Training portal access with permission to edit session records.

INSTRUCTIONS
1. Open the session [Training Coordinator]
   In the training portal, select `Sessions`, then open the session by its confirmed date and title.

2. Select the supported status [Training Coordinator]
   - If the session occurred, select `Completed`.
   - If the organizer cancelled it, select `Cancelled`.
   - Do not select `Completed` when attendance is unresolved.

3. Save and verify the record [Training Coordinator]
   Select `Save`.
   Acceptance check: Reopen the session and confirm that the selected status remains visible.

EXCEPTIONS AND ESCALATION
If attendance is unresolved, leave the current status unchanged and ask the session owner to confirm the outcome.
```

Exact labels and branches appear because the fictional source supplied them. An actual draft must use labels and rules from its own evidence.
