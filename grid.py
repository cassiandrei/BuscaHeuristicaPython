class Grid(object):
    def __init__(self):
        self.matriz = []
        for i in range(15):
            linha = []
            for j in range(15):
                linha.append(0)
            self.matriz.append(linha)

