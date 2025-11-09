
from __future__ import annotations
import argparse
from .map_io import load_map
from .visibility import build_visibility_graph
from .mst import prim_mst
from .nearest import verticeMaisProximo
from .search import path_in_tree
from .plot import plot_map, plot_graph, plot_path
import matplotlib.pyplot as plt

def run(map_path: str):
    md = load_map(map_path)
    g = build_visibility_graph(md)
    tree = prim_mst(g)
    s = t = None
    p = None
    if md.start and tree:
        s = verticeMaisProximo(md.start, tree, md.obstacles)
    if md.goal and tree:
        t = verticeMaisProximo(md.goal, tree, md.obstacles)
    if s and t:
        p = path_in_tree(tree, s, t)
    ax = plot_map(md.obstacles, bounds=md.bounds)
    plot_graph(g, ax=ax)
    if md.start and s:
        ax.plot([md.start[0], s[0]], [md.start[1], s[1]], linewidth=2)
    if md.goal and t:
        ax.plot([md.goal[0], t[0]], [md.goal[1], t[1]], linewidth=2)
    if p:
        plot_path(p, ax=ax, annotate=True)
    if md.start:
        ax.scatter([md.start[0]], [md.start[1]], marker='x')
    if md.goal:
        ax.scatter([md.goal[0]], [md.goal[1]], marker='s')
    plt.title("Mapa (formato do professor) + Grafo + MST + pernas até vértices visíveis mais próximos")
    plt.show()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--map", "-m", required=True, help="Caminho para arquivo de mapa no formato do professor")
    args = ap.parse_args()
    run(args.map)
