import random

# Game Intro
def intro():
    print(''' 
          Welcome to the Number Guessing Game!
          
          In this game, the computer will randomly select a number
          within a specified range, and it's your job to guess 
          what the numver is. You will be given hints after each
          guess to help you get closer to the correct number.
          
          How to play:
          1. Choose the range of the number(e.g. between 1 and 100)
          2. The CPU will randomly pick a number within that range
          3. You will have chances to guess the number.
          4. After each guess, you will receive feedback:
            - If you guess is too high, you will be told "Too high"
            - If you guess is too low, you will be told "Too low"
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
    
    #check user input the correct input
    if lower_bound < upper_bound:
        return lower_bound, upper_bound
    else:
        print('Invalid input, lower bound must be less than the upper bound. Please try again!')

    return lower_bound, upperbound

intro() #game intro, explain rule

#ask user for the lower and upper bound
lower_bound, upper_bound = user_range()

#the computer number 
cpu_number = cpu_num(lower_bound, upper_bound)



attempts = 0 #tracks the attempt at each guess for the user

while True:
    try:
        guess = int(input(f'Enter your guess ({lower_bound}-{upper_bound}): '))
        attempts += 1
        
        if guess < cpu_number:
            print('Too low! Try again. ')
        elif guess > cpu_number:
            print('Too High! Try again. ')
        else:
            print(f'Congratulation! You guessed the correct number {cpu_number} in {attempts} attempts.')
            break
    except ValueError:
        print('Invalid input. Please enter a valid integer')
            


                          





