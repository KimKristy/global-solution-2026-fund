# ==========================================
# ALGORITMO GULOSO - DIJKSTRA
# ==========================================

import heapq


def dijkstra(grafo, origem):

    # Distâncias mínimas
    distancias = {
        vertice: float("inf")
        for vertice in grafo
    }

    distancias[origem] = 0

    # Guarda o caminho
    predecessores = {}

    # Heap (fila de prioridade)
    heap = [(0, origem)]

    operacoes = 0

    while heap:

        distancia_atual, vertice_atual = heapq.heappop(heap)

        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo[vertice_atual]:

            operacoes += 1

            nova_distancia = (
                distancia_atual + peso
            )

            if nova_distancia < distancias[vizinho]:

                distancias[vizinho] = nova_distancia

                predecessores[vizinho] = vertice_atual

                heapq.heappush(
                    heap,
                    (nova_distancia, vizinho)
                )

    return (
        distancias,
        predecessores,
        operacoes
    )


# ==========================================
# RECONSTRUÇÃO DO CAMINHO
# ==========================================

def reconstruir_caminho(
    predecessores,
    origem,
    destino
):

    caminho = []

    atual = destino

    while atual != origem:

        caminho.append(atual)

        atual = predecessores.get(atual)

        if atual is None:
            return []

    caminho.append(origem)

    caminho.reverse()

    return caminho