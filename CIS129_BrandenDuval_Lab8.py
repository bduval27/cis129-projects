# Module 8: Lab 8
# Branden Duval
# October 25, 2024
# This program tests for palindromes given a word from the user

# function for testing palindromes
def is_palindrome():
    breaker = True # determines validity of palindrome without printing whether or not every character is true or false
    user_input = input('Please enter a word: ').lower() # prompts the user for a word and then converts it to lowercase
    user_input = filter(str.isalnum, user_input) # filters out spaces and punctuation from the word given
    user_input = "".join(user_input) # converting the previous line into a string
    user_input2 = []  
    user_input2 += user_input # splits the users input
    for i in range(len(user_input)): # keeps track of indices
        if user_input2.pop() != user_input[i]: # compares the strings
            breaker = False # stops the program
    return breaker

# calls function
call = is_palindrome()
print(call) # prints result