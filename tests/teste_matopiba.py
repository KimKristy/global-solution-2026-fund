# ==========================================
# TESTE - CENÁRIO MATOPIBA
# ==========================================

from data.processed.grafo_matopiba import grafo_matopiba
from src.greedy import (
    dijkstra,
    reconstruir_caminho
)


origem = 1001      # Balsas
destino = 1010     # São Desidério

distancias, predecessores, operacoes = dijkstra(
    grafo_matopiba,
    origem
)

caminho = reconstruir_caminho(
    predecessores,
    origem,
    destino
)

print("\nCENÁRIO MATOPIBA")
print("=" * 40)

print("\nDistâncias:")
print(distancias)

print("\nOperações:")
print(operacoes)

print("\nMelhor caminho:")
print(caminho)

print("\nCusto total:")
print(distancias[destino])