# Build the SOP review queue

This route is read-only. Use it when the user asks what needs review, approval, owner input, verification, publication, or attention next.

1. Rediscover the verified SOP Library from `SOP Manager Home` and verify its schema against [database-contract.md](database-contract.md).
2. Query metadata for records in `Needs Owner Input`, `Ready for Review`, `Changes Requested`, `Generated Draft`, `Approved`, and `Published`. Do not retrieve page bodies unless the user selects one record for a content review.
3. Prioritize records using explicit evidence in this order:
   - an overdue Next Review date;
   - `Ready for Review` or `Changes Requested`;
   - `Needs Owner Input` or unresolved Open Questions;
   - required Compliance Review that is incomplete;
   - Approved records awaiting publication;
   - `Owner Verification: Unverified` or a missing Verified On date;
   - Generated Draft records with an assigned owner.
4. Within the same priority, put the earliest Next Review date first. When dates are absent or tied, sort by SOP Title and say that no stronger ordering evidence exists.
5. For each queued record, show its title, document type, current status, owner, approver, next review date, reason for inclusion, requested next decision, and clickable Notion link. Label missing values instead of guessing them.
6. If the user names a reviewer or owner, filter only on an exact person-property match. Do not infer identity from page content.

Do not change a status, assign an owner, approve, publish, verify, edit, archive, move, share, or delete a record. A request to act on an item is a separate workflow requiring an exact proposed change and confirmation.
