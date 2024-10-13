# Module 6: Hotdog Cookout Lab
# Branden Duval
# October 13, 2024
# This program calculates the number of hot dogs and buns needed for a cookout 

# Program start
def getTotalHotDogs():
    # asks the user for the specifics of the cookout
    attendees = int(input('How many attendees will be arriving? '))
    hotDogs = int(input('How many hot dogs will be given to each attendee? '))
    
    # calculates how many hot dogs are needed for the cookout
    total = attendees * hotDogs
    return total

def showResults(total):
    # states the number of dogs and buns to a package
    DOGS = 10
    BUNS = 8
    
    # calculates the hot dogs and buns left as well as the minimum amount of packages needed for both
    dogsLeft = (DOGS - total % DOGS) % DOGS 
    minDogs = ((total // DOGS) + (0 **(0 ** dogsLeft))) # rounded up because you can't buy a portion of a package of hot dogs 
    bunsLeft = (BUNS - total % BUNS) % BUNS
    minBuns = ((total // BUNS) +  (0 **(0 ** bunsLeft))) # rounded up because you can't buy a portion of a package of buns
   
   # displays the results 
    print(f'Minimum packages of hot dogs needed: {minDogs}')
    print(f'Minimum packages of hot dog buns needed: {minBuns}')
    print(f'Hot dogs remaining: {dogsLeft}')
    print(f'Hot dog buns remaining: {bunsLeft}')
    return total

# main
totalHotDogs = getTotalHotDogs()
showResults(totalHotDogs)