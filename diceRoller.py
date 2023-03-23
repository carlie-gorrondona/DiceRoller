#---------------------------------- IMPORTS AND LIBRARIES ----------------------------------#
import random


#---------------------------------- FUNCTIONS ----------------------------------#

#This function randomly assigns a nummerical value to each die. Once the value of each die is determined, an image prints to the terminal to depict an image of the dice. 
#The calculateRoll() function is called to determine the total value with dieOne and dieTwo passed by reference. The rollAgainMenu function is called to print another 
#menu to give the user an option to roll again or quit.
def rollDice():  
    dieOne = random.randint(1, 6)
    dieTwo = random.randint(1, 6)

    match dieOne:
        case 1:
            print("_________")
            print("|       |")
            print("|   *   |")
            print("|       |")
            print("---------")
        case 2:
            print("_________")
            print("|   *   |")
            print("|       |")
            print("|   *   |")
            print("---------")
        case 3:
            print("_________")
            print("|   *   |")
            print("|   *   |")
            print("|   *   |")
            print("---------")
        case 4:
            print("_________")
            print("| *   * |")
            print("|       |")
            print("| *   * |")
            print("---------")
        case 5:
            print("_________")
            print("| *   * |")
            print("|   *   |")
            print("| *   * |")
            print("---------")
        case 6:
            print("_________")
            print("| *   * |")
            print("| *   * |")
            print("| *   * |")
            print("---------")
        case _:
            print("Invalid dice roll")

    match dieTwo:
        case 1:
            print("_________")
            print("|       |")
            print("|   *   |")
            print("|       |")
            print("---------")
        case 2:
            print("_________")
            print("|   *   |")
            print("|       |")
            print("|   *   |")
            print("---------")
        case 3:
            print("_________")
            print("|   *   |")
            print("|   *   |")
            print("|   *   |")
            print("---------")
        case 4:
            print("_________")
            print("| *   * |")
            print("|       |")
            print("| *   * |")
            print("---------")
        case 5:
            print("_________")
            print("| *   * |")
            print("|   *   |")
            print("| *   * |")
            print("---------")
        case 6:
            print("_________")
            print("| *   * |")
            print("| *   * |")
            print("| *   * |")
            print("---------")
        case _:
            print("Invalid dice roll")

    calculateRoll(dieOne, dieTwo)
    rollAgainMenu()

#This function calculates the total value of the dice by passing their values by reference. Once total value is calculated, a match case statment prints a message
#for the calculated value. 
def calculateRoll(dieOneValue, dieTwoValue):
    totalValue = dieOneValue + dieTwoValue

    match totalValue:
        case 2:
            print("Snake eyes!!! <( | )>  <( | )>\n")
        case 3:
            print("You rolled a three!\n")
        case 4:
            print("Noice! A four.\n")
        case 5:
            print("Yas! A five! Divisible by five. Perfection.\n")
        case 6:
            print("You rolled a six!\n")
        case 7:
            print("Congrats! A seven! The number with the highest odds of being rolled.\n")
        case 8:
            print("Woohoo! An eight!\n")
        case 9:
            print("NINE!\n")
        case 10:
            print("YES!!!! A ten! Divisible by five and ten. Ultimate perfection.\n")
        case 11:
            print("Cool! You rolled an eleven.\n")
        case 12:
            print("Hell yeah! Double sixes!!!!! AKA twelve.\n")
        case _:
            print("What?! How did you even roll this?\n")

#This function prints a menu after each dice roll, so the user can determine whether or not they want to continue rolling or quit.
def rollAgainMenu():
    print("@------------- MENU --------------@")
    print("|        1. Roll Again! :D        |")
    print("|          2. Quit :(             |")
    print("@---------------------------------@")
    playerOption = input("What would you like to do now? ")

    if playerOption == "1":
        rollDice()
    elif playerOption == "2":
        print("Later! Thanks for playing DICE ROLLER!!!!")
    else:
        print("Invalid entry")


#---------------------------------- MAIN ----------------------------------#

print("@---- WELCOME TO DICE ROLLER! ----@\n")
print("@----------- MAIN MENU -----------@")
print("|          1. Roll! :D            |")
print("|          2. Quit :(             |")
print("@---------------------------------@")
playerOption = input("Make your choice: ")

if playerOption == "1":
    rollDice()  
elif playerOption == "2":
    print("Later!")
else:
    print("Invalid choice")