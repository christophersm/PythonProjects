name = input("Type your name: ")
answer = input("Would you like to play a game?")

if answer.lower().strip() == "yes":

    answer = input("You are at a door, would you like to open it? Yes or No?").lower().strip()
    if answer == "yes":
        answer = input("You encounter a dark hallway, would you like to enter the hallway or turn around? type 'enter' or 'turn around'")

        if answer == "enter":
            print("You fell down a trap door and died!")
        else:
            print("You live to see another day!")

    
    elif answer == "no":
        print("You get attacked by the owner of the property and he kills you...Game over!")

    else:
        print("Invalid choice, you lost!")

else:
    print("Good Bye!")


    