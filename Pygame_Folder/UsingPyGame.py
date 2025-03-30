"""
Author: Romain Dzeinse
Date: 5/8/24 (Wednesday Morning right before CALC2 exam at 8am -> Lord please help me make better decisions)
Time: 12:30 am
Continued on: 7/2/24
Time: 7:50 am
File name: Infinite Runner
"""

import pygame
import random

pygame.init()

# Game constants
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
WIDTH = 450
HEIGHT = 300

# Game Window
SCREEN_WIDTH = 1000  # it's in pixels
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinite Runner")  # This is the tittle of the page
background = black

# Game Variables
score = 0
player_x = 50
player_y = 200

# position and size of piece
#                  ((posx, posy, leng, widt))
player = pygame.Rect((500, 500, 20, 20))


# Creating game loop
run = True
while run:

    screen.fill((0, 100, 100))

    pygame.draw.rect(screen, (50, 50, 200), player)

    key = pygame.key.get_pressed()
    "The if and elif statements below allow us to use the up, down, left, and right arrow keys for control"
    # For the left movement
    if key[pygame.K_LEFT]:
        # -1 b/c we want it to move 1 unit to the left, and 0 for the y b/c
        # we only want the x to move, since we're just moving to the left
        player.move_ip(-1, 0)
    # For the right movement
    elif key[pygame.K_RIGHT]:
        # 1 b/c we want it to move 1 unit to the right, and 0 for the y b/c
        # we only want the x to move, since we're just moving to the right
        player.move_ip(1, 0)
    # For the up movement
    elif key[pygame.K_UP]:
        player.move_ip(0, -1)
    # For the down movement
    elif key[pygame.K_DOWN]:
        player.move_ip(0, 1)

    "The if and elif statements below here allow for movement using awsd keys for control"
    # For the left movement
    if key[pygame.K_a]:
        # -1 b/c we want it to move 1 unit to the left, and 0 for the y b/c
        # we only want the x to move, since we're just moving to the left
        player.move_ip(-1, 0)
    # For the right movement
    elif key[pygame.K_d]:
        # 1 b/c we want it to move 1 unit to the right, and 0 for the y b/c
        # we only want the x to move, since we're just moving to the right
        player.move_ip(1, 0)
    # For the up movement
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
    # For the down movement
    elif key[pygame.K_s]:
        player.move_ip(0, 1)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # refreshes the screen
    pygame.display.update()


pygame.quit()


