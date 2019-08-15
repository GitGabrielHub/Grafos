from grafo import Grafo

n = ["J", 'C', "E", "P", "M", "T", "Z"]
g = {"a1":"J-C", "a2":"C-E", "a3":"C-E",
     "a4":"C-P", "a5":"C-P", "a6":"C-M",
     "a7":"C-T", "a8":"M-T", "a9":"T-Z"}


grafo = Grafo(n,g)
print(grafo)