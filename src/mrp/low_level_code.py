from collections import defaultdict

def calculate_low_level_codes(items,bom_lines):
    children=defaultdict(list); parents=defaultdict(list)
    for b in bom_lines:
        children[b.parent_item].append(b.component_item); parents[b.component_item].append(b.parent_item)
    # Detect cycles even when the graph has no top-level node.
    state={i:0 for i in items}
    def dfs(i):
        if state[i]==1: raise ValueError(f"BOM cycle detected involving item: {i}")
        if state[i]==2: return
        state[i]=1
        for c in children[i]:
            if c not in state: state[c]=0
            dfs(c)
        state[i]=2
    for i in list(state): dfs(i)
    top=[i for i in items if i not in parents]; levels={i:0 for i in items}
    def visit(i,lev,path):
        if i in path: raise ValueError(f"BOM cycle detected involving item: {i}")
        levels[i]=max(levels[i],lev); p=set(path); p.add(i)
        for c in children[i]: visit(c,lev+1,p)
    for t in top: visit(t,0,set())
    return levels

def sort_items_by_low_level_code(codes): return sorted(codes,key=lambda i:(codes[i],i))
