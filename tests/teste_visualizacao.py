import sys
import os

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, ROOT_DIR)

from data.processed.grafo_rs import grafo
from src.visualizations import desenhar_grafo

caminho_dijkstra = [
    4314902,
    4313409,
    4305108
]

desenhar_grafo(
    grafo,
    caminho_destacado=caminho_dijkstra
)