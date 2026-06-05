import random


def gerar_grafo(qtd_vertices):

    vertices = list(
        range(qtd_vertices)
    )

    grafo = {}

    for v in vertices:
        grafo[v] = []

    # Garante conectividade mínima
    for i in range(qtd_vertices - 1):

        peso = round(
            random.uniform(1, 10),
            2
        )

        grafo[i].append(
            (i + 1, peso)
        )

        grafo[i + 1].append(
            (i, peso)
        )

    # Arestas extras
    for _ in range(qtd_vertices * 2):

        a = random.randint(
            0,
            qtd_vertices - 1
        )

        b = random.randint(
            0,
            qtd_vertices - 1
        )

        if a != b:

            peso = round(
                random.uniform(1, 10),
                2
            )

            grafo[a].append(
                (b, peso)
            )

            grafo[b].append(
                (a, peso)
            )

    return grafo