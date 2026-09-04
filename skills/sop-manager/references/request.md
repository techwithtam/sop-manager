# Submit a missing-SOP request

Collect a short request title, the search or question that failed, requester name, optional needed-by date, and optional notes. Default the requester to `SOP Manager user`. Never invent a deadline.

Reject or redact client names, account identifiers, contact information, financial data, credentials, or other sensitive details before continuing. Show the exact fields and state that the record will be created with `Status: New`. Ask the user to confirm the request contains no client, account, financial, contact, or credential data and reply exactly `SUBMIT REQUEST`.

Only then create one page in the verified `SOP Requests` database with `Status: New` and `Privacy Confirmed: true`. Call the connector once. If it fails or omits the URL, state that submission was not confirmed and do not retry silently.
