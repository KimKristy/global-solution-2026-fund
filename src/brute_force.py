# ==========================================
# FORÇA BRUTA - ENUMERAÇÃO DE CAMINHOS
# ==========================================

class BruteForceSearch:

    def __init__(self):
        self.melhor_caminho = None
        self.melhor_custo = float("inf")

        self.chamadas_recursivas = 0
        self.caminhos_avaliados = 0

    def encontrar_melhor_caminho(
        self,
        grafo,
        origem,
        destino
    ):

        self.melhor_caminho = None
        self.melhor_custo = float("inf")

        self.chamadas_recursivas = 0
        self.caminhos_avaliados = 0

        self._backtracking(
            grafo,
            origem,
            destino,
            set(),
            [],
            0
        )

        return {
            "melhor_caminho": self.melhor_caminho,
            "melhor_custo": self.melhor_custo,
            "chamadas_recursivas": self.chamadas_recursivas,
            "caminhos_avaliados": self.caminhos_avaliados
        }

    def _backtracking(
        self,
        grafo,
        atual,
        destino,
        visitados,
        caminho,
        custo
    ):

        self.chamadas_recursivas += 1

        visitados.add(atual)
        caminho.append(atual)

        if atual == destino:

            self.caminhos_avaliados += 1

            if custo < self.melhor_custo:

                self.melhor_custo = custo
                self.melhor_caminho = caminho.copy()

        else:

            for vizinho, peso in grafo[atual]:

                if vizinho not in visitados:

                    self._backtracking(
                        grafo,
                        vizinho,
                        destino,
                        visitados,
                        caminho,
                        custo + peso
                    )

        caminho.pop()
        visitados.remove(atual)