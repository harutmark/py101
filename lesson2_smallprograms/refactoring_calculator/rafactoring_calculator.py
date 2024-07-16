def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')

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
        output = float(number1) + float(number2)
    case "-":
        output = float(number1) - float(number2)
    case "*":
        output = float(number1) * float(number2)
    case "/":
        if number2 == '0':
            prompt('You can not divide by zero.')
            output = None
        else:
            output = float(number1) * float(number2)

prompt(f"{number1} {operation} {number2} = {output}")