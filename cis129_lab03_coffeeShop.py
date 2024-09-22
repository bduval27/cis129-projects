'''
Module 3 Lab

Design a program that asks a user for an order and then prints a receipt.

Program does the following
    -Asks the user for an order
    -Calculates the number of items ordered
    -Multiplies the number of items by the cost of the item
    -Multiplies again for the tax 
    -Adds tax to the total
    -Gives the user a detailed list of items and complete total
'''

# asks for customer order
print('***********************************')
print('My Coffee and Muffin Shop')
coffee_bought = int(input('Number of coffees bought?\n'))
muffin_bought = int(input('Number of muffins bought?\n'))
print('***********************************')

# determines the price of each item
coffee_price = 5.00
muffin_price = 4.00

# determines the price of items bought pre-tax
total = (coffee_bought * coffee_price + muffin_bought * muffin_price)

# determines price of items post-tax
tax_total = ((coffee_bought * coffee_price + muffin_bought * muffin_price) * 0.06)

print('\n')

# reviews customer total
print('***********************************')
print('My Coffee and Muffin Shop Receipt')

# reviews order of coffee with price
print(coffee_bought,\
       'Coffee at $5 each: $',\
              format(coffee_bought * coffee_price, ".2f")) # string formatting borrowed from user Armali @ https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points

# reviews order of muffins with price
print(muffin_bought,\
     'Muffins at $4 each: $',\
        format(muffin_bought * muffin_price, ".2f"))

# reviews tax
print('6% tax: $', format(tax_total, ".2f"))

# gives complete total for transaction
print('---------')
print('Total: $',\
    format(total + tax_total, ".2f"))
print('***********************************')