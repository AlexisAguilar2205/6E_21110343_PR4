
import sys

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def prim(self):
        clave = [sys.maxsize] * self.V
        padre = [None] * self.V
        clave[0] = 0
        mstSet = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(clave, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.grafo[u][v] and not mstSet[v] and self.grafo[u][v] < clave[v]:
                    padre[v] = u
                    clave[v] = self.grafo[u][v]

        self.imprimir_mst(padre)

    def min_key(self, clave, mstSet):
        minimo = sys.maxsize
        minimo_indice = -1

        for v in range(self.V):
            if clave[v] < minimo and not mstSet[v]:
                minimo = clave[v]
                minimo_indice = v

        return minimo_indice

    def imprimir_mst(self, padre):
        print("Arista \tPeso")
        for i in range(1, self.V):
            print(f"{padre[i]} - {i}\t{self.grafo[i][padre[i]]}")

# Ejemplo de uso
grafo = Grafo(5)
grafo.grafo = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

grafo.prim()