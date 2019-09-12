class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not (self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

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

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    def vertices_nao_adjacentes(self):
        aresta = list(self.A.values())
        resultado = []
        for x in self.N:
            for y in self.N:
                aresta_indo = x + self.SEPARADOR_ARESTA + y
                aresta_vindo = y + self.SEPARADOR_ARESTA + x
                if (aresta_indo not in aresta) and (aresta_vindo not in aresta):
                    resultado.append(aresta_indo)

        return resultado

    def ha_laco(self):
        for x in self.A.values():
            if x.split(self.SEPARADOR_ARESTA)[0] == x.split(self.SEPARADOR_ARESTA)[1]:
                return True
        return False

    def ha_paralelas(self):
        arestas = self.A.values()
        index1 = 0
        for i in arestas:
            index2 = 0
            aresta = i.split(self.SEPARADOR_ARESTA)
            paralela = aresta[-1] + self.SEPARADOR_ARESTA + aresta[0]
            for j in arestas:
                if index1 != index2:
                    if (j == paralela) or (j == i):
                        return True
                index2 += 1
            index1 += 1
            index2 = 0
        return False

    def grau(self, vertice):
        cont = 0
        for x in self.A:
            if self.A[x].split(self.SEPARADOR_ARESTA)[0] == vertice or self.A[x].split(self.SEPARADOR_ARESTA)[
                1] == vertice:
                cont += 1
        return cont

    def arestas_sobre_vertice(self, vertice):
        arestas = []
        for x in self.A:
            if self.A[x].split(self.SEPARADOR_ARESTA)[0] == vertice or self.A[x].split(self.SEPARADOR_ARESTA)[
                1] == vertice:
                arestas.append(x)
        return arestas

    def eh_completo(self):
        if self.N == []:
            return False
        arestas = self.vertices_nao_adjacentes()
        for x in arestas:
            if x.split(self.SEPARADOR_ARESTA)[0] != x.split(self.SEPARADOR_ARESTA)[1]:
                return False
        return True

    def lista_arestas(self, raiz='', ja_visitado=list()):
        arestas = list()
        for i, v in enumerate(self.A.items()):

            if raiz in v[1] and ((v[1].split('-')[0] not in ja_visitado) and (v[1].split('-')[1])):
                arestas.append(v)
        return arestas

    def padroniza_arestas(self, raiz='', aresta=''):
        aresta_padrao = ''
        if aresta[1].split(self.SEPARADOR_ARESTA)[0] == raiz:
            aresta_padratonhao = aresta[1]
        elif aresta[1].split(self.SEPARADOR_ARESTA)[1] == raiz:
            aresta_padrao = aresta[1].split('-')[1] + self.SEPARADOR_ARESTA + aresta[1].split('-')[0]
        return aresta_padrao

    def visita(self, raiz='', ja_visitados=list(), dfs=list()):
        arestas = self.A.items()
        arestas_raiz = self.lista_arestas(raiz, ja_visitados)
        if raiz in ja_visitados:
            return dfs, ja_visitados
        ja_visitados.append(raiz)

        for i, v in enumerate(arestas_raiz):
            aresta_padrao = self.padroniza_arestas(raiz, v)
            if raiz == aresta_padrao.split(self.SEPARADOR_ARESTA)[0] and (aresta_padrao.split(self.SEPARADOR_ARESTA)[1] not in dfs):
                dfs.append(v[0])
                dfs.append(aresta_padrao.split(self.SEPARADOR_ARESTA)[1])
                self.visita(aresta_padrao.split(self.SEPARADOR_ARESTA)[1], ja_visitados, dfs)
                if aresta_padrao.split('-')[1] not in ja_visitados:
                    ja_visitados.append(aresta_padrao.split(self.SEPARADOR_ARESTA)[1])
        return dfs, ja_visitados

    def dfs(self, raiz=''):
        dfs = list()

        dfs.append(raiz)

        ja_visitado = list()

        dfs, ja_visitado = self.visita(raiz, ja_visitado, dfs)

        return dfs, ja_visitado

    def ha_ciclo_primeira_etapa(self, l, raiz):
        global lista_caminho
        lista_caminho = []

        visitados = [raiz]
        arestas_list = list(self.A.values())
        for arestas in self.A.items():
            if raiz in arestas[1]:
                arestas_list.remove(arestas[1])

        limite = 1
        for x in l:
            for y in l[limite:]:
                lista_caminho.append(raiz + self.SEPARADOR_ARESTA + x)
                if (self.ha_ciclo_segunda_etapa(arestas_list, x, y, visitados)):
                    lista_caminho.append(y + self.SEPARADOR_ARESTA + raiz)
                    return True
                else:
                    visitados = [raiz]
                    lista_caminho = []

            limite += 1



    def arestas_adj_aux(self, vertice, visitados):
        arestas = list()
        vertices = self.N
        a = self.A.values()

        for x in vertices:
            if (vertice != x and x not in visitados):
                aux = vertice + self.SEPARADOR_ARESTA + x
                if (aux in a or aux[::-1] in a):
                    arestas.append(x)
                    lista_caminho.append(aux)
        return arestas

    def ha_ciclo_segunda_etapa(self, arestas, v1, v2, visitados):
        visitados.append(v1)
        aresta = v1 + self.SEPARADOR_ARESTA + v2

        if (aresta in arestas or aresta[::-1] in arestas):
            self.ajustar_lista_caminho(visitados)
            lista_caminho.append(aresta)
            return True

        if self.grau(v1) == 0 or self.grau(v2) == 0:
            return False

        arestas_adjacentes_a_v1 = self.arestas_adj_aux(v1, visitados)
        for x in arestas_adjacentes_a_v1:
            if (self.ha_ciclo_segunda_etapa(arestas, x, v2, visitados)):
                return True
        visitados.remove(v1)
        return False


    def arestas_adj(self, vertice, visitados):
        arestas = list()
        vertices = self.N
        a = self.A.values()

        for x in vertices:
            if (vertice != x and x not in visitados):
                aux = vertice + self.SEPARADOR_ARESTA + x
                if (aux in a or aux[::-1] in a):
                    arestas.append(x)
        return arestas

    def ha_caminho(self, arestas, v1, v2, visitados):
        visitados.append(v1)
        aresta = v1 + self.SEPARADOR_ARESTA + v2

        if (aresta in arestas or aresta[::-1] in arestas):
            return True

        if self.grau(v1) == 0 or self.grau(v2) == 0:
            return False

        arestas_adjacentes_a_v1 = self.arestas_adj(v1, visitados)
        for x in arestas_adjacentes_a_v1:
            if (self.ha_caminho(arestas, x, v2, visitados)):
                return True

        return False

    def ajustar_lista_caminho(self, visitados):
        lista_aux = lista_caminho[::]
        for x in lista_aux:
            v1, v2 = x.split(self.SEPARADOR_ARESTA)
            if (v1 not in visitados or v2 not in visitados):
                lista_caminho.remove(x)

    def ha_ciclo(self):

        for laco in self.A.items():
            v1,v2 = laco[1].split(self.SEPARADOR_ARESTA)
            if(v1 == v2):
                return [v1,laco[0],v2]



        l = []
        arestas = list(self.A.values())
        for x in self.N:
            for y in arestas:
                if x in y:
                    vertice_1, vertice_2 = y.split(self.SEPARADOR_ARESTA)
                    if (vertice_1 != x):
                        l.append(vertice_1)
                    elif (vertice_2 != x):
                        l.append(vertice_2)
            if (len(l) > 1):
                if (self.ha_ciclo_primeira_etapa(l, x)):
                    return self.toString(lista_caminho)

            l = []
        return False

    def toString(self,lista_caminho):
        lista_arestas = list()
        final_list = [lista_caminho[0].split(self.SEPARADOR_ARESTA)[0]]
        for arestas in lista_caminho:
            for itens in self.A.items():
                if (arestas == itens[1]):
                    v1,v2 = arestas.split(self.SEPARADOR_ARESTA)

                    final_list.append(itens[0])
                    final_list.append(v2)
        return final_list

    def conexo(self):
        vertice = self.N[0]

        for v in self.N[1:]:
            if not (self.ha_caminho(list(self.A.values()), vertice, v, [])):
                return False

        return True

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not (i == len(self.A) - 1):  # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str
