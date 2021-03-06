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
main_green = pygame.image.load(os.path.join('assets', 'main_green.jpg'))
main_green = pygame.transform.scale(main_green, (width, height))
bear_img = pygame.image.load(os.path.join('assets', 'bear_red.png'))
bear = pygame.transform.scale(bear_img, (184, 178))
a_let = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'Option A.png')), (80, 80))
b_let = pygame.transform.scale(pygame.image.load(os.path.join('Option B.png')), (80, 80))
# bear_rect = bear.get_rect()
SciLi_mice = pygame.image.load(os.path.join('assets', 'SciLi_mice.png'))
SciLi_mice = pygame.transform.scale(SciLi_mice, (width, height))
Andrews = pygame.image.load(os.path.join('assets', 'andrews.jpg'))
Andrews = pygame.transform.scale(Andrews, (width, height))
Bookstore = pygame.image.load(os.path.join('assets', 'bbookstore.jpg'))
Bookstore = pygame.transform.scale(Bookstore, (width, height))
Blueno = pygame.image.load(os.path.join('assets', 'Blueno.jpg'))
Blueno = pygame.transform.scale(Blueno, (width, height))
classroom = pygame.image.load(os.path.join('assets', 'classroom_pic.jpg'))
classroom = pygame.transform.scale(classroom, (width, height))
dorm_room = pygame.image.load(os.path.join('assets', 'dorm_room.jpg'))
dorm_room = pygame.transform.scale(dorm_room, (width, height))
inside_Rock = pygame.image.load(os.path.join('assets', 'inside_Rock.jpg'))
inside_Rock = pygame.transform.scale(inside_Rock, (width, height))
outside_SciLi = pygame.image.load(os.path.join('assets', 'Outside_sci_li.jpg'))
outside_SciLi = pygame.transform.scale(outside_SciLi, (width, height))
Thayer_street = pygame.image.load(os.path.join('assets','Thayer-Street.jpg'))
Thayer_street = pygame.transform.scale(Thayer_street, (width, height))
VDub  = pygame.image.load(os.path.join('assets', 'Verney-Woolley.jpg'))
VDub = pygame.transform.scale(VDub, (width, height))
main_green_snake = pygame.image.load(os.path.join('assets', 'main_green_snake.jpg'))
main_green_snake = pygame.transform.scale(main_green_snake, (width, height))
Starbucks = pygame.image.load(os.path.join('assets', 'starbucks.jpeg'))
Starbucks = pygame.transform.scale(Starbucks, (width, height))
Beyonce_concert = pygame.image.load(os.path.join('assets', 'beyonce_concert.jpeg'))
Beyonce_concert = pygame.transform.scale(Beyonce_concert, (width, height))
Froyo_store = pygame.image.load(os.path.join('assets', 'froyo_store.jpeg'))
Froyo_store = pygame.transform.scale(Froyo_store, (width, height))
roller_rink = pygame.image.load(os.path.join('assets', 'roller_rink_pic.jpg'))
roller_rink = pygame.transform.scale(roller_rink, (width, height))
movies = pygame.image.load(os.path.join('assets', 'movie_backdrop.jpeg'))
movies = pygame.transform.scale(movies, (width, height))
jail = pygame.image.load(os.path.join('assets', 'jail_pic.jpeg'))
jail = pygame.transform.scale(jail, (width, height))

# font stuff options: 'timesnewroman', 'georgia', 'helvetica'
# 1. create font object
# 2. render text into image with given color
# 3. blit image to screen


def draw_window(bear_rect, a_position, b_position, a_let, b_let, bear, string_bear, string_a, string_b):
    win.fill(red)
    win.blit(background_variable, (0, 0))
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
    bear_rect = pygame.Rect(1000, 200, 184, 178)
    a_position = pygame.Rect((width * 0.33)-40, height * 0.75, 80, 80)
    b_position = pygame.Rect((width * 0.66) - 40, height * 0.75, 80, 80)
    string_bear = 'welcome to the game!'  # no line breaks needed
    string_a = 'testing again again'  # line breaks needed
    string_b = 'answer 2 testing testing'  # line breaks needed
    clock = pygame.time.Clock()
    run = True
    intro = True
    main_game = True
    results = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        # start game text
        # use embedded while loops for intro and game sections
        while intro:
            string_bear = 'Welcome to the game, ill be your guide today! Were going to go on an adventure that you choose. To pick option A blah blah blah'
            # greetings and instructions part
            # wait function to display text or space bar to continue?
            intro = False
        while main_game:
            # questions loop
            # use colliderect function as option selection
            # calculations and conditionals should stay the same
        while results:
            #DISPLAY RESULTS

        keys_pressed = pygame.key.get_pressed()
        bear_movement(keys_pressed, bear_rect)
        draw_window(bear_rect, a_position, b_position, a_let, b_let, bear, string_bear, string_a, string_b)
        pygame.display.flip()
    main()


if __name__ == "__main__":
    main()

