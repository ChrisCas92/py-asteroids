# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()  # Initialize all imported pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create the game window
    clock = pygame.time.Clock()  # Create a clock to manage frame rate
    
    updatable = pygame.sprite.Group()  # Create a group for updateable objects
    drawable = pygame.sprite.Group()  # Create a group for drawable objects
    asteroids = pygame.sprite.Group()  # Create a group for asteroids
    
    Player.containers = (updatable, drawable)  # Set the containers for the Player class
    Asteroid.containers = (asteroids, updatable, drawable)  # Set the containers for the Asteroid class
    AsteroidField.containers = (updatable,)  # Set the containers for the AsteroidField class
    
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Create a player instance at the center of the screen
    asteroidfield = AsteroidField()  # Create an instance of the AsteroidField

    
    dt = 0  # Initialize delta time variable
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        
        screen.fill("black")  # Clear the screen with black color)
        
        for obj in drawable:
            obj.draw(screen)  # Draw all drawable objects on the screen
        
        
        pygame.display.flip()  # Update the display
    
        # limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000.0  # Update player state based on time elapsed
        
    

if __name__ == "__main__":
    main()