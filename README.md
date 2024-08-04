# number_guessing_game
Simple Python command line code for number guessing game
Here's a README file for your Number Guessing Game in Python:

---

# Number Guessing Game

Welcome to the Number Guessing Game! This is a simple Python game where the computer randomly selects a number within a specified range, and your goal is to guess the number. You'll receive hints after each guess to help you get closer to the correct number.

## How to Play

1. Choose the range of the number (e.g., between 1 and 100).
2. The computer will randomly pick a number within that range.
3. You will have chances to guess the number.
4. After each guess, you will receive feedback:
   - If your guess is too high, you will be told "Too high".
   - If your guess is too low, you will be told "Too low".
5. Keep guessing until you find the correct number.
6. The game will display the number of attempts it took you to guess correctly.

## Prerequisites

- Python 3.x

## How to Run the Game

1. Clone this repository or download the `number_guessing_game.py` file.
2. Open a terminal or command prompt and navigate to the directory where the file is located.
3. Run the game by executing the following command:

```bash
python number_guessing_game.py
```

## Game Code

```python
import random

# Game Intro
def intro():
    print(''' 
          Welcome to the Number Guessing Game!
          
          In this game, the computer will randomly select a number
          within a specified range, and it's your job to guess 
          what the number is. You will be given hints after each
          guess to help you get closer to the correct number.
          
          How to play:
          1. Choose the range of the number (e.g. between 1 and 100)
          2. The CPU will randomly pick a number within that range
          3. You will have chances to guess the number.
          4. After each guess, you will receive feedback:
            - If your guess is too high, you will be told "Too high"
            - If your guess is too low, you will be told "Too low"
          5. Keep guessing until you find the correct number.
          6. The game will display the number of attempts it took 
          you to guess correctly.
          ''')

def cpu_num(lower_bound, upper_bound):
    cpu_num = random.randint(lower_bound, upper_bound)
    return cpu_num

def user_range():
    print("Choose your range: ")
    lower_bound = int(input('Enter the lower bound of the range: '))
    upper_bound = int(input('Enter the upper bound of the range: '))

    # Check user input for correct input
    if lower_bound < upper_bound:
        return lower_bound, upper_bound
    else:
        print('Invalid input, lower bound must be less than the upper bound. Please try again!')
        return user_range()

intro() # Game intro, explain rule

# Ask user for the lower and upper bound
lower_bound, upper_bound = user_range()

# The computer number 
cpu_number = cpu_num(lower_bound, upper_bound)

attempts = 0 # Tracks the attempt at each guess for the user

while True:
    try:
        guess = int(input(f'Enter your guess ({lower_bound}-{upper_bound}): '))
        attempts += 1

        if guess < cpu_number:
            print('Too low! Try again.')
        elif guess > cpu_number:
            print('Too high! Try again.')
        else:
            print(f'Congratulations! You guessed the correct number {cpu_number} in {attempts} attempts.')
            break
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

