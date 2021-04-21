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
main_green = pygame.image.load(os.path.join('main_green.jpg'))
main_green = pygame.transform.scale(main_green, (width, height))
bear_img = pygame.image.load(os.path.join('bear_red.png'))
bear = pygame.transform.scale(bear_img, (184, 178))
a_let = pygame.transform.scale(pygame.image.load(os.path.join('Option A.png')), (80, 80))
b_let = pygame.transform.scale(pygame.image.load(os.path.join('Option B.png')), (80, 80))
# bear_rect = bear.get_rect()

# font stuff options: 'timesnewroman', 'georgia', 'helvetica'
# 1. create font object
# 2. render text into image with given color
# 3. blit image to screen


def draw_window(bear_rect, a_position, b_position, a_let, b_let, bear, string_bear, string_a, string_b):
    win.fill(red)
    #win.blit(background, (0, 0))
    win.blit(bear, (bear_rect.x, bear_rect.y))
    win.blit(a_let, (a_position.x, a_position.y))
    win.blit(b_let, (b_position.x, b_position.y))
    text_location = [bear_rect.x - 400, bear_rect.y - 100]
    ptext.draw(string_bear, (text_location[0], text_location[1]), align="center",  width=400)
    ptext.draw(string_a, (a_position.x, a_position.y - 80), width=300)
    ptext.draw(string_b, (b_position.x, b_position.y - 80), width=300)
    pygame.display.flip()


def bear_movement(keys_pressed, bear_rect):
    if keys_pressed[pygame.K_LEFT] and bear_rect.x - VEL > 0:
        bear_rect.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and bear_rect.x + bear_rect[2] + VEL < width:
        bear_rect.x += VEL
    if keys_pressed[pygame.K_UP] and bear_rect.y - VEL > 0:
        bear_rect.y -= VEL
    if keys_pressed[pygame.K_DOWN] and bear_rect.y + bear_rect[3] + VEL < height:
        bear_rect.y += VEL


def main():
    descriptive = 4
    normative = 3
    bear_rect = pygame.Rect(1000, 200, 184, 178)
    a_position = pygame.Rect((width * 0.33)-40, height * 0.75, 80, 80)
    b_position = pygame.Rect((width * 0.66) - 40, height * 0.75, 80, 80)
    string_bear = 'Welcome to our game! I will be your guide on a little choose your own Brown adventure. I will ask you questions with A/B responses. To make a section move me to the letter options displayed on screen. Let"s get started! Press the spacebar to continue.'
    string_a = 'testing again again'  # line breaks needed
    string_b = 'answer 2 testing testing'  # line breaks needed
    clock = pygame.time.Clock()
    run = True
    main_game = False
    results = False
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    string_bear = 'start game text here'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        results_game = True
            if main_game:
                string_bear = 'YAY you have finished the game! But ... it was secretly an experiment about your decision making all along, sorry for not telling you before. press spacebar to continue'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        if descriptive > normative:
                            string_bear = 'Turns out a majority of the decisions you made adhered to descriptive theories. This means that rather than making the rational choice, you tended to follow decision making fallacies and theories used to describe our weird choice. Congrats you’re as illogical as the rest of us!'
                        elif normative > descriptive:
                            string_bear = 'Turns out a majority of the decisions you made were normative. This means that you tended to make the most rational choices, rather than adhering to descriptive theories used to describe frequent fallacies in our decision making. Idk what to tell you make worse decisions more often i guess.'
                        else:
                            string_bear = 'You made the same number of descriptive and normative choices. This means you made an equal number of rational choices and choices that adhere to descriptive theories used to describe frequent fallacies in our decision making. I guess your complex or whatever ...'
                # game questions
            # use break or continue?
        keys_pressed = pygame.key.get_pressed()
        bear_movement(keys_pressed, bear_rect)
        draw_window(bear_rect, a_position, b_position, a_let, b_let, bear, string_bear, string_a, string_b)
        pygame.display.flip()
    main()


if __name__ == "__main__":
    main()

