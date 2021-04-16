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

#Hard semester
elif choice1 == 'B':
    normative += 1
    print('It is the first day of classes, and you just shopped three classes in a row. \nDo you take a break for lunch or shop another class?')
    choice2 = input('Type "lunch" or "class" to make your choice:')
    if choice2 == 'lunch':
        print('Lunch it is! You are not on meal plan this year, but you are really hungry and you are craving a pasta bowl from Andrews. \nYou pay $8.75 in cash for your pasta bowl and sit down, all excited to eat it. \nIt looks like you got the last pasta bowl, though, so someone approaches you saying they REALLY wanted a pasta bowl too.\nThey offer to pay you $9.75 for your pasta bowl - $1.00 more than you initially paid. Do you accept their offer?')
        choice3 = input('Type "yes" or "no" to make your choice:')
        if choice3 == 'yes':
            normative += 1
            print('You are feeling richer now, so you decide to treat yourself to a Brown hoodie. You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. \nAt the front of the bookstore is a grand display of the new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you')
            print('A: Buy the $80 hoodie')
            print('B: Buy the $100 hoodie')
            print('C: Leave the store without buying anything')
            choice4 = input('Type "A", "B", or "C" to make your choice:')
            if choice4 == 'A' or choice4 == 'B':
                descriptive += 1
                print('Unfortunately, you are now broke. You head to the SciLi to look for a summer internship on BrownConnect. \nYou run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the SciLi is. They tell you that the last time they were in the stacks, someone there saw a mouse. \nGross. But you are already so close to the SciLi. Do you decide to go to the Sci Li since you are already so close and all stacks are rightfully terrible, or do you go to the Rock instead?')
                choice5 = input('Type "SciLi" or "Rock" to make your choice:')
                if choice5 == 'SciLi':
                    normative += 1
                    print('You go to the Scili are get attacked by the army of mice hiding in the stacks. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
                elif choice5 == 'Rock':
                    descriptive += 1
                    print('Once at the Rock, you open BrownConnect and find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. \nYou find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. \nBoth applications are due tonight, so you only have time to apply to one. Which internship do you choose?')
                    choice6 = input('Type "first internship" or "second internship" to make your choice:')
                    if choice6 == 'first internship':
                        descriptive += 1
                    elif choice6 == 'second internship':
                        normative += 1
                    print('When you finish the application, you head back to your room. As you pass Blueno, he comes alive and wraps you in his arms to be forever held captive. Cute! Before you hang with Blueno forever, though, let us tell you what kind of decision-maker you are:')

            elif choice4 == 'C': #don't buy the hoodie
                normative += 1
                print('Since you saved yourself some money, you decide to treat yourself to dinner on Thayer. You could really go for some delicious fried chicken, but you have promised yourself you would cut back on fried foods. \nYou have been good about it; you have not had any fried food in two weeks. Do you decide to stick to your goal and get a healthy wrap, or do you reward yourself for your progress and go for the fried chicken?')
                choice7 = input('Type "wrap" or "fried chicken" to make your choice:')
                if choice7 == 'wrap':
                    normative += 1
                    print('Unfortunately, the wrap you got was poisoned. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
                elif choice8 == 'fried chicken': #fried chicken
                    descriptive += 1
                    print('Unfortunately, on the way to the fried chicken place, Christmas Crane falls on you and crushes you. So sad! But, on the bright side, we found out what kind of decision-maker you are:')

        else: #keep the pasta bowl
            descriptive += 1
            print('After all that yummy pasta, you fall into a food coma. You really want some coffee, but you made a goal to only buy coffee a maximum of twice a week. \nYou followed your goal perfectly last week, but you already bought coffee twice this week. \nDo you decide to just go an extra time this week, or do you energize yourself with a nap instead?')
            choice8 = input('Type "coffee" or "nap" to make your choice:')
            if choice8 == 'coffee':
                descriptive += 1
            elif choice8 == 'nap':
                normative +=1
            print('Now, you feel more energized, so you decide to hang with some friends. You guys decide to hang out in Emwool. But, your friend gets a text from her roommate saying her roommate is having some friends over. She suggests you all hang out in your room instead Do you decide to:')
            print('A: Change the location to your room')
            print('B: Stick to your friends room; the more people the better!')
            choice9 = input('Type "A" or "B" to make your choice:')
            if choice9 == 'A':
                normative += 1
                print('You have a great time with your friends and a great rest of the semester! \nSome more good news: we found out what kind of decision-maker you are!')
            elif choice9 == 'B':
                descriptive += 1
                print('On the way to Emwool, you cut through the VDub, and you accidentally get cooked into the meatloaf. So sad! But, on the bright side, we found out what kind of decision-maker you are:')

    elif choice2 == 'class': #shop another class
        print('Good choice! You head to your next class. You read the course description and reviews and it seems super interesting. The teacher walks in and hands out the syllabus; it looks manageable. \nProf then emphasizes that her course is very intense and will require long hours of focused work and diligent time management. She further articulates that 65% of students tend to get a final grade below an A. \nDo you decide to take the class S/NC or take it for a grade?')
        choice10 = input('Type "S/NC" or "grade" to make your choice:')
        if choice10 == 'S/NC' or choice10 == 'SNC':
            descriptive += 1
            print('With all the time you saved from taking the class S/NC, you decide to do some shopping. You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. \nAt the front of the bookstore is a grand display of the new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you')
            print('A: Buy the $80 hoodie')
            print('B: Buy the $100 hoodie')
            print('C: Leave the store without buying anything')
            choice11 = input('Type "A", "B", or "C" to make your choice:')
            if choice11 == 'A' or choice11 == 'B':
                descriptive += 1
                print('Unfortunately, you are now broke. You head to the SciLi to look for a summer internship on BrownConnect. \nYou run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the SciLi is. They tell you that the last time they were in the stacks, someone there saw a mouse. \nGross. But you are already so close to the SciLi. Do you decide to go to the Sci Li since you are already so close and all stacks are rightfully terrible, or do you go to the Rock instead?')
                choice12 = input('Type "SciLi" or "Rock" to make your choice:')
                if choice12 == 'SciLi':
                    normative += 1
                    print('You go to the Scili are get attacked by the army of mice hiding in the stacks. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
                elif choice12 == 'Rock':
                    descriptive += 1
                    print('Once at the Rock, you open BrownConnect and find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. \nYou find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. \nBoth applications are due tonight, so you only have time to apply to one. Which internship do you choose?')
                    choice13 = input('Type "first internship" or "second internship" to make your choice:')
                    if choice13 == 'first internship':
                        descriptive += 1
                    elif choice13 == 'second internship':
                        normative += 1
                    print('When you finish the application, you head back to your room. As you pass Blueno, he comes alive and wraps you in his arms to be forever held captive. Cute! Before you hang with Blueno forever, though, let us tell you what kind of decision-maker you are:')

            elif choice11 == 'C': #don't buy the hoodie
                normative += 1
                print('Since you saved yourself some money, you decide to treat yourself to dinner on Thayer. You could really go for some delicious fried chicken, but you have promised yourself you would cut back on fried foods. \nYou have been good about it; you have not had any fried food in two weeks. Do you decide to stick to your goal and get a healthy wrap, or do you reward yourself for your progress and go for the fried chicken?')
                choice14 = input('Type "wrap" or "fried chicken" to make your choice:')
                if choice14 == 'wrap':
                    normative += 1
                    print('Unfortunately, the wrap you got was poisoned. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
                elif choice14 == 'fried chicken': #fried chicken
                    descriptive += 1
                    print('Unfortunately, on the way to the fried chicken place, Christmas Crane falls on you and crushes you. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
        elif choice10 == 'grade': #take the class for a grade
            normative +=1
            print('Weeks later, the S/NC deadline has passed, but you are struggling in the class. You do not enjoy the material, and you realize you probably do not even need to be in this class. You can drop the class with no fee, but you have already invested 75+ hours of work into the class (5 weeks of work), and you spent $65 on the textbook. Do you drop the class or keep the class?')
            choice15 = input('Type "drop" or "keep" to make your choice:')
            if choice15 == 'drop':
                normative += 1
                print('With all the time you saved from dropping the class, you decide to do some shopping. You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. \nAt the front of the bookstore is a grand display of the new line of hoodies. Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you')
                print('A: Buy the $80 hoodie')
                print('B: Buy the $100 hoodie')
                print('C: Leave the store without buying anything')
                choice16 = input('Type "A", "B", or "C" to make your choice:')
                if choice16 == 'A' or choice16 == 'B':
                    descriptive += 1
                    print('Unfortunately, you are now broke. You head to the SciLi to look for a summer internship on BrownConnect. \nYou run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the SciLi is. They tell you that the last time they were in the stacks, someone there saw a mouse. \nGross. But you are already so close to the SciLi. Do you decide to go to the Sci Li since you are already so close and all stacks are rightfully terrible, or do you go to the Rock instead?')
                    choice17 = input('Type "SciLi" or "Rock" to make your choice:')
                    if choice17 == 'SciLi':
                        normative += 1
                        print('You go to the Scili are get attacked by the army of mice hiding in the stacks. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
                    elif choice17 == 'Rock':
                        descriptive += 1
                        print('Once at the Rock, you open BrownConnect and find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. \nYou find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. \nBoth applications are due tonight, so you only have time to apply to one. Which internship do you choose?')
                        choice18 = input('Type "first internship" or "second internship" to make your choice:')
                        if choice18 == 'first internship':
                            descriptive += 1
                        elif choice18 == 'second internship':
                            normative += 1
                        print('When you finish the application, you head back to your room. As you pass Blueno, he comes alive and wraps you in his arms to be forever held captive. Cute! Before you hang with Blueno forever, though, let us tell you what kind of decision-maker you are:')

                elif choice16 == 'C': #don't buy the hoodie
                    normative += 1
                    print('Since you saved yourself some money, you decide to treat yourself to dinner on Thayer. You could really go for some delicious fried chicken, but you have promised yourself you would cut back on fried foods. \nYou have been good about it; you have not had any fried food in two weeks. Do you decide to stick to your goal and get a healthy wrap, or do you reward yourself for your progress and go for the fried chicken?')
                    choice19 = input('Type "wrap" or "fried chicken" to make your choice:')
                    if choice19 == 'wrap':
                        normative += 1
                        print('Unfortunately, the wrap you got was poisoned. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
                    elif choice19 == 'fried chicken': #fried chicken
                        descriptive += 1
                        print('Unfortunately, on the way to the fried chicken place, Christmas Crane falls on you and crushes you. So sad! But, on the bright side, we found out what kind of decision-maker you are:')
            elif choice15 == 'keep': #keep the class
                descriptive += 1
                print('If you are going to make it through this class, you will need coffee. But, you made a goal to only buy coffee a maximum of twice a week. \nYou followed your goal perfectly last week, but you already bought coffee twice this week. \nDo you decide to just go an extra time this week, or do you energize yourself with a nap instead?')
                choice20 = input('Type "coffee" or "nap" to make your choice:')
                if choice20 == 'coffee':
                    descriptive += 1
                    print('Now, you feel more energized, so you decide to hang with some friends. You guys decide to hang out in Emwool. But, your friend gets a text from her roommate saying her roommate is having some friends over. She suggests you all hang out in your room instead Do you decide to:')
                    print('A: Change the location to your room')
                    print('B: Stick to your friends room; the more people the better!')
                    choice21 = input('Type "A" or "B" to make your choice:')
                    if choice21 == 'A':
                        normative += 1
                        print('You have a great time with your friends and a great rest of the semester! Some more good news: we found out what kind of decision-maker you are!')
                    elif choice21 == 'B':
                        descriptive += 1
                        print('On the way to Emwool, you cut through the VDub, and you accidentally get cooked into the meatloaf. So sad! But, on the bright side, we found out what kind of decision-maker you are:')

                elif choice20 == 'nap': #nap
                    normative += 1
                    print('You peacefully fall asleep and have a great rest of the semester! Some more good news: we found out what kind of decision-maker you are!')

#Results
if normative > descriptive:
    print('You are a rational decision-maker, and the majority of your choices align with  normative decision theories')
elif descriptive>normative:
    print('You are a nonrational decision-maker, and the majority of your choices align with descriptive decision theories')

