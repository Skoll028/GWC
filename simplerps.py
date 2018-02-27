##Import the random package, so the computer can choose at random from given options
from random import *;

print("Welcome to Rock Paper Scissors!");

##Request user input, and check for validation

while True:

    pick = input("Please enter R for rock, P for paper or S for Scissors: ");

    if ((pick.upper() == "R") or (pick.upper() == "S") or (pick.upper() == "P")):
        break;
    else:
        print("Please try again. That isn't a valid input");
        

##Pick the computer's value

options = ["R", "P", "S"];

comp = choice(options);

##Print the computer's choice

print(comp);

##Compare the logical conditions

##If the user picked the same thing as the computer, it is a tie
if (comp == pick.upper()):
    print("It's a tie!");

##Check if it is the win condition
elif (((pick.upper() == "R") and (comp == "S")) or ((pick.upper() == "S") and (comp == "P")) or ((pick.upper() == "") and (comp == "S"))):
    print("You win!");

##Otherwise, you lose
else:
    print("You lose...");
