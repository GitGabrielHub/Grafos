from builtins import Exception
from copy import deepcopy
import sys


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
    MAX = sys.maxsize

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

    def adicionaArestaComPeso(self,a,p):
        self.adicionaAresta(a)
        self.adicionaPeso(a,p)

    def adicionaPeso(self,a,p):
        self.pesos[a] = p

    def retornaPeso(self,a):
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

    def init_djkistra(self,u):
        dic = dict()

        dic[u] = [0,True,None]

        for i in self.N:
            if(i != u ):
                dic[i] = [self.MAX,False,None]
        return dic

    def verifica_fi(self, dic):
        for i in dic.values():
            if not i[1]:
                return False
        return True

    def djkistra(self,origem,destino):
        atributosVertice = self.init_djkistra(origem)
        u = origem
        v = destino
        w = u
        r = None

        while True:

            if w  == destino:
                return self.caminho_djkistra(origem,destino,[],atributosVertice)

            if self.verifica_fi(atributosVertice):
                return False

            adjacentes = self.vertice_sobre_vertice(w)

            for vertice in adjacentes:
                if(atributosVertice[vertice][0] > atributosVertice[w][0] + self.retornaPeso(w + self.SEPARADOR_ARESTA + vertice)):
                    atributosVertice[vertice][0] = atributosVertice[w][0] + self.retornaPeso(w + self.SEPARADOR_ARESTA + vertice)
                    atributosVertice[vertice][2] = w

            minBeta = self.MAX
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
