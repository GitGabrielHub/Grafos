from grafo_adj_nao_dir import Grafo

# grafoParaiba = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
#                     {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T',
#                      'a8': 'M-T', 'a9': 'T-Z'})


#
# g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
# g_p.adicionaAresta('J-C')
# g_p.adicionaAresta('C-E')
# g_p.adicionaAresta('C-E')
# g_p.adicionaAresta('C-P')
# g_p.adicionaAresta('C-P')
# g_p.adicionaAresta('C-M')
# g_p.adicionaAresta('C-T')
# g_p.adicionaAresta('M-T')
# g_p.adicionaAresta('T-Z')
# #g_p.adicionaAresta('Z-Z')
#

# g_p = Grafo(['J', 'C', 'E', 'P'])
# g_p.adicionaAresta('J-C')
# g_p.adicionaAresta('J-E')
# g_p.adicionaAresta('J-P')
# g_p.adicionaAresta('C-E')
# g_p.adicionaAresta('C-P')
# g_p.adicionaAresta('E-P')

g_p = Grafo(['C', 'D'])
g_p.adicionaAresta('D-C')
g_p.adicionaAresta('C-C')


print(g_p)
print(g_p.vertices_nao_adjacentes())
print(g_p.ha_laco())
print(g_p.ha_paralelas())
print(g_p.grau("C"))
print(g_p.arestas_sobre_vertice("C"))

for x in g_p.N:
    print(g_p.grau(x))
