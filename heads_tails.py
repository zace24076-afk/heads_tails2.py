'''
    author: Zac Elder
    date: 10/8/26
    version: 1.0
    description: Game of heads and tails
'''

#-----------libraries--------------------
import random
#----------functions--------------------
# Game play 
def heads_tails():
    user_score = 0
    comp_score = 0
    # Only loops when noone has won yet
    while comp_score != 3 and user_score != 3:
        comp_guess = random.randint(0,1) # generates a random
        # Checking to see if the user has inputed correctly 
        # Check that there is no letters or 
        # 
        try: 
            user_guess = int(input('Type 0 for Heads or 1 for Tails: '))
        except:
            if(user_guess.isaplha()):


        
        if user_guess == comp_guess:
            print('You won this round!')
            user_score += 1
        else:
            print('You lost this round!')
            comp_score += 1

    if user_score == 3:
        print('Congrats {} you beat the computer!!!'.format(first_name))
    else:
        print('You lost, better luck next time {}!'.format(first_name))

# Checking the name validation
def force_name(first_name):
    while (valid): # this means the loop doesn't end until the name is valid
        name = input('What is your first name: ')
        if(len(name) > min_len and len(name) < max_len ): #checking if their names a correct length
            if(name.isalpha()): #checking if the name only includes letters from the alphabet
                print('Your name is valid')
                break # this exits the loop
            else:
                print('Only use letters in your name')
        else:
            print('Your name is an invalid length, try again')
    return first_name # sends the name back to the main routine

def force_age(age):
    while (valid): # this means the loop doesn't end until the name is valid
        age = int(input('What is your age: '))
        if(age > min_age and age < max_age ): #checking if they are in the age range
            if(age.isalpha()):#checking if the name only includes letters from the alphabet
                print('Age is valid')
                break # this exits the loop
            else:
                print('Only use numbers in your name')
        else:
            print('You age is invalid')
    return age # sends the name back to the main routine
# -----------main_routine-----------------
print('Hi, this is the heads and tails game')

# Variables
valid = True
min_len = 2
max_len = 20
first_name = force_name
force_name(first_name)

min_age = 12
max_age = 19
age = force_age
force_age(age)

age = int(input("Enter your age: "))

heads_tails()

