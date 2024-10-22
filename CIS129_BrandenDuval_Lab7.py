# Module 7 Lab: Theater Seating
# Branden Duval
# October 21, 2024
# This program prompts the user for information regarding the seating arrangments in a Theater and returns an accurate final calculation 

# the main function
def main():
    print()

    # declare constants
    COST_A = 20   # cost for seating in section A
    SEATS_A = 300 # number of seats in section A
    COST_B = 15   # cost for seating in section B
    SEATS_B = 500 # number of seats in section B
    COST_C = 10   # cost for seating in section C
    SEATS_C = 200 # number of seats in section C
    COST_D = 0    # added in case of potential update
    SEATS_D = 0   # added in case of potential update
    
    # initialized variables used to calculate the nightly total
    seats_A_taken = 0   # tickets sold in seating section A
    seats_A_revenue = 0 # amount of money generated from the seats sold in seating section A
    seats_B_taken = 0   # tickets sold in seating section B
    seats_B_revenue = 0 # amount of money generated from the seats sold in seating section B
    seats_C_taken = 0   # tickets sold in seating section C 
    seats_C_revenue = 0 # amount of money generated from the seats sold in seating section C
    seats_D_taken = 0   # added in case of potential update
    seats_D_revenue = 0 # added in case of potential update

    # initialized variables used to display the nightly total
    totalRevenue = 0 # adds up the total amount of money generated over all seating sections
    totalSeats = 0   # adds up the total number of seats sold over all seating sections
    
    # welcome message to address the user
    name = input('What is your name? ')
    print(f"Hello, {name}!\nWelcome to the Theater's End of Night sales calculator!")
    print(f'The Theater has a capacity of {SEATS_A + SEATS_B + SEATS_C + SEATS_D} seats and is broken up into different seating sections.')
    print(f'Seating Section A has a capacity of {SEATS_A} with each ticket costing {COST_A}.')
    print(f'Seating Section B has a capacity of {SEATS_B} with each ticket costing {COST_B}.')
    print(f'Seating Section C has a capacity of {SEATS_C} with each ticket costing {COST_C}.')
    # print(f'Seating Section D has a capacity of {SEATS_D} with each ticket costing {COST_D}.')

    # call to inputValues, in case of update: add seats_D_taken to both side of the equation and COST_D to arguments
    seats_A_taken, seats_B_taken, seats_C_taken = inputValues(seats_A_taken, seats_B_taken, seats_C_taken, SEATS_A, SEATS_B, SEATS_C) 

    # call to displayRevenue, in case of of update: add seats_D_revenue before '=', seats_D_taken, and COST_D into the arguments
    seats_A_revenue, seats_B_revenue, seats_C_revenue = displayRevenue(seats_A_taken, seats_B_taken, seats_C_taken, COST_A, COST_B, COST_C)

    # # call to displayTotal, in case of update: add variables seats_D_taken and seats_D_revenue to arguments 
    totalRevenue, totalSeats = displayTotal(seats_A_taken, seats_A_revenue, seats_B_taken, seats_B_revenue, seats_C_taken, seats_C_revenue)

# function used to store the user's seating information as a variable
def inputValues(seats_A_taken, seats_B_taken, seats_C_taken, SEATS_A, SEATS_B, SEATS_C): # add constant SEATS_D and variable seats_D_taken to arguments if updated
    seats_A_taken = int(input(f'Please enter the number of tickets sold for Seating Section A (max {SEATS_A}): '))
    if seats_A_taken < 0 or seats_A_taken > SEATS_A:
        int(input(f'Please enter a valid number of tickets sold for Seating Section A (max {SEATS_A}): '))
    seats_B_taken = int(input(f'Please enter the number of tickets sold for Seating Section B (max {SEATS_B}): '))
    if seats_B_taken < 0 or seats_B_taken > SEATS_B:
        int(input(f'Please enter a valid number of tickets sold for Seating Section B (max {SEATS_B}): '))
    seats_C_taken = int(input(f'Please enter the number of tickets sold for Seating Section C (max {SEATS_C}): '))
    if seats_C_taken < 0 or seats_C_taken > SEATS_C:
        int(input(f'Please enter a valid number of tickets sold for Seating Section C (max {SEATS_C}): '))
    # seats_D_taken = int(input(f'Please enter the number of tickets sold for Seating Section A (max {SEATS_D}): '))
    # if seats_D_taken < 0 or seats_D_taken > SEATS_D:
        # int(input(f'Please enter a valid number of ticekts sold for Seating Section D (max {SEATS_D}): '))
    return(seats_A_taken, seats_B_taken, seats_C_taken) # add variable seats_D_taken into the arguments if updated

# mutates the variables from the last function and returns new variables to be used to calculate the total
def displayRevenue(seats_A_taken, seats_B_taken, seats_C_taken, COST_A, COST_B, COST_C): # add constant COST_D and variable seats_D_taken to arguments if updated
    seats_A_revenue = seats_A_taken * COST_A
    print(f'{seats_A_taken} seats sold in Seating Section A for a total of ${seats_A_revenue}.')
    seats_B_revenue = seats_B_taken * COST_B
    print(f'{seats_B_taken} seats sold in Seating Section B for a total of ${seats_B_revenue}.')
    seats_C_revenue = seats_C_taken * COST_C
    print(f'{seats_C_taken} seats sold in Seating Section C for a total of ${seats_C_revenue}.')
    # seats_D_revenue = seats_D_taken * COST_D
    # print(f'{seats_D_taken} seats sold in Seating Section D for a total of ${seats_D_revenue}')
    return(seats_A_revenue, seats_B_revenue, seats_C_revenue) # add variable seats_D_revenue into arguments if updated

# compiles all prior information to display to the user the theaters total at the end of the night
def displayTotal(seats_A_taken, seats_A_revenue, seats_B_taken, seats_B_revenue, seats_C_taken, seats_C_revenue): # add variables seats_D_taken and seats_D_revenue if updated
    totalSeats = seats_A_taken + seats_B_taken + seats_C_taken # + seats_D_taken if updated
    totalRevenue = seats_A_revenue + seats_B_revenue + seats_C_revenue # + seats_D_revenue if updated
    print(f'{totalSeats} seats sold in all sections for a total revenue of ${totalRevenue} for the night.')
    return(totalRevenue, totalSeats)

# calls main
if __name__ == '__main__':
    main()