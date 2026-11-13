import pandas as pd
from datetime import date
from src.models.bom import BOMLine
def load_bom(path):
    df=pd.read_csv(path)
    out=[]
    for r in df.itertuples():
        to=None if pd.isna(r.effective_to) or str(r.effective_to).strip()=='' else date.fromisoformat(str(r.effective_to))
        out.append(BOMLine(r.parent_item,r.component_item,float(r.quantity),date.fromisoformat(str(r.effective_from)),to))
    return out
