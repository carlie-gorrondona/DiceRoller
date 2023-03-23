#---------------------------------- IMPORTS AND LIBRARIES ----------------------------------#
import random


#---------------------------------- FUNCTIONS ----------------------------------#

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