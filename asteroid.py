# Asteroid class that inherits from Circleshape
# This class represents an asteroid in a game, inheriting properties from Circleshape
import pygame
from circleshape import CircleShape as Circleshape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE, ASTEROID_KINDS

class Asteroid(Circleshape):
    
    def __init__(self, x, y, radius):
        # Initialize the asteroid with position and radius
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        # Draw the asteroid as a circle on the screen
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt  # Update position based on velocity and time delta
        
    def split(self):
        self.kill()  # Remove the asteroid from the game
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # randomize the angle of the split
        random_angle = random.uniform(20, 50)
        
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2