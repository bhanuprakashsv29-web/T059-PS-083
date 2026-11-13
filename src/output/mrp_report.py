def print_mrp_report(rows):
    print("\nMRP TABLE")
    print("-"*100)
    print(f"{'ITEM':10} {'PERIOD':12} {'GROSS':10} {'RECEIPTS':10} {'PROJECTED':12} {'NET':10} {'PLAN':10}")
    for x in rows:
        print(f"{x.item_id:10} {x.period:%Y-%m-%d} {x.gross_requirement:10.1f} {x.scheduled_receipt:10.1f} {x.projected_available:12.1f} {x.net_requirement:10.1f} {x.planned_order_receipt:10.1f}")
