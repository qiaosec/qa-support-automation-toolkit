import argparse
from pathlib import Path

from .analysis import analyze_tickets, to_json_report, to_markdown_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Support Ops Toolkit CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    analyze = sub.add_parser("analyze", help="Analyze support ticket exports")
    analyze.add_argument("input_path")
    analyze.add_argument("--format", choices=["markdown", "json"], default="markdown")
    analyze.add_argument("--output", default="")
    return parser


def run_analyze(input_path: str, output_format: str, output_path: str) -> str:
    report = analyze_tickets(input_path)
    rendered = to_markdown_report(report) if output_format == "markdown" else to_json_report(report)

    if output_path:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")

    return rendered


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "analyze":
        rendered = run_analyze(args.input_path, args.format, args.output)
        print(rendered)


if __name__ == "__main__":
    main()
