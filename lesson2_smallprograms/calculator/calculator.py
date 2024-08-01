'''
Simple calculator program built as part of Launch School cirriculum
PY 101, Lesson 2
'''

import json
# Load the messages from the JSON file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)
# Now 'MESSAGES' contains the loaded messages as a Python dictionary

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

prompt(MESSAGES['welcome'])

while True:
    prompt(MESSAGES["request_first_number"])
    number1 = input('==> ')
    
    while invalid_number(number1):
        prompt(MESSAGES["request_valid_number"])
        number1 = input('==> ')
    
    prompt(MESSAGES["request_second_number"])
    number2 = input('==> ')
    
    while invalid_number(number2):
        prompt(MESSAGES["request_valid_number"])
        number2 = input('==> ')
    
    prompt(MESSAGES["request_operation"])
    prompt(MESSAGES["operation_options"])
    operation = input('==> ')
    
    while operation not in  ["+", "-", "*", "/"]:
        prompt(MESSAGES["operation_options_2"])
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
                prompt(MESSAGES["zero_division_warning"])
                OUTPUT = None
            else:
                OUTPUT = float(number1) / float(number2)
    
    prompt(f"{number1} {operation} {number2} = {OUTPUT}\n")

    #Another Calculation?
    prompt(MESSAGES["another_calculation"])
    prompt(MESSAGES["yes_or_no"])
    another_calculation = input('==> ')
    if another_calculation[0].lower() != 'y':
        break
    else:
        continue