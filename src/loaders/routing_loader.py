import pandas as pd
from src.models.routing import RoutingOperation,WorkCentre
def load_routings(path):
    df=pd.read_csv(path); ops=[]
    for r in df.itertuples(): ops.append(RoutingOperation(r.item_id,int(r.operation_no),r.work_centre_id,float(r.setup_minutes),float(r.run_minutes_per_unit)))
    wcs={wc:WorkCentre(wc,wc,960) for wc in df.work_centre_id.unique()}
    return ops,wcs
