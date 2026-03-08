# Support Ops Toolkit

`Support Ops Toolkit` is a portfolio-ready Python project for QA, technical support, and automation workflows.

It ingests support tickets from CSV or JSON, scores urgency, estimates SLA risk, finds duplicate issues, and generates recruiter-friendly reports.

## Best fit roles

This project is especially useful if you want to position yourself for:

- QA Analyst / Junior QA Engineer
- Technical Support Engineer
- Support Operations Specialist
- Automation-focused Operations or QA roles

## What this project demonstrates

- You can turn raw support data into structured, decision-ready outputs.
- You understand bug duplication, SLA risk, triage priorities, and regression candidates.
- You can package automation work into a tool that is easy for recruiters to review.

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

## Example workflow

1. Export support tickets from a system such as Zendesk, Jira, or an internal CSV dump.
2. Run the toolkit against that export.
3. Review the generated report for:
   - high SLA-risk tickets
   - likely duplicate incidents
   - recurring categories worth regression coverage
4. Share the report with QA or support stakeholders.

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

## Sample command and output

```powershell
python -m src.support_ops_toolkit.cli analyze sample_data\tickets.csv --format markdown --output outputs\sample_report.md
```

The generated example report is available in [outputs/sample_report.md](outputs/sample_report.md).

## Example report

- Summary of open tickets, high-risk tickets, and duplicate groups
- Ranked high-risk issues for support triage
- Duplicate groups for consolidation
- QA regression checklist candidates from recurring issue categories

## Portfolio angle

If you publish this on GitHub, you can present it as:

- a QA/support automation project
- a ticket triage and reporting tool
- a Python automation project with tests and documentation

## Resume / LinkedIn project description

You can describe this project like this:

> Built a Python support-operations toolkit that ingests ticket exports, scores urgency, estimates SLA risk, detects duplicate issues, and generates triage and regression-oriented reports for QA and technical support workflows.

## Documentation

- [QA test plan](docs/qa_test_plan.md)
- [Sample report](docs/sample_report.md)
- [Chinese portfolio pitch](docs/portfolio_pitch_cn.md)

## Next improvements

- add a small web UI
- integrate with Zendesk/Jira exports
- add richer duplicate detection
- add dashboard charts
