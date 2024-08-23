"""
A simple terminal game of Rock, Paper, Scissors against a randomized computer.
"""

import random

WINNING_COMBOS = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper',
}

ABBREVIATIONS = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors',
}

def is_valid(user_input):
    """
    Checks if user_input is valid.
    
    Arguments:
        user_input: user's choice of rock, paper, or scissors
    
    Returns:
        bool: whether user input is valid
    
    """
    return user_input[0].lower() in ['r', 'p', 's']

def prompt(message):
    """ Adds '==> ' before any printed message."""
    print(f"==> {message}")

def display_winner(winner):
    """
    Displays user choice and computer choice, then displays winner
    
    Arguments:
        user_choice: the user's choice of either rock, paper, or scissors
        computer_choice: computer's random choice of rock, paper, or scissors
    
    """
    if winner == 'tie':
        prompt("Uh oh, seems like a tie!")
    elif winner == 'user':
        prompt("Congratulations, you win!")
    else:
        prompt("Sorry, you lose.")
  
def determine_winner(user_choice, computer_choice):
    """
    Determines the winner in a round of rock, paper, scissors
    
    Arguments:
        user_choice: the user's choice of either rock, paper, or scissors
        computer_choice: computer's random choice of rock, paper, or scissors
    
    Returns:
        str: 'user', 'computer', or 'tie'

    """
    if user_choice == computer_choice:
        return 'tie'
    elif WINNING_COMBOS[user_choice] == computer_choice:
        return 'user'
    return 'computer'
    
def main():
    user_wins = 0
    computer_wins = 0
    best_of_five = False
    while user_wins < 3 and computer_wins < 3 or best_of_five:
        prompt('Choose one: "rock," "paper," or "scissors"')
        user_choice = input("==> ")
    
        while not is_valid(user_choice):
            prompt("That's not a valid choice")
            prompt('Please choose between "rock", "paper", or "scissors"')
            user_choice = input("==> ")
    
        # Determine user input
        user_choice = ABBREVIATIONS[user_choice.lower()[0]]
    
        # Computer Makes Random Choice
        computer_choice = random.choice(list(WINNING_COMBOS.keys()))
    
        # Determine Winner
        winner = determine_winner(user_choice, computer_choice)
    
        #Display Round Results
        prompt(f"You chose {user_choice}. The computer chose {computer_choice}.")
        display_winner(winner)
    
        if winner == 'computer':
            computer_wins += 1
        elif winner == 'user':
            user_wins += 1
    
        prompt(f'Your wins: {user_wins}')
        prompt(f'Computer wins: {computer_wins}')
    
        if user_wins >= 3:
            prompt("Congratulations, you are the grand winner!")
            prompt("Thanks for playing. Goodbye!")
            break
        if computer_wins >= 3:
            prompt("Unfortunately, the computer has won best of five games.")
            prompt("Thanks for playing. Goodbye!")
            break
    
        if not best_of_five:
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
            
if __name__ == "__main__":
    main()