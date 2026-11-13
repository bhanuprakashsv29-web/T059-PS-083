import pandas as pd
from datetime import date
from src.models.order import InventoryRecord,OpenOrder
def load_inventory(path):
    df=pd.read_csv(path); return {r.item_id:InventoryRecord(r.item_id,float(r.on_hand)) for r in df.itertuples()}
def load_open_orders(path):
    df=pd.read_csv(path); return [OpenOrder(r.order_id,r.item_id,r.order_type,float(r.quantity),date.fromisoformat(str(r.due_date)),r.status) for r in df.itertuples()]
