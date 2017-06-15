from math import sqrt


class Node(object):
    def __init__(self, pos, custo=0):
        self.pos = pos
        self.custo = custo

    def setheuristica(self, final):
        self.custo += sqrt((pow(final[0] - self.pos[0], 2)) + (pow(final[1] - self.pos[1], 2)))
