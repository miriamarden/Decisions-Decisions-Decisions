# testing out basic pygame stuff
import pygame
import os

import ptext

pygame.init()
width, height = 1200, 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Decisions, Decisions, Decisions')

# initializing variables
white = (255, 255, 255)
blue_green = (155, 250, 255)
magenta = (255, 155, 255)
red = (255, 75, 75)
VEL = 5
FPS = 60

font = pygame.font.SysFont('georgia.ttf', 24)
test_font = font.render('Hello', True, white)
welcome = font.render('Welcome to the Brown experience! Today Ill be your guide.', True, white)

# images
# from stack overflow
# rect = rect.move((x,y))
# screen.blit(img_name, rect)
# define screen size
main_green = pygame.image.load(os.path.join('main_green.jpg'))
main_green = pygame.transform.scale(main_green, (width, height))
bear_img = pygame.image.load(os.path.join('bear_red.png'))
bear = pygame.transform.scale(bear_img, (184, 178))
# bear_rect = bear.get_rect()
# SPACE = pygame.transform.scale(pygame.image.load(
# os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))
# pygame.display.flip()

# font stuff options: 'timesnewroman', 'georgia', 'helvetica'
# 1. create font object
# 2. render text into image with given color
# 3. blit image to screen


def draw_window(bear_rect, bear, welcome):
    win.fill(red)
    win.blit(welcome, (400, 300))
    win.blit(bear, (bear_rect.x, bear_rect.y))
    text_location = [bear_rect.x - 400, bear_rect.y - 100]
    ptext.draw('Honorable choice. You venture into the Brown bookstore with a flexible budget of $60 looking for some merch. \nAt the front of the bookstore is a grand display of Browns new line of hoodies. Each hoodie costs $100. \nYou search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you', (text_location[0], text_location[1]), align="center",  width=400)
    pygame.display.flip()


def magenta_movement(keys_pressed, bear_rect):
    if keys_pressed[pygame.K_LEFT] and bear_rect.x - VEL > 0:
        bear_rect.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and bear_rect.x + bear_rect[2] + VEL < width:
        bear_rect.x += VEL
    if keys_pressed[pygame.K_UP] and bear_rect.y - VEL > 0:
        bear_rect.y -= VEL
    if keys_pressed[pygame.K_DOWN] and bear_rect.y + bear_rect[3] + VEL < height:
        bear_rect.y += VEL


# testing loop with questions ...
# welcome = font.render('Welcome to the Brown experience! Let"s get started!.', True, white)


def main():
    # background = win.fill(red)
    bear_rect = pygame.Rect(1000, 200, 184, 178)
    print(bear_rect.x)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        magenta_movement(keys_pressed, bear_rect)
        draw_window(bear_rect, bear, welcome)
        pygame.display.flip()
    main()


if __name__ == "__main__":
    main()

