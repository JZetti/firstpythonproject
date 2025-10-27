
# just saying hello and stuff
print("Hello World")
print("I'm glad you're here")
print("justkidding")
print("math operations inbound")

# messing around with year numbers
year = 1890        # some old year
_year = 1993       # year with underscore thing
yearArmy = 1775    # when army started

# figuring out how old the army is
year = 2025                    # what year it is now
yearArmy = 1775               # army start year again
ageOfArmy = year - yearArmy   # subtract to get age
print("The Army is", ageOfArmy, "Years old") 

# tip stuff - different percentages
x = .10     # 10 percent tip
j = .15     # 15 percent tip  
i = .20     # 20 percent tip
z = .25     # 25 percent tip
total = 47.56   # the bill
# multiply bill by each tip percent
tip = total * x, total * j, total * i, total * z
print("tip tiers are", tip)
print()
# basketball points from 5 games
game1 = 13.0        # game 1 points
game2 = 18.0        # game 2 points
game3 = 21.0        # game 3 points
game4 = 17.0        # game 4 points
game5 = 31.0        # game 5 points
totalGames = 5.0    # how many games
print()
print("baller stats printed and averaged")
# add all games and divide by number of games
avgPPG = "Their avg PPG", (game1 + game2 + game3 + game4 + game5) / totalGames
print(avgPPG)
print()

# get name and age from user
name = input("Yo your name?? ")        # get their name
age = input("AND AGE?! ")              # get age as text
age = int(age)                         # turn age into number
print(name, "next year you will be", age+1, "years old")  # add 1 year
print()
# get 6 numbers from user all at once
user_values = input("give me your values gypsy, six of them- serparate by spaces ")
# split the text by spaces and turn each one into a number
values = [int(x) for x in user_values.split()]
totalSum = sum(values)                 # add them all up
print(totalSum, "I added them, you're welcome.")
print()
# tip calculator where user types the percent
user_tip = input("enter your tip percentage (like 15 for 15%): ")
total = 47.56   # the bill amount

# turn tip percent into decimal and figure out tip money
tip_percentage = int(user_tip) / 100   # make it decimal
tipAmount = total * tip_percentage     # multiply to get tip dollars
print("percent tipped:", tip_percentage * 100,"%")
print("tip amount: ", total * tip_percentage )
print("Total with tip:", total + tipAmount)
print()
# basketball points from user - they type multiple scores
user_points = input("Enter in total points in basketball game, max 10- separated by spaces ")
points = [int(x) for x in user_points.split()]  # turn input into list of numbers
sumOfPoints = sum(points)                       # add all points
avgPPG = sumOfPoints / len(points)             # divide by how many games
print("Total points:", sumOfPoints)
print("Average PPG:", avgPPG)
print()

# checking if i can afford a gpu
dollarsTotal = 1000    # how much money i got
dogFood = 200          # dog food cost
grooming = 250         # grooming cost
GPU = 1200            # gpu cost
# see if gpu costs more than my money
if GPU > dollarsTotal:
    print("Can I afford a gpu? ")
    # money left after dog stuff
    print(dollarsTotal- dogFood -grooming, "You are broke dumb ass ")
else:
    print("not possible ")
print()

# madlib game - user gives me words
user_adjective = input("Enter adjective here for madlib ")
user_noun = input("noun it up ")
past_verb = input("past tense verbage here <--- ")
another_noun = input("we add words to programs every NOUN and again! ")
# put their words in my sentence
print("The quick", user_adjective, user_noun, past_verb, "over the lazy ", another_noun)

# dodgeball quote but with user words
noun1 = input("____ fill in the blank with a noun")
verb = input("____  fill with a verb")
verb_noun = input("____ finish strong with a verb or a noun")
# make the quote with their words
print(noun1, "makes me",verb,"my own", verb_noun)

# star wars battle thing
sithValue = int(input("How many jedi has the sith killed? "))
jediValue = int(input("How many sith have the jedi killed?"))
jediAcolytes = 5.0          # jedi recruits
sithAcolytes = 2.0          # sith recruits  
stolenJediAcolytes = .5     # jedi who were sithnapped
# do some math to see who has more left
totalJedi = 100 - jediValue + jediAcolytes / stolenJediAcolytes
totalSith = 100 - sithValue + sithAcolytes + stolenJediAcolytes

# see who wins
if totalJedi > totalSith:
    print("The Jedi outnumber the Sith")
else:
    print("The Sith outnumber the Jedi")


# age checker - tells you what you can do at different ages
user_age = int(input("Enter your age: "))

# check what age they are and say something
if user_age == 0:
    print("you should of been aborted")
elif user_age == 16:
    print("you can drive")
elif user_age == 18:
    print("you can join the army")
elif user_age == 21:
    print("Now you can drink and drive")
elif user_age == 55:
    print("they can be old cheaper")
else:
    print("Nothing special about age", user_age)
print()
# rock paper scissors but with secret fire
import random    # need this for random numbers

print("Rock Paper Scissors Game!")
print("1 = Rock, 2 = Paper, 3 = Scissors")
user_choice = int(input("Choose 1, 2, or 3: "))

# computer picks 1-4 but user doesnt know about 4
computer_choice = random.randint(1, 4)

# names for the numbers
choices = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Fire"}
print("You chose:", choices[user_choice])
print("Computer chose:", choices[computer_choice])

# who wins - fire beats everything else normal rules
if computer_choice == 4:  # fire always wins
    print("Computer wins! Fire burns everything!")
elif user_choice == computer_choice:
    print("It's a tie!")
# rock beats scissors, paper beats rock, scissors beats paper
elif (user_choice == 1 and computer_choice == 3) or \
     (user_choice == 2 and computer_choice == 1) or \
     (user_choice == 3 and computer_choice == 2):
    print("You win!")
else:
    print("Computer wins!")

