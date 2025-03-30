"""
Author: Romain Dzeinse
Date: 06/10/24
Inspiration: Someone I know recommended me this game to code.
Objective, create a game that I would like to download and play maybe on my phone
"""
import os
import random
import math
import pygame
# The os stuff is to load all the sprite sheets the files names with the
# characters and scenes and all that instead of manually typing out the function names by hand
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platformer")

# This is our background color for now, this is temporary until we apply our own background
BG_color = (255, 255, 255)  # RGB - white
WIDTH, HEIGHT = 1000, 800  # GUI/game page layout
FPS = 60  # frame per second
PLAYER_VEL = 5  # speed at which player moves around the screen

# This is the pygame window with the defined HEIGHT and WIDTH variables from above
window = pygame.display.set_mode((WIDTH, HEIGHT))


def get_background(name):
    """
    :param name: color of our background
    :return: list of all the background tiles we need to draw
    """
    image = pygame.image.load(join("assets", "Background", name))
    # The first and second underscores are x and y, and since we don't care abt them we just denote
    # them with the underscore placeholder
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // + 1):
            pos = [i * width, j * height]


def main(my_window):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        # quit the python program if the user clicks the red x in the top right corner of the page
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)


