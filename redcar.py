import pygame

class RedCar:

    def __init__(self, x, y, scale_factor=0.7):
        self.x = x
        self.y = y
        self.image = pygame.image.load("redcar.png")
        # Scale the car image
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor)))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.delta = 1

    def move_direction(self, direction):
        if direction == "right" and self.x < 400:
            self.x+=1
        if direction == "left" and self.x > 100:
            self.x-=1
        self.rect.topleft = (self.x, self.y)
