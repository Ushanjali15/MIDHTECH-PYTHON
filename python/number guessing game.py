import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number (1-10): "))

    if guess == number:
        print("🎉 Correct! You guessed the number.")
        break
    elif guess < number:
        print("Hint: Guess a higher number.")
    else:
        print("Hint: Guess a lower number.")
