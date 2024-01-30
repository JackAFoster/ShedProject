'''
This program is shed.py - Individually created by Jack Foster - Last edited 2/26/2023
This program allows you to select the type, style, and siding material, and number of windows for the creation of a shed
Once selected, the program will give you a complete price breakdown and optionally calculate 1-2 year financing options
'''

# Define shed prices
shed_prices = {
    ('G', 'S', 'D'): 5500,
    ('G', 'S', 'V'): 6000,
    ('G', 'S', 'C'): 6700,
    ('G', 'M', 'D'): 7200,
    ('G', 'M', 'V'): 7700,
    ('G', 'M', 'C'): 8400,
    ('G', 'L', 'D'): 8000,
    ('G', 'L', 'V'): 8500,
    ('G', 'L', 'C'): 0,
    ('C', 'S', 'D'): 5800,
    ('C', 'S', 'V'): 6300,
    ('C', 'S', 'C'): 7000,
    ('C', 'M', 'D'): 7500,
    ('C', 'M', 'V'): 8000,
    ('C', 'M', 'C'): 8700,
    ('C', 'L', 'D'): 0,
    ('C', 'L', 'V'): 8800,
    ('C', 'L', 'C'): 0, }

# Define variables
WINDOW_PRICE = 120
TAX_RATE = 0.0625
num_windows = 0
month = 1
interest_rate = float(0.005)
price = 0
total_interest = 0
total_principal = 0
total_payments = 0


# Ask user to determine what shed they are getting and repeat if the answer is invalid
while price == 0:
    style = input("Choose shed style ([G]ambrel or [C]ottage): ").upper()
    if style == "G" or style == "C":
        size = input("Choose shed size ([S]mall, [M]edium, or [L]arge): ").upper()
        if size == "S" or size == "M" or size == "L":
            siding = input("Choose shed siding material ([D]uratemp, [V]inyl, or [C]edar): ").upper()
            if siding == "D" or siding == "V" or siding == "C":
                price = shed_prices[(style, size, siding)]
                if price == 0:
                    print("Invalid input of style, size, and siding. Note: Large Cedar sheds as well as Large Victorian Duratemp sheds are unavailiable")
            else:
                print("Invalid input of siding.")
        else:
            print("Invalid input of size")
    else:
        print("Invalid input of style")

if size in ["M", "L"]:
    num_windows = int(input("How many additional windows do you want? "))

WINDOW_PRICE = WINDOW_PRICE * num_windows

# find total tax owed on shed
tax = price * TAX_RATE

# print order summary
print("="*8+"Order Summary"+"="*8)
print("Shed Style: " + style)
print("Size: \t\t" + size)
print("Siding: \t" + siding)
print("")

# print cost breakdown and total costs, formatted to dollar values, formatted to be evenly spaced
print("Shed: \t\t\t",  '$' + format(price, ',.2f'))

# if windows are purchased, add this to the final cost and print window cost in the price breakdown
if num_windows > 0:
    print("Windows (" + str(num_windows) + "): \t", '$' + format(WINDOW_PRICE, ',.2f').rjust(8))
subtotal = price + WINDOW_PRICE

# continue with cost breakdown
print("Subtotal: \t\t", '$' + format(subtotal, ',.2f').rjust(8))
print("Tax:\t\t\t", '$' + format(tax, ',.2f').rjust(8))
total_price = float(price + tax + WINDOW_PRICE)
print("-"*30)
print("Total: \t\t\t", '$' + format(total_price, ',.2f'))
print("")

# This while loop asks for a payment option and has invalid input catches
option = False
while not option:
    period = input("Please choose your payment option ([F]ull, [O]ne-year, [T]wo-year):\n").upper()
    if period == "F":
        print("Thank you for your payment!")
        option = True
        break
    if period == "O":
        period = float(1)
        option = True
        break
    if period == "T":
        period = float(2)
        option = True
        break
    else:
        print("You've entered an incorrect payment option")


# Function for amortization, M = monthly payment
def calculate_monthly_payment(principal, interest_rate, years):
    # Convert years to months
    n = years * 12
    r = interest_rate
    # Calculate monthly payment amount
    M = principal * r * (1 + r)**n / ((1 + r)**n - 1)
    # Return monthly payment
    return M

# calling function to calc monthly payment
if period != "F":
    amortization_amount = calculate_monthly_payment(total_price, interest_rate, period)
    balance = total_price
    print("Your Monthly Payment Schedule")
    print("-"*72)
    print("Month \t Monthly Payment \t Interest \t Principal \t Remaining Balance")
    # Printing and formatting the payments, the interest, the principal paid, and the remaining balance/month
    while month <= (period*12):
        interest = balance * interest_rate
        balance = interest + balance
        principal = amortization_amount - interest
        balance = balance - amortization_amount
        total_interest = interest + total_interest
        total_principal = principal + total_principal
        total_payments = total_payments + amortization_amount
        print(
            str(month).rjust(3),
            '\t\t$' + format(amortization_amount, ',.2f').rjust(5),
            '\t\t  $' + format(interest, ',.2f').rjust(5),
            '\t\t$' + format(principal, ',.2f').rjust(5),
            '\t\t$' + format(balance, ',.2f').rjust(8))

        month += 1
    # Print final aggregated values
    print("-"*72)
    print("Total:", '\t\t$' + format(total_payments, ',.2f').rjust(5), '\t\t  $' + format(total_interest, ',.2f').rjust(5),'\t\t$' + format(total_principal, ',.2f').rjust(5))
