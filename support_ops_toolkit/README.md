# Support Ops Toolkit

`Support Ops Toolkit` is a portfolio-ready Python project for QA, technical support, and automation workflows.

It ingests support tickets from CSV or JSON, scores urgency, estimates SLA risk, finds duplicate issues, and generates recruiter-friendly reports.

## Why this project exists

This project is designed to showcase:

- QA thinking: clear validation rules, regression-oriented outputs, and reproducible reports
- Support mindset: triage, SLA awareness, duplicate issue detection, and incident summaries
- Automation ability: command-line workflow, structured inputs, structured outputs, and test coverage

## Features

- Load support tickets from CSV or JSON
- Normalize priorities and statuses
- Score urgency from impact, customer tier, age, and keywords
- Estimate SLA breach risk
- Detect likely duplicate issues using lightweight text similarity
- Generate Markdown or JSON reports
- Produce a QA regression checklist from recurring issues

## Project structure

```text
support_ops_toolkit/
  docs/
  sample_data/
  src/support_ops_toolkit/
  tests/
```

## Quick start

```powershell
cd "C:\Users\Administrator\Documents\New project\support_ops_toolkit"
python -m src.support_ops_toolkit.cli analyze sample_data\tickets.csv --format markdown
python -m unittest discover -s tests
```

## Example report

```powershell
python -m src.support_ops_toolkit.cli analyze sample_data\tickets.csv --format markdown --output outputs\sample_report.md
```

## Portfolio angle

If you publish this on GitHub, you can present it as:

- a QA/support automation project
- a ticket triage and reporting tool
- a Python automation project with tests and documentation

## Next improvements

- add a small web UI
- integrate with Zendesk/Jira exports
- add richer duplicate detection
- add dashboard charts
