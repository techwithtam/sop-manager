# Find and use an Approved SOP

Read [finder-answer-contract.md](finder-answer-contract.md) before answering from SOP content.

1. Query the verified `SOP Library` with the fixed filter `Review Status = Approved`. Follow pagination and search the complete Approved-only metadata results by exact SOP ID or title, AI search terms, AI summary, parent process, then document type.
2. If several records may apply, show a short linked list and ask which process the user means. Do not fetch every body and do not combine SOPs.
3. Use metadata alone for find, list, link, status, owner, version, review date, or summary requests.
4. For steps, controls, exceptions, decisions, or definition of done, refetch one selected page. Confirm it still belongs to the verified `SOP Library` and still has `Review Status: Approved` before using its body.
5. Preserve the approved sequence, roles, controls, decisions, and exceptions. If the SOP does not answer the question, say what is missing and direct the user to the process owner.

Link every mentioned record as `[SOP Title (SOP ID)](Notion URL)`. Every Notion-derived claim, answer section, step set, comparison item, warning, and related-document reference must identify and link its source page. Never present Notion content as verified when the connector did not return a stable page URL. If there is no Approved match, say `I could not find an approved SOP for that request.` Then offer the Request route without mentioning drafts or other states.

Warn when owner verification is `Unverified` or `Review Due`, when `Verified` lacks a verified date, or when the next review date is past. Use: `This SOP is approved, but its owner verification is unverified or may be out of date. Check with <Process Owner> in case the process has changed.` If no owner is listed, say so and use `the process owner`.
