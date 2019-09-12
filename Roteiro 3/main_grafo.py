from grafo import Grafo

# grafoParaiba = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
#                     {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T',
#                      'a8': 'M-T', 'a9': 'T-Z'})


n = ["A", "B", "C", "D", "E", "J"]
a = {'a1': 'A-B', 'a2': 'B-C', 'a3': 'B-E', 'a4': 'E-D', 'a5': 'D-A', 'a6': 'C-J'}

grafo = Grafo(n, a)
print(grafo.ha_ciclo())

if (grafo.conexo()):
    print("É conexo")

else:
    print("Não é conexo")

n = ["A", "B", "C", "D", "E", "J"]
a = {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-D', 'a4': 'D-E', 'a5': 'E-A', 'a6': "B-J"}

grafo = Grafo(n, a)
print(grafo.ha_ciclo())

if (grafo.conexo()):
    print("É conexo")

else:
    print("Não é conexo")

n = ["J", "C", "D", "A"]
a = {"a1": "A-J", "a2": "J-C", "a3": "C-D", "a4": "D-J"}

grafo = Grafo(n, a)
print(grafo.ha_ciclo())

if (grafo.conexo()):
    print("É conexo")

else:
    print("Não é conexo")

n = ["A", "B", "C", "D", "E", "J"]
a = {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-D', 'a4': 'D-E', 'a6': "B-J"}

grafo = Grafo(n, a)
print(grafo.ha_ciclo())

if (grafo.conexo()):
    print("É conexo")

else:
    print("Não é conexo")

n = ["A", "B", "C", "D", "E", "J"]
a = {'a1': 'A-B', 'a3': 'C-D', 'a4': 'E-E', 'a6': "B-J"}

grafo = Grafo(n, a)
print(grafo.ha_ciclo())

if (grafo.conexo()):
    print("É conexo")
else:
    print("Não é conexo")
