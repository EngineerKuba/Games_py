#%%
'''
It is a simple guessing game that can run in 2 modes. 
1) User is guessing a random number generated by computer
2) Computer is guessing number generated by user.
'''
import random

def get_ran_num(n):
    '''Define game where user is trying to guess computer number.'''

    ran_num = random.randint(0, n)
    guess = int(input(f"Type your guess >= 0 and =< {n}: "))
    tries = 1
    while guess != ran_num:
        if guess < ran_num:
            guess = int(input("Guess higher."))
            tries += 1
        else:
            guess = int(input("Guess lower."))
            tries += 1

    print(f"Good guess, num == {ran_num}.")
    print(f"It took you {tries} tries.")

def get_guess(n):
    '''Define game where cumputer is trying to guess users number.'''

    tries = 1
    low = 0
    high = n
    number = random.randint(low, high)
    guess = input(f"Is your number lower (l), higher (h) or equal (e) to {number}").lower()
    while guess != "e":
        if guess == "l":
            high = number
            number = random.randint(low, high)
            tries +=1
        elif guess == "h":
            low = number
            number = random.randint(low, high)
            tries +=1
        guess = input(f"Is your number lower (l), higher (h) or equal (e) to {number}").lower()    
    print(f"Guessed number: {number}. \nAfter {tries} tries.")

again = "y"
while again == "y":

    n = int(input("Give range of guess from 0 - "))

    mode = input("Who is guessing? You (M) or computer (C)").lower()
    if mode == "m":
        print("User guessing mode.")
        get_ran_num(n)
    else:
        print("Computer guessing mode.")
        get_guess(n)

    again = input("Do you want to play again? Y/N").lower()
# %%
