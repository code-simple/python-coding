import random

top_of_range = input("Type a Number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("Please type a number Greater than 0")
        quit()
else:
    print("Please type a number next time")
    print(random_number)
    

random_number = random.randint(0,top_of_range) # Generate numbers from -5 to 10
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue # Go back to while loop

    if user_guess==random_number:
        print("You Got it in ",guesses," guesses")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number ")

