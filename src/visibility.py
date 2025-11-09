
from __future__ import annotations
from typing import Dict, List, Tuple
from math import hypot
from .map_io import MapData, all_vertices
from .geometry import segments_intersect, polygon_edges
Point = Tuple[float, float]
def euclid(a: Point, b: Point) -> float:
    return hypot(a[0]-b[0], a[1]-b[1])
def _edge_blocked(a: Point, b: Point, obstacles: List[List[Point]]) -> bool:
    for poly in obstacles:
        for e1, e2 in polygon_edges(poly):
            if a==e1 or a==e2 or b==e1 or b==e2: continue
            if segments_intersect(a, b, e1, e2, proper=True): return True
    return False
def build_visibility_graph(md: MapData) -> Dict[Point, List[Tuple[Point, float]]]:
    verts = all_vertices(md)
    n = len(verts)
    adj: Dict[Point, List[Tuple[Point, float]]] = {v: [] for v in verts}
    for i in range(n):
        for j in range(i+1, n):
            a, b = verts[i], verts[j]
            if not _edge_blocked(a, b, md.obstacles):
                w = euclid(a, b)
                adj[a].append((b, w)); adj[b].append((a, w))
    return adj
