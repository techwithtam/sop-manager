# Report SOP analytics

This route is read-only. Use it for counts, status distribution, governance rates, documentation coverage, review exposure, and missing-SOP request metrics.

1. Rediscover both verified databases from `SOP Manager Home` and verify their schemas against [database-contract.md](database-contract.md).
2. Query all records needed for the requested metric using properties only. Do not fetch SOP page bodies.
3. Supported current-state metrics include:
   - total SOP records by Review Status and Document Type;
   - Approved, Published, AI Searchable, and owner-assigned counts and rates;
   - records overdue or due within 30, 60, and 90 days based on Next Review;
   - verification and compliance-review coverage;
   - records and Approved SOPs by Parent Process;
   - open SOP Requests by status and requested process area;
   - process areas with open requests and no matching Approved SOP, labeled as possible coverage gaps.
4. For every rate, show the numerator, denominator, percentage, and any excluded records. Use the current date in the user's timezone for due-date calculations.
5. Distinguish exact matches from heuristic matches based on titles, summaries, or search terms. Do not present heuristic coverage as confirmed.
6. The default template does not record status-change events. Do not calculate time-to-approval, time-to-publication, throughput trends, or period-over-period changes unless the connected workspace contains verified date or event-history fields that support them.
7. Return a concise summary, the requested metric table, material data-quality limitations, and the audit timestamp. Link the filtered records behind notable exceptions when the connector can provide stable URLs.

Do not create, edit, approve, publish, verify, archive, move, share, or delete anything. Analytics describe observed records; they do not authorize remediation.
