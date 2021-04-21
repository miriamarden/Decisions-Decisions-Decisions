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
brown = (100, 50, 10)
VEL = 5
FPS = 60

font = pygame.font.SysFont('georgia.ttf', 24)
test_font = font.render('Hello', True, white)

# SOUND CODE
pygame.mixer.init()
horn_fail_sound = pygame.mixer.Sound(os.path.join('sound', 'horn_fail_lose.wav'))
yay_sound = pygame.mixer.Sound(os.path.join('sound', 'Yay_sound.wav'))
tada_sound = pygame.mixer.Sound(os.path.join('sound', 'tada_sound.wav'))
bear_song = pygame.mixer.Sound(os.path.join('sound', 'tada_sound.wav'))

# images
bear_img = pygame.image.load(os.path.join('assets', 'bear_red.png'))
bear = pygame.transform.scale(bear_img, (184, 178))
a_let = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'Option A.png')), (80, 80))
b_let = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'Option B.png')), (80, 80))
main_green = pygame.image.load(os.path.join('assets', 'main_green.jpg'))
main_green = pygame.transform.scale(main_green, (width, height))
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
Thayer_street = pygame.image.load(os.path.join('assets', 'Thayer-Street.jpg'))
Thayer_street = pygame.transform.scale(Thayer_street, (width, height))
VDub = pygame.image.load(os.path.join('assets', 'Verney-Woolley.jpg'))
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
the_office = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'doctors_office.jpeg')), (width, height))

def draw_window(bear_rect, a_position, b_position, a_let, b_let, bear, string_bear, string_a, string_b, background):
    win.blit(background, (0, 0))
    win.blit(bear, (bear_rect.x, bear_rect.y))
    win.blit(a_let, (a_position.x, a_position.y))
    win.blit(b_let, (b_position.x, b_position.y))
    text_location = [bear_rect.x - 400, bear_rect.y - 100]
    ptext.draw(string_bear, (text_location[0], text_location[1]), align="center", width=400, color=brown,
               background=white)
    ptext.draw(string_a, (a_position.x-120, a_position.y - 120), fontsize=40, align="center", width=350, color=brown, background=white)
    ptext.draw(string_b, (b_position.x-120, b_position.y - 120), fontsize=40, align="center", width=350, color=brown, background=white)
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
    string_bear = 'Welcome to our game! I will be your guide on a little choose-your-own adventure, Brown style. I will ask you questions with A/B responses. To make a selection, use the arrows on your keyboard to move me to the letter options displayed on screen. Let"s get started! Press the spacebar to continue.'
    string_a = ''  
    string_b = ''  
    background = main_green_snake
    descriptive = 0
    normative = 0
    clock = pygame.time.Clock()
    run = True
    game_on = False
    current_state = 0
    should_update = False

    gameplay_scenarios = {
        'A': {
            #hard semester
            1: [classroom, 'class', 'lunch', 'It is the first day of classes, and you just shopped three classes in a row. Do you take a break for lunch or shop another class?', 'B'],
            #easy semester
            2: [main_green, 'retail', 'eating', 'You are looking for something to distract you from your pain. What shall it be, retail therapy or eating your sorrows away?', 'C']
        },
        'B': {
            #shop another class class
            1: [classroom, 'grade', 'S/NC', 'Good choice! You head to your next class. You read the course description and reviews, and it seems super interesting. The teacher walks in and hands out the syllabus; it looks manageable. Prof then emphasizes that her course is very intense and will require long hours of focused work and diligent time management. She further articulates that 65% of students tend to get a final grade below an A. Do you decide to take the class S/NC or take it for a grade?', 'D1'],
            #go to lunch
            2: [Andrews, 'yes', 'no', 'Lunch it is! You are not on meal plan this year, but you are really hungry and you are craving a pasta bowl from Andrews. You pay $8.75 in cash for your pasta bowl and sit down, all excited to eat it. It looks like you got the last pasta bowl, though, so someone approaches you saying they REALLY wanted a pasta bowl too.They offer to pay you $9.75 for your pasta bowl - $1.00 more than you initially paid. Do you accept their offer?', 'E1']
        },
        'C': {
            1: [Bookstore, 'Leave the store without buying anything', 'Buy the $80 hoodie', 'Honorable choice. You venture into the Brown bookstore with a flexible budget of $60 looking for some merch. At the front of the bookstore is a grand display of Browns new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you', 'D2'],
            2: [Andrews, 'yes', 'no', 'Good choice! You are not on meal plan this year, but you are craving a pasta bowl from Andrews. You pay $8.75 in cash for your pasta bowl and sit down, all excited to eat it. It looks like you got the last pasta bowl, though, so someone approaches you saying they REALLY wanted a pasta bowl too.They offer to pay you $9.75 for your pasta bowl - $1.00 more than you initially paid. Do you accept their offer?', 'E2']
        },
        'D1': {
            #take the class for a grade
            1: [classroom, 'drop', 'keep', 'Weeks later, the S/NC deadline has passed, but you are struggling in the class. You do not enjoy the material, and you realize you probably do not even need to be in this class. You can drop the class with no fee, but you have already invested 75+ hours of work into the class (5 weeks of work), and you spent $65 on the textbook. Do you drop the class or keep the class?', 'F1'],
            #take the class S/NC
            2: [Bookstore, 'Leave the store without buying anything', 'Buy the $80 hoodie', 'With all the time you saved from taking the class S/NC, you decide to do some shopping. You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. At the front of the bookstore is a grand display of the new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you', 'G1']
        },
        'E1': {
            #yes sell pasta
            1: [Bookstore, 'Leave the store without buying anything', 'Buy the $80 hoodie', 'You are feeling richer now, so you decide to treat yourself to a Brown hoodie. You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. At the front of the bookstore is a grand display of the new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you', 'G1'],
            #no sell pasta
            2: [Andrews, 'nap', 'coffee', 'After all that yummy pasta, you fall into a food coma. You really want some coffee, but you made a goal to only buy coffee a maximum of twice a week. You followed your goal perfectly last week, but you already bought coffee twice this week. Do you decide to just go an extra time this week, or do you energize yourself with a nap instead?', 'H1']

        },

        'F1':{
            #drop the class
            1: [Bookstore, 'Leave the store without buying anything', 'Buy the $80 hoodie', 'With all the time you saved from dropping the class, you decide to do some shopping. You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. At the front of the bookstore is a grand display of the new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you' 'G1'],
            #keep the class
            2: [classroom, 'nap', 'coffee', 'If you are going to make it through this class, you will need coffee. But, you made a goal to only buy coffee a maximum of twice a week. You followed your goal perfectly last week, but you already bought coffee twice this week. Do you decide to just go an extra time this week, or do you energize yourself with a nap instead?', 'H1']
        },

        'G1': {
            #Leave the store without buying anything
            1: [Thayer_street, 'wrap', 'fried chicken', 'Since you saved yourself some money, you decide to treat yourself to dinner on Thayer. You could really go for some delicious fried chicken, but you have promised yourself you would cut back on fried foods. You have been good about it; you have not had any fried food in two weeks. Do you decide to stick to your goal and get a healthy wrap, or do you reward yourself for your progress and go for the fried chicken?', 'J1'],
            #Buy the $80 hoodie
            2: [outside_SciLi, 'SciLi', 'Rock', 'Unfortunately, you are now broke. You head to the SciLi to look for a summer internship on BrownConnect. You run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the SciLi is. They tell you that the last time they were in the stacks, someone there saw a mouse. Gross. But you are already so close to the SciLi. Do you decide to go to the Sci Li since you are already so close and all stacks are rightfully terrible, or do you go to the Rock instead?', 'K1']

        },

        'H1': {
            #Both of these paths are the same
            1 and 2: [dorm_room, 'Change the location to your room', 'Stick to your friends room; the more people, the better!', 'Now, you feel more energized, so you decide to hang with some friends. You guys decide to hang out in Emwool. But, your friend gets a text from her roommate saying her roommate is having some friends over. She suggests you all hang out in your room instead Do you decide to:', 'I1'],
        },

        #This is an ending
        'I1': {
            #Your room
            1: [dorm_room, '', '', 'You have a great time with your friends and a great rest of the semester! Some more good news: we found out what kind of decision-maker you are! press the spacebar to continue', ''],
            #Friend's room
            2: [VDub, '', '', 'On the way to Emwool, you cut through the VDub, and you accidentally get cooked into the meatloaf. So sad! But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', '']

        },
        #This is an ending
        'J1': {
            #wrap
            1: [Thayer_street, '', '', 'Unfortunately, the wrap you got was poisoned. So sad! But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', ''],
            #fried chicken
            2: [Thayer_street, '', '', 'Unfortunately, on the way to the fried chicken place, Christmas Crane falls on you and crushes you. So sad! But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', '']
        },

        'K1': {
            #Sci Li
            1: [SciLi_mice, '', '', 'You go to the Scili are get attacked by the army of mice hiding in the stacks. So sad! But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', ''],
            # Rock
            2: [inside_Rock, 'The $15/hour internship with the unknown acceptance rate', 'The $13/hour internship with the 40% acceptance rate','Once at the Rock, you open BrownConnect and find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. You find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. Both applications are due tonight, so you only have time to apply to one. Which internship do you choose?', 'L1']

        },

        'L1': {
            1 and 2: [Blueno, '', '', 'When you finish the application, you head back to your room. As you pass Blueno, he comes alive and wraps you in his arms to be forever held captive. Cute! Before you hang with Blueno forever, though, let us tell you what kind of decision-maker you are! press the spacebar to continue', '']
        },

        'D2': {
            1: [classroom, 'grade', 'S/NC', 'You’re making responsible decisions today! You decide to keep this up and head to your next class. You read the course description and reviews and it seemed super interesting. The teacher walks in and hands out the syllabus – it looks manageable. Prof then emphasizes that her course is very intense and will require long hours of focused work and diligent time management. She further articulates that 65% of students tend to get a final grade below an A. Do you decide to take the class S/NC or take it for a grade?', 'F2'],
            2: [Bookstore, 'flex', 'nap', 'Now that you have made your purchase, are you going to flex with your new hoodie on the main green or choose modesty and take a cozy nap in your toasty new fit?', 'G2']
        },
        'E2': {
            1: [inside_Rock, 'second internship', 'first internship', 'With money on the mind you decide to look for internships at the Rock. You open BrownConnect and find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. You find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. Both applications are due tonight, so you only have time to apply to one. Which internship do you choose?', 'H2'],
            2: [classroom, 'drop', 'keep', 'Yum! Your tummy is full and and you are ready for your next class. You have been struggling in this one but the S/NC deadline has passed. You do not enjoy the material, and you realize you probably do not even need to be in this class. You can drop the class with no fee, but you have already invested 75+ hours of work into the class (5 weeks of work), and you spent $65 on the textbook. Do you drop the class or keep the class?', 'I2']
        },
        'F2': {
            1: [classroom, 'roller rink', 'movies', 'You are proud of your courage and decide to treat yourself with an adventure. Are you going to the roller rink or the movie theatre?', 'J2'],
            2: [Starbucks, 'no', 'yes', 'You are feeling liberated and think you deserve to feed your coffee addiction, however you made a goal to only buy coffee a maximum of twice a week. You followed your goal perfectly last week, but you already bought coffee twice this week. Do you decide to just go an extra time this week?', 'K2' ]
        },
        'G2': {
            1: [main_green, 'SciLi', 'Rock', 'You are starting to feel insecure about how good you look. Are you all beauty and no brains?? You decide to head to the Scili to validate your smartness. While walking over you run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the SciLi is. They tell you that the last time they were in the stacks, someone there saw a mouse. Gross. But you are already so close to the SciLi. Do you decide to go to the Sci Li since you are already so close and all stacks are rightfully terrible, or do you go to the Rock instead?', 'L2'],
            2: [Andrews, 'yes', 'no', 'You just had the snuggliest nap of your life. Now you have the post nap munchies. You are not on meal plan this year, but you are craving a pasta bowl from Andrews. You pay $8.75 in cash for your pasta bowl and sit down, all excited to eat it. It looks like you got the last pasta bowl, though, so someone approaches you saying they REALLY wanted a pasta bowl too. They offer to pay you $9.75 for your pasta bowl - $1.00 more than you initially paid. Do you accept their offer?', 'M2']
        },
        'H2': {
            1: [Starbucks, 'no', 'yes', 'Applying for internships is tiring. Coffee break? You made a goal to only buy coffee a maximum of twice a week. You followed your goal perfectly last week, but you already bought coffee twice this week. Do you decide to just go an extra time this week?', 'N2'],
            2: [Bookstore, 'Leave the bookstore without buying anything' 'Buy the $80 hoodie', 'You’re about to be swimming in green so you need some new drip - preferably some threads that rep your school! You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. At the front of the bookstore is a grand display of Browns new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you...', 'O2']
        },
        'I2': {
            1: [outside_SciLi, 'SciLi', 'Rock', 'You’re feeling a little academically insecure so you decide to go to the library and beat the books. You’re on your way to a late night grind in the stacks at the SciLi. You run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the scili is. They tell you that the last time they were in the stacks, someone there saw a mouse. Gross. But you’re already so close to the SciLi. Do you decide to go to the Sci Li since you’re already so close and all stacks are rightfully terrible, or do you go to the Rock instead?', 'P2'],
            2: [inside_Rock, 'Change location to your room', 'Stick to your friends room; the more the merrier!', 'You see your friends at the Rock and decide to hang out later. You guys decide to hang out in Emwool. But, your friend gets a text from her roommate saying her roommate is having some friends over. She suggests you all hang out in your room instead Do you decide to:', 'Q2']
        },
        'J2': {
            1: [roller_rink, '', '', 'You fall and somebody skates over your face, mangling it horribly, so you drop out of school and join the circus. But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', ''],
            2: [movies, '', '', 'The movie inspires you and helps you discover your true purpose in life - you dropout of school to become a country music star. Plus, we found out what kind of decision-maker you are! press the spacebar to continue', '']
        },
        'K2': {
            1: [Starbucks, '', '', 'You drop out of school and become an ambassador for self control and overcoming addiction. Your success is overwhelming. Plus, more good news: we found out what kind of decision-maker you are! press the spacebar to continue', ''],
            2: [Starbucks, '', '', 'You have a caffeine overload and pass out in Starbucks. Brown ships you back to your home state/country because they do not condone drug addiction on campus! But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', '']
        },
        'L2': {
            1: [SciLi_mice, '', '', 'The mice of SciLi have made you their king/queen! You decide you no longer have use for education. More good news: we found out what kind of decision-maker you are! press the spacebar to continue', ''],
            2: [inside_Rock, 'Change the location to you room', 'Stick to your friends room; the more people the better!', 'After a bit of studying at the Rock you decide you deserve to hang out with some friends. You and your friends decide to hang out in Emwool. But, your friend gets a text from her roommate saying her roommate is having some friends over. She suggests you all hang out in your room instead Do you decide to:', 'R2']
        },
        'M2': {
            1: [dorm_room, '', '', 'A blizzard hits PVD and you have no pasta so you starve to death in your dorm. But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', ''],
            2: [Andrews, '', '', 'You have a severe lactose intolerance reaction to the pasta and explode from the gas build up within you. But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', '']
        },
        'N2': {
            1: [classroom, '', '', 'Low on energy, you fall asleep in class and your professor despises you forever. They destroy your academic reputation and you end up dropping out. But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', ''],
            2: [classroom, '', '', 'Feeling energized you start the semester off strong! You are sure to make dean’s list. Plus, we found out what kind of decision-maker you are! press the spacebar to continue', '']
        },
        'O2': {
            1: [Beyonce_concert, '', '', 'You lose a nipple to frostbite but you go see Beyonce in concert with the money you saved at the Bookstore! Plus, more good news: we found out what kind of decision-maker you are! press the spacebar to continue', ''],
            2: [Bookstore, '', '', 'The shuttle runs you over as you leave the bookstore! You can’t afford the surgery you need because you maxed your card in the bookstore and Health services can’t afford to pay fot it because of COVID cutbacks :( But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', '']
        },
        'P2': {
            1: [SciLi_mice, 'froyo', 'nap', 'You make friends with the mice and get a week`s worth of work done! You decide to celebrate. Will it be froyo or a well deserved nap?', 'S2'],
            2: [inside_Rock, 'Change the location to your room', 'Stick to your friends room; the more people the better!', 'You see your friends at the Rock and decide to hang out later. You guys decide to hang out in Emwool. But, your friend gets a text from her roommate saying her roommate is having some friends over. She suggests you all hang out in your room instead Do you decide to:', 'T2']
        },
        'Q2': {
            1: [dorm_room, '', '', 'You and your friends bond in a special way and become life long companions forever :D Plus, more good news: we found out what kind of decision-maker you are! press the spacebar to continue', ''],
            2: [jail, '', '', 'One of your ditsy friends gets lost on the way and you are convicted of their murder. You spend the rest of your life in PVD jail. But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', '']
        },
        'R2': {
            1: [dorm_room, '', '', 'You and your friends laugh yourselves into a semester long coma - literally. But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', ''],
            2: [main_green_snake, '', '', 'On the way to Emwool you trip over someone’s illegal pet snake and it eats you. But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', '']
        },
        'S2': {
            1: [Froyo_store, '', '', 'BRAIN FREEZE!! You contract a rare condition called super serious brain freeze and are no longer able to pursue higher level education. But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', ''],
            2: [dorm_room, '', '', 'You wake up with an idea for a startup company and become a millionaire by senior year. Plus, more good news: we found out what kind of decision-maker you are! press the spacebar to continue', '']
        },
        'T2': {
            1: [dorm_room, '', '', 'You and your friends bond in a special way and become life long companions forever :D Plus, more good news: we found out what kind of decision-maker you are! press the spacebar to continue', ''],
            2: [jail, '', '', 'One of your ditsy friends gets lost on the way and you are convicted of their murder. You spend the rest of your life in PVD jail. But, on the bright side, we found out what kind of decision-maker you are! press the spacebar to continue', '']
        }

    }

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if current_state == 0:
                    background = main_green_snake
                    scenario = 'A'
                    string_bear = 'Right before your flight to Brown for your first semester of university you had a huge fight with your bestfriend since 3rd grade - they said they dont wanna be long distance friends (?). You are pursuing a double major, so it would be wise of you to start the heavy lifting from early. However, you are heartbroken and unsure of your ability to offer your best work. Do you'
                    string_a = 'Take harder courses - you are a soldier!'
                    string_b = 'Take mostly easy courses to prevent yourself from having a mental breakdown mid semester'
                    # should_update = False
                    game_on = True
                    current_state += 1
                     # game_over = False somewhere in the dictionary
                elif current_state == 1: # and game_over = True
                    background = the_office
                    # remove rectangles
                    a_let.reshape
                    game_on = False
                    string_bear = 'YAY you have finished the game! You worked so hard, please have a seat on the couch ... Turns out this was secretly an experiment about your decision making all along, sorry for not telling you before. press spacebar to continue'
                    current_state += 1
                elif current_state == 2:
                    if descriptive > normative:
                        string_bear = 'Turns out a majority of the decisions you made adhered to descriptive theories. This means that rather than making the rational choice, you tended to follow decision making fallacies and theories used to describe our weird choice. Congrats you’re as illogical as the rest of us!'
                    elif normative > descriptive:
                        string_bear = 'Turns out a majority of the decisions you made were normative. This means that you tended to make the most rational choices, rather than adhering to descriptive theories used to describe frequent fallacies in our decision making. Idk what to tell you make worse decisions more often i guess.'
                    else:
                        string_bear = 'You made the same number of descriptive and normative choices. This means you made an equal number of rational choices and choices that adhere to descriptive theories used to describe frequent fallacies in our decision making. I guess your complex or whatever ...'
                    current_state += 1
                elif current_state == 3:
                    string_bear = 'Thank you for playing! press space bar to quit.'
                    current_state += 1
                elif current_state == 4:
                    run = False
                pygame.event.clear()

        if game_on:
            if a_position.colliderect(bear_rect):
                option, should_update = 1, True
                normative += 1
            elif b_position.colliderect(bear_rect):
                option, should_update = 2, True
                descriptive += 1
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

