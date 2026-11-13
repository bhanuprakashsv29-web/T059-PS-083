import pandas as pd
from datetime import date
from src.models.order import MPSOrder
def load_mps(path):
    df=pd.read_csv(path); return [MPSOrder(r.order_id,r.item_id,float(r.quantity),date.fromisoformat(str(r.due_date))) for r in df.itertuples()]
