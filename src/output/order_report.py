def print_order_report(orders):
    print("\nPLANNED ORDERS")
    print("-"*90)
    for o in orders:
        print(f"{o.order_id} | {o.item_id} | qty={o.quantity:g} | release={o.release_date} | due={o.due_date} | {o.source}")
