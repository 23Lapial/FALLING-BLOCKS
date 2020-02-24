#!/usr/bin/env python3

import pygame
import sys
import random

pygame.init()
pygame.font.init()

# SCREEN
WIDTH = 400
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PYTHON GAME TEST')

score = 0

# COLORS
RED = (250, 0, 0)
WHITE = (230, 230, 230)

# PLAYER
player_pos = [0, HEIGHT - 50]
player_size = [50, 50]

# ENEMY
enemy_list = []

enemy_pos = [0, 0]
enemy_size = [50, 50]

# FONTS
font = pygame.font.SysFont('lucidia console', 50)

def add_enemy():
    # check enemy list equal to 0
    # add enemy to enemy list

    while len(enemy_list) == 0:
        enemy_list.append('enemy')


def draw_enemy():
    # add enemy to game for every
    # enemy item in enemy list

    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size[0], enemy_size[1]))

        enemy_pos[1] += .25


def detect_collision():

    if player_pos[0] == enemy_pos[0] and player_pos[1] == enemy_pos[1]:
        sys.exit()


game_active = True

while game_active:

    # QUIT GAME
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        # PLAYER MOVEMENT
        if event.type == pygame.KEYDOWN:
            # RIGHT AND LEFT
            if event.key == pygame.K_RIGHT:
                player_pos[0] += player_size[0]
            elif event.key == pygame.K_LEFT:
                player_pos[0] -= player_size[0]

    screen.fill((0, 0, 0))

    add_enemy()

    draw_enemy()

    # RESET ENEMY Y
    if enemy_pos[1] == HEIGHT:
        enemy_pos[0] = random.randrange(0, WIDTH-50, 50)
        enemy_pos[1] = 0
        enemy_list.pop()
        score += 1


    detect_collision()

    # SCORE DISPLAY
    score_display = font.render(str(score), True, WHITE)
    screen.blit(score_display, (0, 0))

    # DRAW PLAYER
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size[0], player_size[1]))

    pygame.display.update()
