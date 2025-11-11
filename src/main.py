
from __future__ import annotations
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from .map_io import load_map, MapData
from .visibility import build_visibility_graph
from .mst import prim_mst
from .nearest import verticeMaisProximo
from .search import path_in_tree
from .plot import plot_map, plot_graph, plot_path
import matplotlib.pyplot as plt

Point = Tuple[float, float]
Graph = Dict[Point, List[Tuple[Point, float]]]

def _compute_artifacts(map_path: str):
    md: MapData = load_map(map_path)
    g: Graph = build_visibility_graph(md)
    tree: Graph = prim_mst(g)
    s = t = None
    p: Optional[List[Point]] = None
    if md.start and tree:
        s = verticeMaisProximo(md.start, tree, md.obstacles)
    if md.goal and tree:
        t = verticeMaisProximo(md.goal, tree, md.obstacles)
    if s and t:
        p = path_in_tree(tree, s, t)
    return md, g, tree, s, t, p

def run(map_path: str):
    md, g, tree, s, t, p = _compute_artifacts(map_path)
    ax = plot_map(md.obstacles, bounds=md.bounds, obstacle_label="Obstáculos")
    # Grafo de visibilidade (arestas e vértices) - cores mais vívidas
    plot_graph(
        g,
        ax=ax,
        edge_label="Arestas do grafo de visibilidade",
        node_label="Vértices visíveis",
        edge_color="turquoise",
        edge_alpha=0.35,
        edge_linewidth=1.4,
        node_color="dodgerblue",
        node_size=16,
    )
    # MST sobre o grafo de visibilidade (destaque forte)
    if tree:
        plot_graph(
            tree,
            ax=ax,
            edge_label="MST",
            edge_color="crimson",
            edge_alpha=0.95,
            edge_linewidth=2.5,
            draw_nodes=False,
        )
    # Pernas até os vértices mais próximos (vivas)
    if md.start and s:
        ax.plot(
            [md.start[0], s[0]], [md.start[1], s[1]],
            linewidth=2.5, color="limegreen", alpha=0.95,
            label="Conexão do start ao vértice mais próximo",
        )
    if md.goal and t:
        ax.plot(
            [md.goal[0], t[0]], [md.goal[1], t[1]],
            linewidth=2.5, color="fuchsia", alpha=0.95,
            label="Conexão do goal ao vértice mais próximo",
        )
    # Caminho na MST (amarelo forte)
    if p:
        plot_path(p, ax=ax, annotate=True, label="Caminho na MST", color="gold", linewidth=4)
    # Start e Goal
    if md.start:
        ax.scatter([md.start[0]], [md.start[1]], marker='x', c='red', s=60, label='Start', zorder=3)
    if md.goal:
        ax.scatter([md.goal[0]], [md.goal[1]], marker='s', c='lime', s=60, label='Goal', zorder=3)
    plt.title("Mapa + Grafo de visibilidade + MST + Conexões ao vértice mais próximo + Caminho (vívido)")
    ax.legend(loc='upper right', frameon=True, fontsize=9)

    # Salva automaticamente uma cópia na pasta data/
    root = Path(__file__).resolve().parents[1]
    data_dir = root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    map_name = Path(map_path).stem
    outfile = data_dir / f"{map_name}__run.png"
    ax.figure.savefig(outfile, dpi=200, bbox_inches="tight")
    plt.show()

def save_variants(map_path: str, outdir: str):
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    md, g, tree, s, t, p = _compute_artifacts(map_path)
    map_name = Path(map_path).stem

    variants = [
        {
            "name": "default",
            "title": "Default: Grafo, MST e Caminho",
            "vis": {"edge_color": "lightgray", "edge_alpha": 0.6, "node_color": "#666666", "node_size": 12},
            "mst": {"edge_color": "tab:blue", "edge_alpha": 0.9, "edge_linewidth": 2.0},
            "path": {"color": "tab:orange", "linewidth": 3.0},
            "legs": {"start_color": "tab:green", "goal_color": "tab:purple", "alpha": 0.9, "lw": 2.0},
            "show_mst": True, "show_path": True, "show_legs": True,
        },
        {
            "name": "mst-highlight",
            "title": "Destaque para a MST",
            "vis": {"edge_color": "#bbbbbb", "edge_alpha": 0.2, "node_color": "#999999", "node_size": 8},
            "mst": {"edge_color": "crimson", "edge_alpha": 1.0, "edge_linewidth": 3.0},
            "path": {"color": "#ffbf00", "linewidth": 2.5},
            "legs": {"start_color": "#888888", "goal_color": "#888888", "alpha": 0.5, "lw": 1.5},
            "show_mst": True, "show_path": True, "show_legs": True,
        },
        {
            "name": "path-highlight",
            "title": "Destaque para o Caminho",
            "vis": {"edge_color": "#cccccc", "edge_alpha": 0.15, "node_color": "#aaaaaa", "node_size": 6},
            "mst": {"edge_color": "#aaaaaa", "edge_alpha": 0.2, "edge_linewidth": 1.0},
            "path": {"color": "tab:red", "linewidth": 4.0},
            "legs": {"start_color": "#4444aa", "goal_color": "#aa44aa", "alpha": 0.7, "lw": 2.0},
            "show_mst": True, "show_path": True, "show_legs": True,
        },
        {
            "name": "vis-only",
            "title": "Apenas Grafo de Visibilidade",
            "vis": {"edge_color": "tab:gray", "edge_alpha": 0.8, "node_color": "#333333", "node_size": 14},
            "mst": {},
            "path": {},
            "legs": {},
            "show_mst": False, "show_path": False, "show_legs": False,
        },
        {
            "name": "mst-only",
            "title": "Apenas MST",
            "vis": {},
            "mst": {"edge_color": "tab:blue", "edge_alpha": 0.95, "edge_linewidth": 2.5},
            "path": {},
            "legs": {},
            "show_mst": True, "show_path": False, "show_legs": False,
        },
    ]

    for v in variants:
        fig, ax = plt.subplots()
        plot_map(md.obstacles, bounds=md.bounds, obstacle_label="Obstáculos", ax=ax)
        # vis graph
        if g and v.get("vis") is not None and v["vis"]:
            plot_graph(
                g, ax=ax,
                edge_label="Grafo de visibilidade",
                node_label="Vértices visíveis",
                **v["vis"],
            )
        # mst
        if v.get("show_mst", True) and tree:
            plot_graph(
                tree, ax=ax, draw_nodes=False,
                edge_label="MST",
                **v.get("mst", {}),
            )
        # legs
        if v.get("show_legs", False):
            legs = v.get("legs", {})
            lw = legs.get("lw", 2.0); alpha = legs.get("alpha", 0.9)
            if md.start and s:
                ax.plot([md.start[0], s[0]], [md.start[1], s[1]], linewidth=lw, color=legs.get("start_color", "tab:green"), alpha=alpha, label="Conexão Start→Vértice")
            if md.goal and t:
                ax.plot([md.goal[0], t[0]], [md.goal[1], t[1]], linewidth=lw, color=legs.get("goal_color", "tab:purple"), alpha=alpha, label="Conexão Goal→Vértice")
        # path
        if v.get("show_path", True) and p:
            plot_path(p, ax=ax, annotate=True, label="Caminho na MST", **v.get("path", {}))
        # start/goal markers sempre úteis
        if md.start:
            ax.scatter([md.start[0]], [md.start[1]], marker='x', c='tab:red', s=50, label='Start', zorder=3)
        if md.goal:
            ax.scatter([md.goal[0]], [md.goal[1]], marker='s', c='tab:green', s=50, label='Goal', zorder=3)
        ax.legend(loc='upper right', frameon=True, fontsize=9)
        plt.title(v.get("title", v["name"]))
        outfile = out / f"{map_name}__{v['name']}.png"
        fig.savefig(outfile, dpi=200, bbox_inches="tight")
        plt.close(fig)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--map", "-m", required=True, help="Caminho para arquivo de mapa no formato do professor")
    ap.add_argument("--save-variants", "-o", help="Diretório de saída: salva várias imagens com colorações/destaques diferentes e não abre janela interativa")
    args = ap.parse_args()
    if args.save_variants:
        save_variants(args.map, args.save_variants)
    else:
        run(args.map)
