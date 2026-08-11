'''
    author: Zac Elder
    date: 10/8/26
    version: 1.0
    description: Game of heads and tails
'''

#-----------libraries--------------------

import random

#----------functions--------------------
def heads_tails():
    user_score = 0
    comp_score = 0
    
    while comp_score != 3 and user_score != 3:
        comp_guess = random.randint(0,1)
        user_guess = int(input("Type 0 for Heads or 1 for Tails: "))
        
        if user_guess == comp_guess:
            print("You won this round!")
            user_score += 1
        else:
            print("You lost this round!")
            comp_score += 1

    if user_score == 3:
        print("Congrats {} you beat the computer!!!".format(first_name))
    else:
        print("You lost, better luck next time {}!".format(first_name))


# -----------main_routine-----------------
print("Hi, this is the heads and tails game")
first_name = str(input("What is your name: "))


age = int(input("Enter your age: "))
heads_tails()
#i love cufvvvekjfe
#jerfkwjebfjkw
#gklvnlv