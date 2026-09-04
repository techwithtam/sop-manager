# SOP Manager Plugin

This installable plugin gives a team one conversational SOP entry point. The assistant determines whether the user wants to create a draft, find or use an Approved SOP, audit the library, prioritize a review queue, report analytics, or submit a missing-SOP request.

The package contains one skill and uses the product's official Notion connector. It does not declare or install an MCP server and contains no token, private database ID, or API schema. Users connect Notion, duplicate the [public SOP Manager template](https://techwithtam.notion.site/SOP-Manager-Home-3d0eee7418198147b744ebfcd27c2bba), and ask the assistant to set it up. The assistant finds the databases from the template's home page, so users do not copy database IDs.

## What it enforces

- Creation classifies Core Processes, SOPs, Work Instructions, and Checklists and uses a complete type-specific template.
- Normative instructions require source evidence; inferences, gaps, conflicts, and optional improvements remain outside the clean procedure.
- Review View includes the clean draft, high-impact approver questions, and a compact review note. Audit View adds field-level evidence traceability.
- A neutral operational writing standard applies by default. An optional organization profile can change voice, terminology, labels, and formatting without weakening safety rules.
- Search instructions require `Review Status: Approved` and metadata-first retrieval.
- Full content is used only after the selected page is rechecked against the template's SOP Library and `Approved` status.
- Owner verification warnings remain separate from approval status.
- SOP creation can only create a non-searchable `Generated Draft` with human review required.
- Missing-SOP requests can only create a `New` record in the configured request database.
- Audits use database properties and counts, do not read non-Approved SOP bodies, and never repair findings automatically.
- Review queues are metadata-first and never change approval or publication state.
- Analytics show their populations and formulas and do not invent historical trends.
- Both write paths require a privacy attestation, an exact preview confirmation phrase, and one verifiable Notion result.
- No tool can approve, publish, overwrite, update, or delete an SOP.

## Build and test

From this directory:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build_package.py
```

The build creates two direct-upload files from the same skill source:

- `dist/claude/sop-manager.plugin` for Claude.
- `dist/openai/sop-manager-skill.zip` for ChatGPT skill upload where that control is available.

If Claude Code is installed, also run:

```bash
claude plugin validate .
claude --plugin-dir .
```

Then invoke `/sop-manager:sop-manager` or describe the SOP task in plain language.

## Install in Cowork

1. Build the `.plugin` file.
2. Open Claude Desktop and select **Cowork**.
3. Open **Customize**, then **Plugins**.
4. Choose the upload option and select `sop-manager.plugin`.
5. In **Customize**, open **Connectors** and connect Claude's native Notion connector if it is not already connected.
6. Open the [public SOP Manager Notion template](https://techwithtam.notion.site/SOP-Manager-Home-3d0eee7418198147b744ebfcd27c2bba) and choose **Duplicate** to copy it into the connected workspace.
7. Start a new Cowork task and say `Set up SOP Manager.` Claude finds `SOP Manager Home`, verifies its linked databases, and reports any missing fields.
8. Ask to create an SOP, find an Approved SOP, audit the library, review the queue, report analytics, or request a missing SOP.

The plugin does not install or register an MCP server. No API credential entry is required.

## Install in ChatGPT

1. Open **Plugins**, select **Skills**, then choose **Create** and **Upload from your computer**.
2. Upload `sop-manager-skill.zip`.
3. Connect ChatGPT's official Notion app.
4. Duplicate the [public SOP Manager Notion template](https://techwithtam.notion.site/SOP-Manager-Home-3d0eee7418198147b744ebfcd27c2bba).
5. Start a new chat and say `Set up SOP Manager.`

Skill upload availability depends on the ChatGPT plan, workspace settings, role, and product surface. The download contains the same SOP Manager workflow as the Claude plugin, packaged in the upload format ChatGPT documents for custom skills.

## Use in Claude Code

Download or clone the standalone repository, then start Claude Code with the plugin directory:

```bash
claude --plugin-dir /path/to/sop-manager
```

This loads the plugin directly without adding a marketplace. Start a new session after replacing the downloaded files.

## Use in Codex

Download the repository and copy the `skills/sop-manager` folder into your Codex skills directory. Restart Codex or start a new task so it discovers the skill. Codex CLI does not currently expose a command for directly installing a standalone plugin archive, so this is a direct skill installation rather than a marketplace installation.

## Notion database contract

The public template creates `SOP Manager Home`, `SOP Library`, and `SOP Requests`. The home page links the two databases and acts as the discoverable configuration record.

The SOP Library uses: `SOP Title`, `SOP ID`, `Document Type`, `Review Status`, `Process Owner`, `Approver`, `Parent Process`, `Compliance Review`, `Open Questions`, `Version`, `Source Reference`, `Review Frequency`, `Visibility`, `AI Searchable`, `AI Summary`, `AI Search Terms`, `Related SOP Recommendations`, `Owner Verification`, `Verified On`, `Next Review`, `Related SOPs`, and `Decision Notes`.

The request data source uses `Request`, `Status`, `Search Query`, `Requested By`, `Needed By`, `Notes`, and `Privacy Confirmed`. Status options must include `New`. If a team renames a property, update and retest the plugin instructions rather than asking end users to map fields.

## Credential boundary

Claude's native Notion connector acts with the connected user's permissions. Connect only the intended workspace and review Claude's requested access during OAuth. The package contains no token, database ID, client record, or raw transcript.

Official packaging references: [Cowork plugin installation](https://claude.com/docs/cowork/guide/plugins) and [Claude plugin reference](https://code.claude.com/docs/en/plugins-reference).
