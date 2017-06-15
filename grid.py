from random import randint


class Grid(object):
    def __init__(self, colunas, linhas):
        self.matriz = []
        for i in range(colunas):
            linha = []
            for j in range(linhas):
                linha.append(0)
            self.matriz.append(linha)

    def geraObstaculos(self, linhas, colunas):
        obstaculos = int((linhas * colunas) * 40 / 100)
        while obstaculos > 0:
            lin = randint(0, linhas - 1)
            col = randint(0, colunas - 1)
            if self.matriz[lin][col] != -1:
                self.matriz[lin][col] = -1
                obstaculos -= 1
