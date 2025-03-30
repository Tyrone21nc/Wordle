"""
Author: Romain Dzeinse
Date: 5/9/24
Objective: Create a mini-game using the PyGame library
"""
import pygame
import os

# Screen creation with its width, and height
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game using Pygame!")
WHITE = (100, 200, 100)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 100, 75
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("BlueSpaceship.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,
                                                                  (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("red_image.jpg"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,
                                                               (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)


def draw_window():
    # Change bgcolor to white
    WIN.fill(WHITE)
    # We need to update it now that we just changed the background color to white
    WIN.blit(YELLOW_SPACESHIP, (300, 100))
    WIN.blit(RED_SPACESHIP, (500, 50))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        # This for loop is will prevent infinite loop
        for event in pygame.event.get():
            # the line above does:
            # for event in [list_of_events]
            if event.type == pygame.QUIT:
                # Now it checks if the event type equals the QUIT event, which is clicking
                # the x on the top right of the window
                run = False
                # Then we set run equal to false
        draw_window()

    # This is also to quit pygame
    pygame.quit()


if __name__ == "__main__":
    main()
