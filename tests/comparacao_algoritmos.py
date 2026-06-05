import sys
import os
import statistics

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, ROOT_DIR)

from src.graph_generator import gerar_grafo
from src.greedy import dijkstra
from src.brute_force import BruteForceSearch
from src.performance_monitor import PerformanceMonitor

tamanhos = [5, 8, 10, 12]

print("\nCOMPARAÇÃO DOS ALGORITMOS")
print("=" * 60)

for n in tamanhos:

    tempos_dijkstra = []
    tempos_brute = []

    for _ in range(50):

        grafo = gerar_grafo(n)

        resultado_dij = (
            PerformanceMonitor.medir(
                dijkstra,
                grafo,
                0
            )
        )

        tempos_dijkstra.append(
            resultado_dij["tempo_ms"]
        )

        busca = BruteForceSearch()

        resultado_fb = (
            PerformanceMonitor.medir(
                busca.encontrar_melhor_caminho,
                grafo,
                0,
                n - 1
            )
        )

        tempos_brute.append(
            resultado_fb["tempo_ms"]
        )

    media_dij = statistics.mean(
        tempos_dijkstra
    )

    media_fb = statistics.mean(
        tempos_brute
    )

    print(
        f"N={n:<2} | "
        f"Dijkstra={media_dij:.4f} ms | "
        f"Força Bruta={media_fb:.4f} ms"
    )