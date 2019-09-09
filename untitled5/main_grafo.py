from grafo import Grafo

#grafoParaiba = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
#                     {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T',
#                      'a8': 'M-T', 'a9': 'T-Z'})


#n = ["A","B","C","D","E","J"]
n = ["A","B","C","D","E","J","I"]

#a = {'a1': 'A-B', 'a2': 'B-C', 'a3': 'B-E', 'a4': 'E-D', 'a5': 'D-A', 'a6': 'C-J'}
a = {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-D', 'a4': 'D-E', 'a5': 'E-A','a6': "I-J",'a7' : "J-I" }

grafo = Grafo(n,a)
grafo.ha_ciclo()
print(a)