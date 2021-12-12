import random 

top_of_range = input("Type the highest number you want the computer to select a random number from: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time!")
        continue
    
    if user_guess == random_number:
        print("You guessed the correct number!")
        break
    else:
        if user_guess > random_number:
            print("You guessed too high!")
        else:
            print("you guessed too low!")

print("It took you", guesses, "guesses to get the correct number!")

