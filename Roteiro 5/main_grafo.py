from grafo_adj_nao_dir import Grafo

# grafoParaiba = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
#                     {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T',
#                      'a8': 'M-T', 'a9': 'T-Z'})



g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p.adicionaAresta('J-C')
g_p.adicionaAresta('C-E')
g_p.adicionaAresta('C-E')
g_p.adicionaAresta('C-P')
g_p.adicionaAresta('C-P')
g_p.adicionaAresta('C-M')
g_p.adicionaAresta('C-T')
g_p.adicionaAresta('M-T')
g_p.adicionaAresta('T-Z')
# g_p.adicionaAresta('H-I')
# g_p.adicionaAresta('Z-Z')


# g_p = Grafo(['J', 'C', 'E', 'P'])
# g_p.adicionaAresta('J-C')
# g_p.adicionaAresta('J-E')
# g_p.adicionaAresta('J-P')
# g_p.adicionaAresta('C-E')
# g_p.adicionaAresta('C-P')
# g_p.adicionaAresta('E-P')

# g_p = Grafo(['C', 'D'])
# g_p.adicionaAresta('D-C')
# g_p.adicionaAresta('C-C')


# g_p = Grafo(['A','B','C','D','E','J'])
# g_p.adicionaAresta('A-B')
# g_p.adicionaAresta('A-C')
# g_p.adicionaAresta('C-D')
# g_p.adicionaAresta('C-J')
# g_p.adicionaAresta('C-J')
# g_p.adicionaAresta('D-E')

print(g_p)
# print(g_p.vertices_nao_adjacentes())
# print(g_p.ha_laco())
# print(g_p.ha_paralelas())
# print(g_p.grau("C"))
# print(g_p.arestas_sobre_vertice("C"))
# print(g_p.vertice_sobre_vertice("P"))
print(g_p.ha_caminho("J","E"))
print(g_p.conexo())
print(g_p.caminho_euleriano()[::-1])
