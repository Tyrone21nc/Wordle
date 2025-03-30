"""
Author: Romain Dzeinse
Date: 5/9/24
Objective: Create a mini-game using the PyGame library
"""
import pygame

# Screen creation with its length
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    run = True
    while run:
        # This for loop is will prevent infinite loop
        for event in pygame.event.get():
            # the line above does:
            # for event in [list_of_events]
            if event.type == pygame.QUIT:
                # Now it checks if the event type equals the QUIT event, which is clicking
                # the x on the top right of the window
                run = False
                # Then we set run equal to false
    # This is also to quit pygame
    pygame.quit()


if __name__ == "__main__":
    main()



