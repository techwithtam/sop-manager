#!/usr/bin/env python3
"""Build deterministic Claude-plugin and OpenAI-skill downloads."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = ROOT.parents[1] if ROOT.parent.name == "plugins" else ROOT
CLAUDE_OUTPUT = REPOSITORY / "dist" / "claude" / "sop-manager.plugin"
OPENAI_OUTPUT = REPOSITORY / "dist" / "openai" / "sop-manager-skill.zip"
SKILL_ROOT = ROOT / "skills" / "sop-manager"
EXCLUDED_PARTS = {"__pycache__", ".pytest_cache", ".DS_Store", "tests", "scripts"}


def include(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    return (
        not any(part in EXCLUDED_PARTS for part in relative.parts)
        and relative.parts[0] not in {".codex-plugin"}
        and "agents" not in relative.parts
        and path.suffix not in {".pyc", ".env"}
    )


def main() -> None:
    CLAUDE_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(CLAUDE_OUTPUT, "w", ZIP_DEFLATED) as archive:
        for path in sorted(item for item in ROOT.rglob("*") if item.is_file() and include(item)):
            relative = path.relative_to(ROOT)
            info = ZipInfo(str(relative), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = (0o755 if path.suffix == ".py" else 0o644) << 16
            archive.writestr(info, path.read_bytes())
    OPENAI_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(OPENAI_OUTPUT, "w", ZIP_DEFLATED) as archive:
        for path in sorted(item for item in SKILL_ROOT.rglob("*") if item.is_file()):
            if any(part in EXCLUDED_PARTS for part in path.relative_to(SKILL_ROOT).parts):
                continue
            relative = Path("sop-manager") / path.relative_to(SKILL_ROOT)
            info = ZipInfo(str(relative), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
        license_path = ROOT / "LICENSE"
        info = ZipInfo("sop-manager/LICENSE", date_time=(2026, 1, 1, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        archive.writestr(info, license_path.read_bytes())

    print(CLAUDE_OUTPUT)
    print(OPENAI_OUTPUT)


if __name__ == "__main__":
    main()
