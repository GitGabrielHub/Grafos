from Dijjstrkarkarak import Grafo

grafo = Grafo()

grafo.adicionaVertice("A")
grafo.adicionaVertice("B")
grafo.adicionaVertice("C")
grafo.adicionaVertice("D")
grafo.adicionaVertice("E")
grafo.adicionaVertice("F")



grafo.adicionaAresta("B-A")
grafo.adicionaAresta("A-C")
grafo.adicionaAresta("C-E")
grafo.adicionaAresta("B-D")
grafo.adicionaAresta("D-E")
grafo.adicionaAresta("A-D")
grafo.adicionaAresta("D-B")
grafo.adicionaAresta("B-F")
grafo.adicionaAresta("C-F")
grafo.adicionaAresta("F-A")

print(grafo)

print(grafo.djkistra_drone("B", "E",1,5,['F','C']))