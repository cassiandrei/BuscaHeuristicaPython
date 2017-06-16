from random import randint


class Grid(object):
    '''
     Classe para Gerenciar a Grid
    '''

    def __init__(self, colunas, linhas):
        '''
        Função construtora da Grid
        :param colunas: Numero de colunas 
        :param linhas: Numero de linhas
        '''
        # Gera a matriz[linhas][colunas]
        self.matriz = []
        for i in range(colunas):
            linha = []
            for j in range(linhas):
                linha.append(0)
            self.matriz.append(linha)

    def geraObstaculos(self, linhas, colunas, percentual):
        '''
        Função que gera obstaculos na Grid aleatoriamente sem repetição
        :param linhas: Numero de linhas
        :param colunas: Numero de Colunas
        :param percentual: Numero percentual de obstaculos
        :return: 
        '''
        obstaculos = int((linhas * colunas) * percentual / 100)
        while obstaculos > 0:
            lin = randint(0, linhas - 1)
            col = randint(0, colunas - 1)
            if self.matriz[lin][col] == 0:
                self.matriz[lin][col] = -1
                obstaculos -= 1

    def imprime(self, linhas, colunas, pygame, screen, janelaw, janelah):
        '''
        Função que atualiza o grid na tela a cada Frame
        :param linhas: Numero de linhas da Grid
        :param colunas: Numero de colunas da Grid
        :param pygame: objeto GUI
        :param screen: janela criada
        :param janelaw: largura da resolução
        :param janelah: altura da resolução
        :return: 
        '''

        # Gera quadrados
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
        '''
        Função que imprime a melhor rota ate o objetivo
        :param atual: no objetivo
        :return: 
        '''
        # metodo recursivo acessando o pai ate o nó inicial
        if atual.pai is not None:
            self.imprimerota(atual.pai)
        self.matriz[atual.pos[0]][atual.pos[1]] = 1
