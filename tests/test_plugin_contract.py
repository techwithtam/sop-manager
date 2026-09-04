import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
MANIFEST = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
OPENAI_MANIFEST = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text())
SKILL = (ROOT / "skills" / "sop-manager" / "SKILL.md").read_text()
REFERENCES = "\n".join(path.read_text() for path in sorted((ROOT / "skills" / "sop-manager" / "references").glob("*.md")))
REFERENCE_ROOT = ROOT / "skills" / "sop-manager" / "references"


class PluginContractTests(unittest.TestCase):
    def test_uses_native_connector_without_declaring_an_mcp_server(self):
        self.assertFalse((ROOT / ".mcp.json").exists())
        self.assertNotIn("userConfig", MANIFEST)
        self.assertNotIn("mcpServers", OPENAI_MANIFEST)

    def test_platform_manifests_share_identity_and_version(self):
        self.assertEqual(MANIFEST["name"], OPENAI_MANIFEST["name"])
        self.assertEqual(MANIFEST["version"], OPENAI_MANIFEST["version"])
        self.assertEqual(OPENAI_MANIFEST["skills"], "./skills/")

    def test_setup_requires_no_tokens_ids_or_schema_configuration(self):
        setup = (ROOT / "skills" / "sop-manager" / "references" / "setup.md").read_text()
        self.assertIn("current product's official Notion connector", setup)
        self.assertIn("Do not request or accept an API token", setup)
        self.assertIn("SOP Manager Home", setup)
        self.assertIn("SOP Library", setup)
        self.assertIn("SOP Requests", setup)
        self.assertIn("never have to copy an internal Notion ID", setup)
        self.assertIn("public SOP Manager template", setup)
        self.assertIn("https://techwithtam.notion.site/SOP-Manager-Home-", setup)
        self.assertIn("Markdown links", setup)
        self.assertIn("A plain page title is not sufficient", setup)
        self.assertIn("stable Notion URL", setup)

    def test_skill_description_has_concrete_route_triggers(self):
        for trigger in (
            "set up SOP Manager",
            "create an SOP",
            "find an approved SOP",
            "audit my SOP library",
            "show the SOP review queue",
            "report SOP analytics",
            "request a missing SOP",
        ):
            self.assertIn(f'"{trigger}"', SKILL)

    def test_manifests_point_to_the_standalone_repository(self):
        repository = "https://github.com/techwithtam/sop-manager"
        for manifest in (MANIFEST, OPENAI_MANIFEST):
            self.assertEqual(manifest["homepage"], repository)
            self.assertEqual(manifest["repository"], repository)

    def test_public_plugin_uses_mit_license(self):
        license_text = (ROOT / "LICENSE").read_text()
        self.assertEqual(MANIFEST["license"], "MIT")
        self.assertEqual(OPENAI_MANIFEST["license"], "MIT")
        self.assertIn("MIT License", license_text)
        self.assertIn("Copyright (c) 2026 SOP Manager contributors", license_text)

    def test_find_is_approved_only_and_metadata_first(self):
        find = (ROOT / "skills" / "sop-manager" / "references" / "find.md").read_text()
        self.assertIn("Review Status = Approved", find)
        self.assertIn("Use metadata alone", find)
        self.assertIn("refetch one selected page", find)
        self.assertIn("still has `Review Status: Approved`", find)
        self.assertIn("finder-answer-contract.md", find)

    def test_finder_links_sources_and_never_combines_sops(self):
        contract = (REFERENCE_ROOT / "finder-answer-contract.md").read_text()
        self.assertIn("Always link Notion pages", contract)
        self.assertIn("stable Notion page URL", contract)
        self.assertIn("Never combine SOPs", contract)
        self.assertIn("Do not merge steps", contract)
        self.assertIn("The approved SOP does not specify this.", contract)
        for mode in ("Find", "List", "Summarize", "Follow", "Question", "Compare"):
            self.assertIn(f"`{mode}`", contract)

    def test_create_is_draft_only_and_confirmation_gated(self):
        create = (ROOT / "skills" / "sop-manager" / "references" / "create.md").read_text()
        self.assertIn("CREATE DRAFT", create)
        self.assertIn("Review Status: Generated Draft", create)
        self.assertIn("AI Searchable: false", create)
        self.assertIn("Owner Verification: Unverified", create)
        self.assertIn("empty `Related SOPs` relation", create)

    def test_create_routes_to_complete_generation_system(self):
        create = (REFERENCE_ROOT / "create.md").read_text()
        required = {
            "document-types-and-hierarchy.md",
            "standard-document-templates.md",
            "field-evidence-and-review-guide.md",
            "operational-writing-guide.md",
            "privacy-compliance-and-approval.md",
            "organization-profile.md",
            "synthetic-sop-example.md",
            "synthetic-work-instruction-example.md",
            "synthetic-core-process-and-checklist-examples.md",
        }
        self.assertTrue(required.issubset({path.name for path in REFERENCE_ROOT.glob("*.md")}))
        for name in required - {
            "synthetic-sop-example.md",
            "synthetic-work-instruction-example.md",
            "synthetic-core-process-and-checklist-examples.md",
        }:
            self.assertIn(name, create)

    def test_generation_system_preserves_document_and_evidence_boundaries(self):
        hierarchy = (REFERENCE_ROOT / "document-types-and-hierarchy.md").read_text()
        template = (REFERENCE_ROOT / "standard-document-templates.md").read_text()
        evidence = (REFERENCE_ROOT / "field-evidence-and-review-guide.md").read_text()
        for document_type in ("Core Process", "SOP", "Work Instruction", "Checklist"):
            self.assertIn(document_type, hierarchy)
            self.assertIn(document_type, template)
        for status in ("Observed", "Inferred", "Missing", "Conflicting"):
            self.assertIn(status, evidence)
        self.assertIn("Evidence Appendix", evidence)
        self.assertIn("COMPLIANCE REVIEW: HUMAN DETERMINATION REQUIRED", template)

    def test_examples_are_synthetic_and_cannot_supply_process_facts(self):
        example_names = (
            "synthetic-sop-example.md",
            "synthetic-work-instruction-example.md",
            "synthetic-core-process-and-checklist-examples.md",
        )
        for name in example_names:
            example = (REFERENCE_ROOT / name).read_text()
            self.assertIn("Synthetic", example)
            self.assertIn("Never reuse", example)

    def test_request_is_confirmed_and_database_scoped(self):
        request = (ROOT / "skills" / "sop-manager" / "references" / "request.md").read_text()
        self.assertIn("SUBMIT REQUEST", request)
        self.assertIn("verified `SOP Requests` database", request)
        self.assertIn("Status: New", request)
        self.assertIn("Privacy Confirmed: true", request)

    def test_audit_is_read_only_and_does_not_expose_draft_bodies(self):
        audit = (ROOT / "skills" / "sop-manager" / "references" / "audit.md").read_text()
        self.assertIn("This route is read-only", audit)
        self.assertIn("Do not fetch the body", audit)
        self.assertIn("AI Searchable: true", audit)
        self.assertIn("Label these as candidates", audit)
        self.assertIn("Do not include unrelated result titles", audit)
        self.assertIn("Additional select options are not schema defects", audit)
        self.assertIn("Do not create, edit, approve, publish, archive, move, share, or delete anything", audit)

    def test_review_queue_is_prioritized_and_read_only(self):
        review = (ROOT / "skills" / "sop-manager" / "references" / "review-queue.md").read_text()
        self.assertIn("This route is read-only", review)
        self.assertIn("overdue Next Review date", review)
        self.assertIn("requested next decision", review)
        self.assertIn("Do not change a status", review)

    def test_analytics_exposes_formulas_and_rejects_unsupported_trends(self):
        analytics = (ROOT / "skills" / "sop-manager" / "references" / "analytics.md").read_text()
        self.assertIn("properties only", analytics)
        self.assertIn("numerator, denominator, percentage", analytics)
        self.assertIn("does not record status-change events", analytics)
        self.assertIn("Do not calculate time-to-approval", analytics)

    def test_product_files_are_client_neutral_and_secret_free(self):
        text = json.dumps(MANIFEST) + SKILL + REFERENCES
        for forbidden in (
            "vantage point",
            "ninety",
            "grace",
            "tech with tam",
            "dawn again",
            "tam nguyen",
            "notion_api_token",
        ):
            self.assertNotIn(forbidden, text.lower())
        self.assertNotIn("—", text)

    def test_product_files_contain_no_private_database_identifiers(self):
        text = json.dumps(MANIFEST) + json.dumps(OPENAI_MANIFEST) + SKILL + REFERENCES
        public_template_id = "3d0eee7418198147b744ebfcd27c2bba"
        self.assertNotRegex(text.replace(public_template_id, ""), r"(?i)(?:[0-9a-f]{32}|[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12})")

    def test_selected_home_page_is_a_hard_scope_boundary(self):
        setup = (ROOT / "skills" / "sop-manager" / "references" / "setup.md").read_text()
        self.assertIn("discard every non-matching search result", setup)
        self.assertIn("Never quote, summarize, link, or recommend another page or database", setup)


if __name__ == "__main__":
    unittest.main()
