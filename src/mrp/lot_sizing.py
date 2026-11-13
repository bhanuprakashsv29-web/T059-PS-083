import math
from datetime import timedelta
def apply_lot_sizing(item,net_requirements):
    out={}
    for period,net in sorted(net_requirements.items()):
        if net<=0: out[period]=0.; continue
        rule=item.lot_size_rule.upper()
        if rule=='LFL': q=net
        elif rule=='FOQ':
            if item.lot_size_quantity<=0: raise ValueError(f"FOQ quantity must be greater than 0 for {item.item_id}")
            q=math.ceil(net/item.lot_size_quantity)*item.lot_size_quantity
        elif rule=='POQ':
            if item.period_order_quantity<=0: raise ValueError(f"POQ weeks must be greater than 0 for {item.item_id}")
            end=period+timedelta(days=item.period_order_quantity*7); q=sum(v for d,v in net_requirements.items() if period<=d<=end)
        else: raise ValueError(f"Unknown lot size rule: {item.lot_size_rule}")
        if item.minimum_order_quantity>0:q=max(q,item.minimum_order_quantity)
        if item.order_multiple>0:q=math.ceil(q/item.order_multiple)*item.order_multiple
        out[period]=q
    return out
