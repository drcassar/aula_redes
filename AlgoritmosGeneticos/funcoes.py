import random


def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.
    
    Args:
      individiuo: lista contendo os genes das caixas binárias
    
    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo)


def gene_cb():
    """Gera um gene válido para o problema das caixas binárias
    
    Return:
      Um valor zero ou um.
    """
    lista = [0, 1]
    gene = random.choice(lista)
    return gene


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

def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias.
    
    Args:
      tamanho: tamanho da população.
      n: número de genes de um individuo.
    
    Returns:
      Uma lista onde cada item é um indiviuo. Um individuo é uma lista com n genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao


def selecao_roleta_max(populacao, fitness):
    """Seleciona individuos de uma população usando o método da roleta.
    
    Nota: apenas funciona para problemas de maximização.
    
    Args:
      populacao: lista com todos os individuos da população
      fitness: lista com o valor da funcao objetivo dos individuos da população
    
    Returns:
      População dos indivíduos selecionados.
    """
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada


def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.
    
    Args:
      individiuo: lista contendo os genes das caixas binárias
    
    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo)


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
    