import random

###############################################################################
#                                   Suporte                                   #
##############################################################################+


# NOVIDADE
def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2

    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.

    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist


# NOVIDADE
def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).

    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.

    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())

    return cidades


###############################################################################
#                                    Genes                                    #
###############################################################################


def gene_cb():
    """Gera um gene válido para o problema das caixas binárias

    Return:
      Um valor zero ou um.
    """
    lista = [0, 1]
    gene = random.choice(lista)
    return gene


def gene_cnb(valor_max_caixa):
    """Gera um gene válido para o problema das caixas não-binárias

    Args:
      valor_max_caixa: número inteiro representando o maior valor possível que
      pode existir dentro de uma caixa.

    Return:
      Um valor entre zero a `valor_max_caixa` (inclusive).
    """
    gene = random.randint(0, valor_max_caixa)
    return gene


def gene_letra(letras):
    """Sorteia uma letra.

    Args:
      letras: letras possíveis de serem sorteadas.

    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra


###############################################################################
#                                  Indivíduos                                 #
###############################################################################


def individuo_cb(n):
    """Gera um individuo para o problema das caixas binárias.

    Args:
      n: número de genes do indivíduo.

    Return:
       Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo


def individuo_cnb(n_genes, valor_max_caixa):
    """Gera um individuo para o problema das caixas não-binárias.

    Args:
      n_genes: número de genes do indivíduo.
      valor_max_caixa: maior número inteiro possível dentro de uma caixa

    Return:
       Uma lista com n genes. Cada gene é um valor entre zero e
       `valor_max_caixa`.
    """
    individuo = []
    for i in range(n_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo


def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha

    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.

    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato


# NOVIDADE
def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante

    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    pass


###############################################################################
#                                  População                                  #
###############################################################################


def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias.

    Args:
      tamanho: tamanho da população.
      n: número de genes do indivíduo.

    Returns:
      Uma lista onde cada item é um indiviuo. Um individuo é uma lista com `n`
      genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao


def populacao_cnb(tamanho, n_genes, valor_max_caixa):
    """Cria uma população no problema das caixas não-binárias.

    Args:
      tamanho: tamanho da população.
      n_genes: número de genes do indivíduo.
      valor_max_caixa: maior número inteiro possível dentro de uma caixa

    Returns:
      Uma lista onde cada item é um indiviuo. Um individuo é uma lista com
      `n_genes` genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cnb(n_genes, valor_max_caixa))
    return populacao


def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha

    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.

    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao


# NOVIDADE
def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.

    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao


###############################################################################
#                                   Seleção                                   #
###############################################################################


def selecao_roleta_max(populacao, fitness):
    """Seleciona individuos de uma população usando o método da roleta.

    Nota: apenas funciona para problemas de maximização.

    Args:
      populacao: lista com todos os individuos da população
      fitness: lista com o valor da funcao objetivo dos individuos da população

    Returns:
      População dos indivíduos selecionados.
    """
    populacao_selecionada = random.choices(
        populacao, weights=fitness, k=len(populacao)
    )
    return populacao_selecionada


def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    minimização.

    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos individuos da população
      tamanho_torneio: quantidade de invidiuos que batalham entre si

    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados


###############################################################################
#                                  Cruzamento                                 #
###############################################################################


def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples.

    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo

    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos.
    """
    ponto_de_corte = random.randint(1, len(pai) - 1)

    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]

    return filho1, filho2


# NOVIDADE
def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.

    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.

    Ver pág. 37 do livro do Wirsansky.

    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo

    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    pass


###############################################################################
#                                   Mutação                                   #
###############################################################################


def mutacao_cb(individuo):
    """Realiza a mutação de um gene no problema das caixas binárias

    Args:
      individuo: uma lista representado um individuo no problema das caixas
      binárias

    Return:
      Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo


def mutacao_cnb(individuo, valor_max_caixa):
    """Realiza a mutação de um gene no problema das caixas não-binárias

    Args:
      individuo:
        uma lista representado um individuo no problema das caixas não-binárias
      valor_max_caixa:
        maior número inteiro possível dentro de uma caixa

    Return:
      Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo


def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.

    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.

    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo


# NOVIDADE
def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.

    Args:
      individuo: uma lista representado um individuo.

    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    pass


###############################################################################
#                         Função objetivo - indivíduos                        #
###############################################################################


def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.

    Args:
      individiuo: lista contendo os genes das caixas binárias

    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo)


def funcao_objetivo_cnb(individuo):
    """Computa a função objetivo no problema das caixas não-binárias.

    Args:
      individiuo: lista contendo os genes das caixas não-binárias

    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo)


def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha

    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir

    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca


# NOVIDADE
def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.

    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0

    # preencher o código

    return distancia


###############################################################################
#                         Função objetivo - população                         #
###############################################################################


def funcao_objetivo_pop_cb(populacao):
    """Calcula a funcao objetivo para todos os membros de uma população

    Args:
      populacao: lista com todos os individuos da população

    Return:
      Lista de valores represestando a fitness de cada individuo da população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness


def funcao_objetivo_pop_cnb(populacao):
    """Calcula a funcao objetivo para todos os membros de uma população

    Args:
      populacao: lista com todos os individuos da população

    Return:
      Lista de valores represestando a fitness de cada individuo da população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cnb(individuo)
        fitness.append(fobj)
    return fitness


def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir

    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado


# NOVIDADE
def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.

    Args:
      populacao:
        Lista com todos os inviduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado
