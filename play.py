import pygame

class Play:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.not_clicked_image = pygame.image.load("play_button.png")
        self.play_button_hover_image = pygame.image.load("play_button_hover.png")
        self.image = self.not_clicked_image
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .4, self.image_size[1] * .4)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()

                
    def see_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            collide = "yes"
        else:
            collide = "no"
            
        if collide == "yes":
            self.image = self.play_button_hover_image
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            width = int(self.image_size[0] * 0.72)
            height = int(self.image_size[1] * 0.72)
            self.image = pygame.transform.scale(self.image, (width, height))
            self.image_size = self.image.get_size()
            
        if collide == "no":
            self.image = self.not_clicked_image
            self.image = self.not_clicked_image
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * .4, self.image_size[1] * .4)
            self.image = pygame.transform.scale(self.image, scale_size)
            self.image_size = self.image.get_size()
