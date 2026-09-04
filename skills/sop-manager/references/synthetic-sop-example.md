# Synthetic example: SOP pattern

This fictional example demonstrates structure only. Never reuse its process facts.

## Example source summary

A facilities coordinator receives a room-reset request after an internal workshop. The coordinator removes temporary materials, checks equipment, reports damage, and records completion. The source does not identify the escalation owner or required record location.

## Draft excerpt

```text
RESET A WORKSHOP ROOM

Document type: SOP
Status: Draft: Human Review Required
Process owner: Facilities Coordinator
Primary parent: TBD: confirm with process owner

PURPOSE
Return the workshop room to its standard configuration and identify damage before the next reservation.

PROCEDURE
1. Remove temporary materials [Facilities Coordinator]
   Remove workshop supplies, temporary signs, and waste from the room.
   Done when: Only standard room materials remain.

2. Check room equipment [Facilities Coordinator]
   Confirm the display, cables, and remote are present. Record visible damage without attempting an unsupported repair.

3. Restore the standard layout [Facilities Coordinator]
   Return tables and chairs to the documented room layout.

4. Record completion [Facilities Coordinator]
   Record the reset and any damage in the approved location.
   Done when: The reset is recorded and damage has been routed for review.

DEFINITION OF DONE
The room matches its standard layout, equipment is present, temporary materials are removed, and completion is recorded.

QUESTIONS FOR APPROVER
- Where must completion and damage be recorded?
- Who receives a damage escalation?
```

The missing record location and escalation owner remain questions. They are not invented inside the procedure.
