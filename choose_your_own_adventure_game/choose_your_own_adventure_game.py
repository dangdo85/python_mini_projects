name = input("Typ your name: ")
print("Welcome", name, "to this adventure!")
answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Would you like to swim or walk?")

    if answer == "swim":
        print("You swam across and were eaten by alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = print("You come to a bridge, it looks woobly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer= input("You crossed the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        if answer == "yes":
            print("You talked to the stranger and they gave you gold. You WIN!")
        elif answer == "no":
            print("You ignored the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")
else:
    print()