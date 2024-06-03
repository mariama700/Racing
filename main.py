import pygame
from redcar import RedCar
from logo import Logo
from play import Play
from sound import Sound
from highway import Highway

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Road Busters")

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

r = 86
g = 71
b = 51
collide = "no"
c1 = RedCar(100, 100)
logo = Logo(120, 50)
sound = Sound(475, 10)
play_button = Play(165, 250)
highway = Highway(10, 0)
c1.image = pygame.transform.rotate(c1.image, 180)

# render the text for later

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
soundoff = False
show_rules = False
    
        # --- Main event loop
while run:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if sound.rect.collidepoint(event.pos):
                soundoff = not soundoff
                sound.see_sound_off(soundoff)
            if play_button.rect.collidepoint(event.pos):
                show_rules = True
        play_button.see_hover()

    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        c1.move_direction("right")
    if keys[pygame.K_a]:
        c1.move_direction("left")

    screen.fill((r, g, b))
    if show_rules == False:
        screen.blit(logo.image, logo.rect)
        screen.blit(play_button.image, play_button.rect)
    if show_rules == True:
        screen.blit(highway.image, highway.rect)
    #screen.blit(c1.image, c1.rect)
    screen.blit(sound.image, sound.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
