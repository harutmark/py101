'''
A simple terminal game of Rock, Paper, Scissors against a randomized computer.
'''

import random

def is_valid(user_choice):
    if user_choice.lower().startswith('r'):
        return True
    elif user_choice.lower().startswith('p'):
        return True
    elif user_choice.lower().startswith('s'):
        return True
    else:
        return False

def prompt(message):
    '''
    Adds "==> " before any printed message
    '''
    print(f"==> {message}")
    
def display_winner(user_choice, computer_choice):
    '''
    Displays user and computer choice, then displays winner
    '''
    prompt(f"You chose {user_choice}. The computer chose {computer_choice}.")
    
    if ((user_choice == 'rock' and computer_choice == 'scissors') or  #User Wins
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')):
        prompt("Congratulations, you win!")
    elif ((user_choice == 'rock' and computer_choice == 'paper') or   #CPU wins
        (user_choice == 'paper' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'rock')):
        prompt("Sorry, you lose.")
    elif (user_choice == computer_choice):                            # Tie
        prompt("Uh oh, seems like a tie!")
    else:                                                             # Error
        prompt("Woah! Seems like something went wrong.")

while True:
    prompt(f'Choose one: "rock," "paper," or "scissors"')
    user_choice = input("==> ")
    
    while is_valid(user_choice) == False:
        prompt("That's not a valid choice")
        prompt('Please choose between "rock", "paper", or "scissors"')
        user_choice = input("==> ")
        
    if user_choice.lower().startswith('r'):
        user_choice = 'rock'
    elif user_choice.lower().startswith('p'):
        user_choice = 'paper'
    elif user_choice.lower().startswith('s'):
        user_choice = 'scissors'
    
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
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
