# ! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from math import sqrt

import node
import grid

janelaw = 640
janelah = 480

pygame.init()
screen = pygame.display.set_mode((janelaw, janelah), 0, 32)
pygame.display.set_caption('Trabalho 2 - Busca Heuristica A* - Aluno Cassiano Andrei')

grid = grid.Grid()

inicial = (0, 0)
grid.matriz[inicial[0]][inicial[1]] = 1
final = (14, 1)
grid.matriz[final[0]][final[1]] = 2


atual = node.Node(inicial)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((255, 255, 255))

    print(atual.pos)
    melhor = None
    if atual.pos == final:
        break
    elif len(atual.vizinhos) == 0:
        if atual.pos[0] - 1 >= 0:
            pos = (atual.pos[0] - 1, atual.pos[1])
            custo = atual.custo + 1
            hx = sqrt(pow(final[0] - pos[0], 2) + pow(final[1] - pos[1], 2))
            atual.vizinhos.append(node.Node(pos, custo, hx))
            print(hx+custo)
            print("Criou vizinho: ", atual.vizinhos[-1].pos)
            if melhor is None or (hx + custo) < (melhor.custo + melhor.heuristica):
                melhor = atual.vizinhos[-1]

        if atual.pos[0] + 1 <= 14:
            pos = (atual.pos[0] + 1, atual.pos[1])
            custo = atual.custo + 1
            hx = sqrt(pow(final[0] - pos[0], 2) + pow(final[1] - pos[1], 2))
            atual.vizinhos.append(node.Node(pos, custo, hx))
            print(hx + custo)
            print("Criou vizinho: ", atual.vizinhos[-1].pos)
            if melhor is None or (hx + custo) < (melhor.custo + melhor.heuristica):
                melhor = atual.vizinhos[-1]

        if atual.pos[1] - 1 >= 0:
            pos = (atual.pos[0], atual.pos[1] - 1)
            custo = atual.custo + 1
            hx = sqrt(pow(final[0] - pos[0], 2) + pow(final[1] - pos[1], 2))
            atual.vizinhos.append(node.Node(pos, custo, hx))
            print(hx + custo)
            print("Criou vizinho: ", atual.vizinhos[-1].pos)
            if melhor is None or (hx + custo) < (melhor.custo + melhor.heuristica):
                melhor = atual.vizinhos[-1]

        if atual.pos[1] + 1 <= 14:
            pos = (atual.pos[0], atual.pos[1] + 1)
            custo = atual.custo + 1
            hx = sqrt(pow(final[0] - pos[0], 2) + pow(final[1] - pos[1], 2))
            atual.vizinhos.append(node.Node(pos, custo, hx))
            print(hx + custo)
            print("Criou vizinho: ", atual.vizinhos[-1].pos)
            if melhor is None or (hx + custo) < (melhor.custo + melhor.heuristica):
                melhor = atual.vizinhos[-1]
    else:
        for vizinho in atual.vizinhos:
            if melhor is None or (vizinho.hx + vizinho.custo) < (melhor.custo + melhor.heuristica):
                melhor = vizinho
                melhor.custo += 1

    grid.matriz[atual.pos[0]][atual.pos[1]] = 0
    grid.matriz[melhor.pos[0]][melhor.pos[1]] = 1
    atual = melhor

    for i in range(0, 15):
        for j in range(0, 15):
            if grid.matriz[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 255),
                                 [(janelaw / 15) * i, (janelah / 15) * j, janelaw / 15, janelah / 15])
            elif grid.matriz[i][j] == 2:
                pygame.draw.rect(screen, (0, 0, 0),
                                 [(janelaw / 15) * i, (janelah / 15) * j, janelaw / 15, janelah / 15])
            else:
                pygame.draw.rect(screen, (255, 0, 0),
                                 [(janelaw / 15) * i, (janelah / 15) * j, janelaw / 15, janelah / 15], 2)
    pygame.display.update()
    time_passed = clock.tick(1)
