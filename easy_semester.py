#Easy semester
if choice1 == 'A':
    descriptive += 1
    print('You are looking for something to distract you from your breakup pain. What shall it be, retail therapy or eating your sorrows away?')
    choice2 = input('Type "retail" or "food" to make your choice:')
    if choice2 == 'retail':
        #neither descriptive nor normative
        print('Honorable choice. You venture into the Brown bookstore with a flexible budget of $60 looking for some merch. \nAt the front of the bookstore is a grand display of Browns new line of hoodies. Each hoodie costs $100. \nYou search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you…')
        print('A: Buy the $80 hoodie')
        print('B: Buy the $100 hoodie')
        print('C: Leave the store without buying anything')
        choice3 = input('Type "A", "B", or "C" to make your choice:')
        if choice3 == 'A' or choice3 == 'B':
            descriptive += 1
	        print('Now that you’ve made your purchase, are you going to flex with your new hoodie on the main green or choose modesty and take a cozy nap in your toasty new fit?’)
	        choice4 = input('Type "flex" or "nap" to make your choice:')
	        if choice4 == 'flex'
                #neither normative nor descriptive
	            print('You are starting to feel insecure about how good you look. Are you all beauty and no brains?? You decide to head to the Scili to validate your smartness. \nWhile walking over you run into your friend outside of Caswell and talk for a bit. You both end up complaining about how dusty and depressing some of the scili is. They tell you that the last time they were in the stacks, someone there saw a mouse.\nGross. But you’re already so close to the SciLi. Do you decide to go to the Sci Li since you’re already so close and all stacks are rightfully terrible, or do you go to the Rock instead?’)
	            choice5 = input('Type "SciLi" or "Rock" to make your choice:')
                if choice5 == 'SciLi':
                    normative += 1
	                print('The mice of SciLi have made you their king/queen! You decide you no longer have use for education')
	            else:
                    descriptive += 1
                    print('After a bit of studying at the Rock you decide you deserve to hang out with some friends. You and your friends decide to hang out in Emwool. \nBut, your friend gets a text from her roommate saying her roommate is having some friends over. She suggests you all hang out in your room instead Do you decide to:')
                    print('A: Change the location to your room')
                    print('B: Stick to your friends room; the more people the better!')
                    choice6 = input('Type "A" or "B" to make your choice:')
                    if choice6== 'A':
                        normative += 1
                        print('You and your friends laugh yourselves into a semester long coma - literally')
                    else:
                        descriptive += 1
                        print('On the way to Emwool you trip over someone’s illegal pet snake and it eats you.')
            else: #take nap instead of flex
                print('You just had the snuggliest nap of your life. Now you have the post nap munchies. You are not on meal plan this year, but you are craving a pasta bowl from Andrews. \nYou pay $8.75 in cash for your pasta bowl and sit down, all excited to eat it. \nIt looks like you got the last pasta bowl, though, so someone approaches you saying they REALLY wanted a pasta bowl too.\nThey offer to pay you $9.75 for your pasta bowl - $1.00 more than you initially paid. Do you accept their offer?')
                choice7 = input('Type "yes" or "no" to make your choice:')
                if choice7 == 'yes':
                    normative += 1
                    print('A blizzard hits PVD and you have no pasta so you starve to death in your dorm')
                else:
                    descriptive +=1
                    print('You have a severe lactose intolerance reaction to the pasta and explode from the gas build up within you')
        else: #don't buy hoodie
            normative +=1
            print('You’re making responsible decisions today! You decide to keep this up and head to your next class. \nYou read the course description and reviews and it seemed super interesting. The teacher walks in and hands out the syllabus – it looks manageable. \nProf then emphasizes that her course is very intense and will require long hours of focused work and diligent time management. She further articulates that 65% of students tend to get a final grade below an A. \nDo you decide to take the class S/NC or take it for a grade?')
            choice8 = input('Type "S/NC" or "grade" to make your choice:')
            if choice8 == 'S/NC' or choice8 == 'SNC':
                descriptive += 1
                print('You are feeling liberated and think you deserve to feed your coffee addiction, however you made a goal to only buy coffee a maximum of twice a week. \nYou followed your goal perfectly last week, but you already bought coffee twice this week. \nDo you decide to just go an extra time this week?')
                choice9 = input('Type "yes" or "no" to make your choice:')
                if choice9 == 'yes':
                    descriptive += 1
                    print('You have a caffeine overload and pass out in Starbucks. Brown ships you back to your home state/country because they don’t condone drug addiction on campus!)
                else:
                    normative +=1
                    print('You drop out of school and become an ambassador for self control and overcoming drug addiction. Your success is overwhelming.')
            else: #take class for grade
                normative +=1
                print('You are proud of your courage and decide to treat yourself with an adventure. Are you going to the roller rink or the movie theatre?')
                choice10 = input('Type "roller rink" or "movies" to make your choice')
                if choice10 = 'roller rink':
                    #neither normative nor descriptive
                    print('You fall and somebody skates over your face, mangling it horribly, so you drop out of school and join the circus.')
                else:
                    print('The movie inspires you and helps you discover your true purpose in life - you dropout of school to become a country music star')
    else: #food instead of retail therapy
        #neither normative nor descriptive
        print('Good choice! You are not on meal plan this year, but you are craving a pasta bowl from Andrews. \nYou pay $8.75 in cash for your pasta bowl and sit down, all excited to eat it. \nIt looks like you got the last pasta bowl, though, so someone approaches you saying they REALLY wanted a pasta bowl too.\nThey offer to pay you $9.75 for your pasta bowl - $1.00 more than you initially paid. Do you accept their offer?')
        choice11 = input('Type "yes" or "no" to make your choice:')
        if choice11 == 'yes':
            normative += 1
            print('With money on the mind you decide to look for internships at the Rock. You open BrownConnect and find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. \nYou find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. \nBoth applications are due tonight, so you only have time to apply to one. Which internship do you choose?')
            choice12 = input('Type "first internship" or "second internship" to make your choice:')
            if choice12 == 'first internship':
                descriptive += 1
                print('You’re about to be swimming in green so you need some new drip - preferably some threads that rep your school! \nYou venture into the Brown bookstore with a flexible budget of $60, looking for some merch. At the front of the bookstore is a grand display of Browns new line of hoodies. \nEach hoodie costs $100. You search in the back of the store for other hoodie options and find a cute hoodie from last year for $80. Do you…')
                print('A: Buy the $80 hoodie')
                print('B: Buy the $100 hoodie')
                print('C: Leave the store without buying anything')
                choice13 = input('Type "A", "B", or "C" to make your choice:')
                if choice13 == 'A' or choice3 == 'B':
                    descriptive += 1
                    print('The shuttle runs you over as you leave the bookstore! You can’t afford the surgery you need because \nyou maxed your card in the bookstore and Health services can’t afford to pay fot it because of COVID cutbacks :(')
                else:
                    normative +=1
                    print('You lose a nipple to frostbite but you go see Beyonce in concert with the money you saved at the Bookstore!')
            else: #second internship
                normative +=1
                print('Applying for internships is tiring. Coffee break? You made a goal to only buy coffee a maximum of twice a week. \nYou followed your goal perfectly last week, but you already bought coffee twice this week. \nDo you decide to just go an extra time this week?')
                if choice14 == 'yes':
                    descriptive +=1
                    print('Feeling energized you start the semester off strong! You are sure to make dean’s list.')
                else:
                    normative +=1
                    print('Low on energy, you fall asleep in class and your professor despises you forever. They destroy your academic reputation and you end up dropping out and becoming homeless')
        else: #keep pasta
            descriptive +=1
            print('Yum! Your tummy is full and and you are ready for your next class. You have been struggling in this one but the S/NC deadline has passed. \nYou do not enjoy the material, and you realize you probably do not even need to be in this class. \nYou can drop the class with no fee, but you have already invested 75+ hours of work into the class (5 weeks of work), and you spent $65 on the textbook. Do you drop the class or keep the class?')
            choice15 = input('Type "drop" or "keep" to make your choice:')
            if choice15 == 'drop':
                normative += 1
                print('You’re feeling a little academically insecure so you decide to go to the library and beat the books. \nYou’re on your way to a late night grind in the stacks at the SciLi. You run into your friend outside of Caswell and talk for a bit. \nYou both end up complaining about how dusty and depressing some of the scili is. They tell you that the last time they were in the stacks, someone there saw a mouse. \nGross. \nBut you’re already so close to the SciLi. Do you decide to go to the Sci Li since you’re already so close and all stacks are rightfully terrible, or do you go to the Rock instead?')
                choice16 = input('Type "SciLi" or "Rock" to make your choice)
                if choice16 == 'SciLi':
                    normative += 1
                    print('You make friends with the mice and get a week`s worth of work done! You decide to celebrate. Will it be froyo or a well deserved nap?')
                    choice17 = input('Type "froyo" or "nap" to make your choice')
                    if choice17== 'froyo':
                        #neither normative nor descriptive
                        print('BRAIN FREEZE!! You contract a rare condition called super serious brain freeze and are no longer able to pursue higher level education.')
                    else:
                        print('You wake up with an idea for a startup company and become a millionaire by senior year.')
                else:
                    descriptive +=1
                    print('You see your friends at the Rock and decide to hang out later. You guys decide to hang out in Emwool. \nBut, your friend gets a text from her roommate saying her roommate is having some friends over. \nShe suggests you all hang out in your room instead Do you decide to:')
                    print('A: Change the location to your room')
                    print('B: Stick to your friends room; the more people the better!')
                    choice18 = input('Type "A" or "B" to make your choice:')
                    if choice18 == 'A':
                        normative += 1
                        print('You and your friends bond in a special way and become life long companions forever :D')
                    else:
                        descriptive +=1
                        print('One of your ditsy friends gets lost on the way and you are convicted of their murder. You spend the rest of your life in PVD jail')
            else: #keep class
                descriptive +=1
                print('Classes are back to back today. You read the course description and reviews and it seemed super interesting. \nThe teacher walks in and hands out the syllabus – it looks manageable. \nProf then emphasizes that her course is very intense and will require long hours of focused work and diligent time management. She further articulates that 65% of students tend to get a final grade below an A. \nDo you decide to take the class S/NC or take it for a grade?')
                choice19 = input('Type "S/NC" or "grade" to make your choice:')
                if choice19 == 'S/NC' or choice8 == 'SNC':
                    descriptive += 1
                    print('You have a peaceful and restful semester!')
                else:
                    normative +=1
                    print('You feel energized by your courage and decide to search for internships. You head over the Rock and hop onto BrownConnect.\nYou find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. \nYou find a second internship that pays $15 an hour, 40 hours per week. You do not know the acceptance rate of this internship. \nBoth applications are due tonight, so you only have time to apply to one. Which internship do you choose?')
                    choice20 = input('Type "first internship" or "second internship" to make your choice:')
                    if choice20 == 'first internship':
                        descriptive += 1
                        print('You brag to your friends about how you are a shoe-in for the internship you applied to and they become spiteful and never speak to you again. You are lonely forever')
                    else:
                        normative +=1
                        print('A few weeks later you are notified that you got the internship! All of your career dreams come true.')


















