#Initialize variables
descriptive = 0
normative = 0

print('Hi! Welcome to "Decisions, Decisions, Decisions," a choose-your-own-adventure game that will take you through the semester of a Brown student.')
user_name = input('What is your name?')
print('Nice to meet you', user_name)

#Choice 1: Immune Neglect
print('Alex, your partner of 4 years, the love of your life, just broke up with you right before your flight to Brown for your first semester of university - they said they cannot do long distance.')
print('You are pursuing a double major, so it would be wise of you to start the heavy lifting from early. However, you are heartbroken and unsure of your ability to offer your best work. Do you')
print('A: Take mostly easy courses to prevent yourself from having a mental breakdown mid semester')
print('B: Take harder courses - you are a soldier!')

choice1 = input('Type "A" or "B" to make your choice:')

#Easy semester
if choice1 == 'A':
    descriptive += 1
    print(
        'You are looking for something to distract you from your breakup pain. What shall it be, retail therapy or eating your sorrows away?')
    choice2A = input('Type "retail" or "food" to make your choice:')
    if choice2A == 'retail':
        #neither descriptive nor normative
        print('Honorable choice. You venture into the Brown bookstore with a flexible budget of $60 looking for some merch. \nAt the front of the bookstore is a grand display of Browns new line of hoodies. Each hoodie costs $100. \nYou search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you')
        print('A: Buy the $80 hoodie')
        print('B: Buy the $100 hoodie')
        print('C: Leave the store without buying anything')
        choice3A = input('Type "A", "B", or "C" to make your choice:')
        if choice3A == 'A' or choice3A == 'B':
            descriptive += 1
            print('Now that you have made your purchase, are you going to flex with your new hoodie on the main green or choose modesty and take a cozy nap in your toasty new fit?')
            choice4A = input('Type "flex" or "nap" to make your choice:')
            if choice4A == 'flex':
                #neither normative nor descriptive
                print('You are starting to feel insecure about how good you look. Are you all beauty and no brains?? You decide to head to the Scili to validate your smartness. \nWhile walking over you run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the SciLi is. They tell you that the last time they were in the stacks, someone there saw a mouse.\nGross. But you are already so close to the SciLi. Do you decide to go to the Sci Li since you are already so close and all stacks are rightfully terrible, or do you go to the Rock instead?')
                choice5A = input('Type "SciLi" or "Rock" to make your choice:')
                if choice5A == 'SciLi':
                    normative += 1
                    print('The mice of SciLi have made you their king/queen! You decide you no longer have use for education. More good news: we found out what kind of decision-maker you are!')
                elif choice5A == 'Rock':
                    descriptive += 1
                    print('After a bit of studying at the Rock you decide you deserve to hang out with some friends. You and your friends decide to hang out in Emwool. \nBut, your friend gets a text from her roommate saying her roommate is having some friends over. She suggests you all hang out in your room instead Do you decide to:')
                    print('A: Change the location to your room')
                    print('B: Stick to your friends room; the more people the better!')
                    choice6A = input('Type "A" or "B" to make your choice:')
                    if choice6A== 'A':
                        normative += 1
                        print('You and your friends laugh yourselves into a semester long coma - literally. But, on the bright side, we found out what kind of decision-maker you are!')
                    elif choice6A == 'B':
                        descriptive += 1
                        print('On the way to Emwool you trip over someone’s illegal pet snake and it eats you. But, on the bright side, we found out what kind of decision-maker you are!')
            elif choice4A == 'nap':  # take nap instead of flex
                print('You just had the snuggliest nap of your life. Now you have the post nap munchies. You are not on meal plan this year, but you are craving a pasta bowl from Andrews. \nYou pay $8.75 in cash for your pasta bowl and sit down, all excited to eat it. \nIt looks like you got the last pasta bowl, though, so someone approaches you saying they REALLY wanted a pasta bowl too.\nThey offer to pay you $9.75 for your pasta bowl - $1.00 more than you initially paid. Do you accept their offer?')
                choice7A = input('Type "yes" or "no" to make your choice:')
                if choice7A == 'yes':
                    normative += 1
                    print('A blizzard hits PVD and you have no pasta so you starve to death in your dorm. But, on the bright side, we found out what kind of decision-maker you are!')
                elif choice7A == 'no':
                    descriptive += 1
                    print('You have a severe lactose intolerance reaction to the pasta and explode from the gas build up within you. But, on the bright side, we found out what kind of decision-maker you are!')
        elif choice3A == 'C':  # don't buy hoodie
            normative += 1
            print('You’re making responsible decisions today! You decide to keep this up and head to your next class. \nYou read the course description and reviews and it seemed super interesting. The teacher walks in and hands out the syllabus – it looks manageable. \nProf then emphasizes that her course is very intense and will require long hours of focused work and diligent time management. She further articulates that 65% of students tend to get a final grade below an A. \nDo you decide to take the class S/NC or take it for a grade?')
            choice8A = input('Type "S/NC" or "grade" to make your choice:')
            if choice8A == 'S/NC' or choice8A == 'SNC':
                descriptive += 1
                print('You are feeling liberated and think you deserve to feed your coffee addiction, however you made a goal to only buy coffee a maximum of twice a week. \nYou followed your goal perfectly last week, but you already bought coffee twice this week. \nDo you decide to just go an extra time this week?')
                choice9A = input('Type "yes" or "no" to make your choice:')
                if choice9A == 'yes':
                    descriptive += 1
                    print('You have a caffeine overload and pass out in Starbucks. Brown ships you back to your home state/country because they do not condone drug addiction on campus! But, on the bright side, we found out what kind of decision-maker you are!')
                elif choice9A == 'no':
                    normative +=1
                    print('You drop out of school and become an ambassador for self control and overcoming drug addiction. Your success is overwhelming. Plus, more good news: we found out what kind of decision-maker you are!')
            elif choice8A == 'grade': #take class for grade
                normative +=1
                print('You are proud of your courage and decide to treat yourself with an adventure. Are you going to the roller rink or the movie theatre?')
                choice10A = input('Type "roller rink" or "movies" to make your choice')
                if choice10A == 'roller rink':
                    #neither normative nor descriptive
                    print('You fall and somebody skates over your face, mangling it horribly, so you drop out of school and join the circus. But, on the bright side, we found out what kind of decision-maker you are!')
                elif choice10A == 'movies':
                    print('The movie inspires you and helps you discover your true purpose in life - you dropout of school to become a country music star. Plus, we found out what kind of decision-maker you are')
    elif choice2A == 'food': #food instead of retail therapy
        #neither normative nor descriptive
        print('Good choice! You are not on meal plan this year, but you are craving a pasta bowl from Andrews. \nYou pay $8.75 in cash for your pasta bowl and sit down, all excited to eat it. \nIt looks like you got the last pasta bowl, though, so someone approaches you saying they REALLY wanted a pasta bowl too.\nThey offer to pay you $9.75 for your pasta bowl - $1.00 more than you initially paid. Do you accept their offer?')
        choice11A = input('Type "yes" or "no" to make your choice:')
        if choice11A == 'yes':
            normative += 1
            print('With money on the mind you decide to look for internships at the Rock. You open BrownConnect and find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. \nYou find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. \nBoth applications are due tonight, so you only have time to apply to one. Which internship do you choose?')
            choice12A = input('Type "first internship" or "second internship" to make your choice:')
            if choice12A == 'first internship':
                descriptive += 1
                print('You’re about to be swimming in green so you need some new drip - preferably some threads that rep your school! \nYou venture into the Brown bookstore with a flexible budget of $60, looking for some merch. At the front of the bookstore is a grand display of Browns new line of hoodies. \nEach hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you…')
                print('A: Buy the $80 hoodie')
                print('B: Buy the $100 hoodie')
                print('C: Leave the store without buying anything')
                choice13A = input('Type "A", "B", or "C" to make your choice:')
                if choice13A == 'A' or choice13A == 'B':
                    descriptive += 1
                    print('The shuttle runs you over as you leave the bookstore! You can’t afford the surgery you need because \nyou maxed your card in the bookstore and Health services can’t afford to pay fot it because of COVID cutbacks :( But, on the bright side, we found out what kind of decision-maker you are!')
                elif choice13A == 'C':
                    normative +=1
                    print('You lose a nipple to frostbite but you go see Beyonce in concert with the money you saved at the Bookstore! Plus, more good news: we found out what kind of decision-maker you are!')
            elif choice12A == 'second internship': #second internship
                normative +=1
                print('Applying for internships is tiring. Coffee break? You made a goal to only buy coffee a maximum of twice a week. \nYou followed your goal perfectly last week, but you already bought coffee twice this week. \nDo you decide to just go an extra time this week?')
                choice14A = input('Type "yes" or "no" to make your choice')
                if choice14A == 'yes':
                    descriptive +=1
                    print('Feeling energized you start the semester off strong! You are sure to make dean’s list.')
                elif choice14A == 'no':
                    normative +=1
                    print('Low on energy, you fall asleep in class and your professor despises you forever. They destroy your academic reputation and you end up dropping out. But, on the bright side, we found out what kind of decision-maker you are!')
        elif choice11A == 'no': #keep pasta
            descriptive +=1
            print('Yum! Your tummy is full and and you are ready for your next class. You have been struggling in this one but the S/NC deadline has passed. \nYou do not enjoy the material, and you realize you probably do not even need to be in this class. \nYou can drop the class with no fee, but you have already invested 75+ hours of work into the class (5 weeks of work), and you spent $65 on the textbook. Do you drop the class or keep the class?')
            choice15A = input('Type "drop" or "keep" to make your choice:')
            if choice15A == 'drop':
                normative += 1
                print('You’re feeling a little academically insecure so you decide to go to the library and beat the books. \nYou’re on your way to a late night grind in the stacks at the SciLi. You run into your friend outside of Caswell and talk for a bit. \nYou both end up complaining about how dusty and depressing some of the scili is. They tell you that the last time they were in the stacks, someone there saw a mouse. \nGross. \nBut you’re already so close to the SciLi. Do you decide to go to the Sci Li since you’re already so close and all stacks are rightfully terrible, or do you go to the Rock instead?')
                choice16A = input('Type "SciLi" or "Rock" to make your choice')
                if choice16A == 'SciLi':
                    normative += 1
                    print('You make friends with the mice and get a week`s worth of work done! You decide to celebrate. Will it be froyo or a well deserved nap?')
                    choice17A = input('Type "froyo" or "nap" to make your choice')
                    if choice17A== 'froyo':
                        #neither normative nor descriptive
                        print('BRAIN FREEZE!! You contract a rare condition called super serious brain freeze and are no longer able to pursue higher level education. But, on the bright side, we found out what kind of decision-maker you are!')
                    elif choice17A == 'nap':
                        print('You wake up with an idea for a startup company and become a millionaire by senior year. Plus, more good news: we found out what kind of decision-maker you are!')
                elif choice16A == 'Rock':
                    descriptive +=1
                    print('You see your friends at the Rock and decide to hang out later. You guys decide to hang out in Emwool. \nBut, your friend gets a text from her roommate saying her roommate is having some friends over. \nShe suggests you all hang out in your room instead Do you decide to:')
                    print('A: Change the location to your room')
                    print('B: Stick to your friends room; the more people the better!')
                    choice18A = input('Type "A" or "B" to make your choice:')
                    if choice18A == 'A':
                        normative += 1
                        print('You and your friends bond in a special way and become life long companions forever :D Plus, more good news: we found out what kind of decision-maker you are!')
                    elif choice18A == 'B':
                        descriptive +=1
                        print('One of your ditsy friends gets lost on the way and you are convicted of their murder. You spend the rest of your life in PVD jail. But, on the bright side, we found out what kind of decision-maker you are!')
            elif choice15A == 'keep': #keep class
                descriptive +=1
                print('Classes are back to back today. You read the course description and reviews and it seemed super interesting. \nThe teacher walks in and hands out the syllabus – it looks manageable. \nProf then emphasizes that her course is very intense and will require long hours of focused work and diligent time management. She further articulates that 65% of students tend to get a final grade below an A. \nDo you decide to take the class S/NC or take it for a grade?')
                choice19A = input('Type "S/NC" or "grade" to make your choice:')
                if choice19A == 'S/NC' or choice19A == 'SNC':
                    descriptive += 1
                    print('You have a peaceful and restful semester!')
                elif choice19A == 'grade':
                    normative +=1
                    print('You feel energized by your courage and decide to search for internships. You head over the Rock and hop onto BrownConnect.\nYou find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. \nYou find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. \nBoth applications are due tonight, so you only have time to apply to one. Which internship do you choose?')
                    choice20A = input('Type "first internship" or "second internship" to make your choice:')
                    if choice20A == 'first internship':
                        descriptive += 1
                        print('You brag to your friends about how you are a shoe-in for the internship you applied to and they become spiteful and never speak to you again. You are lonely forever. But, on the bright side, we found out what kind of decision-maker you are!')
                    elif choice20A == 'second internship':
                        normative +=1
                        print('A few weeks later you are notified that you got the internship! All of your career dreams come true. Plus, more good news: we found out what kind of decision-maker you are!')


#Hard semester
elif choice1B == 'B':
    normative += 1
    print('It is the first day of classes, and you just shopped three classes in a row. \nDo you take a break for lunch or shop another class?')
    choice2B = input('Type "lunch" or "class" to make your choice:')
    if choice2B == 'lunch':
        print('Lunch it is! You are not on meal plan this year, but you are really hungry and you are craving a pasta bowl from Andrews. \nYou pay $8.75 in cash for your pasta bowl and sit down, all excited to eat it. \nIt looks like you got the last pasta bowl, though, so someone approaches you saying they REALLY wanted a pasta bowl too.\nThey offer to pay you $9.75 for your pasta bowl - $1.00 more than you initially paid. Do you accept their offer?')
        choice3B = input('Type "yes" or "no" to make your choice:')
        if choice3B == 'yes':
            normative += 1
            print('You are feeling richer now, so you decide to treat yourself to a Brown hoodie. You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. \nAt the front of the bookstore is a grand display of the new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you')
            print('A: Buy the $80 hoodie')
            print('B: Buy the $100 hoodie')
            print('C: Leave the store without buying anything')
            choice4B = input('Type "A", "B", or "C" to make your choice:')
            if choice4B == 'A' or choice4B == 'B':
                descriptive += 1
                print('Unfortunately, you are now broke. You head to the SciLi to look for a summer internship on BrownConnect. \nYou run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the SciLi is. They tell you that the last time they were in the stacks, someone there saw a mouse. \nGross. But you are already so close to the SciLi. Do you decide to go to the Sci Li since you are already so close and all stacks are rightfully terrible, or do you go to the Rock instead?')
                choice5B = input('Type "SciLi" or "Rock" to make your choice:')
                if choice5B == 'SciLi':
                    normative += 1
                    print('You go to the Scili are get attacked by the army of mice hiding in the stacks. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
                elif choice5B == 'Rock':
                    descriptive += 1
                    print('Once at the Rock, you open BrownConnect and find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. \nYou find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. \nBoth applications are due tonight, so you only have time to apply to one. Which internship do you choose?')
                    choice6B = input('Type "first internship" or "second internship" to make your choice:')
                    if choice6B == 'first internship':
                        descriptive += 1
                    elif choice6B == 'second internship':
                        normative += 1
                    print('When you finish the application, you head back to your room. As you pass Blueno, he comes alive and wraps you in his arms to be forever held captive. Cute! Before you hang with Blueno forever, though, let us tell you what kind of decision-maker you are:')

            elif choice4B == 'C': #don't buy the hoodie
                normative += 1
                print('Since you saved yourself some money, you decide to treat yourself to dinner on Thayer. You could really go for some delicious fried chicken, but you have promised yourself you would cut back on fried foods. \nYou have been good about it; you have not had any fried food in two weeks. Do you decide to stick to your goal and get a healthy wrap, or do you reward yourself for your progress and go for the fried chicken?')
                choice7B = input('Type "wrap" or "fried chicken" to make your choice:')
                if choice7B == 'wrap':
                    normative += 1
                    print('Unfortunately, the wrap you got was poisoned. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
                elif choice7B == 'fried chicken': #fried chicken
                    descriptive += 1
                    print('Unfortunately, on the way to the fried chicken place, Christmas Crane falls on you and crushes you. So sad! But, on the bright side, we found out what kind of decision-maker you are:')

        else: #keep the pasta bowl
            descriptive += 1
            print('After all that yummy pasta, you fall into a food coma. You really want some coffee, but you made a goal to only buy coffee a maximum of twice a week. \nYou followed your goal perfectly last week, but you already bought coffee twice this week. \nDo you decide to just go an extra time this week, or do you energize yourself with a nap instead?')
            choice8B = input('Type "coffee" or "nap" to make your choice:')
            if choice8B == 'coffee':
                descriptive += 1
            elif choice8B == 'nap':
                normative +=1
            print('Now, you feel more energized, so you decide to hang with some friends. You guys decide to hang out in Emwool. But, your friend gets a text from her roommate saying her roommate is having some friends over. She suggests you all hang out in your room instead Do you decide to:')
            print('A: Change the location to your room')
            print('B: Stick to your friends room; the more people the better!')
            choice9B = input('Type "A" or "B" to make your choice:')
            if choice9B == 'A':
                normative += 1
                print('You have a great time with your friends and a great rest of the semester! \nSome more good news: we found out what kind of decision-maker you are!')
            elif choice9B == 'B':
                descriptive += 1
                print('On the way to Emwool, you cut through the VDub, and you accidentally get cooked into the meatloaf. So sad! But, on the bright side, we found out what kind of decision-maker you are:')

    elif choice2B == 'class': #shop another class
        print('Good choice! You head to your next class. You read the course description and reviews and it seems super interesting. The teacher walks in and hands out the syllabus; it looks manageable. \nProf then emphasizes that her course is very intense and will require long hours of focused work and diligent time management. She further articulates that 65% of students tend to get a final grade below an A. \nDo you decide to take the class S/NC or take it for a grade?')
        choice10B = input('Type "S/NC" or "grade" to make your choice:')
        if choice10B == 'S/NC' or choice10B == 'SNC':
            descriptive += 1
            print('With all the time you saved from taking the class S/NC, you decide to do some shopping. You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. \nAt the front of the bookstore is a grand display of the new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you')
            print('A: Buy the $80 hoodie')
            print('B: Buy the $100 hoodie')
            print('C: Leave the store without buying anything')
            choice11B = input('Type "A", "B", or "C" to make your choice:')
            if choice11B == 'A' or choice11B == 'B':
                descriptive += 1
                print('Unfortunately, you are now broke. You head to the SciLi to look for a summer internship on BrownConnect. \nYou run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the SciLi is. They tell you that the last time they were in the stacks, someone there saw a mouse. \nGross. But you are already so close to the SciLi. Do you decide to go to the Sci Li since you are already so close and all stacks are rightfully terrible, or do you go to the Rock instead?')
                choice12B = input('Type "SciLi" or "Rock" to make your choice:')
                if choice12B == 'SciLi':
                    normative += 1
                    print('You go to the Scili are get attacked by the army of mice hiding in the stacks. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
                elif choice12B == 'Rock':
                    descriptive += 1
                    print('Once at the Rock, you open BrownConnect and find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. \nYou find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. \nBoth applications are due tonight, so you only have time to apply to one. Which internship do you choose?')
                    choice13B = input('Type "first internship" or "second internship" to make your choice:')
                    if choice13B == 'first internship':
                        descriptive += 1
                    elif choice13 == 'second internship':
                        normative += 1
                    print('When you finish the application, you head back to your room. As you pass Blueno, he comes alive and wraps you in his arms to be forever held captive. Cute! Before you hang with Blueno forever, though, let us tell you what kind of decision-maker you are:')

            elif choice11B == 'C': #don't buy the hoodie
                normative += 1
                print('Since you saved yourself some money, you decide to treat yourself to dinner on Thayer. You could really go for some delicious fried chicken, but you have promised yourself you would cut back on fried foods. \nYou have been good about it; you have not had any fried food in two weeks. Do you decide to stick to your goal and get a healthy wrap, or do you reward yourself for your progress and go for the fried chicken?')
                choice14B = input('Type "wrap" or "fried chicken" to make your choice:')
                if choice14B == 'wrap':
                    normative += 1
                    print('Unfortunately, the wrap you got was poisoned. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
                elif choice14B == 'fried chicken': #fried chicken
                    descriptive += 1
                    print('Unfortunately, on the way to the fried chicken place, Christmas Crane falls on you and crushes you. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
        elif choice10B == 'grade': #take the class for a grade
            normative +=1
            print('Weeks later, the S/NC deadline has passed, but you are struggling in the class. You do not enjoy the material, and you realize you probably do not even need to be in this class. You can drop the class with no fee, but you have already invested 75+ hours of work into the class (5 weeks of work), and you spent $65 on the textbook. Do you drop the class or keep the class?')
            choice15B = input('Type "drop" or "keep" to make your choice:')
            if choice15B == 'drop':
                normative += 1
                print('With all the time you saved from dropping the class, you decide to do some shopping. You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. \nAt the front of the bookstore is a grand display of the new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you')
                print('A: Buy the $80 hoodie')
                print('B: Buy the $100 hoodie')
                print('C: Leave the store without buying anything')
                choice16B = input('Type "A", "B", or "C" to make your choice:')
                if choice16B == 'A' or choice16B == 'B':
                    descriptive += 1
                    print('Unfortunately, you are now broke. You head to the SciLi to look for a summer internship on BrownConnect. \nYou run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the SciLi is. They tell you that the last time they were in the stacks, someone there saw a mouse. \nGross. But you are already so close to the SciLi. Do you decide to go to the Sci Li since you are already so close and all stacks are rightfully terrible, or do you go to the Rock instead?')
                    choice17B = input('Type "SciLi" or "Rock" to make your choice:')
                    if choice17B == 'SciLi':
                        normative += 1
                        print('You go to the Scili are get attacked by the army of mice hiding in the stacks. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
                    elif choice17B == 'Rock':
                        descriptive += 1
                        print('Once at the Rock, you open BrownConnect and find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. \nYou find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. \nBoth applications are due tonight, so you only have time to apply to one. Which internship do you choose?')
                        choice18B = input('Type "first internship" or "second internship" to make your choice:')
                        if choice18B == 'first internship':
                            descriptive += 1
                        elif choice18B == 'second internship':
                            normative += 1
                        print('When you finish the application, you head back to your room. As you pass Blueno, he comes alive and wraps you in his arms to be forever held captive. Cute! Before you hang with Blueno forever, though, let us tell you what kind of decision-maker you are:')

                elif choice16B == 'C': #don't buy the hoodie
                    normative += 1
                    print('Since you saved yourself some money, you decide to treat yourself to dinner on Thayer. You could really go for some delicious fried chicken, but you have promised yourself you would cut back on fried foods. \nYou have been good about it; you have not had any fried food in two weeks. Do you decide to stick to your goal and get a healthy wrap, or do you reward yourself for your progress and go for the fried chicken?')
                    choice19B = input('Type "wrap" or "fried chicken" to make your choice:')
                    if choice19B == 'wrap':
                        normative += 1
                        print('Unfortunately, the wrap you got was poisoned. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
                    elif choice19B == 'fried chicken': #fried chicken
                        descriptive += 1
                        print('Unfortunately, on the way to the fried chicken place, Christmas Crane falls on you and crushes you. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
            elif choice15B == 'keep': #keep the class
                descriptive += 1
                print('If you are going to make it through this class, you will need coffee. But, you made a goal to only buy coffee a maximum of twice a week. \nYou followed your goal perfectly last week, but you already bought coffee twice this week. \nDo you decide to just go an extra time this week, or do you energize yourself with a nap instead?')
                choice20B = input('Type "coffee" or "nap" to make your choice:')
                if choice20B == 'coffee':
                    descriptive += 1
                    print('Now, you feel more energized, so you decide to hang with some friends. You guys decide to hang out in Emwool. But, your friend gets a text from her roommate saying her roommate is having some friends over. She suggests you all hang out in your room instead Do you decide to:')
                    print('A: Change the location to your room')
                    print('B: Stick to your friends room; the more people the better!')
                    choice21B = input('Type "A" or "B" to make your choice:')
                    if choice21B == 'A':
                        normative += 1
                        print('You have a great time with your friends and a great rest of the semester! Some more good news: we found out what kind of decision-maker you are!')
                    elif choice21B == 'B':
                        descriptive += 1
                        print('On the way to Emwool, you cut through the VDub, and you accidentally get cooked into the meatloaf. So sad! But, on the bright side, we found out what kind of decision-maker you are:')

                elif choice20B == 'nap': #nap
                    normative += 1
                    print('You peacefully fall asleep and have a great rest of the semester! Some more good news: we found out what kind of decision-maker you are!')

#Results
if normative > descriptive:
    print('You are a rational decision-maker, and the majority of your choices align with  normative decision theories')
elif descriptive>normative:
    print('You are a nonrational decision-maker, and the majority of your choices align with descriptive decision theories')
else:
    print('You made an equal number of rational and nonrational decisions.')

