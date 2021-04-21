# testing out basic pygame stuff
import pygame
import os
import ptext

pygame.init()
width, height = 1200, 900
win = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Decisions, Decisions, Decisions')
##use pdraw to add a background color to the text

# SOUND CODE
pygame.mixer.init()
horn_fail_sound = pygame.mixer.Sound(os.path.join('sound', 'horn_fail_lose.wav'))
yay_sound = pygame.mixer.Sound(os.path.join('sound', 'Yay_sound.wav'))
tada_sound = pygame.mixer.Sound(os.path.join('sound', 'tada_sound.wav'))
bear_song = pygame.mixer.Sound(os.path.join('sound', 'tada_sound.wav'))

# in game loop
# pygame.mixer.music.play(-1)

# initializing variables
white = (255, 255, 255)
blue_green = (155, 250, 255)
magenta = (255, 155, 255)
red = (255, 75, 75)
brown = (100, 50, 10)
VEL = 5
FPS = 60

font = pygame.font.SysFont('georgia.ttf', 24, red)
test_font = font.render('Hello', True, white)
welcome = font.render('Welcome to the Brown experience! Today Ill be your guide.', True, white)

# images
# main_green = pygame.image.load(os.path.join('Main Green.png'))
# main_green = pygame.transform.scale(main_green, (width, height))
bear_img = pygame.image.load(os.path.join('bear_red.png'))
bear = pygame.transform.scale(bear_img, (184, 178))
a_let = pygame.transform.scale(pygame.image.load(os.path.join('Option A.png')), (80, 80))
b_let = pygame.transform.scale(pygame.image.load(os.path.join('Option B.png')), (80, 80))

SciLi_mice = pygame.image.load(os.path.join('SciLi_mice.png'))
SciLi_mice = pygame.transform.scale(SciLi_mice, (width, height))
Andrews = pygame.image.load(os.path.join('andrews.jpg'))
Andrews = pygame.transform.scale(Andrews, (width, height))
Bookstore = pygame.image.load(os.path.join('bbookstore.jpg'))
Bookstore = pygame.transform.scale(Bookstore, (width, height))
Blueno = pygame.image.load(os.path.join('Blueno.jpg'))
Blueno = pygame.transform.scale(Blueno, (width, height))
classroom = pygame.image.load(os.path.join('classroom_pic.jpg'))
classroom = pygame.transform.scale(classroom, (width, height))
dorm_room = pygame.image.load(os.path.join('dorm_room.jpg'))
dorm_room = pygame.transform.scale(dorm_room, (width, height))
inside_Rock = pygame.image.load(os.path.join('Rock_stacks.jpg'))
inside_Rock = pygame.transform.scale(inside_Rock, (width, height))
outside_SciLi = pygame.image.load(os.path.join('Outside_sci_li.jpg'))
outside_SciLi = pygame.transform.scale(outside_SciLi, (width, height))
Thayer_street = pygame.image.load(os.path.join('Thayer-Street.jpg'))
Thayer_street = pygame.transform.scale(Thayer_street, (width, height))


# VDub  = pygame.image.load(os.path.join('Verney-Woolley.jpg.jpg'))
# VDub = pygame.transform.scale(VDub, (width, height))
# bear_rect = bear.get_rect()

# font stuff options: 'timesnewroman', 'georgia', 'helvetica'
# 1. create font object
# 2. render text into image with given color
# 3. blit image to screen


def draw_window(bear_rect, a_position, b_position, a_let, b_let, bear, string_bear, string_a, string_b, background, ):
    win.blit(background, (0, 0))
    win.blit(bear, (bear_rect.x, bear_rect.y))
    win.blit(a_let, (a_position.x, a_position.y))
    win.blit(b_let, (b_position.x, b_position.y))
    text_location = [bear_rect.x - 400, bear_rect.y - 100]
    ptext.draw(string_bear, (text_location[0], text_location[1]), align="center", width=400, color=brown,
               background=white)
    ptext.draw(string_a, (a_position.x, a_position.y - 80), width=300, background=brown)
    ptext.draw(string_b, (b_position.x, b_position.y - 80), width=300, background=brown)
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
    a_position = pygame.Rect((width * 0.33) - 40, height * 0.75, 80, 80)
    b_position = pygame.Rect((width * 0.66) - 40, height * 0.75, 80, 80)
    string_bear = ''  # no line breaks needed
    string_a = ''  # line breaks needed
    string_b = ''  # line breaks needed
    clock = pygame.time.Clock()
    run = True
    intro = True
    main_game = True

    gameplay_scenarios = {
        'A': {
            1: [Andrews, 'retail', 'food', 'retail or food therapy?', 'B'],
            2: [classroom, 'lunch', 'class', 'It is the first day of classes, and you just shopped three classes in a row. Do you take a break for lunch or shop another class?', 'C']
        },
        'B': {
            1: [Bookstore, 'Buy the $80 hoodie', 'Leave the store', 'Honorable choice. You venture into the Brown bookstore with a flexible budget of $60 looking for some merch. At the front of the bookstore is a grand display of Browns new line of hoodies.\nEach hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you', 'D'],
            2: [Bookstore, 'flex', 'nap', 'Now that you have made your purchase, are you going to flex with your new hoodie on the main green or choose modesty and take a cozy nap in your toasty new fit? ', 'E']
        },
        'C': {
            1: [Andrews, 'yes', 'no', 'Lunch it is! You are not on meal plan this year, but you are really hungry and you are craving a pasta bowl from Andrews. \nYou pay $8.75 in cash for your pasta bowl and sit down, all excited to eat it. It looks like you got the last pasta bowl, though, so someone approaches you saying they REALLY wanted a pasta bowl too.They offer to pay you $9.75 for your pasta bowl - $1.00 more than you initially paid. Do you accept their offer?', 'F'],
            2: [classroom,'S/NC', 'grade', 'Good choice! You head to your next class. You read the course description and reviews and it seems super interesting. The teacher walks in and hands out the syllabus; it looks manageable. Prof then emphasizes that her course is very intense and will require long hours of focused work and diligent time management. She further articulates that 65% of students tend to get a final grade below an A. Do you decide to take the class S/NC or take it for a grade?' 'G']
        }
    }


    background = classroom
    scenario = 'A'
    string_bear = 'Alex, your partner of 4 years, the love of your life, just broke up with you right before your flight to Brown for your first semester of university - they said they cannot do long distance. You are pursuing a double major, so it would be wise of you to start the heavy lifting from early. However, you are heartbroken and unsure of your ability to offer your best work. Do you'
    string_a = 'Take mostly easy courses to prevent yourself from having a mental breakdown mid semester'
    string_b = 'Take harder courses - you are a soldier!'
    should_update = False

    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): ###Revanna
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        # start game text
        # use embedded while loops for intro and game sections
        while intro:
            descriptive = 0
            normative = 0
            pygame.mixer.Sound.play(bear_song)
            string_bear = 'Welcome to the game, ill be your guide today! Were going to go on an adventure that you choose. To pick option A blah blah blah'
            # greetings and instructions part
            # wait function to display text or space bar to continue?
            intro = False

        if a_position.colliderect(bear_rect):
            option, should_update = 1, True
        elif b_position.colliderect(bear_rect):
            option, should_update = 2, True
        else:
            should_update = False

        keys_pressed = pygame.key.get_pressed()
        bear_movement(keys_pressed, bear_rect)
        if should_update:
            bear_rect = pygame.Rect(1000, 200, 184, 178)
            background, string_a, string_b, string_bear, scenario = gameplay_scenarios[scenario][option]
        draw_window(bear_rect, a_position, b_position, a_let, b_let, bear, string_bear, string_a, string_b, background)
        pygame.display.flip()


if __name__ == "__main__":
    main()


        keys_pressed = pygame.key.get_pressed()
        bear_movement(keys_pressed, bear_rect)
        draw_window(bear_rect, a_position, b_position, a_let, b_let, bear, string_bear, string_a, string_b, background)
        pygame.display.flip()
    main()


if __name__ == "__main__":
    main()
