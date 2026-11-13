# Decision Log

## D-001 — Python dataclasses
Chosen for small, explicit domain objects and easy unit testing.

## D-002 — Pandas for CSV loading
Chosen for concise validation/parsing while keeping the planning logic independent of pandas.

## D-003 — Monday-Saturday calendar
Required by BR-05. Sunday is excluded; holidays are injectable rather than hard-coded.

## D-004 — Safety stock is a floor, not demand
Projected available is calculated after gross demand and receipts. Net requirement fills the gap to safety stock.

## D-005 — Deterministic priority
EDD, then order value, then order ID makes scheduling reproducible.
