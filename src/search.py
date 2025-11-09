
from __future__ import annotations
from typing import Dict, List, Tuple, Optional
from collections import deque
Point = Tuple[float, float]
Graph = Dict[Point, List[Tuple[Point, float]]]
def path_in_tree(tree: Graph, s: Point, t: Point) -> Optional[List[Point]]:
    if s not in tree or t not in tree: return None
    parent = {s: None}; q = deque([s])
    while q:
        u = q.popleft()
        if u == t: break
        for v, _ in tree[u]:
            if v not in parent: parent[v] = u; q.append(v)
    if t not in parent: return None
    cur = t; out = []
    while cur is not None: out.append(cur); cur = parent[cur]
    out.reverse(); return out
