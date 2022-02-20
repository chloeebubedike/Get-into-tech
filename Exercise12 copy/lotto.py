#Import the random module
import random

#Create a variable to hold random numbers. Set used because it does not accept duplicate values
lottery_number = set(())

#Loop over random number generator while length of lottery variable is under 6 and add random number to set
while len(lottery_number) < 6:
    #Generates random number between 1 - 50 (1 step)
    random_num = random.randrange(1, 51, 3)
    #Adds random number generated to lottery number set
    lottery_number.add(random_num)

print(lottery_number)
