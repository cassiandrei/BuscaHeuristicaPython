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
        obstaculos = int((linhas * colunas) * 20 / 100)
        while obstaculos > 0:
            lin = randint(0, linhas - 1)
            col = randint(0, colunas - 1)
            if self.matriz[lin][col] == 0:
                self.matriz[lin][col] = -1
                obstaculos -= 1

    def imprime(self, linhas, colunas, pygame, screen, janelaw, janelah):
        for i in range(0, colunas):
            for j in range(0, linhas):
                if self.matriz[i][j] == 1:
                    pygame.draw.rect(screen, (0, 0, 255),
                                     [(janelaw / colunas) * i, (janelah / linhas) * j, janelaw / colunas,
                                      janelah / linhas])
                elif self.matriz[i][j] == 2:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     [(janelaw / colunas) * i, (janelah / linhas) * j, janelaw / colunas,
                                      janelah / linhas])
                elif self.matriz[i][j] == -1:
                    pygame.draw.rect(screen, (255, 0, 0),
                                     [(janelaw / colunas) * i, (janelah / linhas) * j, janelaw / colunas,
                                      janelah / linhas])
                else:
                    pygame.draw.rect(screen, (255, 0, 0),
                                     [(janelaw / colunas) * i, (janelah / linhas) * j, janelaw / colunas,
                                      janelah / linhas],
                                     2)

    def imprimerota(self, atual):
        if atual.pai is not None:
            self.imprimerota(atual.pai)
        self.matriz[atual.pos[0]][atual.pos[1]] = 1