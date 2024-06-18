import pygame

class BlueCar:

    def __init__(self, x, y, scale_factor=0.7):
        self.x = x
        self.y = y
        self.image = pygame.image.load("blueCar.png")
        # Scale the car image
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor)))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.delta = 1
