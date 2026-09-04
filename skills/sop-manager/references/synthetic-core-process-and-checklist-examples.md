# Synthetic examples: Core Process and Checklist patterns

These fictional examples demonstrate document boundaries only. Never reuse their process facts.

## Core Process excerpt

```text
FULFILL AN INTERNAL EQUIPMENT REQUEST

Document type: Core Process
Status: Draft: Human Review Required
Process owner: Operations Manager

STAGES
1. Receive the approved request [Operations Coordinator]
2. Confirm availability and delivery requirements [Operations Coordinator]
3. Prepare the equipment [Equipment Specialist]
4. Transfer custody [Equipment Specialist]
5. Record completion [Operations Coordinator]

DEFINITION OF DONE
The approved equipment is transferred to the requester and custody is recorded.
```

The stages show outcomes and handoffs. Detailed inventory screens and transfer steps belong in child SOPs or Work Instructions.

## Checklist excerpt

```text
VERIFY EQUIPMENT RETURN

Document type: Checklist
Status: Draft: Human Review Required
Process owner: Equipment Specialist
Primary parent: Receive returned equipment
Order matters: Yes

CHECKLIST
- Match the equipment identifier to the custody record.
- Confirm all listed components were returned.
- Record visible damage without including personal information in notes.
- Update the return record.

COMPLETION GATE
The identifier and components match, condition is recorded, and the custody record shows the return.

EXCEPTION GATE
Stop and route discrepancies to the process owner. Do not close the return record.
```
