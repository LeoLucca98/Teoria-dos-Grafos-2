
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple, Optional
Point = Tuple[float, float]
@dataclass
class MapData:
    bounds: Optional[Tuple[float, float]]
    obstacles: List[List[Point]]
    free_vertices: List[Point]
    start: Optional[Point]
    goal: Optional[Point]
def _parse_xy_commas(s: str) -> Point:
    parts = [p.strip() for p in s.split(",")]
    if len(parts) != 2:
        raise ValueError(f"Linha não é um par 'x, y': {s!r}")
    return float(parts[0]), float(parts[1])
def load_map(path: str) -> MapData:
    with open(path, "r", encoding="utf-8") as f:
        raw = [ln.strip() for ln in f if ln.strip() and not ln.strip().startswith("#")]
    if len(raw) < 3:
        raise ValueError("Arquivo de mapa incompleto.")
    start = _parse_xy_commas(raw[0]); goal = _parse_xy_commas(raw[1])
    n_obs = int(raw[2]); idx = 3
    obstacles: List[List[Point]] = []
    for k in range(n_obs):
        if idx >= len(raw): raise ValueError(f"Faltam dados para o obstáculo {k+1}.")
        n_quinas = int(raw[idx]); idx += 1
        poly: List[Point] = []
        for i in range(n_quinas):
            if idx >= len(raw): raise ValueError(f"Faltam quinas para o obstáculo {k+1}.")
            poly.append(_parse_xy_commas(raw[idx])); idx += 1
        if len(poly) < 3: raise ValueError(f"Obstáculo {k+1} precisa de pelo menos 3 quinas.")
        obstacles.append(poly)
    return MapData(bounds=None, obstacles=obstacles, free_vertices=[], start=start, goal=goal)
def all_vertices(md: MapData):
    v = []
    for poly in md.obstacles: v.extend(poly)
    seen = set(); out = []
    for p in v:
        if p not in seen:
            out.append(p); seen.add(p)
    return out
