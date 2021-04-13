# Decisions-Decisions-Decisions
 #Initialize variables
descriptive = 0
normative = 0

print('Hi! Welcome to "Decisions, Decisions, Decisions," a choose-your-own-adventure game that will take you through the semester of a Brown student.')


#Choice 1: Immune Neglect
print ('Alex, your partner of 4 years, the love of your life, just broke up with you right before your flight to Brown for your first semester of university - they said they can’t do long distance.')
print('You are pursuing a double major, so it would be wise of you to start the heavy lifting from early.  However, you are heartbroken and unsure of your ability to offer your best work. Do you…')
print('A: Take 2 easy courses and 2 hard courses, to prevent yourself from having a mental breakdown mid semester')
print('B: Take 3 hard requirements and 1 easy course – you’re a soldier!')

choice1 = input('Type "A" or "B" to make your choice:')

if choice1 == 'A':
    descriptive = descriptive + 1
elif choice1 == 'B':
    normative = normative + 1

#Choice 2: Anchoring
print('You venture into the Brown bookstore with a flexible budget of $60, looking for some merch. At the front of the bookstore is a grand display of the new Brown hoodies.')
print('Each hoodie costs $100. You search in the back of the store for other hoodie options and find a cite hoodie from last year for $80. Do you…')
print('A: Buy the $80 hoodie')
print('B: Leave the store without buying anything')

choice2 = input('Type "A" or "B" to make your choice:')

if choice2 == 'A':
    descriptive = descriptive + 1
elif choice2 == 'B':
    normative = normative + 1

#Choice 3: Framing
print('You are happily seated in your first class of the semester. You read the course description and reviews and it seems super interesting.')
print('The teacher walks in and hands out the syllabus – it looks manageable. Prof then emphasizes that her course is very intense and will require long hours of focused work and diligent time management.')
print('She further articulates that 65% of students tend to get a final grade below an A. Do you decide to...')
print('A: Take the class pass fail because it seems like it’ll be tough')
print('B: Take the class for a grade and have faith in your academic ability and diligence, seeing that you read the reviews and descriptions and it seemed manageable')

choice3 = input('Type "A" or "B" to make your choice:')

if choice3 == 'A':
    descriptive = descriptive + 1
elif choice3 == 'B':
    normative = normative + 1

#Choice 4: Sunk Cost Fallacy
print('You grudgingly head to your APMA class. You realize that you no longer have any interest in the material, nor do you have any need for this class; in fact, you really don’t like the class.')
print('You can drop the class with no fee, but you have already invested 75+ hours of work into the class (5 weeks of work), and you spent $65 on the textbook. Do you...')
print('A: drop the class')
print('B: stay in the class')

choice4 = input('Type "A" or "B" to make your choice:')

if choice4 == 'A':
    normative = normative + 1
elif choice4 == 'B':
    descriptive = descriptive + 1

#Choice 5: Progress Bias
print('It’s midterm season and you have become a coffee fiend. Sleep deprivation is so expensive! You realized a few weeks ago that you went to Starbucks five times in one week. Yikes.')
print('To not go broke, you made a goal to only go a maximum of twice a week, which you followed perfectly last week.')
print('It’s friday, you finished your last exam, and your friends want to grab Starbucks and sit in the sun. But you already went twice this week. Do you...')
print('A: Just go an extra time this week, I mean you met your goal last week anyway.')
print('B: Stick to your goal and keep your spending down. Water is pretty good too.')

choice5 = input('Type "A" or "B" to make your choice:')

if choice5 == 'A':
    descriptive = descriptive + 1
elif choice5 == 'B':
    normative = normative + 1

#Choice 6: Endowment Effect
print('It’s dinner time! Unfortunately, you do not have any meal swipes or flex points, but you are really hungry and you are craving a pasta bowl from Andrews.')
print('You pay $8.75 in cash for your pasta bowl and sit down, all excited to eat it. It looks like you got the last pasta bowl, though, so someone approaches you saying they REALLY wanted a pasta bowl too.')
print('They offer to pay you $9.75 for your pasta bowl - $1.00 more than you initially paid. Do you accept their offer?')

choice6 = input('Type "Yes" or "No" to make your choice:')

if choice6 == 'Yes':
    normative = normative + 1
elif choice6 == 'No':
    descriptive = descriptive + 1

#Choice 7: Availability Heuristic
print('You’re on your way to a late night grind in the stacks at the SciLi. You run into your friend outside of Caswell and talk for a bit.')
print('You both end up complaining about how dusty and depressing some of the scili is. They tell you that the last time they were in the stacks, someone there saw a mouse. Gross.')
print('But you’re already so close to the SciLi….. Do you decide to:')
print('A: Go to the sci li since you’re already so close and all stacks are rightfully terrible ')
print('B: Go to the Rock stacks; mice are nasty!')

choice7 = input('Type "A" or "B" to make your choice:')

if choice7 == 'A':
    normative = normative + 1
elif choice7 == 'B':
    descriptive = descriptive + 1

#Choice 8: Ambiguity Effect
print('You sit down in the SciLi and browse BrownConnect, looking for summer internships to apply to.')
print('You find one internship that says it has a 40% acceptance rate and pays $13 an hour, 40 hours per week. You find a second internship that pays $15 an hour, 40 hours per week.')
print('You do not know the acceptance rate of this internship. Both applications are due tonight, so you only have time to apply to one. Which internship do you choose?')

choice8 = input('Type "first internship" or "second internship" to make your choice:')

if choice8 == 'second internship':
    normative = normative + 1
elif choice8 == 'first internship':
    descriptive = descriptive + 1

#Choice 9: Confirmation Bias
print('It is spring weekend!!! You and your friends are trying to figure out whose room you should prepare in before you head out for the show.')
print('You guys already decided to go to your friend who lives in emwools room. You like hanging out in their room the best because it is bigger and they have a way nicer bathroom.')
print('Before you start getting ready, your friend texts and says everyone should meet in your room instead because her roommates friends showed up and the room is kinda crowded, also you live closer to the main green.  Do you decide to:')
print('A: Change the location to your room since it is closer')
print('B: Stick to your friends room; the more people the better!')

choice9 = input('Type "A" or "B" to make your choice:')

if choice9 == 'A':
    normative = normative + 1
elif choice9 == 'B':
    descriptive = descriptive + 1

if normative>descriptive:
    print('You are a rational decision-maker, and the majority of your choices align with  normative decision theories')
elif descriptive>normative:
    print('You are a nonrational decision-maker, and the majority of your choices align with descriptive decision theories')
