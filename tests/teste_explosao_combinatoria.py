import sys
import os
import matplotlib.pyplot as plt

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, ROOT_DIR)

from src.graph_generator import gerar_grafo
from src.brute_force import BruteForceSearch

tamanhos = [5, 6, 7, 8, 9, 10]

caminhos = []
recursivas = []

for n in tamanhos:

    grafo = gerar_grafo(n)

    busca = BruteForceSearch()

    resultado = busca.encontrar_melhor_caminho(
        grafo,
        0,
        n - 1
    )

    caminhos.append(
        resultado["caminhos_avaliados"]
    )

    recursivas.append(
        resultado["chamadas_recursivas"]
    )

# ==========================
# CAMINHOS X N
# ==========================

plt.figure(figsize=(10, 6))

plt.plot(
    tamanhos,
    caminhos,
    marker="o",
    linewidth=3,
    label="Caminhos Avaliados"
)

plt.title(
    "Figura 6 – Crescimento do Número de Caminhos",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Número de Vértices (N)")
plt.ylabel("Quantidade de Caminhos")

plt.grid(True)

plt.legend()

plt.figtext(
    0.5,
    0.01,
    "Fonte: Resultados obtidos pela busca exaustiva com backtracking.",
    ha="center",
    fontsize=9
)

plt.subplots_adjust(bottom=0.12)

plt.savefig(
    "report/caminhos_x_n.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================
# RECURSÃO X N
# ==========================

plt.figure(figsize=(10, 6))

plt.plot(
    tamanhos,
    recursivas,
    marker="s",
    linewidth=3,
    label="Chamadas Recursivas"
)

plt.title(
    "Figura 7 – Crescimento das Chamadas Recursivas",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Número de Vértices (N)")
plt.ylabel("Chamadas Recursivas")

plt.grid(True)

plt.legend()

plt.figtext(
    0.5,
    0.01,
    "Fonte: Instrumentação do algoritmo de força bruta.",
    ha="center",
    fontsize=9
)

plt.subplots_adjust(bottom=0.12)

plt.savefig(
    "report/recursao_x_n.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nGráficos gerados com sucesso!")