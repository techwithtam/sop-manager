# Set up SOP Manager

Use the current product's official Notion connector. Do not request or accept an API token, integration secret, MCP installation, API schema, or database ID.

1. Confirm the user connected the Notion workspace that contains their duplicated SOP Manager template.
2. Search for the exact page title `SOP Manager Home`.
3. If no exact page exists, give the user the [public SOP Manager template](https://techwithtam.notion.site/SOP-Manager-Home-3d0eee7418198147b744ebfcd27c2bba) and tell them to choose **Duplicate**. Ask them to select the workspace connected to the current product, then resume setup after the copy finishes. Do not search unrelated private content.
4. If several exact pages exist, show their clickable links and ask the user which workspace to use.
5. Fetch the selected home page and follow only its two named database links: `SOP Library` and `SOP Requests`.
6. Verify both schemas against [database-contract.md](database-contract.md). Report missing or incompatible fields without altering the databases.
7. Confirm setup with Markdown links to the selected `SOP Manager Home`, `SOP Library`, and `SOP Requests` pages. A plain page title is not sufficient. Use the stable Notion URL returned by the connector for each link. If any stable URL is unavailable, identify that item as unverified instead of reporting setup as complete. Use those linked databases for the current conversation and rediscover them from the home page in later conversations.

The home page is the configuration record. The user should never have to copy an internal Notion ID. Do not create, rename, move, share, or change a Notion page during setup unless the user sees the exact proposed change and confirms it.

Once one exact home page is selected, discard every non-matching search result. Never quote, summarize, link, or recommend another page or database returned by the search.
