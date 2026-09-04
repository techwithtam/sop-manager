# Audit the SOP library

This route is read-only. Use it when the user asks about library health, governance gaps, review readiness, stale SOPs, missing ownership, or documentation coverage.

1. Rediscover `SOP Library` and `SOP Requests` from the verified `SOP Manager Home` page. Verify their schemas against [database-contract.md](database-contract.md).
   Ignore every page or database outside the selected home page, even if it appears in connector search results. Do not include unrelated result titles, links, or summaries in the report.
2. Query properties and counts from both databases. Do not fetch the body of Draft, Needs Owner Input, Ready for Review, Changes Requested, Superseded, or otherwise non-Approved SOPs.
3. Check for:
   - `AI Searchable: true` on a record whose `Review Status` is not `Approved`.
   - Approved SOPs missing a Process Owner, Approver, Source Reference, Review Frequency, or Next Review date.
   - SOPs with an overdue Next Review date or `Owner Verification: Unverified`.
   - Records with open questions, missing parent-process relationships, or unresolved compliance review.
   - Possible duplicates or overlaps based on titles, SOP IDs, search terms, summaries, and parent processes. Label these as candidates, not confirmed duplicates.
   - Open SOP Requests and process areas with requests but no matching Approved SOP.
4. If the connector cannot calculate a metric or a required property is missing, state the limitation. Do not invent dates, elapsed times, coverage percentages, or historical trends.
   Additional select options are not schema defects when every required option is present.
5. Return:
   - an overall health summary based only on observed records;
   - findings ordered by operational risk;
   - the affected record names and clickable Notion links;
   - a short recommended next-action list for human owners;
   - the query scope and audit timestamp.

Do not create, edit, approve, publish, archive, move, share, or delete anything. If the user asks to fix a finding, explain the proposed change and handle it as a separate request with the applicable confirmation boundary.
