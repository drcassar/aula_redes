from graphviz import Digraph


def _tracar(raiz):
    """Função originalmente criada por Andrej Karpathy para construção de grafo.

    Referência: https://github.com/karpathy/micrograd
    """

    vertices, arestas = set(), set()

    def construir(v):
        if v not in vertices:
            vertices.add(v)
            for progenitor in v.progenitor:
                arestas.add((progenitor, v))
                construir(progenitor)

    construir(raiz)
    return vertices, arestas


def plota_grafo(raiz):
    """Função originalmente criada por Andrej Karpathy para construção de grafo.

    Referência: https://github.com/karpathy/micrograd
    """

    grafo = Digraph(format="svg", graph_attr={"rankdir": "LR"})
    vertices, arestas = _tracar(raiz)

    for v in vertices:
        uid = str(id(v))

        # fmt: off
        if hasattr(v, "rotulo") and (hasattr(v, "grad")):
            label="{ %s | data %.4f | grad %.4f }" % (v.rotulo, v.data, v.grad)
        elif hasattr(v, "rotulo"):
            label="{ %s | data %.4f }" % (v.rotulo, v.data)
        else:
            label="{ data %.4f }" % (v.data)
        # fmt: on

        grafo.node(
            name=uid,
            label=label,
            shape="record",
        )

        if v.operador_mae:
            grafo.node(name=uid + v.operador_mae, label=v.operador_mae)
            grafo.edge(uid + v.operador_mae, uid)

    for n1, n2 in arestas:
        grafo.edge(str(id(n1)), str(id(n2)) + n2.operador_mae)

    return grafo
