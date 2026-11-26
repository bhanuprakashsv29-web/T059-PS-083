# T059-PS-083 — MRP Explosion and Finite-Capacity Production Scheduling Engine

## Overview

A Python 3.10+ command-line planning engine for multi-level Material Requirements Planning (MRP) and finite-capacity production scheduling.

## Core Capabilities

- Item master, BOM, routing, MPS, inventory and open-order CSV loaders
- Multi-level BOM explosion with low-level coding and effectivity dates
- Gross-to-net MRP with safety-stock floor
- LFL, FOQ and POQ lot sizing with MOQ and order multiples
- Working-day lead-time offsetting (Monday-Saturday; Sunday/holidays excluded)
- Planned production/purchase orders and pegging to top-level MPS demand
- Backward finite-capacity scheduling at 960 minutes/work-centre/day by default
- Forward scheduling when backward planning reaches today
- EDD → order value → order ID priority
- Setup consolidation for same item/work-centre/day
- MRP/schedule exceptions
- Human-readable reports and Gantt-style schedule output
- Rerun/delta reporting after MPS changes or order delays

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.main --data-dir data --today 2026-11-14
```

## Tests

Run the complete test suite using:

```bash
python -m pytest -q
```

## Demo Video

[Watch the 5-minute project demonstration](https://drive.google.com/drive/folders/1uUhqZ4bpA-fH30t6kmGz3KbF42kqbGBF)

## Command Examples

```bash
python -m src.main --data-dir data --today 2026-11-14
python -m src.main --data-dir data --today 2026-11-14 --json
```

## Design Assumptions

- Sunday is non-working. Monday-Saturday are working unless listed as holidays.
- Holidays are supplied to the lead-time calculator through the engine API; the CSV sample uses no holidays.
- Planned order receipt date is the component/parent need date. Release is calculated by working-day lead-time offset.
- For make items, routings drive finite-capacity scheduling. Buy items are not put on a production work-centre schedule.
- Scrap is applied as `parent_qty × BOM_qty / (1 - scrap%)` and then rounded to UOM precision (EA whole units, KG 0.1).
- Effectivity is evaluated against the planned order start date.

## Project Structure

```text
src/
├── models/       domain dataclasses
├── loaders/      CSV input readers
├── mrp/          low-level code, explosion, netting, lot sizing, lead time, planning, pegging
├── scheduling/   capacity, priority, backward/forward scheduling and orchestration
├── exceptions/   exception model and rules
├── output/       console/report helpers
├── engine/       end-to-end planning engine
└── main.py       CLI

tests/             unit/integration tests
data/              sample input data
docs/              design and decision log
```

## Project Execution

The engine processes manufacturing data through the following workflow:

```text
Input CSV Data
      ↓
BOM Explosion
      ↓
Low-Level Coding
      ↓
Gross-to-Net MRP
      ↓
Lot Sizing
      ↓
Planned Orders
      ↓
Lead-Time Offset
      ↓
Finite-Capacity Scheduling
      ↓
Exceptions & Reports
```

## Team

**Team ID:** T059  
**Problem Statement ID:** PS-083  
**Problem:** MRP Explosion and Finite-Capacity Production Scheduling Engine