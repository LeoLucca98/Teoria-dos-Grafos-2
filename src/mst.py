
from __future__ import annotations
from typing import Dict, List, Tuple, Set
from heapq import heappush, heappop
Point = Tuple[float, float]
Graph = Dict[Point, List[Tuple[Point, float]]]
def prim_mst(g: Graph, start: Point=None) -> Graph:
    if not g: return {}
    if start is None: start = next(iter(g))
    mst_adj: Graph = {v: [] for v in g}
    visited: Set[Point] = set([start])
    heap = []
    for v, w in g[start]: heappush(heap, (w, start, v))
    while heap and len(visited) < len(g):
        w, u, v = heappop(heap)
        if v in visited: continue
        mst_adj[u].append((v, w)); mst_adj[v].append((u, w))
        visited.add(v)
        for x, wx in g[v]:
            if x not in visited: heappush(heap, (wx, v, x))
    mst_adj = {k:v for k,v in mst_adj.items() if v or k==start}
    return mst_adj
