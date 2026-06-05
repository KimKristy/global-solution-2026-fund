import sys
import os

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(0, ROOT_DIR)

from src.data_structures import BinarySearchTree
from src.greedy import (
    dijkstra,
    reconstruir_caminho
)
from src.brute_force import BruteForceSearch

from data.processed.grafo_rs import grafo


# ==========================================
# TESTE BST
# ==========================================

def test_bst_insert():

    bst = BinarySearchTree()

    bst.insert(
        (1, "Cidade A", 0.8, 1000, 10000)
    )

    bst.insert(
        (2, "Cidade B", 0.5, 1000, 10000)
    )

    bst.insert(
        (3, "Cidade C", 0.9, 1000, 10000)
    )

    assert bst.root is not None


def test_bst_height():

    bst = BinarySearchTree()

    bst.insert(
        (1, "Cidade A", 0.8, 1000, 10000)
    )

    bst.insert(
        (2, "Cidade B", 0.5, 1000, 10000)
    )

    bst.insert(
        (3, "Cidade C", 0.9, 1000, 10000)
    )

    assert bst.height() > 0


# ==========================================
# TESTE DIJKSTRA
# ==========================================

def test_dijkstra():

    origem = 4314902

    distancias, predecessores, operacoes = (
        dijkstra(
            grafo,
            origem
        )
    )

    assert (
        distancias[4305108] == 2.4
    )


def test_caminho_dijkstra():

    origem = 4314902
    destino = 4305108

    distancias, predecessores, operacoes = (
        dijkstra(
            grafo,
            origem
        )
    )

    caminho = reconstruir_caminho(
        predecessores,
        origem,
        destino
    )

    assert caminho == [
        4314902,
        4313409,
        4305108
    ]


# ==========================================
# TESTE FORÇA BRUTA
# ==========================================

def test_bruteforce():

    busca = BruteForceSearch()

    resultado = (
        busca.encontrar_melhor_caminho(
            grafo,
            4314902,
            4305108
        )
    )

    assert (
        resultado["melhor_custo"]
        == 2.4
    )


def test_bruteforce_path():

    busca = BruteForceSearch()

    resultado = (
        busca.encontrar_melhor_caminho(
            grafo,
            4314902,
            4305108
        )
    )

    assert (
        resultado["melhor_caminho"]
        ==
        [
            4314902,
            4313409,
            4305108
        ]
    )