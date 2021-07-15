import pygame
import random
from pygame.locals import *  # importar tudo


def collision(c1, c2):   # para testar colisão
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


pygame.init()  # iniciar ações

# começando pela tela

screen = pygame.display.set_mode((600, 600))  # tamanho da tela 600x600 pixels
pygame.display.set_caption('Snake')  # título do jogo

snake = [(200, 200), (210, 200), (220, 200)]  # representar a cobra como uma lista de segmentos, uma dupla de [(x,y)]
# posicionada dentro do nosso quadrado da tela
snake_skin = pygame.Surface((10, 10))  # definindo que a "pele" de nossa cobra é essa sprite de superfície
snake_skin.fill((255, 255, 255))  # a nossa cobrinha será branca, em RGB

# criar a maçã que a cobra vai comer
apple = pygame.Surface((10, 10))  # tamanho da maçã
apple.fill((255, 0, 0))  # cor da maçã
apple_pos = (10*random.randint(0, 59), 10*random.randint(0, 59))  # dupla de números aleatorios entre 0 e 590,
# que é o ultimo lugar que posso colocar antes de sair da tela
# 10* para sempre estar alinhado com a cobra

# definindo direções
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
my_direction = LEFT  # quero que a cobra comece indo pra esquerda, vamos plotar na tela na função blot

clock = pygame.time.Clock()  # mudar o tempo de fps do jogo
game_over = False

# laço infinito para rodar o jogo continuamente
# define-se aqui eventos do jogador (apertar botão ou outra entrada pro jogo)
while not game_over:
    clock.tick(20)  # valor do fps
    for event in pygame.event.get():
        if event.type == QUIT:  # se apertar botão de fechar
            pygame.quit()
        # para controlar a cobra
        if event.type == KEYDOWN:  # se uma tecla foi apertada
            if event.key == K_UP:  # se o evento foi uma key up
                my_direction = UP
            if event.key == K_DOWN:  # se o evento foi uma key down
                my_direction = DOWN
            if event.key == K_RIGHT:  # se o evento foi uma key right
                my_direction = RIGHT
            if event.key == K_LEFT:  # se o evento foi uma key left
                my_direction = LEFT

    if collision(snake[0], apple_pos):
        apple_pos = (10*random.randint(0, 59), 10*random.randint(0, 59))  # aparecer em outro lugar aleatorio
        snake.append((0, 0))  # cobra aumentou e toma posição da cauda, logo na função abaixo

    # para o restante do corpo da cobra, cada pedaço do corpo ocupa a posição que o pedaço da frente tava ocupando antes
    # se tiver indo pra esquerda, pedaço x ocupa o espaço que o pedaço da esquerda de x tava ocupando
    for i in range(len(snake) - 1, 0, -1):   # range(comprimento da cobra menos o rabo, vai ate posicao 0,
        # e ir decrementando, ao invés de incrementando)

        # a posição i ocupa a posicao i-1
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    # agora para movimentar a cobrinha dependendo de my_direction:
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)  # cabeça da cobra snake[0] y diminui na tela para cima
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)  # cabeça da cobra snake[0] y aumenta na tela para baixo
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])  # cabeça da cobra snake[0] x aumenta na tela para a direita
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])  # cabeça da cobra snake[0] x diminui na tela para a esquerda

# fazer game over se tocar na parede
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    # verificar se a cobra toca nela mesma
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break
    if game_over:
        break

    # para o restante do corpo da cobra, cada pedaço do corpo ocupa a posição que o pedaço da frente tava ocupando antes
    # se tiver indo pra esquerda, pedaço x ocupa o espaço que o pedaço da esquerda de x tava ocupando
    for i in range(len(snake)-1, 0, -1):  # range(comprimento da cobra menos o rabo, vai ate posicao 0,
        # e ir decrementando, ao invés de incrementando)
        # a posição i ocupa a posicao i-1
        snake[i] = (snake[i-1][0], snake[i-1][1])
    screen.fill((0, 0, 0))  # limpar a tela para atualiza-la com novas informações
    screen.blit(apple, apple_pos)  # printar na tela uma maçã numa posição aleatória
    for pos in snake:  # para cada posição da snake, fazer atualização da tela para andar, com função blit
        # screen.blit(pygame.Surface((10,10)), pos)
        # passando um gráfico para a tela com um sprite e uma posição onde aparecer o sprite

        screen.blit(snake_skin, pos)  # substitui o Surface. poderia utilizar imagem,
        # qualquer coisa gráfica que irá se mover, chamamos sprite
    pygame.display.update()  # atualizar todas as vezes que correr o laço 'while'
