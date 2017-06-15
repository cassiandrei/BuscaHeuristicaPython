# ! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit

import node
import grid

janelaw = 800
janelah = 600

pygame.init()
screen = pygame.display.set_mode((janelaw, janelah), 0, 32)
pygame.display.set_caption('Trabalho 2 - Busca Heuristica A* - Aluno Cassiano Andrei')

linhas = 15
colunas = 15

grid = grid.Grid(colunas, linhas)
grid.geraObstaculos(linhas, colunas)

inicial = (0, 0)
grid.matriz[inicial[0]][inicial[1]] = 1
final = (colunas - 1, linhas - 1)
grid.matriz[final[0]][final[1]] = 2

inicio = node.Node(inicial)
inicio.setheuristica(final)

abertos = []
open = []
closed = []
open.append(inicio)
abertos.append(inicio.pos)

while len(open) > 0:
    melhor = None
    for no in open:
        if melhor is None or no.custo < melhor.custo:
            melhor = no
    if melhor.pos == final:
        break
    else:
        print(melhor.pos, abertos)
        abertos.remove(melhor.pos)
        open.remove(melhor)
        closed.append(melhor.pos)
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            pos = (melhor.pos[0] + i, melhor.pos[1] + j)
            # testa se tem não obstaculo ou se está acessando dentro da grid
            if 0 <= pos[0] < colunas and 0 <= pos[1] < linhas and grid.matriz[pos[0]][
                pos[1]] != -1 and pos != melhor.pos:
                if pos not in closed and pos not in abertos:
                    novo = node.Node(pos)
                    novo.setheuristica(final)
                    novo.custo += melhor.custo
                    open.append(novo)
                    abertos.append(novo.pos)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((255, 255, 255))

    if len(closed) == 0:
        break
    else:
        x = closed.pop(0)
        grid.matriz[x[0]][x[1]] = 1
    for i in range(0, colunas):
        for j in range(0, linhas):
            if grid.matriz[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 255),
                                 [(janelaw / colunas) * i, (janelah / linhas) * j, janelaw / colunas,
                                  janelah / linhas])
            elif grid.matriz[i][j] == 2:
                pygame.draw.rect(screen, (0, 0, 0),
                                 [(janelaw / colunas) * i, (janelah / linhas) * j, janelaw / colunas,
                                  janelah / linhas])
            elif grid.matriz[i][j] == -1:
                pygame.draw.rect(screen, (255, 0, 0),
                                 [(janelaw / colunas) * i, (janelah / linhas) * j, janelaw / colunas,
                                  janelah / linhas])
            else:
                pygame.draw.rect(screen, (255, 0, 0),
                                 [(janelaw / colunas) * i, (janelah / linhas) * j, janelaw / colunas,
                                  janelah / linhas],
                                 2)
    pygame.display.update()
    grid.matriz[x[0]][x[1]] = 0
    time_passed = clock.tick(15)
