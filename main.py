import pygame
import random
from redcar import RedCar
from logo import Logo
from play import Play
from sound import Sound
from highway import Highway
from highway import Rules
from bluecar import BlueCar
from pygame import mixer

# set up pygame modules
pygame.init()
pygame.font.init()
pygame.mixer.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Road Busters")

# setting up the screen
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
r = 86
g = 71
b = 51

# important variables for the game
logo = Logo(120, 50)
sound = Sound(475, 10)
play_button = Play(165, 250)
rules = Rules(45, 20)
red_car = RedCar(275, 300)
blue_car = BlueCar(-400, -400)
positions = [(110, 60), (170, 60), (230, 60), (290,60)]
red_car.image = pygame.transform.rotate(red_car.image, 180)
score = 100
blue_y = 0

# Create highway segments
highway1 = Highway(10, 0)
highway2 = Highway(10, -370)  # Position it above highway1
highway3 = Highway(10, -740)  # Position it above highway2

run = True
soundoff = False
show_rules = False
playing = False

#printing stuff
score_statement = "Health: " + str(round(score, 1))
end_statement = "You died!"
display_score = my_font.render(score_statement, True, (0, 0, 0))
display_end = my_font.render(end_statement, True, (0, 0, 0))


def move_blue_car():
    global blue_y
    global blue_car
    global count
    global score
    blue_y += 1
    if blue_y == 370:
        blue_y = -100
        blue_car.rect.x, blue_car.rect.y = random.choice(positions)  # Update bluecar position
        score += 1

# --- Main event loop
while run:
    blue_car = BlueCar(blue_car.rect.x, blue_y)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        # seeing if user closes the game (don't work about this)
        if event.type == pygame.QUIT:
            run = False

        # turns sound button on and off, sees if play button is being clicked
        if event.type == pygame.MOUSEBUTTONUP:
            if sound.rect.collidepoint(event.pos):
                soundoff = not soundoff
                sound.see_sound_off(soundoff)
            if play_button.rect.collidepoint(event.pos):
                start_time = current_time
                show_rules = True
                play_button = Play(-400, -400)
        play_button.see_hover()
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        red_car.move_direction("right")
    if keys[pygame.K_a]:
        red_car.move_direction("left")

    #random needed
    score_statement = "Health: " + str(round(score, 1))
    if score >= 0:
        display_score = my_font.render(score_statement, True, (0, 0, 0))
    # blit zone
    screen.fill((r, g, b))
    if show_rules == False:
        screen.blit(logo.image, logo.rect)
        screen.blit(play_button.image, play_button.rect)
    else:
        # Update highway positions
        highway1.rect.y += 1
        highway2.rect.y += 1
        highway3.rect.y += 1

        # Wrap highway segments when they reach the bottom of the screen
        if highway1.rect.y > SCREEN_HEIGHT:
            highway1.rect.y = -370
        if highway2.rect.y > SCREEN_HEIGHT:
            highway2.rect.y = -370
        if highway3.rect.y > SCREEN_HEIGHT:
            highway3.rect.y = -370

        # Blit highway segments
        if score >= 0:
            screen.blit(highway1.image, highway1.rect)
            screen.blit(highway2.image, highway2.rect)
            screen.blit(highway3.image, highway3.rect)
        
            if current_time - start_time <= 1000:  # show rules for 7 seconds
                screen.blit(rules.image, rules.rect)
            if current_time - start_time > 2000:
                screen.blit(red_car.image, red_car.rect)
                screen.blit(display_score, (10,0))
            if current_time - start_time > 3000:
                if red_car.rect.colliderect(blue_car.rect) != True:
                    move_blue_car()
                else:
                    score -= 0.1
                screen.blit(blue_car.image, blue_car.rect)  # Draw the blue car
        if score < 0:
            screen.blit(display_end, (150, 250))
            
    # screen.blit(c1.image, c1.rect)
    screen.blit(sound.image, sound.rect)
    pygame.display.update()

pygame.quit()

