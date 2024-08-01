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
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]

prompt(messages('welcome'))

while True:
    prompt(messages("request_first_number"))
    number1 = input('==> ')
    
    while invalid_number(number1):
        prompt(messages("request_valid_number"))
        number1 = input('==> ')
    
    prompt(messages("request_second_number"))
    number2 = input('==> ')
    
    while invalid_number(number2):
        prompt(messages("request_valid_number"))
        number2 = input('==> ')
    
    prompt(messages("request_operation"))
    prompt(messages("operation_options"))
    operation = input('==> ')
    
    while operation not in  ["+", "-", "*", "/"]:
        prompt(messages("operation_options_2"))
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
                prompt(messages("zero_division_warning"))
                OUTPUT = None
            else:
                OUTPUT = float(number1) / float(number2)
    
    prompt(f"{number1} {operation} {number2} = {OUTPUT}\n")

    #Another Calculation?
    prompt(messages("another_calculation"))
    prompt(messages("yes_or_no"))
    another_calculation = input('==> ')
    if another_calculation[0].lower() != 'y':
        break
