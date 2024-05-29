import pygame
from pygame import image
from pygame.transform import scale

#TO DO: Make function to change scale rather than repeating code
class Sound:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sound_on_image = pygame.image.load("sound.png")
        self.sound_off_image = pygame.image.load("soundoff.png")
        self.image = self.sound_on_image
        #changing scale
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .2, self.image_size[1] * .2)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()

    def see_sound_off(self, soundoff):
        if soundoff:
            self.image = self.sound_off_image
            #changing scale
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            width = int(self.image_size[0] * 0.2)
            height = int(self.image_size[1] * 0.2)
            self.image = pygame.transform.scale(self.image, (width, height))
            self.image_size = self.image.get_size()
    
        else:
            self.image = self.sound_on_image
            #changing scale
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            width = int(self.image_size[0] * 0.2)
            height = int(self.image_size[1] * 0.2)
            self.image = pygame.transform.scale(self.image, (width, height))
            self.image_size = self.image.get_size()
