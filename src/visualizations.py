import networkx as nx
import matplotlib.pyplot as plt


# ==========================================
# DADOS DOS MUNICÍPIOS
# ==========================================

MUNICIPIOS = {
    4314902: ("Porto Alegre", 0.95),
    4304606: ("Canoas", 0.90),
    4318705: ("São Leopoldo", 0.85),
    4313409: ("Novo Hamburgo", 0.82),
    4305108: ("Caxias do Sul", 0.60),
    4314407: ("Pelotas", 0.70),
    4301602: ("Bagé", 0.55),
    4323002: ("Viamão", 0.80),
    4316808: ("Santa Maria", 0.65),
    4303509: ("Campo Bom", 0.75)
}


# ==========================================
# CORES POR RISCO
# ==========================================

def obter_cor(risco):

    if risco >= 0.80:
        return "red"

    elif risco >= 0.60:
        return "gold"

    return "lightgreen"


# ==========================================
# GRAFO DOS MUNICÍPIOS
# ==========================================

def desenhar_grafo(grafo, caminho_destacado=None):

    G = nx.Graph()

    for origem in grafo:

        for destino, peso in grafo[origem]:

            G.add_edge(
                origem,
                destino,
                weight=peso
            )

    plt.figure(figsize=(16, 10))

    pos = nx.spring_layout(
        G,
        seed=42,
        k=1.2
    )

    labels = {
        codigo: MUNICIPIOS[codigo][0]
        for codigo in MUNICIPIOS
    }

    cores = [
        obter_cor(
            MUNICIPIOS[vertice][1]
        )
        for vertice in G.nodes()
    ]

    nx.draw_networkx_nodes(
        G,
        pos,
        node_color=cores,
        node_size=3000
    )

    nx.draw_networkx_labels(
        G,
        pos,
        labels,
        font_size=8,
        font_weight="bold"
    )

    nx.draw_networkx_edges(
        G,
        pos,
        width=2
    )

    pesos = nx.get_edge_attributes(
        G,
        "weight"
    )

    nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=pesos,
    font_size=9,
    label_pos=0.35,
    bbox=dict(
        facecolor="white",
        edgecolor="none",
        alpha=0.8
    )
    )

    # ======================================
    # DESTACA O CAMINHO DO DIJKSTRA
    # ======================================

    if caminho_destacado:

        arestas_caminho = []

        for i in range(
            len(caminho_destacado) - 1
        ):

            arestas_caminho.append(
                (
                    caminho_destacado[i],
                    caminho_destacado[i + 1]
                )
            )

        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=arestas_caminho,
            width=2,
            edge_color="blue"
        )

    plt.title(
        "Rede de Municípios do Rio Grande do Sul",
        fontsize=16,
        fontweight="bold"
    )

    plt.figtext(
        0.5,
        0.01,
        "Fonte: Dados sintéticos baseados em municípios afetados pelas enchentes do RS.",
        ha="center",
        fontsize=9
    )

    plt.tight_layout()

    plt.subplots_adjust(
    bottom = 0.10
    )

    plt.savefig(
        "report/grafo_municipios.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ==========================================
# TEMPO X N
# ==========================================

def grafico_tempo(
    tamanhos,
    tempos_fb,
    tempos_dijkstra
):

    plt.figure(figsize=(10, 6))

    plt.plot(
        tamanhos,
        tempos_fb,
        marker="o",
        linewidth=3,
        label="Força Bruta"
    )

    plt.plot(
        tamanhos,
        tempos_dijkstra,
        marker="s",
        linewidth=3,
        label="Dijkstra"
    )

    plt.title(
        "Tempo de Execução × Número de Vértices",
        fontsize=15
    )

    plt.xlabel(
        "Quantidade de Vértices"
    )

    plt.ylabel(
        "Tempo (ms)"
    )

    plt.grid(True)

    plt.legend()

    plt.savefig(
        "report/tempo_x_n.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ==========================================
# GAP DE OTIMALIDADE
# ==========================================

def grafico_gap(
    tamanhos,
    gaps
):

    plt.figure(figsize=(10, 6))

    plt.plot(
        tamanhos,
        gaps,
        marker="D",
        linewidth=3
    )

    plt.title(
        "Gap de Otimalidade (%)",
        fontsize=15
    )

    plt.xlabel(
        "Quantidade de Vértices"
    )

    plt.ylabel(
        "Gap (%)"
    )

    plt.grid(True)

    plt.savefig(
        "report/gap_otimalidade.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

from collections import deque

def desenhar_bst(root):

    if root is None:
        return

    G = nx.DiGraph()

    fila = deque([root])

    while fila:

        atual = fila.popleft()

        label = (
            f"{atual.municipio[1]}\n"
            f"({atual.risco:.2f})"
        )

        G.add_node(label)

        if atual.left:

            left_label = (
                f"{atual.left.municipio[1]}\n"
                f"({atual.left.risco:.2f})"
            )

            G.add_edge(
                label,
                left_label
            )

            fila.append(
                atual.left
            )

        if atual.right:

            right_label = (
                f"{atual.right.municipio[1]}\n"
                f"({atual.right.risco:.2f})"
            )

            G.add_edge(
                label,
                right_label
            )

            fila.append(
                atual.right
            )

    plt.figure(figsize=(20, 12))

    pos = nx.spring_layout(
        G,
        seed=42,
        k=3.0,
        iterations=100
    )

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=5000,
        font_size=8
    )

    plt.title(
        "BST dos Municípios por Índice de Risco"
    )

    plt.savefig(
        "report/bst_municipios.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()