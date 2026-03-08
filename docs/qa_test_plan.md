# QA Test Plan

## Scope

Validate the CLI workflow for:

- CSV and JSON parsing
- ticket normalization
- urgency scoring
- SLA risk estimation
- duplicate detection
- Markdown and JSON report generation

## Test scenarios

1. Load a valid CSV export with mixed priorities and statuses.
2. Load a valid JSON export with the same schema.
3. Confirm normalization maps unknown priority values to `medium`.
4. Confirm `resolved` tickets are not treated as active SLA risks.
5. Confirm old high-impact tickets are ranked above fresh low-impact tickets.
6. Confirm similar login-related tickets are grouped as likely duplicates.
7. Confirm Markdown report contains overview, top risks, duplicates, and regression checklist.
8. Confirm JSON report contains structured keys suitable for downstream automation.

## Exit criteria

- Unit tests pass
- Sample data produces a report without runtime errors
- Duplicate groups and risk ranking are stable across repeated runs
