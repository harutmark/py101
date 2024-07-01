# Let the user know they've entered the program

print('Welcome to Calculator!')


# Ask the user for the first number

num1 = float(input('What is your first input?: '))


# Ask the user for the second number

num2 = float(input('What is your second input?: '))


# Ask the user for an operation to perform on the 2 inputs

operation = input('What operation would you like to perform on your inputs?'
                  '\n+ -> Add\n- -> Subtract\n* -> Multiply\n/ -> Divide'
                  '\nOperation: ')


# Perform the operation and print result

if operation == '+':                        # Addition
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
    
elif operation == '-':                      # Subtraction
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')
    
elif operation == '*':                      # Multiplication
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')
    
elif operation == '/':                      # Division
    result = num1 / num2
    print(f'{num1} / {num2} = {result}')
