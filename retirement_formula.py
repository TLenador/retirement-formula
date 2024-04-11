import math

# Function for getting integer input
def get_integer_input(prompt):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            return value
        except ValueError:
            print('Please enter a valid number.')

# Function for getting float input
def get_positive_float_input(prompt):
    while True:
        value = input(prompt)
        try:
            value = float(value)
            if value <= 0:
                print('Please enter a positive number.')
                continue
            return value
        except ValueError:
            print('Please enter a valid number.')

def get_float_input(prompt):
    while True:
        value = input(prompt)
        try:
            value = float(value)
            return value
        except ValueError:
            print('Please enter a valid number.')

def calculate_principal_needed(buyp, yrs, livinter):
    incm = buyp * (1 + 0.03) ** yrs
    return int(incm / livinter)

def calculate_future_principal(curprin, inv, perc):
    return curprin * (1 + perc)**3 + ((inv * ((1 + perc)**3-1)) / perc)

buyp = get_integer_input('If you retired today, how much money do you think you would need each year? ')
yrs = get_integer_input('How many years from now do you want to retire? ')
inv = get_integer_input('How much money will you invest each year for the next three years? ')

print('\nAnnual buying power: ${:,}'.format(buyp))
print('Years:', yrs)
print('Annual investment for three years: ${:,}'.format(inv))

# Compound frequency
incm = buyp * (1 + 0.03) ** yrs
incm = round(incm)
print('\nIncome needed in', yrs, 'years, considering an average annual inflation rate of 3%: ${:,}'.format(incm))

# Custom percentage/how much to live on
livinter = get_positive_float_input('\nHow much interest do you plan on living on in retirement? (Recommended: 4 [based on the "4% Rule"])')

livinter /= 100  # Convert to decimal

print('\nThe amount of interest you will live on is {:.1%}'.format(livinter))

# Principle needed to net the needed income using the living interest rate (livinter)
prin = calculate_principal_needed(buyp, yrs, livinter)
print("Principle needed to retire: ${:,}".format(prin))

# Only Roth IRAs? All investments?
curprin = get_integer_input('\nHow much do you already have invested in retirement accounts? ')
taxcurprin = get_float_input("How much of your current retirement investments are NOT in a Roth account? ")
perc = get_positive_float_input("What average interest rate do you expect to receive on your investments? (If you're not sure, put 8) ")
perc /= 100  # Convert to decimal

# This figures out the curprin after 3 years of investments, assuming an average interest rate of perc
curprin = calculate_future_principal(curprin, inv, perc)
curprin = round(curprin)
print("Principle in three years: ${:,}".format(curprin))

# peeproth is the max someone can put into a Roth IRA (7000, 14000, etc.)
peeproth_input = get_integer_input("How many people will be opening accounts for your retirement? (If you're not sure, say '1') ")
peeproth = peeproth_input * 7000
yrs = yrs - 3
newinv = (perc * (prin - curprin * (1 + perc) ** yrs)) / ((1 + perc) ** yrs - 1)

# Figure out all of the taxable income. Initial investment, 3 years of investing, and 30 years from now
taxcurprin = (taxcurprin * (1 + perc)**3)
if inv > peeproth:
    taxinv = inv - peeproth
    taxcurprin = taxcurprin + ((taxinv * ((1 + perc)**3-1)) / perc)
if newinv > peeproth:
    taxinv = newinv - peeproth
    taxprin = (taxcurprin * (1 + perc)**yrs) + ((taxinv * ((1 + perc)**yrs-1)) / perc)
    taxprin = round(taxprin)

yrs = yrs + 3
newinv = round(newinv)
print("\nYou will need to invest for", yrs, "years to reach your retirement goal.")
print('Starting in three years, this is how much you will need to invest each year to reach your goal: ${:,}'.format(newinv))
print("This will get you to your needed principle of ${:,}".format(prin), "for you to retire.")
ninc = newinv / 0.15
ninc = round(ninc)
print("For your annual investment to be 15% of your income, in three years you'll need an income of ${:,}".format(ninc))

try:
    if taxprin:
        print("Upon retirement, this is how much of your principle will be taxable: ${:,}".format(taxprin))
except: pass

rothdec = input("\nWould you like to see how long you will need to invest if you only invested in Roth accounts? (yes or no) ")
if rothdec == 'yes':
    yrs = yrs - 3
    while newinv > peeproth:
        yrs += 1
        prin = prin * (1 + 0.03)
        newinv = (perc * (prin - curprin * (1 + perc) ** yrs)) / ((1 + perc) ** yrs - 1)
    yrs = yrs + 3
    newinv = round(newinv)
    print("\nYou will need to invest for", yrs, "years to reach your retirement goal.")
    print('Starting in three years, this is how much you will need to invest each year to reach your goal: ${:,}'.format(newinv))
    ninc = newinv / 0.15
    ninc = round(ninc)
    print("For your annual investment to be 15% of your income, in three years you'll need an income of ${:,}".format(ninc))

print('\nToodles')