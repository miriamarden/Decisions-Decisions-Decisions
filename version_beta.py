# testing out basic pygame stuff
import pygame
width, height = 900, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Decisions, Decisions, Decisions')

#initializing variables
white = (255, 255, 255)
blue_green = (155, 250, 255)
magenta = (255, 155, 255)
VEL = 5
FPS = 60

win.fill(blue_green)
#pygame.display.flip()
#def draw_window(magenta_rect):


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
        win.fill(blue_green)
        pygame.draw.rect(win, magenta, magenta_rect)
        magenta_movement(keys_pressed, magenta_rect)
        pygame.display.flip()
    main()


if __name__ == "__main__":
    main()

