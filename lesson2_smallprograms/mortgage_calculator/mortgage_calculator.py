def prompt(message):
    print(f"==> {message}")

#Intro
prompt("Hello, welcome to the mortgage calculator!")
prompt("Use this program to calculate monthly payments on loans.")

#Collect Info
prompt("What is the total loan amount?")
loan_amount = float(input('--> $ '))

prompt('What is your annual percentage rate (APR) as a percent?')
APR = float(input('--> APR %: '))
APR = APR / 100     #Convert to decimal format
monthly_rate = APR / 12

prompt('What is the duration of your loan in months? (2 years = 24 months)')
duration_months = int(input('--> Months: '))

#Make Calculations
monthly_payment = loan_amount * (monthly_rate / (1 - (1 + monthly_rate) ** (-duration_months)))
total_payment = monthly_payment * duration_months
total_interest = total_payment - loan_amount

#prompt Result
print('==>')
prompt('Thank you for your information. Here are your results:')
prompt(f'Monthly Payment: ${monthly_payment:,.2f}')
prompt(f'Total of {duration_months} monthly payments: ${total_payment:,.2f}')
prompt(f'Total Interest: ${total_interest:,.2f}')