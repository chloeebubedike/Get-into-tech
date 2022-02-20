import random
# Prompt user input
user_input = input("Please enter Rock (R), Paper (P) or Scissors (S):").upper()


#Convert user input into Rock, Paper or Scisscors
def user_input_converter(input):
    if input == 'R':
        return 'Rock'
    elif input == 'S':
        return 'Scissors'
    elif input == 'P':
        return 'Paper'
    else:
        return 'Please enter R (rock), P (paper) or S (scissors)'

#Capture converted user input
user_input_converted = user_input_converter(user_input)
print(user_input_converted)


#Random number generator
def random_number_generator():
    random_num = random.randrange(1, 3, 1)
    return random_num


#Convert computer choice into input
def computer_input_converter(com_input):
    if com_input == 0:
        return 'Rock'
    elif com_input == 2:
        return 'Scissors'
    elif com_input == 1:
        return 'Paper'

#Capture computer choice
computer_choice = computer_input_converter(random_number_generator())
print(computer_choice)


#Compare user and computer to decide who wins
def decide_winner(user_input, com_input):
    if user_input == com_input:
        return 'Its a draw!'
    elif user_input == 'Paper' and com_input == 'Rock':
        return 'User wins!'
    elif user_input == 'Scissors' and com_input == 'Paper':
        return 'User wins!'
    elif user_input == 'Rock' and com_input == 'Scissors':
        return 'User wins!'
    else:
        return 'Computer wins!'


winner = decide_winner(user_input_converted, computer_choice)
print(winner)