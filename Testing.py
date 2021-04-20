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
#main_green = pygame.image.load(os.path.join('main_green.jpg'))
#main_green = pygame.transform.scale(main_green, (width, height))
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
inside_Rock = pygame.image.load(os.path.join('inside_Rock.jpg'))
inside_Rock = pygame.transform.scale(inside_Rock, (width, height))
outside_SciLi = pygame.image.load(os.path.join('Outside_sci_li.jpg'))
outside_SciLi = pygame.transform.scale(outside_SciLi, (width, height))
Thayer_street = pygame.image.load(os.path.join('Thayer-Street.jpg'))
Thayer_street = pygame.transform.scale(Thayer_street, (width, height))
VDub  = pygame.image.load(os.path.join('Verney-Woolley.jpg'))
VDub = pygame.transform.scale(VDub, (width, height))
#bear_rect = bear.get_rect()

# font stuff options: 'timesnewroman', 'georgia', 'helvetica'
# 1. create font object
# 2. render text into image with given color
# 3. blit image to screen


def draw_window(bear_rect, a_position, b_position, a_let, b_let, bear, string_bear, string_a, string_b, background):
    win.blit(background, (0,0))
    win.blit(bear, (bear_rect.x, bear_rect.y))
    win.blit(a_let, (a_position.x, a_position.y))
    win.blit(b_let, (b_position.x, b_position.y)
    text_location = [bear_rect.x - 400, bear_rect.y - 100]
    #text_location = [bear_rect.x - 400, bear_rect.y - 100]
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
    string_bear = ''  # no line breaks needed
    string_a = ''  # line breaks needed
    string_b = ''  # line breaks needed
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
            descriptive = 0
            normative = 0
            string_bear = 'Welcome to the game, ill be your guide today! Were going to go on an adventure that you choose. To pick option A blah blah blah'
            # greetings and instructions part
            # wait function to display text or space bar to continue?
            intro = False
        while main_game:
            #win.blit(SciLi_mice, [0,0])
            background = SciLi_mice
            string_bear = 'Alex, your partner of 4 years, the love of your life, just broke up with you right before your flight to Brown for your first semester of university - they said they cannot do long distance. You are pursuing a double major, so it would be wise of you to start the heavy lifting from early. However, you are heartbroken and unsure of your ability to offer your best work. Do you'
            string_a = 'Take mostly easy courses to prevent yourself from having a mental breakdown mid semester'
            string_b = 'Take harder courses - you are a soldier!'
            if bear_rect.colliderect(b_position):
                string_bear = 'It is the first day of classes, and you just shopped three classes in a row. Do you take a break for lunch or shop another class?'
                string_a = 'lunch'
                string_b = 'class'
                if bear_rect.colliderect(a_position):
                    string_bear = 'Lunch it is! You are not on meal plan this year, but you are really hungry and you are craving a pasta bowl from Andrews. \nYou pay $8.75 in cash for your pasta bowl and sit down, all excited to eat it. It looks like you got the last pasta bowl, though, so someone approaches you saying they REALLY wanted a pasta bowl too.They offer to pay you $9.75 for your pasta bowl - $1.00 more than you initially paid. Do you accept their offer?'
                    string_a = 'yes'
                    string_b = 'no'
                    if bear_rect.colliderect(a_position):
                        normative += 1
                        string_bear = 'You are feeling richer now, so you decide to treat yourself to a Brown hoodie. You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. At the front of the bookstore is a grand display of the new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you'
                        string_a = 'Buy the $80 hoodie'
                        string_b = 'Leave the store without buying anything'
                        if bear_rect.colliderect(a_position):
                            descriptive += 1
                            string_bear = 'Unfortunately, you are now broke. You head to the SciLi to look for a summer internship on BrownConnect. You run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the SciLi is. They tell you that the last time they were in the stacks, someone there saw a mouse. Gross. But you are already so close to the SciLi. Do you decide to go to the Sci Li since you are already so close and all stacks are rightfully terrible, or do you go to the Rock instead?'
                            string_a = 'SciLi'
                            string_b = 'Rock'
                            if bear_rect.colliderect(a_position):
                                normative += 1
                                string_bear = 'You go to the Scili are get attacked by the army of mice hiding in the stacks. So sad! But, on the bright side, we found out what kind of decision-maker you are:'
                                #pygame.mixer.Sound.play(horn_fail_sound)
                            elif bear_rect.colliderect(b_position):
                                descriptive += 1
                                string_bear = 'Once at the Rock, you open BrownConnect and find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. You find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. Both applications are due tonight, so you only have time to apply to one. Which internship do you choose?'
                                string_a = 'first internship'
                                string_b = 'second internship'
                                if bear_rect.colliderect(a_position):
                                    descriptive += 1
                                elif bear_rect.colliderec(b_position):
                                    normative += 1
                                string_bear = 'When you finish the application, you head back to your room. As you pass Blueno, he comes alive and wraps you in his arms to be forever held captive. Cute! Before you hang with Blueno forever, though, let us tell you what kind of decision-maker you are:'
                                #pygame.mixer.Sound.play(horn_fail_sound)
                        elif bear_rect.colliderec(b_position):
                            normative += 1
                            string_bear = 'Since you saved yourself some money, you decide to treat yourself to dinner on Thayer. You could really go for some delicious fried chicken, but you have promised yourself you would cut back on fried foods. \nYou have been good about it; you have not had any fried food in two weeks. Do you decide to stick to your goal and get a healthy wrap, or do you reward yourself for your progress and go for the fried chicken?'
                            string_a = 'wrap'
                            string_b = 'fried chicken'
                            if bear_rect.colliderect(a_position):
                                normative += 1
                                string_bear = 'Unfortunately, the wrap you got was poisoned. So sad! But, on the bright side, we found out what kind of decision-maker you are:'
                            elif bear_rect.colliderect(b_position):
                                descriptive += 1
                                string_bear = 'Unfortunately, on the way to the fried chicken place, Christmas Crane falls on you and crushes you. So sad! But, on the bright side, we found out what kind of decision-maker you are:'
                                #pygame.mixer.Sound.play(horn_fail_sound)
                    elif bear_rect.colliderect(b_position):
                        descriptive += 1
                        string_bear = 'After all that yummy pasta, you fall into a food coma. You really want some coffee, but you made a goal to only buy coffee a maximum of twice a week. \nYou followed your goal perfectly last week, but you already bought coffee twice this week. Do you decide to just go an extra time this week, or do you energize yourself with a nap instead?'
                        string_a = 'coffee'
                        string_b = 'nap'
                        if bear_rect.colliderect(a_position):
                            descriptive += 1
                        elif bear_rect.colliderect(b_position):
                            normative += 1
                        string_bear = 'Now, you feel more energized, so you decide to hang with some friends. You guys decide to hang out in Emwool. But, your friend gets a text from her roommate saying her roommate is having some friends over. She suggests you all hang out in your room instead Do you decide to:'
                        string_a = 'Change the location to your room'
                        string_b = 'Stick to your friends room; the more people the better!'
                        if bear_rect.colliderect(a_position):
                            normative += 1
                            string_bear = 'You have a great time with your friends and a great rest of the semester! Some more good news: we found out what kind of decision-maker you are!'
                            #pygame.mixer.Sound.play(yay_sound)
                        elif bear_rect.colliderect(b_position):
                            descriptive += 1
                            string_bear = 'On the way to Emwool, you cut through the VDub, and you accidentally get cooked into the meatloaf. So sad! But, on the bright side, we found out what kind of decision-maker you are:'
                            #pygame.mixer.Sound.play(horn_fail_sound)
                elif bear_rect.colliderect(b_position): #shop another class
                    string_bear = 'Good choice! You head to your next class. You read the course description and reviews and it seems super interesting. The teacher walks in and hands out the syllabus; it looks manageable. Prof then emphasizes that her course is very intense and will require long hours of focused work and diligent time management. She further articulates that 65% of students tend to get a final grade below an A. Do you decide to take the class S/NC or take it for a grade?'
                    string_a = 'S/NC'
                    string_b = 'grade'
                    if bear_rect.colliderect(a_position):
                        descriptive += 1
                        string_bear = 'With all the time you saved from taking the class S/NC, you decide to do some shopping. You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. \nAt the front of the bookstore is a grand display of the new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you'
                        string_a = 'Buy the $80 hoodie'
                        string_b = 'Leave the store without buying anything'
                        if bear_rect.colliderect(a_position):
                            descriptive += 1
                            string_bear = 'Unfortunately, you are now broke. You head to the SciLi to look for a summer internship on BrownConnect. You run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the SciLi is. They tell you that the last time they were in the stacks, someone there saw a mouse. Gross. But you are already so close to the SciLi. Do you decide to go to the Sci Li since you are already so close and all stacks are rightfully terrible, or do you go to the Rock instead?'
                            string_a = 'SciLi'
                            string_b = 'Rock'
                            if bear_rect.colliderect(a_position):
                                normative += 1
                                string_bear = 'You go to the Scili are get attacked by the army of mice hiding in the stacks. So sad! But, on the bright side, we found out what kind of decision-maker you are:'
                                #pygame.mixer.Sound.play(horn_fail_sound)
                            elif bear_rect.colliderect(b_position):
                                descriptive += 1
                                string_bear = 'Once at the Rock, you open BrownConnect and find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. You find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. Both applications are due tonight, so you only have time to apply to one. Which internship do you choose?'
                                string_a = 'first internship'
                                string_b = 'second internship'
                                if bear_rect.colliderect(a_position):
                                    descriptive += 1
                                elif bear_rect.colliderec(b_position):
                                    normative += 1
                                string_bear = 'When you finish the application, you head back to your room. As you pass Blueno, he comes alive and wraps you in his arms to be forever held captive. Cute! Before you hang with Blueno forever, though, let us tell you what kind of decision-maker you are:'
                                #pygame.mixer.Sound.play(horn_fail_sound)
                        elif bear_rect.colliderec(b_position):
                            normative += 1
                            string_bear = 'Since you saved yourself some money, you decide to treat yourself to dinner on Thayer. You could really go for some delicious fried chicken, but you have promised yourself you would cut back on fried foods. \nYou have been good about it; you have not had any fried food in two weeks. Do you decide to stick to your goal and get a healthy wrap, or do you reward yourself for your progress and go for the fried chicken?'
                            string_a = 'wrap'
                            string_b = 'fried chicken'
                            if bear_rect.colliderect(a_position):
                                normative += 1
                                string_bear = 'Unfortunately, the wrap you got was poisoned. So sad! But, on the bright side, we found out what kind of decision-maker you are:'
                            elif bear_rect.colliderect(b_position):
                                descriptive += 1
                                string_bear = 'Unfortunately, on the way to the fried chicken place, Christmas Crane falls on you and crushes you. So sad! But, on the bright side, we found out what kind of decision-maker you are:'
                                #pygame.mixer.Sound.play(horn_fail_sound)
                    if bear_rect.colliderect(b_position): #take the class for a grade
                        normative += 1
                        string_bear = 'Weeks later, the S/NC deadline has passed, but you are struggling in the class. You do not enjoy the material, and you realize you probably do not even need to be in this class. You can drop the class with no fee, but you have already invested 75+ hours of work into the class (5 weeks of work), and you spent $65 on the textbook. Do you drop the class or keep the class?'
                        string_a = 'drop'
                        string_b = 'keep'
                        if bear_rect.colliderect(a_position):
                            normative += 1
                            string_bear = 'With all the time you saved from taking the class S/NC, you decide to do some shopping. You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. \nAt the front of the bookstore is a grand display of the new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you'
                            string_a = 'Buy the $80 hoodie'
                            string_b = 'Leave the store without buying anything'
                            if bear_rect.colliderect(a_position):
                                descriptive += 1
                                string_bear = 'Unfortunately, you are now broke. You head to the SciLi to look for a summer internship on BrownConnect. You run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the SciLi is. They tell you that the last time they were in the stacks, someone there saw a mouse. Gross. But you are already so close to the SciLi. Do you decide to go to the Sci Li since you are already so close and all stacks are rightfully terrible, or do you go to the Rock instead?'
                                string_a = 'SciLi'
                                string_b = 'Rock'
                                if bear_rect.colliderect(a_position):
                                    normative += 1
                                    string_bear = 'You go to the Scili are get attacked by the army of mice hiding in the stacks. So sad! But, on the bright side, we found out what kind of decision-maker you are:'
                                    #pygame.mixer.Sound.play(horn_fail_sound)
                                elif bear_rect.colliderect(b_position):
                                    descriptive += 1
                                    string_bear = 'Once at the Rock, you open BrownConnect and find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. You find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. Both applications are due tonight, so you only have time to apply to one. Which internship do you choose?'
                                    string_a = 'first internship'
                                    string_b = 'second internship'
                                    if bear_rect.colliderect(a_position):
                                        descriptive += 1
                                    elif bear_rect.colliderec(b_position):
                                        normative += 1
                                    string_bear = 'When you finish the application, you head back to your room. As you pass Blueno, he comes alive and wraps you in his arms to be forever held captive. Cute! Before you hang with Blueno forever, though, let us tell you what kind of decision-maker you are:'
                                    #pygame.mixer.Sound.play(horn_fail_sound)
                            elif bear_rect.colliderec(b_position):
                                normative += 1
                                string_bear = 'Since you saved yourself some money, you decide to treat yourself to dinner on Thayer. You could really go for some delicious fried chicken, but you have promised yourself you would cut back on fried foods. \nYou have been good about it; you have not had any fried food in two weeks. Do you decide to stick to your goal and get a healthy wrap, or do you reward yourself for your progress and go for the fried chicken?'
                                string_a = 'wrap'
                                string_b = 'fried chicken'
                                if bear_rect.colliderect(a_position):
                                    normative += 1
                                    string_bear = 'Unfortunately, the wrap you got was poisoned. So sad! But, on the bright side, we found out what kind of decision-maker you are:'
                                elif bear_rect.colliderect(b_position):
                                    descriptive += 1
                                    string_bear = 'Unfortunately, on the way to the fried chicken place, Christmas Crane falls on you and crushes you. So sad! But, on the bright side, we found out what kind of decision-maker you are:'
                                    #pygame.mixer.Sound.play(horn_fail_sound)
                        elif bear_rect.colliderect(b_position): #keep the class
                            descriptive += 1
                            string_bear = 'If you are going to make it through this class, you will need coffee. But, you made a goal to only buy coffee a maximum of twice a week. \nYou followed your goal perfectly last week, but you already bought coffee twice this week. Do you decide to just go an extra time this week, or do you energize yourself with a nap instead?'
                            string_a = 'coffee'
                            string_b = 'nap'
                            if bear_rect.colliderect(a_position):
                                descriptive += 1
                            elif bear_rect.colliderect(b_position):
                                normative += 1
                            string_bear = 'Now, you feel more energized, so you decide to hang with some friends. You guys decide to hang out in Emwool. But, your friend gets a text from her roommate saying her roommate is having some friends over. She suggests you all hang out in your room instead Do you decide to:'
                            string_a = 'Change the location to your room'
                            string_b = 'Stick to your friends room; the more people the better!'
                            if bear_rect.colliderect(a_position):
                                normative += 1
                                string_bear = 'You have a great time with your friends and a great rest of the semester! Some more good news: we found out what kind of decision-maker you are!'
                                #pygame.mixer.Sound.play(yay_sound)
                            elif bear_rect.colliderect(b_position):
                                descriptive += 1
                                string_bear = 'On the way to Emwool, you cut through the VDub, and you accidentally get cooked into the meatloaf. So sad! But, on the bright side, we found out what kind of decision-maker you are:'
                                #pygame.mixer.Sound.play(horn_fail_sound)
            main_game = False


        #while results:
            #DISPLAY RESULTS

        keys_pressed = pygame.key.get_pressed()
        bear_movement(keys_pressed, bear_rect)
        draw_window(bear_rect, a_position, b_position, a_let, b_let, bear, string_bear, string_a, string_b, background)
        pygame.display.flip()
    main()


if __name__ == "__main__":
    main()

