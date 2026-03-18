print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go?")
direction = input("\t Type \"left\" or \"right\"\n")

if direction == "right" or direction == "Right":
    print("You fell into a hole. Game Over.")
elif direction == "left" or direction == "Left":
    # Continue in game
    print("You have come to a lake. There is an island in the middle of the lake.")
    lake = input('\t Type "wait" to wait for a boat. Type"swim" to swim across.\n')

    if lake == "swim" or lake == "Swim":
        print("You got attacked by an angry trout. Game Over.")
    elif lake == "wait" or lake == "Wait":
        print("You arrived at the island unharmed. There is a house with 3 doors.")
        door = input("\t One red, one yellow and one blue. Which colour do you choose?\n")

        if door == "red" or door == "Red":
            print("It's a room full of fire. Game Over.")
        elif door == "yellow" or door == "Yellow":
            print("You found the treasure! You Win!")
        elif door == "blue" or door == "Blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    else:
        print("Invalid choice! Start again.")

else:
    print("Invalid choice! Start again.")