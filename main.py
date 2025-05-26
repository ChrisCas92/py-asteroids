# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    pygame.init()  # Initialize all imported pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create the game window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        player.draw(screen)  # Draw the player on the screen
        pygame.display.flip()  # Update the display
    
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Create a player instance at the center of the screen

    


if __name__ == "__main__":
    main()