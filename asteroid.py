# Asteroid class that inherits from Circleshape
# This class represents an asteroid in a game, inheriting properties from Circleshape
import pygame
from circleshape import CircleShape as Circleshape

class Asteroid(Circleshape):
    
    def __init__(self, x, y, radius):
        # Initialize the asteroid with position and radius
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        # Draw the asteroid as a circle on the screen
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt  # Update position based on velocity and time delta