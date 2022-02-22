# Import random module
import random


# Function to get allocate input
def allocate_user_input(user_input_letter):
    if user_input_letter == 'R':
        return 'Rock'
    elif user_input_letter == 'S':
        return 'Scissors'
    elif user_input_letter == 'P':
        return 'Paper'
    else:
        return 'You have selected an invalid character. Please choose R (rock), P (paper) or S (scissors) to play!'


# Function to generate random number
def generate_random_number():
    return random.randrange(1, 3, 1)


# Convert computer choice into input (Rock, Paper or Scissors)
def allocate_computer_input(computer_input):
    if computer_input == 0:
        return 'Rock'
    elif computer_input == 2:
        return 'Scissors'
    elif computer_input == 1:
        return 'Paper'


# Compare user and computer input values to decide who wins
def decide_winner(compared_user_input, compared_computer_input):
    if compared_user_input == compared_computer_input:
        return "it's a draw!"
    elif compared_user_input == 'Paper' and compared_computer_input == 'Rock':
        return 'you win!'
    elif compared_user_input == 'Scissors' and compared_computer_input == 'Paper':
        return 'you win!'
    elif compared_user_input == 'Rock' and compared_computer_input == 'Scissors':
        return 'you win!'
    else:
        return 'the computer wins!'


# Function to print game script
def print_game_script(user_input, computer_input, decided_winner):
    if user_input == 'Rock' or user_input == 'Scissors' or user_input == 'Paper':
        print("You have chosen {}".format(user_input.lower()))
        print("The computer has chosen {}".format(computer_input.lower()))
        print("Therefore, {}".format(decided_winner))
    else:
        print(user_input)


# Prompt user input
user_input_value = input("Please enter Rock (R), Paper (P) or Scissors (S):").upper()

# Allocate user input
user_input_converted_value = allocate_user_input(user_input_value)

# Allocate user choice
computer_choice_converted_value = allocate_computer_input(generate_random_number())

# Decide winner
winner = decide_winner(user_input_converted_value, computer_choice_converted_value)

# Print game script
print_game_script(user_input_converted_value, computer_choice_converted_value, winner)


