import random

# The game is to guess a number between 1 and 100 
low = 1
high = 100

# Randomly choose a number between 1 and 100
random_number = random.randint(1,100)

while True:    
    guess = int(input(f"Guess a number between {low} and {high}: "))
    if guess < low or guess > high:
        print("The number is not valid. Please enter a new number.")
        continue

    if random_number == guess:
        print(f"The number is {random_number}")
        break

    else:
        if guess > random_number:
            high = guess

        else:
            low = guess