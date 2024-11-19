# Module 11: Lab 11: Exercise 9.3
# Branden Duval
# November 18, 2024
# This program lets a user create a csv file for a class' grades

# imports the csv module
import csv

# the main program
with open ('grades.csv', mode = 'w', newline = '') as grades:
    writer = csv.writer(grades)
    while True: # first while loop for the sentinel value of 'q'
        while True: # ugly second while loop to sanitize first name inputs
            firstName = input("Please enter student's first name or 'q' to quit: ")
            if len(firstName.strip()) < 1: # prompts the user for a new input if the entered input is spaces or less than 1 character
                print("Please enter the student's first name (at least 1 character long).") 
            else:
                break # breaking from inner while loop if name is valid
        if firstName == 'q': # the sentinel value
            break # breaks if sentinel value is input
        while True: # third ugly while loop to sanitize last name inputs
            lastName = input("Please enter student's last name: ")
            if len(lastName.strip()) < 1: # prompts the user for a new input if the entered input is spaces or less than 1 character
                print("Please enter student's last name (at least 1 character long).")
            else:
                break # breaking from inner while loop if name is valid
        exam1Grade = int(input("Please enter student's grade for exam 1: "))
        if exam1Grade < 0 or exam1Grade > 100: # grades can not be -1 or 101
            print('Please enter a valid grade.') # tells the user so
        exam2Grade = int(input("Please enter student's grade for exam 2: "))
        if exam2Grade < 0 or exam2Grade > 100: # grades can not be -1 or 101
            print('Please enter a valid grade.') # tells the user so
        exam3Grade = int(input("Please enter student's grade for exam 3: "))
        if exam3Grade < 0 or exam3Grade > 100: # grades can not be -1 or 101
            print('Please enter a valid grade.') # you should get the idea by now
        writer.writerow([firstName, lastName, exam1Grade, exam2Grade, exam3Grade]) # writes the csv file