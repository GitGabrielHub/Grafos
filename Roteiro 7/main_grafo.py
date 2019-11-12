from grafo import Grafo

grafo = Grafo()

grafo.adicionaVertice("A")
grafo.adicionaVertice("B")
grafo.adicionaVertice("C")
grafo.adicionaVertice("D")
grafo.adicionaVertice("E")

grafo.adicionaAresta("A-B")
grafo.adicionaAresta("A-C")
grafo.adicionaAresta("C-E")
grafo.adicionaAresta("B-D")
grafo.adicionaAresta("D-E")

print(grafo)
print(grafo.djkistra("A","E"))
