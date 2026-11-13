import argparse
import json
from pathlib import Path
from datetime import date
from src.engine.planning_engine import PlanningEngine
from src.output.mrp_report import print_mrp_report
from src.output.order_report import print_order_report
from src.output.schedule_report import print_schedule_report

def main():
    ap=argparse.ArgumentParser(description='MRP Explosion and Finite-Capacity Production Scheduling Engine')
    ap.add_argument('--data-dir',type=Path,default=Path('data'))
    ap.add_argument('--today',type=lambda s:date.fromisoformat(s),default=date.today())
    ap.add_argument('--json',action='store_true')
    args=ap.parse_args()
    result=PlanningEngine(args.data_dir,args.today).run()
    if args.json:
        print(json.dumps({'low_level_codes':result['low_level_codes'],'planned_orders':[o.__dict__ for o in result['planned_orders']], 'exceptions':result['exceptions'],'schedules':[s.__dict__ for s in result['schedules']]},default=str,indent=2))
        return
    print('T059-PS-083 | MRP Explosion and Finite-Capacity Production Scheduling')
    print('Today:',args.today)
    print('Low-level codes:',result['low_level_codes'])
    print_mrp_report(result['mrp_rows'])
    print_order_report(result['planned_orders'])
    print_schedule_report(result['schedules'])
    print('\nEXCEPTIONS')
    print('\n'.join(result['exceptions']) if result['exceptions'] else 'None')

if __name__=='__main__': main()
