import sys
import os

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, ROOT_DIR)

from src.visualizations import (
    grafico_tempo,
    grafico_gap
)

# ==========================
# DADOS REAIS OBTIDOS
# ==========================

tamanhos = [5, 8, 10, 12]

tempos_dijkstra = [
    0.0185,
    0.0284,
    0.0362,
    0.0481
]

tempos_bruteforce = [
    0.0673,
    0.5949,
    3.7801,
    24.2847
]

# ==========================
# GAP
# ==========================

gaps = [
    0,
    0,
    0,
    0
]

# ==========================
# GERAR FIGURAS
# ==========================

grafico_tempo(
    tamanhos,
    tempos_bruteforce,
    tempos_dijkstra
)

grafico_gap(
    tamanhos,
    gaps
)

print(
    "\nGráficos gerados com sucesso!"
)