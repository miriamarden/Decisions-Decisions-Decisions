# testing out basic pygame stuff
import pygame
import os

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


def draw_window(magenta_rect, bear, test_font):
    win.fill(red)
    win.blit(test_font, (400, 300))
    win.blit(bear, (magenta_rect.x, magenta_rect.y))
    pygame.display.flip()


def magenta_movement(keys_pressed, magenta_rect):
    if keys_pressed[pygame.K_LEFT] and magenta_rect.x - VEL > 0:
        magenta_rect.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and magenta_rect.x + magenta_rect[2] + VEL < width:
        magenta_rect.x += VEL
    if keys_pressed[pygame.K_UP] and magenta_rect.y - VEL > 0:
        magenta_rect.y -= VEL
    if keys_pressed[pygame.K_DOWN] and magenta_rect.y + magenta_rect[3] + VEL < height:
        magenta_rect.y += VEL


def main():
    #background = win.fill(red)
    magenta_rect = pygame.Rect(0, 0, 50, 50)
    print(magenta_rect.x)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        magenta_movement(keys_pressed, magenta_rect)
        draw_window(magenta_rect, bear, test_font)
        pygame.display.flip()
    main()


if __name__ == "__main__":
    main()

