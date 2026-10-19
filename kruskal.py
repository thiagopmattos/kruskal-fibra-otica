"""Algoritmo de Kruskal para Árvore Geradora Mínima (MST).

Aplicação: conectar laboratórios de uma universidade com o mínimo
de metros de cabo de fibra ótica.
"""

from typing import Hashable

Aresta = tuple[Hashable, Hashable, float]


class UnionFind:
    """Union-Find (conjuntos disjuntos) com compressão de caminho e união por rank."""

    def __init__(self, vertices):
        self.pai = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def encontrar(self, v):
        """Retorna o representante (raiz) do conjunto de v, de forma iterativa."""
        raiz = v
        while self.pai[raiz] != raiz:
            raiz = self.pai[raiz]
        while self.pai[v] != raiz:  # compressão de caminho
            self.pai[v], v = raiz, self.pai[v]
        return raiz

    def unir(self, u, v) -> bool:
        """Une os conjuntos de u e v.

        Retorna False se já estavam no mesmo conjunto (a aresta formaria ciclo).
        """
        raiz_u, raiz_v = self.encontrar(u), self.encontrar(v)
        if raiz_u == raiz_v:
            return False
        if self.rank[raiz_u] < self.rank[raiz_v]:  # união por rank
            raiz_u, raiz_v = raiz_v, raiz_u
        self.pai[raiz_v] = raiz_u
        if self.rank[raiz_u] == self.rank[raiz_v]:
            self.rank[raiz_u] += 1
        return True


def kruskal(vertices: list, arestas: list[Aresta], passos: list | None = None
            ) -> tuple[list[Aresta], float]:
    """Calcula a MST de um grafo conexo, ponderado e não direcionado.

    Args:
        vertices: lista de vértices.
        arestas: lista de tuplas (u, v, peso). Não é modificada.
        passos: se for uma lista, recebe o registro de cada decisão
            (aresta, aceita?, custo acumulado), útil para o relatório.

    Returns:
        (arestas_da_mst, custo_total)

    Raises:
        ValueError: se o grafo for desconexo.

    Complexidade: O(E log E), dominada pela ordenação.
    """
    uf = UnionFind(vertices)
    mst: list[Aresta] = []
    custo_total = 0

    for u, v, peso in sorted(arestas, key=lambda a: a[2]):
        aceita = uf.unir(u, v)  # unir() já detecta ciclo
        if aceita:
            mst.append((u, v, peso))
            custo_total += peso
        if passos is not None:
            passos.append(((u, v, peso), aceita, custo_total))
        if len(mst) == len(vertices) - 1:
            break

    if len(mst) != len(vertices) - 1:
        raise ValueError("O grafo é desconexo: não existe árvore geradora.")

    return mst, custo_total
