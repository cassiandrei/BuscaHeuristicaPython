class Node(object):
    def __init__(self, custo=0, hx=0):
        self.custo = custo
        self.vizinhos = []
        self.heuristica = hx

    def add(self, vizinho):
        self.vizinhos.append(vizinho)