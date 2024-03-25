#GOOGLE COLAB

import math

def get_integer_input(prompt):
    return int(input(prompt))

def get_positive_float_input(prompt):
    while True:
        value = float(input(prompt))
        if value <= 0:
            print('Please enter a positive number.')
            continue
        return value

def get_float_input(prompt):
    return float(input(prompt))

def calculate_principal_needed(buyp, yrs, livinter):
    incm = buyp * (1 + 0.03) ** yrs
    return int(incm / livinter)

def calculate_future_principal(curprin, inv, perc):
    return curprin * (1 + perc)**3 + ((inv * ((1 + perc)**3-1)) / perc)

buyp = get_integer_input('How much annual buying power do you want when you retire? ')
yrs = get_integer_input('How many years from now do you want to retire? ')
inv = get_integer_input('How much money will you invest each year for the next three years? ')

print('\nAnnual buying power: ${:,}'.format(buyp))
print('Years:', yrs)
print('Annual investment for three years: ${:,}'.format(inv))

incm = buyp * (1 + 0.03) ** yrs
incm = round(incm)
print('\nIncome needed in', yrs, 'years, considering an average of 3% annual inflation, is ${:,}'.format(incm))

totinter = get_positive_float_input("\nHow much interest do you anticipate receiving during retirement? (If you're not sure, say 5) ")
livinter = get_positive_float_input('How much interest do you plan on living on in retirement? (Recommended: 3 less than your total expected interest) ')

totinter /= 100  # Convert to decimal
livinter /= 100  # Convert to decimal

print('\nTotal interest is {:.1%} and living interest is {:.1%}'.format(totinter, livinter))

prin = calculate_principal_needed(buyp, yrs, livinter)
print("Principle needed to retire: ${:,}".format(prin))

curprin = get_integer_input('\nHow much do you already have invested in retirement accounts? ')
taxcurprin = get_float_input("How much of your current retirement investments are NOT in a Roth account? ")
perc = get_positive_float_input("What is your expected average interest rate of your investments? (If you're not sure, put 8) ")
perc /= 100  # Convert to decimal

curprin = calculate_future_principal(curprin, inv, perc)
curprin = round(curprin)
print("Principle in three years: ${:,}".format(curprin))

peeproth_input = get_integer_input("How many people will be opening accounts for your retirement? (If you're not sure, say '1') ")
peeproth = peeproth_input * 7000
yrs = yrs - 3
newinv = (perc * (prin - curprin * (1 + perc) ** yrs)) / ((1 + perc) ** yrs - 1)

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
print('\nThis is your needed annual investment in three years: ${:,}'.format(newinv))
print('This is how many years from now you will need to invest to reach your retirement goals:', yrs, 'years')
ninc = newinv / 0.15
ninc = round(ninc)
print("For your annual investment to be 15% of your income, you'll need an income of ${:,}".format(ninc))

try:
    if taxprin:
        print("This is how much of your principle will be taxable: ${:,}".format(taxprin))
except: pass

rothdec = input("\nWould you like to see how long you will need to invest for if you only invested in Roth accounts? (yes or no) ")
if rothdec == 'yes':
    yrs = yrs - 3
    while newinv > peeproth:
        yrs += 1
        prin = prin * (1 + 0.03)
        newinv = (perc * (prin - curprin * (1 + perc) ** yrs)) / ((1 + perc) ** yrs - 1)
    yrs = yrs + 3
    newinv = round(newinv)
    print('\nThis is your needed annual investment in three years: ${:,}'.format(newinv))
    print('This is how many years from now you will need to invest to reach your retirement goals:', yrs, 'years')
    ninc = newinv / 0.15
    ninc = round(ninc)
    print("For your annual investment to be 15% of your income, you'll need an income of ${:,}".format(ninc))

print('\ntoodles')
