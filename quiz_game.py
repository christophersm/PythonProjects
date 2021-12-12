print("Welcome to the Star Wars quiz game!")

playing = input("Do you want to play, yes or no? ")

if playing.lower() != "yes":
    quit()

print("Ok! Let's play!")

score = 0

answer = input("What year was Star Wars IV - A New Hope Released? ")
if answer == "1977":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who wrote and directed Star Wars IV - A New Hope? George Hamill, George Ford, Gary Kurtz or George Lucas ").lower()
if answer == "george lucas":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Darth Vader's last name? ").lower()
if answer == "skywalker":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does Luke Skywalker go onto become? Ninja, Samurai, Knight, or Jedi ").lower()
if answer == "jedi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str((score/4) * 100) + "% " + "correct.")
