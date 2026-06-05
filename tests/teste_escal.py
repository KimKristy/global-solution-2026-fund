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
from src.performance_monitor import (
    PerformanceMonitor
)

tamanhos = [
    5,
    8,
    10,
    12,
    20,
    50,
    100
]

print("\nRESULTADOS MÉDIOS")
print("=" * 50)

for n in tamanhos:

    tempos = []

    for _ in range(100):

        grafo = gerar_grafo(n)

        resultado = (
            PerformanceMonitor.medir(
                dijkstra,
                grafo,
                0
            )
        )

        tempos.append(
            resultado["tempo_ms"]
        )

    media = statistics.mean(
        tempos
    )

    desvio = statistics.stdev(
        tempos
    )

    print(
        f"N={n:<3} | "
        f"Média={media:.4f} ms | "
        f"Desvio={desvio:.4f}"
    )