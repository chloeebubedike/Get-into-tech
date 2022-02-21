import random

# Prompt user input
user_input = input("Please enter Rock (R), Paper (P) or Scissors (S):").upper()


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
user_input_converted = user_input_converter(user_input)
if user_input_converted == 'Rock' or user_input_converted == 'Scissors' or user_input_converted == 'Paper':
    print("You have chosen {}".format(user_input_converted.lower()))
else:
    print(user_input_converted)


# Random number generator

def random_number_generator():
   random_num = random.randrange(1, 3, 1)
   return random_num


# Convert computer choice into input
def computer_input_converter(com_input):
    if com_input == 0:
        return 'Rock'
    elif com_input == 2:
        return 'Scissors'
    elif com_input == 1:
        return 'Paper'


# Capture computer choice
computer_choice = computer_input_converter(random_number_generator())
if user_input_converted == 'Rock' or user_input_converted == 'Scissors' or user_input_converted == 'Paper':
    print("The computer has chosen {}".format(computer_choice.lower()))


# Compare user and computer to decide who wins
def decide_winner(final_user_input, com_input):
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


winner = decide_winner(user_input_converted, computer_choice)
if user_input_converted == 'Rock' or user_input_converted == 'Scissors' or user_input_converted == 'Paper':
    print("Therefore, {}".format(winner))
else:
    print("No winner")
