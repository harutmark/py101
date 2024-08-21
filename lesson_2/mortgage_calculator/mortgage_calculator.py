'''
Use this program to determing monthly payments and total interest on loans,
including mortgages and car loans.
'''

def prompt(message):
    '''
    Adds "==> " before every printed terminal message
    '''
    print(f'==> {message}')
    
def invalid_number(number_str):
    '''
    if input is unable to convert to float, returns True
    if input is able to convert to float, returns False
    '''
    try:
        float(number_str)
    except ValueError:
        return True
    return False

#Intro
prompt("Hello, welcome to the mortgage calculator!")
prompt("Use this program to calculate monthly payments on loans.")

while True:
    #Collect Info
    prompt("What is the total loan amount?")
    loan_amount = input('==> $')
    while invalid_number(loan_amount):
        print("==>")
        prompt("Hmm, that doesn't seem like a valid input.")
        prompt("Please, enter an integer or decimal value, avoiding commas.")
        prompt("What is the total loan amount?")
        loan_amount = input('==> $')
    loan_amount = float(loan_amount)
    
    prompt('What is your annual percentage rate (APR) as a percent?')
    APR = input('==> APR %: ')
    while invalid_number(APR):
        print("==>")
        prompt("Hmm, that doesn't seem like a valid input.")
        prompt("Please enter an integer or decimal value.")
        prompt("Please avoid commas (,) or the percent (%) symbol.")
        prompt("What is your annual percentage rate (APR) as a percent?")
        APR = input('==> APR %: ')
    APR = float(APR)
    APR = APR / 100     #Convert to decimal format
    monthly_rate = APR / 12     #Convert to Monthly
    
    prompt('What is the duration of your loan in months? (2 years = 24 months)')
    duration_months = input('==> Months: ')
    while invalid_number(duration_months):
        print("==>")
        prompt("Invalid input, please enter an integer")
        prompt("What's the duration of your loan in months? (2yrs = 24months)")
        duration_months = input('==> Months: ')
    duration_months = int(duration_months)
    
    #Make Calculations
    monthly_payment = loan_amount * (monthly_rate / (1 - (1 + monthly_rate) ** (-duration_months)))
    total_payment = monthly_payment * duration_months
    total_interest = total_payment - loan_amount
    
    #Display Results
    print('==>')
    prompt('Thank you for your information. Here are your results:')
    prompt(f'Monthly Payment: ${monthly_payment:,.2f}')
    prompt(f'Total of {duration_months} monthly payments: ${total_payment:,.2f}')
    prompt(f'Total Interest: ${total_interest:,.2f}')
    
    #Another Calculation
    prompt("Would you like to perform another calculation? y/n")
    again = input().lower()
    if again.startswith('y'):
        continue
    if again.startswith('n'):
        prompt("Goodbye")
        break
    else:
        prompt("Unrecognized input, closing mortgage calculator.")
        prompt("Please restart program to make another calculation,")
        prompt("Goodbye")
        break
