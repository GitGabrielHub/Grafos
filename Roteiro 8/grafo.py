from builtins import Exception
from copy import deepcopy
import sys
import random

class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class MatrizInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0
    pesos = dict()
    pesos.clear()
    MAX = sys.maxsize - 1

    def __init__(self, V=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if V == None:
            V = list()
        if M == None:
            M = list()

        for v in V:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    M[k].append(0)


        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                # if i>j and not(M[i][j] == '-'):
                #                 #     raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada') // momentaneamente comentado


                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not(self.arestaValida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = list(M)

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA)+1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

    def existeAresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v) # Adiciona vértice na lista de vértices
            self.M.append([]) # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) -1:
                    self.M[k].append(0) # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append(0)  # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0) # adiciona os elementos da linha do vértice

        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)

            self.M[i_a1][i_a2] += 1 #adiciona a aresta, agora na forma direcionada

        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def adicionaArestaComPeso(self,a,p = None):
        if p is None:
            p = 1
        self.adicionaAresta(a)
        self.adicionaPeso(a,p)

    def adicionaArestaNaoDirecionadaComPeso(self, a, p): #Método que direciona 'V1-V2' e vice e versa para que se possa ser considerado não-direcionado
        self.adicionaAresta(a)
        self.adicionaAresta(a[::-1]) #Inverte a aresta 'A-B' para 'B-A'
        self.adicionaPeso(a, p)
        self.adicionaPeso(a[::-1], p)

    def adicionaPeso(self,a,p): #Manipula-se um dicionário para adicionar como chave a aresta e como valor o peso da respectiva
        self.pesos[a] = p

    def retornaPeso(self,a):
        try:
            return self.pesos[a]
        except:
            return 1

    def remove_aresta(self, a):
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            if self.existeAresta(a):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                self.M[i_a1][i_a2] -= 1

        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))


    def maior(self, a1, a2):
        if a1 > a2:
            return a1
        return a2

    def desconsidera_paralelas(self, matriz):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] >= 1:
                    matriz[i][j] = 1
        return matriz


    def warshall(self):

        matriz_copia = deepcopy(self.M)
        matriz_copia = self.desconsidera_paralelas(matriz_copia)

        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if matriz_copia[j][i] >= 1:
                    for k in range(len(self.N)):
                        matriz_copia[j][k] = self.maior(matriz_copia[j][k], matriz_copia[i][k])

        return matriz_copia

    def vertice_sobre_vertice(self, vertice):
        vertices = list()
        index = self.N.index(vertice)

        for indice_vertice_1 in range(len(self.N)):
            if self.M[index][indice_vertice_1] > 0:
                vertices.append(self.N[indice_vertice_1])
        return vertices

    def init_djkistra(self,u,carga_atual):
        dic = dict()

        dic[u] = [0,True,None,carga_atual]

        for i in self.N:
            if(i != u ):
                dic[i] = [self.MAX,False,None,0]
        return dic

    def verifica_fi(self, dic):
        for i in dic.values():
            if not i[1]:
                return False
        return True

    def djkistra(self,origem,destino):
        atributosVertice = self.init_djkistra(origem,0)
        u = origem
        v = destino
        w = u
        r = None

        while True:

            if w  == destino:
                if(atributosVertice[w][2] is None):
                    return False
                caminho = self.caminho_djkistra(origem,destino,[],atributosVertice)
                caminho.reverse()
                return caminho

            if self.verifica_fi(atributosVertice):
                return False

            adjacentes = self.vertice_sobre_vertice(w)

            for vertice in adjacentes:
                if(atributosVertice[vertice][0] > atributosVertice[w][0] + self.retornaPeso(w + self.SEPARADOR_ARESTA + vertice)):
                    atributosVertice[vertice][0] = atributosVertice[w][0] + self.retornaPeso(w + self.SEPARADOR_ARESTA + vertice)
                    atributosVertice[vertice][2] = w

            minBeta = self.MAX + 1
            for vertice in self.N:
                if( atributosVertice[vertice][0] < minBeta and not atributosVertice[vertice][1]):
                    minBeta = atributosVertice[vertice][0]
                    r = vertice

            atributosVertice[r][1] = True
            w = r


    def caminho_djkistra(self, origem, destino, lista,atributosVertice):
        lista.append(destino)
        if(origem == destino):
            return lista
        return self.caminho_djkistra(origem,atributosVertice[destino][2],lista,atributosVertice)

    def djkistra_drone(self, origem, destino, carga_atual, carga_maxima, vertices_recargas = []):
        atributosVertice = self.init_djkistra(origem,carga_atual)
        u = origem
        v = destino
        w = u
        r = None

        while True:

            carga_atual = atributosVertice[w][3]

            if (w in vertices_recargas):
                print("recarreguei em ", w)
                carga_atual = carga_maxima

            carga_atual -= 1

            if w == destino:
                if (atributosVertice[w][2] is None):
                    return False

                caminho = self.caminho_djkistra(origem, destino, [], atributosVertice)
                caminho.reverse()
                return caminho

            if self.verifica_fi(atributosVertice):
                return False

            adjacentes = self.vertice_sobre_vertice(w)

            for vertice in adjacentes:
                atributosVertice[vertice][3] = carga_atual
                if (atributosVertice[vertice][0] > atributosVertice[w][0] + self.retornaPeso (
                        w + self.SEPARADOR_ARESTA + vertice) and (carga_atual > 0 or vertice in vertices_recargas)):
                    atributosVertice[vertice][0] = atributosVertice[w][0] + self.retornaPeso(
                        w + self.SEPARADOR_ARESTA + vertice)
                    atributosVertice[vertice][2] = w


            minBeta = self.MAX + 1
            for vertice in self.N:
                if (atributosVertice[vertice][0] < minBeta and not atributosVertice[vertice][1]):
                    minBeta = atributosVertice[vertice][0]
                    r = vertice

            atributosVertice[r][1] = True
            w = r

    def get_min(self, pesos={}):

        menor = min(pesos.values())

        for i in pesos:
            if pesos[i] == menor:
                return i

    def get_max(self, pesos={}):

        maior = max(pesos.values())

        for i in pesos:
            if pesos[i] == maior:
                return i

    def separa_buckets(self, pesos={}):

        mini = self.get_min(pesos)
        maxi = self.get_max(pesos)

        b = 15  # qtde de buckets

        buckets = []
        for i in range(b):
            buckets.append([])

        for i in pesos:
            index = ((pesos[i] - pesos[mini]) /
                     (pesos[maxi] - pesos[mini]))
            index = index * (b - 1)

            index = index + 1

            index = int(index // 1)

            if index == 15:
                index = 14

            buckets[index].append(i)

        return buckets

    def get_key(self, conj, vert):
        for i in conj:
            if vert in conj[i]:
                return i

    def monta_caminho(self, grafo, vertice, cont, caminho=[]):
        caminho.append(vertice)
        caminho.append("a{}".format(cont))
        cont += 1
        adjacentes = self.vertice_sobre_vertice(vertice)
        for v in adjacentes:
            self.monta_caminho(grafo, v, cont, caminho)
        return caminho

    def kruskal(self):
        buckets = self.separa_buckets(self.pesos)

        conjuntos = {}

        for i in range(len(self.N)):
            conjuntos[i] = [self.N[i]]

        n_1 = False

        msp = Grafo()
        conta_arestas = 0

        while not n_1:
            for balde in buckets:
                for aresta in balde:
                    a = aresta
                    vertice1 = a.split(self.SEPARADOR_ARESTA)[0]
                    vertice2 = a.split(self.SEPARADOR_ARESTA)[1]

                    key1 = self.get_key(conjuntos, vertice1)
                    key2 = self.get_key(conjuntos, vertice2)

                    if key1 != key2:
                        for vertice in conjuntos[key2]:
                            conjuntos[key1].append(vertice)
                        conjuntos.pop(key2)
                        if vertice1 not in msp.N:
                            msp.adicionaVertice(vertice1)
                        if vertice2 not in msp.N:
                            msp.adicionaVertice(vertice2)
                        msp.adicionaArestaComPeso(a, self.pesos[a])
                        conta_arestas += 1

                    if len(conjuntos) == 1 or conta_arestas == len(self.N) - 1:
                        n_1 = True
                        break
                if n_1:
                    break
        if n_1:
            return msp

        return False

    def vertice_sobre_vertice_para_o_spanning_tree(self,vertice, vertices_no_spanning_tree): #metodo que pega os vértices adjacentes ao vértice passado como parâmetro, considerando que tais vértices não estejam na árvore
        vertices = list()
        index = self.N.index(vertice)

        for indice_vertice_1 in range(len(self.N)):
            if self.M[index][indice_vertice_1] > 0 and self.N[indice_vertice_1] not in vertices_no_spanning_tree:
                vertices.append(self.N[indice_vertice_1])
        return vertices

    def spanning_tree_prim(self):

        vertice_arbitrario = ""
        minimo = min(self.pesos.values())
        for i in self.pesos.items():
            if(i[1] == minimo):
                vertice_arbitrario = i[0][0]
                break

        print("Vertice escolhido como raiz: ",vertice_arbitrario)
        adjacentes = list()

        spanning_tree = list() #Lista que receberá arestas correspondentes ao spanning_tree
        vertices_no_spanning_tree = [vertice_arbitrario] #Vertices já no spanning tree
        peso = self.MAX

        aresta_spanning_tree = vertice_spanning_tree = None

        while True:
            if(len(vertices_no_spanning_tree) == len(self.N)): #Condição de parada se todos os vértices ja estiverem na árvore
                return spanning_tree

            for vertice in vertices_no_spanning_tree:
                for vertices_adjacentes in self.vertice_sobre_vertice_para_o_spanning_tree(vertice,vertices_no_spanning_tree):
                    adjacentes.append(vertices_adjacentes)

            for vertice_na_tree in vertices_no_spanning_tree:
                for vertice in adjacentes:
                    aresta = vertice_na_tree + self.SEPARADOR_ARESTA + vertice
                    if(aresta in self.pesos and self.retornaPeso(aresta) < peso): #pegando aresta de menor peso existente que ainda não está na spanning tree
                        peso = self.retornaPeso(aresta)
                        aresta_spanning_tree = aresta
                        vertice_spanning_tree = vertice

            spanning_tree.append(aresta_spanning_tree)
            vertices_no_spanning_tree.append(vertice_spanning_tree)
            peso = self.MAX
            adjacentes = []


    def __str__(self):
            '''
            Fornece uma representação do tipo String do grafo.
            O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
            :return: Uma string que representa o grafo
            '''

            # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
            espaco = ' ' * (self.__maior_vertice)

            grafo_str = espaco + ' '

            for v in range(len(self.N)):
                grafo_str += self.N[v]
                if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                    grafo_str += ' '

            grafo_str += '\n'

            for l in range(len(self.M)):
                grafo_str += self.N[l] + ' '
                for c in range(len(self.M)):
                    grafo_str += str(self.M[l][c]) + ' '
                grafo_str += '\n'

            return grafo_str