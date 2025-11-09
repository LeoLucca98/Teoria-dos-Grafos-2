
from __future__ import annotations
from typing import Dict, List, Tuple, Optional
from math import hypot
from .geometry import segments_intersect, polygon_edges

Point = Tuple[float, float]
Graph = Dict[Point, List[Tuple[Point, float]]]

def _segment_blocked(a: Point, b: Point, obstacles: List[List[Point]]) -> bool:
    for poly in obstacles:
        for e1, e2 in polygon_edges(poly):
            # Permite tocar exatamente nas quinas
            if a==e1 or a==e2 or b==e1 or b==e2:
                continue
            if segments_intersect(a, b, e1, e2, proper=True):
                return True
    return False

def verticeMaisProximo(p: Point, graph: Graph, obstacles: List[List[Point]]) -> Optional[Point]:
    """Retorna o vértice do grafo mais próximo VISÍVEL a partir de p.
    Se nenhum vértice for visível (segmento p->v cruza obstáculos), retorna None.
    """
    # Ordena por distância Euclidiana e devolve o primeiro que seja visível
    for v in sorted(graph.keys(), key=lambda v: hypot(p[0]-v[0], p[1]-v[1])):
        if not _segment_blocked(p, v, obstacles):
            return v
    return None
