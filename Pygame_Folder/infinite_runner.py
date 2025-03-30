"""
Author: Romain Dzeinse
Date: 7/2/24
File name: infinite_runner.py
Objective: Create an endless running game
"""

import random
import pygame

pygame.init()

# game constants
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
light_blue = (50, 175, 175)
WIDTH = 450
HEIGHT = 300

# game variables
score = 0
player_x = 60
player_y = 200
y_change = 0
gravity = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinite Runner")  # This is the tittle at the top of the game
background = black
fps = 60  # Speed of the game
font = pygame.font.Font('freesansbold.ttf', 16)  # freesansbold.tff is the default text, you can change whenever
timer = pygame.time.Clock()

running = True
# Main Game loop
while running:
    timer.tick(fps)  # speed of game
    screen.fill(background)  # background of the window
    # This is for the floor, what we want to be the floor of the window
    #                               [x-position, y-position, width, height]
    floor = pygame.draw.rect(screen, white, [0, 220, WIDTH, 5])
    player = pygame.draw.rect(screen, green, [player_x, player_y, 20, 20])

    for event in pygame.event.get():
        # If user presses the red X on top right corner, it will close the game window
        if event.type == pygame.QUIT:
            running = False
        #
        if event.type == pygame.KEYDOWN:  # keydown is keyboard key press, keyup is keyboard key release
            if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and y_change == 0:
                y_change = 18  # This value is good for the way the game is
            if event.key== pygame.K_RIGHT:
                pass

    if y_change > 0 or player_y < 200:
        player_y -= y_change  # subtracting a height of y_change -> 18
        y_change -= gravity
    if player_y > 200:
        player_y = 200
    if player_y == 200 and y_change < 0:
        y_change = 0

    pygame.display.flip()

pygame.quit()





