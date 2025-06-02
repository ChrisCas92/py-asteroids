import pygame
from circleshape import CircleShape as Circleshape

class Shot (Circleshape):
    def __init__(self, x, y, radius):
        # Initialize the shot with position and radius
        super().__init__(x, y, radius)
        self.color = "yellow"  # Color of the shot

    def draw(self, screen):
        # Draw the shot as a circle on the screen
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        # Update position based on velocity and time delta
        self.position += self.velocity * dt