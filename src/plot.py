
from __future__ import annotations
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
Point = Tuple[float, float]
Graph = Dict[Point, List[Tuple[Point, float]]]
def plot_map(obstacles: List[List[Point]], bounds=None, ax=None):
    if ax is None: fig, ax = plt.subplots()
    for poly in obstacles:
        xs = [p[0] for p in poly] + [poly[0][0]]
        ys = [p[1] for p in poly] + [poly[0][1]]
        ax.plot(xs, ys)
    if bounds: ax.set_xlim(0, bounds[0]); ax.set_ylim(0, bounds[1])
    ax.set_aspect('equal', adjustable='box'); return ax
def plot_graph(g: Graph, ax=None):
    if ax is None: fig, ax = plt.subplots()
    for u, neigh in g.items():
        for v, _ in neigh: ax.plot([u[0], v[0]], [u[1], v[1]])
    xs = [u[0] for u in g.keys()]; ys = [u[1] for u in g.keys()]
    ax.scatter(xs, ys); return ax
def plot_path(path: List[Point], ax=None, annotate=True):
    if not path: return ax
    if ax is None: fig, ax = plt.subplots()
    xs = [p[0] for p in path]; ys = [p[1] for p in path]
    ax.plot(xs, ys, linewidth=3)
    if annotate:
        for i, p in enumerate(path): ax.annotate(str(i), (p[0], p[1]))
    return ax
