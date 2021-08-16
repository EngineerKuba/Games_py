#%%
"""
This is a simple rock paper scissors game. 
User need to pick his weapon then cumputer picks his randomly.
Results are evluated.
"""
import random

def roshambo():
    user = input("Pick your weapon \n'r' = rock\n's' = scissors\n'p' = paper\n")
    computer = random.choice(['r', 'p', 's'])
    dictionary = {'r':'rock',  'p':'paper', 's':'scissors'}
    print(f"Users choice {dictionary.get(user)}")
    print(f"Computers choice {dictionary.get(computer)}")
    if user == computer:
        return print("Tie!")
    if win(user, computer):
        return print("You won!!")
    
    return print("Computer won\nMachine taking over human again\n:(:(:(")

def win(player_1, player_2):
    # Returns wheather player_1 won
    if player_1 == 'r' and player_2 == 's' or player_1 =='p' and player_2 == 'r' \
    or player_1 == 's' and player_2 == 'p':
        return True

again = 'y'
while again == 'y':
    print('\nNEW GAME:\n')
    roshambo()
    again = input("Wanna play again? Y/N \n").lower()
