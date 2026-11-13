import math
def is_effective(b,start_date): return start_date>=b.effective_from and (b.effective_to is None or start_date<=b.effective_to)
def round_to_uom(q,uom):
    if uom.upper()=='EA': return math.ceil(q)
    if uom.upper()=='KG': return math.ceil(q*10)/10
    return q
def calculate_component_requirement(parent_quantity,bom_quantity,scrap_percent,component_uom):
    f=1-scrap_percent/100
    if f<=0: raise ValueError('Scrap percentage cannot be 100% or greater')
    return round_to_uom(parent_quantity*bom_quantity/f,component_uom)
def explode_bom(parent_item,parent_quantity,start_date,bom_lines,items):
    out={}
    for b in bom_lines:
        if b.parent_item==parent_item and is_effective(b,start_date):
            c=items[b.component_item]; q=calculate_component_requirement(parent_quantity,b.quantity,c.scrap_percent,c.uom); out[b.component_item]=out.get(b.component_item,0)+q
    return out
def explode_multilevel_bom(demand,start_date,bom_lines,items,low_level_codes):
    total={}; pending=dict(demand); queue=sorted(demand,key=lambda i:(low_level_codes.get(i,0),i)); processed=set()
    while queue:
        p=queue.pop(0)
        if p in processed: continue
        q=pending.get(p,0)
        if q<=0: processed.add(p); continue
        for c,qty in explode_bom(p,q,start_date,bom_lines,items).items():
            total[c]=total.get(c,0)+qty; pending[c]=pending.get(c,0)+qty
            if c not in processed: queue.append(c)
        processed.add(p); queue.sort(key=lambda i:(low_level_codes.get(i,0),i))
    return total
