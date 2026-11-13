from pathlib import Path
from datetime import date
from src.engine.planning_engine import PlanningEngine
def test_engine_runs():
 r=PlanningEngine(Path('data'),date(2026,11,14)).run(); assert r['planned_orders'] and r['schedules']; assert all(o.pegging for o in r['planned_orders'])
