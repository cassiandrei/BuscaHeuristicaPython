class Node(object):
    def __init__(self, pos, custo=0, hx=0):
        self.pos = pos
        self.custo = custo
        self.vizinhos = []
        self.heuristica = hx

    def add(self, vizinho):
        self.vizinhos.append(vizinho)