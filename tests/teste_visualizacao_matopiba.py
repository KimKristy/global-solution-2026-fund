from data.processed.grafo_matopiba import grafo_matopiba
from src.visualizations import desenhar_grafo_matopiba

caminho_dijkstra = [
    1001,
    1002,
    1005,
    1010
]

desenhar_grafo_matopiba(
    grafo_matopiba,
    caminho_dijkstra
)