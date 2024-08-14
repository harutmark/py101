'''
A simple terminal game of Rock, Paper, Scissors against a randomized computer.
'''

import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    '''
    Adds "==> " before any printed message
    '''
    print(f"==> {message}")
    
def display_winner(user_choice, computer_choice):
    '''
    Displays user choice and computer choice, then determines winner
    '''
    prompt(f"You chose {user_choice}. The computer chose {computer_choice}.")
    
    if ((user_choice == 'rock' and computer_choice == 'scissors') or #User Wins
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')):
        prompt("Congratulations, you win!")
    elif ((user_choice == 'rock' and computer_choice == 'paper') or  #CPU wins
        (user_choice == 'paper' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'rock')):
        prompt("Sorry, you lose.")
    elif (user_choice == computer_choice):                           #Tie
        prompt("Uh oh, seems like a tie!")
    else:
        prompt("Woah! Seems like something went wrong.")

   
while True:
    #User Makes Selection 
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    user_choice = input("==> ")
    
    while user_choice not in VALID_CHOICES:     #Ensure selection is valid
        prompt("That's not a valid choice")
        prompt('Please choose between "rock", "paper", or "scissors"')
        user_choice = input("==> ")
    
    computer_choice = random.choice(VALID_CHOICES)
    
    display_winner(user_choice, computer_choice)
    
    prompt("Would you like to play again? (y/n)")
    again = input("==> ")
    again = again.lower()
    if again.startswith('y'):
        continue
    elif again.startswith('n'):
        prompt('Okay, thanks for playing. Goodbye!')
        break
    else:
        prompt("Invalid input. Closing Program.")
        prompt("Please relaunch program if you'd like to play again.")
        prompt("Thank for playing! Goodbye.")
        break
