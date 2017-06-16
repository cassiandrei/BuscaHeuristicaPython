from math import sqrt


class Node(object):
    '''
    Classe que representa um nó da arvore
    '''
    def __init__(self, pos, custo=0, pai=None):
        '''
        Função construtora da Node
        :param pos: posição do nó na Grid
        :param custo: função custo
        :param pai: nó pai
        '''
        self.pos = pos
        self.custo = custo
        self.pai = pai

    def setheuristica(self, final):
        '''
        Função que calcula a Função Euclidiana do nó até o objetivo
        :param final: nó objetivo
        :return: 
        '''
        self.custo += sqrt((pow(final[0] - self.pos[0], 2)) + (pow(final[1] - self.pos[1], 2)))
