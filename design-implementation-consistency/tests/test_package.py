"""Structural checks only, not a semantic UI audit engine."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_local_reference_links(self):
        count = 0
        for doc in ROOT.rglob("*.md"):
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
                if re.match(r"[a-zA-Z][\w+.-]*:", target) or target.startswith("#"):
                    continue
                path = (doc.parent / target.split("#", 1)[0]).resolve()
                self.assertTrue(path.is_relative_to(ROOT), target)
                self.assertTrue(path.is_file(), f"{doc.name}: {target}")
                count += 1
        self.assertGreater(count, 0)

    def test_example_import_resolves(self):
        source = (ROOT / "examples/implementation.tsx").read_text(encoding="utf-8")
        imports = re.findall(r'import "([^"]+)"', source)
        self.assertTrue(imports)
        for name in imports:
            self.assertTrue((ROOT / "examples" / name).is_file())

    def test_report_json_example_is_valid(self):
        text = (ROOT / "references/report-format.md").read_text(encoding="utf-8")
        blocks = re.findall(r"```json\n(.*?)\n```", text, re.S)
        self.assertTrue(blocks)
        for block in blocks:
            report = json.loads(block)
            checks = report["checks"]
            for level in ("critical", "high", "medium", "low"):
                self.assertEqual(report["summary"][level], sum(c["severity"] == level.upper() for c in checks))
            self.assertEqual(report["summary"]["unverified"], sum(c["status"] == "UNVERIFIED" for c in checks))
            self.assertEqual(report["summary"]["passed"], sum(c["status"] == "PASS" for c in checks))
            self.assertTrue(all(c["severity"] is None for c in checks if c["status"] == "UNVERIFIED"))

    def test_expected_report_citations(self):
        css = (ROOT / "examples/implementation.css").read_text(encoding="utf-8").splitlines()
        tsx = (ROOT / "examples/implementation.tsx").read_text(encoding="utf-8").splitlines()
        for line, text in [(6, "font-weight: 600"), (9, "flex-direction: row"), (10, "gap: 16px"), (12, "border-radius: 6px"), (13, "min-width: 768px")]:
            self.assertIn(text, css[line - 1])
        self.assertIn(">Start</button>", tsx[8])


if __name__ == "__main__":
    unittest.main()
