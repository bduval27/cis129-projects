# Lab 5: The Bottle Return Program
# Branden Duval
# October 6, 2024
# This program calculates the total number of bottles and the total payout from user input and can be repeated

# Declare local variables
totalBottles = 0  # stores accumulated bottles
counter = 0       # controls the loop
todayBottles = 0  # stores the number of bottles returned in a day
totalPayout = 0   # stores the calculated value of totalBottles times .10
keepGoing = "y"   # will be used to run the program again
NBR_OF_DAYS = 7   # specifies the number of days

# Loop to run program again
while keepGoing == "y":
    # prompts user for bottles over the course of a week and calculates the total payout
    while counter < NBR_OF_DAYS: 
        todayBottles = int(input(f'Enter number of bottles returned for day #{counter + 1}: '))
        totalBottles += todayBottles
        counter += 1 
    PAYOUT_PER_BOTTLE = .10
    totalPayout = PAYOUT_PER_BOTTLE * totalBottles
    
    # prints the users total and then resets the values of variables
    print('\nNumber of bottles collected: ', totalBottles)
    print(f'The total payout is: {totalPayout:.2f} \n')
    totalBottles = 0 # resets number of bottles to 0
    totalPayout = 0 # resets to 0 for multiple runs
    counter = 0 # resets counter between weeks
    
    print("Do you want to enter another week's worth of data?")
    keepGoing = input(f'(Enter y or n): ') # loops program if user inputs y
    print()