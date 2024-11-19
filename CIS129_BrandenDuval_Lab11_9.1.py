# Module 11 Lab 11: Exercise 9.1 
# Branden Duval
# November 18, 2024
# This program enables a user to store any number of grades into a plain text file

# the program
with open('grades.txt', mode = 'w') as grades: # opens a file to write
    while True: # while loop for the sentinel value
        while True: # ugly second while loop for sanitization
            try:
                studentID = int(input("Please enter student ID or '-1' to quit: "))
                break
            except ValueError:
                print('Please enter a valid numeric student ID.')
        if studentID == -1: # the sentinel value
            grades.write('\n')
            break # breaks if sentinel value is entered
        lastName = input("Please enter student's last name: ") # not using a try/except clause in an attempt to be inclusive towards those with numbers as last names
        while True: # third loop to sanitize grade values
            grade = float(input('Enter student grade: ')) # unsure of whether a number or letter was wanted, opted for a number to format
            if grade < 0 or grade > 100:  
                print('Invalid grade')
            else:
                break
        grades.write(f'{studentID} {lastName} {grade:.2f}\n') # writes the plain text file