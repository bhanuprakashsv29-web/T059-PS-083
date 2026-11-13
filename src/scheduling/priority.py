def calculate_order_value(planned_order,item): return planned_order.quantity*item.standard_cost
def priority_key(planned_order,item): return (planned_order.due_date,-calculate_order_value(planned_order,item),planned_order.order_id)
def sort_planned_orders(planned_orders,items): return sorted(planned_orders,key=lambda o:priority_key(o,items[o.item_id]))
