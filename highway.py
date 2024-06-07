#make rules slightly transparent
#make popup show after 5 seconds
import pygame


class Highway:
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = pygame.image.load("highway.png")
    self.image_size = self.image.get_size()
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

class Rules:
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = pygame.image.load("rules.png")
    self.image_size = self.image.get_size()
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
    scale_size = (self.image_size[0] * .62, self.image_size[1] * .62)
    self.image = pygame.transform.scale(self.image, scale_size)
    self.image_size = self.image.get_size()
