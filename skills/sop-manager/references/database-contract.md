# Notion template contract

The public template contains one `SOP Manager Home` page with links to these databases.

## SOP Library

- `SOP Title`: title
- `SOP ID`: text
- `Document Type`: select with Core Process, SOP, Work Instruction, Checklist
- `Review Status`: select with Generated Draft, Needs Owner Input, Ready for Review, Changes Requested, Approved, Published, Superseded
- `Process Owner`: text
- `Approver`: text
- `Parent Process`: text
- `Compliance Review`: select with Not needed, Needed, Approved, Changes requested
- `Open Questions`: number
- `Version`: text
- `Source Reference`: text
- `Review Frequency`: select
- `Visibility`: select
- `AI Searchable`: checkbox
- `AI Summary`: text
- `AI Search Terms`: text
- `Related SOP Recommendations`: text
- `Owner Verification`: select with Unverified, Verified, Review Due
- `Verified On`: date
- `Next Review`: date
- `Related SOPs`: relation to SOP Library
- `Decision Notes`: text

The page body stores the SOP content.

## SOP Requests

- `Request`: title
- `Status`: select that includes New. Additional workflow statuses are allowed.
- `Search Query`: text
- `Requested By`: text
- `Needed By`: date
- `Notes`: text
- `Privacy Confirmed`: checkbox
