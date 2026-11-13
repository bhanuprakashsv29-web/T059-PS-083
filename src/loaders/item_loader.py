import pandas as pd
from src.models.item import Item
def load_items(path):
    df=pd.read_csv(path)
    return {r.item_id:Item(r.item_id,r.description,r.make_buy,int(r.lead_time_days),r.lot_size_rule,float(r.lot_size_quantity),int(r.period_order_quantity),float(r.minimum_order_quantity),float(r.order_multiple),float(r.safety_stock),float(r.scrap_percent),r.uom,float(r.standard_cost)) for r in df.itertuples()}
