import random

# Prompt user input
user_input_value = input("Please enter Rock (R), Paper (P) or Scissors (S):").upper()


# Convert user input into Rock, Paper or Scissors
def user_input_converter(initial_user_input):
    if initial_user_input == 'R':
        return 'Rock'
    elif initial_user_input == 'S':
        return 'Scissors'
    elif initial_user_input == 'P':
        return 'Paper'
    else:
        return 'You have selected an invalid character. Please choose R (rock), P (paper) or S (scissors) to play!'


# Capture converted user input
user_input_converted_value = user_input_converter(user_input_value)
if user_input_converted_value == 'Rock' or user_input_converted_value == 'Scissors' or user_input_converted_value == 'Paper':
    print("You have chosen {}".format(user_input_converted_value.lower()))
else:
    print(user_input_converted_value)


# Random number generator

def random_number_generator():
    random_num = random.randrange(1, 3, 1)
    return random_num


# Convert computer choice into input
def computer_input_converter(computer_input):
    if computer_input == 0:
        return 'Rock'
    elif computer_input == 2:
        return 'Scissors'
    elif computer_input == 1:
        return 'Paper'


# Capture computer choice
computer_choice_converted_value = computer_input_converter(random_number_generator())
if user_input_converted_value == 'Rock' or user_input_converted_value == 'Scissors' or user_input_converted_value == 'Paper':
    print("The computer has chosen {}".format(computer_choice_converted_value.lower()))


# Compare user and computer to decide who wins
def winner_decider(final_user_input, com_input):
    if final_user_input == com_input:
        return "it's a draw!"
    elif final_user_input == 'Paper' and com_input == 'Rock':
        return 'you win!'
    elif final_user_input == 'Scissors' and com_input == 'Paper':
        return 'you win!'
    elif final_user_input == 'Rock' and com_input == 'Scissors':
        return 'you win!'
    else:
        return 'the computer wins!'


winner = winner_decider(user_input_converted_value, computer_choice_converted_value)
if user_input_converted_value == 'Rock' or user_input_converted_value == 'Scissors' or user_input_converted_value == 'Paper':
    print("Therefore, {}".format(winner))

