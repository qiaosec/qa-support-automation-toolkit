import json
import tempfile
import unittest
from pathlib import Path

from src.support_ops_toolkit.analysis import analyze_tickets, to_markdown_report
from src.support_ops_toolkit.cli import run_analyze
from src.support_ops_toolkit.loader import load_tickets, normalize_priority


ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "sample_data" / "tickets.csv"


class ToolkitTests(unittest.TestCase):
    def test_load_tickets_from_csv(self):
        tickets = load_tickets(SAMPLE)
        self.assertEqual(len(tickets), 10)
        self.assertEqual(tickets[0].ticket_id, "1001")

    def test_priority_normalization_defaults_to_medium(self):
        self.assertEqual(normalize_priority("unknown"), "medium")
        self.assertEqual(normalize_priority("P0"), "critical")

    def test_analysis_detects_duplicates(self):
        report = analyze_tickets(str(SAMPLE))
        duplicate_values = list(report["duplicates"].values())
        self.assertTrue(any("1001" in ids and "1004" in ids for ids in duplicate_values))
        self.assertTrue(any("1002" in ids and "1008" in ids for ids in duplicate_values))

    def test_markdown_report_contains_sections(self):
        report = analyze_tickets(str(SAMPLE))
        markdown = to_markdown_report(report)
        self.assertIn("## Summary", markdown)
        self.assertIn("## Top Risks", markdown)
        self.assertIn("## Duplicate Groups", markdown)

    def test_cli_json_output(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "report.json"
            rendered = run_analyze(str(SAMPLE), "json", str(output_path))
            payload = json.loads(rendered)
            self.assertEqual(payload["summary"]["ticket_count"], 10)
            self.assertTrue(output_path.exists())


if __name__ == "__main__":
    unittest.main()
