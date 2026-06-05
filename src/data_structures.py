# ==========================================
# ESTRUTURAS DE DADOS - GLOBAL SOLUTION 2026
# ==========================================

class Node:
    """
    Nó da Árvore Binária de Busca (BST)
    """

    def __init__(self, municipio):
        self.municipio = municipio

        # índice de risco é a chave
        self.risco = municipio[2]

        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    # -------------------------
    # INSERÇÃO
    # -------------------------
    def insert(self, municipio):

        if self.root is None:
            self.root = Node(municipio)
        else:
            self._insert(self.root, municipio)

    def _insert(self, current, municipio):

        risco = municipio[2]

        if risco < current.risco:

            if current.left is None:
                current.left = Node(municipio)
            else:
                self._insert(current.left, municipio)

        else:

            if current.right is None:
                current.right = Node(municipio)
            else:
                self._insert(current.right, municipio)

    # -------------------------
    # IN ORDER
    # -------------------------
    def in_order(self):

        resultado = []

        self._in_order(self.root, resultado)

        return resultado

    def _in_order(self, node, resultado):

        if node:

            self._in_order(node.left, resultado)

            resultado.append(node.municipio)

            self._in_order(node.right, resultado)

    # -------------------------
    # BUSCA POR INTERVALO
    # -------------------------
    def search_range(self, minimo, maximo):

        resultado = []

        self._search_range(
            self.root,
            minimo,
            maximo,
            resultado
        )

        return resultado

    def _search_range(
        self,
        node,
        minimo,
        maximo,
        resultado
    ):

        if node is None:
            return

        if minimo < node.risco:
            self._search_range(
                node.left,
                minimo,
                maximo,
                resultado
            )

        if minimo <= node.risco <= maximo:
            resultado.append(node.municipio)

        if node.risco < maximo:
            self._search_range(
                node.right,
                minimo,
                maximo,
                resultado
            )

    # -------------------------
    # ALTURA
    # -------------------------
    def height(self):

        return self._height(self.root)

    def _height(self, node):

        if node is None:
            return 0

        esquerda = self._height(node.left)
        direita = self._height(node.right)

        return 1 + max(esquerda, direita)

    # -------------------------
    # REMOÇÃO
    # -------------------------
    def remove(self, risco):

        self.root = self._remove(
            self.root,
            risco
        )

    def _remove(self, node, risco):

        if node is None:
            return node

        if risco < node.risco:

            node.left = self._remove(
                node.left,
                risco
            )

        elif risco > node.risco:

            node.right = self._remove(
                node.right,
                risco
            )

        else:

            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            sucessor = self._min_value_node(
                node.right
            )

            node.municipio = sucessor.municipio
            node.risco = sucessor.risco

            node.right = self._remove(
                node.right,
                sucessor.risco
            )

        return node

    def _min_value_node(self, node):

        atual = node

        while atual.left:
            atual = atual.left

        return atual


# ==========================================
# GRAFO
# ==========================================

class Graph:

    def __init__(self):
        self.adjacencia = {}

    def add_vertex(self, vertice):

        id_municipio = vertice[0]

        if id_municipio not in self.adjacencia:
            self.adjacencia[id_municipio] = []

    def add_edge(self, origem, destino, peso):

        self.adjacencia[origem].append(
            (destino, peso)
        )

        self.adjacencia[destino].append(
            (origem, peso)
        )

    def get_neighbors(self, vertice):

        return self.adjacencia.get(
            vertice,
            []
        )

    def show_graph(self):

        for vertice, vizinhos in self.adjacencia.items():

            print(
                f"{vertice} -> {vizinhos}"
            )