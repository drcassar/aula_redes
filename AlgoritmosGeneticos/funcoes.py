def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.
    
    Args:
      individiuo: lista contendo os genes das caixas binárias
    
    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo)