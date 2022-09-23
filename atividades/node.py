class Node:
    valor = 0
    proximo = None
    amterior = None

    def __init__(self, valor=0, proximo=None, anterior=None):
        self.valor = valor
        self.proximo = proximo
        self.anterior = anterior
