# QA Support Automation Toolkit

Portfolio-ready Python project for QA, technical support, and automation workflows.

This repository contains the main project in `support_ops_toolkit/`.

## What this project does

- Loads support ticket exports from CSV or JSON
- Scores urgency and estimates SLA risk
- Detects likely duplicate incidents
- Generates Markdown or JSON reports
- Produces QA regression checklist candidates from recurring issues

## Best fit roles

- QA Analyst / Junior QA Engineer
- Technical Support Engineer
- Support Operations Specialist
- Automation-focused QA or support roles

## Main project folder

- [Project README](support_ops_toolkit/README.md)
- [English portfolio pitch](support_ops_toolkit/docs/portfolio_pitch_en.md)
- [Chinese portfolio pitch](support_ops_toolkit/docs/portfolio_pitch_cn.md)
- [Sample report](support_ops_toolkit/outputs/sample_report.md)

## Quick start

```powershell
cd support_ops_toolkit
python -m src.support_ops_toolkit.cli analyze sample_data\tickets.csv --format markdown
python -m unittest discover -s tests
```

## Why the code lives in a subfolder

This local repository also contains other untracked workspace directories.  
The actual GitHub portfolio project is the `support_ops_toolkit` folder and the supporting documents above.
