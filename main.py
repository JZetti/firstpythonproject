
#Greet the user
print("Hello World")
print("I'm glad you're here")
print("justkidding")
print("math operations inbound")

year =1890
_year =1993
yearArmy = 1775

# calculate army age 
year = 2025
yearArmy = 1775
ageOfArmy = year - yearArmy
print("The Army is", ageOfArmy, "Years old") 

#new variables
x = .10
j = .15
i = .20
z = .25
total = 47.56
tip = total * x, total * j, total * i, total * z
print("tip tiers are", tip)

#avg
game1 = 13.0
game2 = 18.0
game3 = 21.0
game4 = 17.0
game5 = 31.0
totalGames = 5.0
print()
print("baller stats printed and averaged")
avgPPG = "Their avg PPG", (game1 + game2 + game3 + game4 + game5) / totalGames
print(avgPPG)
print()

#age with user input
name = input("Yo your name?? ")
age = input("AND AGE?! ")
age = int(age)
print(name, "next year you will be", age+1, "years old")

#6 values from some cosmic being
user_values = input("give me your values gypsy, six of them- serparate by spaces ")
values = [int(x) for x in user_values.split()]
totalSum = sum(values)
print(totalSum, "I added them, you're welcome.")

#just the tip pt2
user_tip = input("enter your tip percentage (like 15 for 15%): ")
total = 47.56

# Convert tip to decimal and calculate tip amount
tip_percentage = int(user_tip) / 100  
tipAmount = total * tip_percentage    
print("percent tipped:", tip_percentage * 100,"%")
print("tip amount: ", total * tip_percentage )
print("Total with tip:", total + tipAmount)

#Basketball pt2
user_points = input("Enter in total points in basketball game, max 10- separated by spaces ")
points = [int(x) for x in user_points.split()]
sumOfPoints = sum(points)
avgPPG = sumOfPoints / len(points)  # Divide by number of games, not the string
print("Total points:", sumOfPoints)
print("Average PPG:", avgPPG)
print()

#Self calculation real world example
dollarsTotal = 1000
dogFood = 200
grooming = 250
GPU = 1200
if GPU > dollarsTotal:
    print("Can I afford a gpu? ")
    print(dollarsTotal- dogFood -grooming, "You are broke dumb ass ")
else:
    print("not possible ")
print()
#madlib madness
user_adjective = input("Enter adjective here for madlib ")
user_noun = input("noun it up ")
past_verb = input("past tense verbage here <--- ")
another_noun = input("we add words to programs every NOUN and again! ")
print("The quick", user_adjective, user_noun, past_verb, "over the lazy ", another_noun)

#personal madlib/ dodgeball quote
noun1 = input("____ fill in the blank with a noun")
verb = input("____  fill with a verb")
verb_noun = input("____ finish strong with a verb or a noun")
print(noun1, "makes me",verb,"my own", verb_noun)

sithValue = int(input("How many jedi has the sith killed? "))
jediValue = int(input("How many sith have the jedi killed?"))
jediAcolytes = 5.0
sithAcolytes = 2.0
stolenJediAcolytes = .5
totalJedi = 100 - jediValue + jediAcolytes / stolenJediAcolytes
totalSith = 100 - sithValue + sithAcolytes + stolenJediAcolytes

if totalJedi > totalSith:
    print("The Jedi outnumber the Sith")
else:
    print("The Sith outnumber the Jedi")


#user age pt 2
user_age = int(input("Enter your age: "))

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

#rock paper scissors, fire
import random

print("Rock Paper Scissors Game!")
print("1 = Rock, 2 = Paper, 3 = Scissors")
user_choice = int(input("Choose 1, 2, or 3: "))

# Computer randomly chooses 1-4 (including secret fire option)
computer_choice = random.randint(1, 4)

# Display choices
choices = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Fire"}
print("You chose:", choices[user_choice])
print("Computer chose:", choices[computer_choice])

# Game logic
if computer_choice == 4:  # Fire beats everything
    print("Computer wins! Fire burns everything!")
elif user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 1 and computer_choice == 3) or \
     (user_choice == 2 and computer_choice == 1) or \
     (user_choice == 3 and computer_choice == 2):
    print("You win!")
else:
    print("Computer wins!")

