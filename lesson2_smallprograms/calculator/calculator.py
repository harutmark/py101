'''
Simple calculator program built as part of Launch School cirriculum
PY 101, Lesson 2, Assignment 11
This is a refactored version of the original calculator built for Assignment 7
'''

def prompt(message):
    '''
    Adds an '==> ' prefix to all terminal outputs
    '''
    print(f"==> {message}")

def invalid_number(number_str):
    '''
    Checks to see if user input is invalid (not float or integer)
    Invalid inputs return True, Valid inputs return False
    Valid = float or integer, Invalid = Not Float or Integer
    '''
    try:
        float(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')

while True:
    prompt("What's the first number?")
    number1 = input('==> ')
    
    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input('==> Please enter an integer or decimal: ')
    
    prompt("What's the second number?")
    number2 = input('==> ')
    
    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
        number2 = input('==> Please enter an integer or decimal: ')
    
    prompt("What operation would you like to perform?")
    operation = input('==> +, -, *, or /?: ')
    
    while operation not in  ["+", "-", "*", "/"]:
        prompt("You must choose +, -, *, or /")
        operation = input('==> ')
    
    match operation:
        case "+":
            OUTPUT = float(number1) + float(number2)
        case "-":
            OUTPUT = float(number1) - float(number2)
        case "*":
            OUTPUT = float(number1) * float(number2)
        case "/":
            if number2 == '0':
                prompt('You can not divide by zero.')
                OUTPUT = None
            else:
                OUTPUT = float(number1) * float(number2)
    
    prompt(f"{number1} {operation} {number2} = {OUTPUT}")

    #Another Calculation?
    prompt('Would you like to perform another calculation? y/n')
    another_calculation = input()
    if another_calculation[0].lower() != 'y':
        break
    else:
        continue