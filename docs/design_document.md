# Design Document

## 1. Architecture
The solution follows a layered design: CSV loaders → domain models → MRP services → scheduling services → reports → CLI.

## 2. MRP flow
1. Load master data and transactions.
2. Calculate low-level codes from every BOM.
3. Aggregate MPS gross requirements by due date.
4. Net each item against on-hand and scheduled receipts while maintaining safety stock.
5. Apply lot-sizing rules.
6. Offset planned order releases by lead time.
7. Explode planned parent demand into child requirements using the planned order start date for BOM effectivity.
8. Attach pegging information back to the MPS order.

## 3. Finite-capacity flow
Production planned orders are scheduled against routing operations. Operations are considered in reverse routing order so the final operation is placed first and predecessor operations can be scheduled earlier. Each work centre has daily capacity. Backward scheduling is attempted first; if capacity is unavailable through today, forward scheduling is used and a CAPACITY_SHORT exception is retained.

## 4. Priority
EDD is primary. For equal due dates, larger order value (`quantity × standard cost`) wins. Order ID is the deterministic tie-breaker.

## 5. Setup consolidation
The scheduler tracks setup minutes separately by `(work_centre, day, item)`. Multiple operations for the same item/work centre/day share one setup. The sample orchestration uses the same setup-aware capacity accounting.

## 6. Rerun and delta
The engine can run against a baseline input and a changed input. `compare_plans()` identifies added, removed and changed planned orders by order ID.

## 7. Edge cases
- BOM cycles are rejected.
- Missing BOM items or routing work centres raise clear errors.
- Zero/invalid FOQ or POQ values raise errors.
- Scrap of 100% or more is rejected.
- Sunday is skipped for scheduling and lead-time calculations.
- Past-due releases are moved to today and flagged PAST_DUE.
