import pygame

class Sound:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("sound.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .2, self.image_size[1] * .2)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
    def see_sound_off(self, soundoff):
        if soundoff == True:
            self.image = pygame.image.load("soundoff.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * .2, self.image_size[1] * .2)
            self.image = pygame.transform.scale(self.image, scale_size)
