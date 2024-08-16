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

user_wins = 0
computer_wins = 0
best_of_five = False
while user_wins < 3 or computer_wins < 3 or best_of_five:
    prompt(f'Choose one: "rock," "paper," or "scissors"')
    user_choice = input("==> ")
    
    while is_valid(user_choice) == False:
        prompt("That's not a valid choice")
        prompt('Please choose between "rock", "paper", or "scissors"')
        user_choice = input("==> ")
        
    # Determine user input
    if user_choice.lower().startswith('r'):
        user_choice = 'rock'
    elif user_choice.lower().startswith('p'):
        user_choice = 'paper'
    elif user_choice.lower().startswith('s'):
        user_choice = 'scissors'
    
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    #Determine Winner for win count
    if ((user_choice == 'rock' and computer_choice == 'scissors') or  #User Wins
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')):
        winner = 'user'
    elif ((user_choice == 'rock' and computer_choice == 'paper') or   #CPU wins
        (user_choice == 'paper' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'rock')):
        winner = 'computer'
    elif (user_choice == computer_choice):                            # Tie
        winner = 'tie'
    
    display_winner(user_choice, computer_choice)
    
    if winner == 'computer':
        computer_wins += 1
    elif winner == 'user':
        user_wins += 1
    
    prompt(f'Your wins: {user_wins}')
    prompt(f'Computer wins: {computer_wins}')
    
    if best_of_five == True and user_wins >= 3:
        prompt("Congratulations, you are the grand winner!")
        prompt("Thanks for playing. Goodbye!")
        break
    elif best_of_five == True and computer_wins >= 3:
        prompt("Unfortunately, the computer has won best of five games.")
        prompt("Thanks for playing. Goodbye!")
        break
    
    if best_of_five == False:
        prompt("Would you like to play best of five? (y/n)")
        best_of_five = input("==> ")
        best_of_five = best_of_five.lower()
        if best_of_five.startswith('y'):
            best_of_five = True
        elif best_of_five.startswith('n'):
            prompt('Okay, thanks for playing. Goodbye!')
            break
        else:
            prompt("Invalid input. Closing Program.")
            prompt("Please relaunch program if you'd like to play again.")
            prompt("Thank for playing! Goodbye.")
            break
