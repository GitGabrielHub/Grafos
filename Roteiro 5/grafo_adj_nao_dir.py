# -*- coding: utf-8 -*-

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
                    if k>l:
                        M[k].append('-')
                    else:
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
                if i>j and not(M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')


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
                    self.M[self.N.index(v)].append('-') # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
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
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += 1
            else:
                self.M[i_a2][i_a1] += 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

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
                if i_a1 < i_a2:
                    self.M[i_a1][i_a2] -= 1
                else:
                    self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def vertices_nao_adjacentes(self):

        lista_nao_adj = list()

        for indice_1 in range(len(self.M)):
            for indice_2 in range(indice_1,(len(self.M))):
                if(self.M[indice_1][indice_2] == 0):
                    arestas = self.N[indice_1] + self.SEPARADOR_ARESTA + self.N[indice_2]
                    lista_nao_adj.append(arestas)

        return lista_nao_adj

    def ha_laco(self):

        for indice in range(len(self.M)):
            if(self.M[indice][indice] >= 1):
                return True

        return False

    def ha_paralelas(self):

        for indice_1 in range(len(self.M)):
            for indice_2 in range(indice_1,(len(self.M))):
                if(self.M[indice_1][indice_2] >=2):
                    return True

        return False

    def grau(self,vertice):
        index = self.N.index(vertice)+1
        cont = 0

        for indice_1 in range(index):
            for indice_2 in range(indice_1,len(self.M)):
                if(self.M[indice_1][indice_2] > 0 and index-1 in (indice_1,indice_2)):
                    cont+= self.M[indice_1][indice_2]
        return cont

    def arestas_sobre_vertice(self,vertice):
        index = self.N.index(vertice) + 1
        l = []

        for indice_1 in range(index):
            for indice_2 in range(indice_1, len(self.M)):
                if (self.M[indice_1][indice_2] > 0 and index - 1 in (indice_1, indice_2)):
                    arestas = self.N[indice_1] + self.SEPARADOR_ARESTA + self.N[indice_2]
                    l.append(arestas)

        return l

    def eh_completo(self):

        for indice_1 in range(len(self.M)):
            for indice_2 in range(indice_1+1,(len(self.M))):
                if(self.M[indice_1][indice_2] == 0):
                    return False
        return True

    def vertice_sobre_vertice(self,vertice, visitados = []):
        vertices = list()
        index = self.N.index(vertice) + 1

        for indice_1 in range(index):
            for indice_2 in range(indice_1, len(self.M)):
                if (self.M[indice_1][indice_2] > 0 and index - 1 in (indice_1, indice_2)):
                    v1,v2 = self.N[indice_1],self.N[indice_2]
                    if(v1 != vertice and v1 not in visitados): # Adicona a lista vertices adjacentes ao vértive em questão considerando que tal vértice
                        vertices.append(v1)                    # não esteja na lista de visitados.
                    elif(v2 not in visitados):
                        vertices.append(v2)

        return vertices

    def ha_caminho(self,v1,v2,visitados = []):
        if (self.N.index(v1) > self.N.index(v2)):       # Já que o grafo não é direcionado então 'J-Z' == 'Z-J' e o índice de v1 é sempre <= ao índice de v2
            aux = v2                                    # já que apenas da diagonal principal para cima é considerada na matriz de adjacência para grafos não direcionados.
            v2 = v1
            v1 = aux

        visitados.append(v1)
        ind_1 = self.N.index(v1)
        ind_2 = self.N.index(v2)

        if(self.M[ind_1][ind_2] > 0):
            return True

        vertices = self.vertice_sobre_vertice(v1,visitados)
        if(vertices == []):
            return False

        if(self.grau(v1) == 0 or self.grau(v2) == 0):
            return False

        for vertice in vertices:
            if(self.ha_caminho(vertice,v2,visitados)):
                return True

        return False

    def conexo(self):
        vertice = self.N[0]
        for v in self.N[1::]:
            if not(self.ha_caminho(vertice,v,[])):
                return False
        return True

    def matriz_vazia(self):

        for vertice in self.N:
            if(self.grau(vertice) > 0):
                return False
        return True

    def vertice_sobre_vertice_euleriano(self, vertice, visitados=[]):
        vertices = list()
        index = self.N.index(vertice) + 1

        for indice_1 in range(index):
            for indice_2 in range(indice_1, len(self.M)):
                if (self.M[indice_1][indice_2] > 0 and index - 1 in (indice_1, indice_2)):
                    v1, v2 = self.N[indice_1], self.N[indice_2]
                    if (v1 != vertice and (v1 not in visitados or self.grau(v1) > 0)):  # Adicona a lista vertices adjacentes ao vértive em questão considerando que tal vértice
                        vertices.append(v1)  # não esteja na lista de visitados.
                    elif (v2 not in visitados or self.grau(v2) > 0):
                        vertices.append(v2)

        return vertices

    def caminho_euleriano(self):
        if not (self.conexo()):
            return False

        for vertice in self.N:
            lista = self.eh_euleriano(vertice,[],[])
            if( lista != []):
                lista.append(vertice)
                return lista
        return []

    def eh_euleriano(self,vertice,caminho = [],visitados = []):
        visitados.append(vertice)
        vertices = self.vertice_sobre_vertice_euleriano(vertice,visitados)

        if(self.matriz_vazia() and vertices == []):
            return True


        for v in vertices:
            ind_1 = self.N.index(vertice)
            ind_2 = self.N.index(v)
            if (ind_1 > ind_2):
                aux = ind_2
                ind_2 = ind_1
                ind_1 = aux

            self.M[ind_1][ind_2] -= 1

            if(self.eh_euleriano(v,caminho,visitados)):
                caminho.append(v)
                caminho.append(vertice + self.SEPARADOR_ARESTA + v)
                return caminho
            else:
                self.M[ind_1][ind_2] += 1

        return []

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' '*(self.__maior_vertice)

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































