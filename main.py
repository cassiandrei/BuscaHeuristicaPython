# ! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
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
final = (14, 14)
grid.matriz[final[0]][final[1]] = 2

atual = node.Node(inicial)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((255, 255, 255))

    if atual.pos == final:
        break
    else:
        pass
    
    for i in range(0, 15):
        for j in range(0, 15):
            if grid.matriz[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 255), [(janelaw/15)*i, (janelah/15)*j, janelaw/15, janelah/15])
            elif grid.matriz[i][j] == 2:
                pygame.draw.rect(screen, (0, 0, 0), [(janelaw / 15) * i, (janelah / 15) * j, janelaw / 15, janelah / 15])
            else:
                pygame.draw.rect(screen, (255, 0, 0), [(janelaw / 15) * i, (janelah / 15) * j, janelaw / 15, janelah / 15], 2)
    pygame.display.update()
    time_passed = clock.tick(1)