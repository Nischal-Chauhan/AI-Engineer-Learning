secret_number = 5

guess = input("Guess the number: ")
guess = int(guess)

while guess != secret_number:
    if guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

    guess = input("Guess the number: ")
    guess = int(guess)

print("Correct! You guessed the number.")
