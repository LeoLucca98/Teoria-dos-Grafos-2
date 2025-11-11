
from __future__ import annotations
from typing import Dict, List, Tuple, Optional
import matplotlib.pyplot as plt
Point = Tuple[float, float]
Graph = Dict[Point, List[Tuple[Point, float]]]
def plot_map(
    obstacles: List[List[Point]],
    bounds=None,
    ax=None,
    *,
    obstacle_label: Optional[str] = "Obstáculos",
    obstacle_color: str = "black",
    obstacle_alpha: float = 0.8,
):
    """Plota os polígonos (obstáculos) do mapa.

    Params
    - obstacles: lista de polígonos (cada polígono é uma lista de pontos)
    - bounds: tupla (largura, altura)
    - ax: eixo Matplotlib opcional
    - obstacle_label: rótulo para legenda (apenas no primeiro polígono)
    - obstacle_color/alpha: estilo das bordas dos polígonos
    """
    if ax is None:
        fig, ax = plt.subplots()
    first = True
    for poly in obstacles:
        xs = [p[0] for p in poly] + [poly[0][0]]
        ys = [p[1] for p in poly] + [poly[0][1]]
        label = obstacle_label if first else "_nolegend_"
        ax.plot(xs, ys, color=obstacle_color, alpha=obstacle_alpha, label=label)
        first = False
    if bounds:
        ax.set_xlim(0, bounds[0])
        ax.set_ylim(0, bounds[1])
    ax.set_aspect('equal', adjustable='box')
    return ax

def plot_graph(
    g: Graph,
    ax=None,
    *,
    edge_label: Optional[str] = None,
    node_label: Optional[str] = None,
    edge_color: str = "#888888",
    edge_alpha: float = 0.6,
    edge_linewidth: float = 1.0,
    node_color: str = "#444444",
    node_size: float = 15,
    draw_nodes: bool = True,
):
    """Plota um grafo em um eixo.

    - edge_label/node_label: rótulos opcionais para legenda
    - draw_nodes: permite suprimir nós (útil para sobrepor múltiplos grafos)
    """
    if ax is None:
        fig, ax = plt.subplots()
    first_edge = True
    for u, neigh in g.items():
        for v, _ in neigh:
            # Só rotula a primeira aresta para evitar entradas duplicadas
            label = edge_label if first_edge else "_nolegend_"
            ax.plot(
                [u[0], v[0]], [u[1], v[1]],
                color=edge_color, alpha=edge_alpha, linewidth=edge_linewidth,
                label=label,
            )
            first_edge = False
    if draw_nodes and g:
        xs = [u[0] for u in g.keys()]
        ys = [u[1] for u in g.keys()]
        ax.scatter(xs, ys, c=node_color, s=node_size, label=node_label)
    return ax

def plot_path(
    path: List[Point],
    ax=None,
    annotate: bool = True,
    *,
    label: Optional[str] = None,
    color: str = "tab:orange",
    linewidth: float = 3.0,
    alpha: float = 0.9,
):
    """Plota um caminho ordenado de pontos.

    - label: rótulo para legenda
    - annotate: numera os vértices do caminho
    """
    if not path:
        return ax
    if ax is None:
        fig, ax = plt.subplots()
    xs = [p[0] for p in path]
    ys = [p[1] for p in path]
    ax.plot(xs, ys, linewidth=linewidth, color=color, alpha=alpha, label=label)
    if annotate:
        for i, p in enumerate(path):
            ax.annotate(str(i), (p[0], p[1]))
    return ax
