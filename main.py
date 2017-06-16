# ! /usr/bin/env python
'''
Aluno Cassiano Andrei Schneider
Disciplina: Inteligễncia Artificial
Trabalho: Busca Heurística aplicada em uma Grid

Pacotes necessários: 
    Python versão 3, pygame
    
Para instalar o pygame use:
    $apt-get install python3-pip
    $pip3 install pygame
Para executar use: 
    $python3 main.py

Observações: 
    Obstaculos podem impedir o acesso até o objetivo
    Use ESC para fechar
    Para melhor visualização foi limitado a taxa de frames/segundos em 10
    
Exemplo de entrada:
    Digite o numero de linhas do Grid: 15
    Digite o numero de Colunas do Grid: 15
    Digite o percentual de obstaculos: 20
    Digite a posição inicial x: 0
    Digite a posição inicial y: 0
    Digite a posição objetivo x: 14
    Digite a posição objetivo y: 14
    
Repositório: https://github.com/cassiandrei/BuscaHeuristicaPython
'''

import pygame
from sys import exit

import node
import grid


'''
 Leitura dos parametros
'''


linhas = int(input("Digite o numero de linhas do Grid: "))
colunas = int(input("Digite o numero de Colunas do Grid: "))
grid = grid.Grid(colunas, linhas)
percentual = int(input("Digite o percentual de obstaculos: "))
if 0 <= percentual < 90:
    grid.geraObstaculos(linhas, colunas, percentual)
else:
    print("Percentual deve estar entre 0 e 90")
    exit()
try:
    inicial = (int(input("Digite a posição inicial x: ")), int(input("Digite a posição inicial y: ")))
    grid.matriz[inicial[0]][inicial[1]] = 1
    final = (int(input("Digite a posição objetivo x: ")), int(input("Digite a posição objetivo y: ")))
    grid.matriz[final[0]][final[1]] = 2
except IndexError:
    print("posição fora da grid, execute novamente")
    exit()
except ValueError:
    print("Valor invalido (esperado um valor inteiro)")
    exit()


'''
 Configuração da Janela
'''


janelaw = 1200
janelah = 1024
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Trabalho 2 - Busca Heuristica A* - Aluno Cassiano Andrei')
print(pygame.display.get_wm_info())


'''
    Iniciando a Arvore
'''


inicio = node.Node(inicial)  # Nó raiz
inicio.setheuristica(final)


'''
    Inicializando variáveis de configuração da Busca Heurística A*
'''

custototal = 0
custo = 0
abertos = []
open = []
closed = []
open.append(inicio)
abertos.append(inicio.pos)


'''
    Iniciando o Loop e a busca A*
'''


clock = pygame.time.Clock()
#  Enquanto tiver nodos abertos execute o loop:
while len(open) > 0:

    #  Pressionou ESC?
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit()

    #  limpa a tela
    screen.fill((255, 255, 255))

    #  busca o no aberto com menor função custo
    melhor = None
    for no in open:
        if melhor is None or no.custo < melhor.custo:
            melhor = no
    print("Visitado: ", melhor.pos, end="")

    #  Testa se ele é o objetivo
    if melhor.pos == final:
        break

    #  Se nao for, insere na lista de nos fechados e remove da lista de nos abertos
    else:
        custototal += 1
        melhor.custo += custo
        abertos.remove(melhor.pos)
        open.remove(melhor)
        closed.append(melhor.pos)

        #  atualiza custo
        custo = melhor.custo

        # Analisa vizinhos
        print("Novos Estados gerados: ", end="")
        for pos in [(melhor.pos[0] + 1, melhor.pos[1]), (melhor.pos[0] - 1, melhor.pos[1]),
                    (melhor.pos[0], melhor.pos[1] + 1), (melhor.pos[0], melhor.pos[1] - 1)]:

            #  testa se tem não obstaculo ou se está acessando dentro da grid
            if 0 <= pos[0] < colunas and 0 <= pos[1] < linhas and grid.matriz[pos[0]][pos[1]] != -1 and pos != melhor.pos:

                #  testa se vizinho nao esta na lista de nos abertos e fechados
                if pos not in closed and pos not in abertos:

                    # cria nó vizinho
                    novo = node.Node(pos)

                    # calcula função custo (estimativa função euclidiana)
                    novo.setheuristica(final)

                    # seta seu pai
                    novo.pai = melhor

                    # insere na fula de nos abertos
                    open.append(novo)
                    abertos.append(novo.pos)
                    print(novo.pos, "Custo:", novo.custo, end=" ")
        print(" ")


    '''
        Atualização da Grid
    '''


    grid.matriz[melhor.pos[0]][melhor.pos[1]] = 1
    grid.imprime(linhas, colunas, pygame, screen, janelaw, janelah)
    pygame.display.update()
    grid.matriz[melhor.pos[0]][melhor.pos[1]] = 0
    time_passed = clock.tick(10)

'''
    Imprime melhor ROTA
'''

print("CUSTO TOTAL: ", custototal)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit()
    grid.imprimerota(melhor)
    grid.imprime(linhas, colunas, pygame, screen, janelaw, janelah)
    pygame.display.update()
