# Support Ops Toolkit

Python project for QA, technical support, and automation workflows.

This tool ingests support ticket exports, scores urgency, estimates SLA risk, detects likely duplicate issues, and generates recruiter-friendly reports.

## Why it matters

Support and QA teams often have raw ticket exports but no fast way to:

- rank the most urgent incidents
- spot duplicate issues
- identify categories that should become regression tests

This project turns that raw data into a structured report that is easier to act on.

## Best fit roles

- QA Analyst / Junior QA Engineer
- Technical Support Engineer
- Support Operations Specialist
- Automation-focused QA or support roles

## What it demonstrates

- QA thinking: clear validation rules, repeatable outputs, and regression-oriented reporting
- Support mindset: triage, SLA awareness, duplicate issue grouping, and operational prioritization
- Automation ability: command-line workflow, structured inputs, structured outputs, and test coverage

## Features

- Load support tickets from CSV or JSON
- Normalize priorities and statuses
- Score urgency from impact, customer tier, age, and keywords
- Estimate SLA breach risk
- Detect likely duplicate issues using lightweight text similarity
- Generate Markdown or JSON reports
- Produce QA regression checklist candidates from recurring issues

## Example workflow

1. Export support tickets from a system such as Zendesk, Jira, or an internal CSV dump.
2. Run the toolkit against that export.
3. Review the generated report for:
   - high SLA-risk tickets
   - likely duplicate incidents
   - recurring categories worth regression coverage
4. Share the report with QA or support stakeholders.

## Quick start

```powershell
python -m src.support_ops_toolkit.cli analyze sample_data\tickets.csv --format markdown
python -m unittest discover -s tests
```

## Example output

```powershell
python -m src.support_ops_toolkit.cli analyze sample_data\tickets.csv --format markdown --output outputs\sample_report.md
```

The generated example report is available in [outputs/sample_report.md](outputs/sample_report.md).

Short output preview:

```text
## Summary
- Ticket count: 10
- Open tickets: 9
- High SLA risk tickets: 2
- Duplicate groups: 2
```

## Resume / LinkedIn project description

> Built a Python support-operations toolkit that ingests ticket exports, scores urgency, estimates SLA risk, detects duplicate issues, and generates triage and regression-oriented reports for QA and technical support workflows.

## Documentation

- [QA test plan](docs/qa_test_plan.md)

## Next improvements

- add a small web UI
- integrate with Zendesk/Jira exports
- add richer duplicate detection
- add dashboard charts
