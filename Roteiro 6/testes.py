from Matriz_adj_dir import Grafo


grafo = Grafo()

Grafo.adicionaVertice(grafo,"A")
Grafo.adicionaVertice(grafo,"B")
Grafo.adicionaVertice(grafo,"C")
Grafo.adicionaVertice(grafo,"D")
Grafo.adicionaVertice(grafo,"E")
Grafo.adicionaVertice(grafo,"F")
Grafo.adicionaVertice(grafo,"G")
Grafo.adicionaVertice(grafo,"H")
Grafo.adicionaVertice(grafo,"I")
Grafo.adicionaVertice(grafo,"J")
Grafo.adicionaVertice(grafo,"K")
Grafo.adicionaVertice(grafo,"L")
Grafo.adicionaVertice(grafo,"M")
Grafo.adicionaVertice(grafo,"N")
Grafo.adicionaVertice(grafo,"O")
Grafo.adicionaVertice(grafo,"P")
Grafo.adicionaVertice(grafo,"Q")
Grafo.adicionaVertice(grafo,"R")
Grafo.adicionaVertice(grafo,"S")
Grafo.adicionaVertice(grafo,"T")

Grafo.adicionaAresta(grafo, "A-B")
Grafo.adicionaAresta(grafo, "A-C")
Grafo.adicionaAresta(grafo, "B-C")
Grafo.adicionaAresta(grafo, "B-D")
Grafo.adicionaAresta(grafo, "C-E")
Grafo.adicionaAresta(grafo, "D-E")
Grafo.adicionaAresta(grafo, "D-F")
Grafo.adicionaAresta(grafo, "E-F")
Grafo.adicionaAresta(grafo, "G-H")
Grafo.adicionaAresta(grafo, "H-I")
Grafo.adicionaAresta(grafo, "I-J")
Grafo.adicionaAresta(grafo, "J-K")
Grafo.adicionaAresta(grafo, "G-L")
Grafo.adicionaAresta(grafo, "H-M")
Grafo.adicionaAresta(grafo, "O-J")
Grafo.adicionaAresta(grafo, "L-M")
Grafo.adicionaAresta(grafo, "M-N")
Grafo.adicionaAresta(grafo, "N-O")
Grafo.adicionaAresta(grafo, "O-L")
Grafo.adicionaAresta(grafo, "B-G")
Grafo.adicionaAresta(grafo, "D-K")
Grafo.adicionaAresta(grafo, "F-J")
Grafo.adicionaAresta(grafo, "E-I")
Grafo.adicionaAresta(grafo, "T-P")
Grafo.adicionaAresta(grafo, "P-Q")
Grafo.adicionaAresta(grafo, "Q-R")
Grafo.adicionaAresta(grafo, "R-S")
Grafo.adicionaAresta(grafo, "S-P")
Grafo.adicionaAresta(grafo, "S-T")
Grafo.adicionaAresta(grafo, "R-T")
Grafo.adicionaAresta(grafo, "T-C")
Grafo.adicionaAresta(grafo, "Q-D")


print(Grafo.__str__(grafo))



# print(Grafo.grau(grafo, 'F'))



# print(Grafo.vertices_adjacentes(grafo,'A'))
# print(Grafo.vertices_adjacentes(grafo,'B'))
# print(Grafo.vertices_adjacentes(grafo,'C'))
# print(Grafo.vertices_adjacentes(grafo,'D'))
# print(Grafo.vertices_adjacentes(grafo,'E'))
# print(Grafo.vertices_adjacentes(grafo,'F'))

# print(Grafo.caminho_euleriano(grafo))

# ciclo = Grafo.ciclo_hamiltoniano(grafo)
# print(ciclo)



grafo2 = Grafo()
print('1\n', grafo2.M)

Grafo.adicionaVertice(grafo2,"A")
print('2\n', grafo2.M)

Grafo.adicionaVertice(grafo2,"B")
print('3\n', grafo2.M)

Grafo.adicionaVertice(grafo2,"C")
print('4\n', grafo2.M)

Grafo.adicionaVertice(grafo2,"D")
print('5\n', grafo2.M)

Grafo.adicionaVertice(grafo2,"E")
print('6\n', grafo2.M)

Grafo.adicionaAresta(grafo2, "A-B")
Grafo.adicionaAresta(grafo2, "A-D")
Grafo.adicionaAresta(grafo2, "B-C")
Grafo.adicionaAresta(grafo2, "B-E")
Grafo.adicionaAresta(grafo2, "C-D")
Grafo.adicionaAresta(grafo2, "D-E")
Grafo.adicionaAresta(grafo2, "C-A")

print()



Grafo.adicionaVertice(grafo2,'F')

print(grafo2)
print(grafo2.M)


# ciclo2= Grafo.ciclo_hamiltoniano(grafo2)
#
# print(ciclo2)

matriz_incidencia = Grafo.warshall(grafo2)
print(matriz_incidencia)
vertices = ['A', 'B', 'C', 'D', 'E', 'F']

matriz_incidenciaa = Grafo(vertices, matriz_incidencia)

print(matriz_incidenciaa)



