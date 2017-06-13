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



clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((255, 255, 255))
    for i in range(0, 15):
        for j in range(0, 15):
            pygame.draw.rect(screen, (255, 0, 0), [(janelaw/15)*i, (janelah/15)*j, janelaw/15, janelah/15], 2)
    pygame.display.update()
    time_passed = clock.tick(30) 