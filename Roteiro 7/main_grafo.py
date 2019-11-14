from grafo import Grafo
import string

grafoDrone = Grafo()
alfabeto = list(string.ascii_uppercase)

for letra in alfabeto:
    grafoDrone.adicionaVertice(letra)

for num in range(1,8):
    grafoDrone.adicionaVertice(str(num))


grafoDrone.adicionaAresta('A-B')
grafoDrone.adicionaAresta('A-C')
grafoDrone.adicionaAresta('A-D')

grafoDrone.adicionaAresta('B-H')
grafoDrone.adicionaAresta('B-I')

grafoDrone.adicionaAresta('C-F')

grafoDrone.adicionaAresta('D-C')
grafoDrone.adicionaAresta('D-E')

grafoDrone.adicionaAresta('E-F')
grafoDrone.adicionaAresta('E-L')

grafoDrone.adicionaAresta('F-G')
grafoDrone.adicionaAresta('F-J')
grafoDrone.adicionaAresta('F-K')

grafoDrone.adicionaAresta('G-J')
grafoDrone.adicionaAresta('G-D')

grafoDrone.adicionaAresta('H-G')

grafoDrone.adicionaAresta('L-M')

grafoDrone.adicionaAresta('K-N')

grafoDrone.adicionaAresta('J-I')
grafoDrone.adicionaAresta('J-O')

grafoDrone.adicionaAresta('I-P')

grafoDrone.adicionaAresta('M-Q')

grafoDrone.adicionaAresta('N-R')

grafoDrone.adicionaAresta('O-5')
grafoDrone.adicionaAresta('O-R')
grafoDrone.adicionaAresta('O-Q')

grafoDrone.adicionaAresta('P-T')
grafoDrone.adicionaAresta('P-R')

grafoDrone.adicionaAresta('Q-R')

grafoDrone.adicionaAresta('R-5')
grafoDrone.adicionaAresta('R-Y')

grafoDrone.adicionaAresta('5-T')
grafoDrone.adicionaAresta('5-V')

grafoDrone.adicionaAresta('T-U')

grafoDrone.adicionaAresta('Y-1')
grafoDrone.adicionaAresta('Y-Z')

grafoDrone.adicionaAresta('X-R')

grafoDrone.adicionaAresta('V-X')
grafoDrone.adicionaAresta('V-W')
grafoDrone.adicionaAresta('V-2')

grafoDrone.adicionaAresta('U-7')
grafoDrone.adicionaAresta('U-W')

grafoDrone.adicionaAresta('1-X')
grafoDrone.adicionaAresta('1-3')

grafoDrone.adicionaAresta('7-6')

grafoDrone.adicionaAresta('6-3')

grafoDrone.adicionaAresta('3-4')
grafoDrone.adicionaAresta('3-S')

print(grafoDrone)

# grafo = Grafo()
#
# grafo.adicionaVertice("A")
# grafo.adicionaVertice("B")
# grafo.adicionaVertice("C")
# grafo.adicionaVertice("D")
# grafo.adicionaVertice("E")
# grafo.adicionaVertice("F")
#
# grafo.adicionaAresta("B-A")
# grafo.adicionaAresta("A-C")
# grafo.adicionaAresta("C-E")
# grafo.adicionaAresta("B-D")
# grafo.adicionaAresta("D-E")
# grafo.adicionaAresta("A-D")
# grafo.adicionaAresta("D-B")
# grafo.adicionaAresta("B-F")
# grafo.adicionaAresta("C-F")
# grafo.adicionaAresta("F-A")
#
# print(grafo)
#
print(grafoDrone.djkistra_drone("A", "S",3,5,['L','R','U','6']))