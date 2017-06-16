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
custo = 0

abertos = []
open = []
closed = []
open.append(inicio)
abertos.append(inicio.pos)

clock = pygame.time.Clock()
while len(open) > 0:
    screen.fill((255, 255, 255))
    melhor = None
    for no in open:
        if melhor is None or no.custo < melhor.custo:
            melhor = no
    print("Visitado: ", melhor.pos, end="")
    if melhor.pos == final:
        break
    else:
        melhor.custo += custo
        abertos.remove(melhor.pos)
        open.remove(melhor)
        closed.append(melhor.pos)

        custo = melhor.custo
        print("Novos Estados gerados: ", end="")
        for pos in [(melhor.pos[0] + 1, melhor.pos[1]), (melhor.pos[0] - 1, melhor.pos[1]),
                    (melhor.pos[0], melhor.pos[1] + 1), (melhor.pos[0], melhor.pos[1] - 1)]:
            # testa se tem não obstaculo ou se está acessando dentro da grid
            if 0 <= pos[0] < colunas and 0 <= pos[1] < linhas and grid.matriz[pos[0]][pos[1]] != -1 and pos != melhor.pos:
                if pos not in closed and pos not in abertos:
                    novo = node.Node(pos)
                    novo.setheuristica(final)
                    novo.pai = melhor
                    open.append(novo)
                    abertos.append(novo.pos)
                    print(novo.pos, end="")
        print(" ")

    grid.matriz[melhor.pos[0]][melhor.pos[1]] = 1
    grid.imprime(linhas, colunas, pygame, screen, janelaw, janelah)
    pygame.display.update()
    grid.matriz[melhor.pos[0]][melhor.pos[1]] = 0
    time_passed = clock.tick()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    grid.imprimerota(melhor)
    grid.imprime(linhas, colunas, pygame, screen, janelaw, janelah)
    pygame.display.update()
