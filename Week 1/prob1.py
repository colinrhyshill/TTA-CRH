import random
myName = input("Gib Name.\n")
number = random.randint(1, 10)
guess = int(input(myName +", gib number between 1 and 10. Gib right meow.\n"))
if guess == number:
    print("Have treato u guessed rightly.")
else:
    print("Bonk. Go to wrong number jail.")