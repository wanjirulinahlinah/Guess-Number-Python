import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    
    while True:
        # Get the player's guess
        guess = int(input("Enter your guess (between 1 and 100): "))
        
        # Compare the guess with the random number
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number correctly!")
            break

if __name__ == "__main__":
    guess_the_number()