# Module 11: Lab 11: Exercise 9.2
# Branden Duval
# November 18, 2024
# This program reads the information from the created 'grades.txt' file and displays the total, count, and average

# variables to calculate the average
counter = 0     # initialized counter
totalGrades = 0 # initialized the class grade total

with open('grades.txt', 'r') as grades:
    print(f'{"ID":<4}{"Name":<7}{"Grade"}')
    for record in grades:
        record = record.strip() # strips the new lines (\n) from the record
        if record: # if a record is to be read
            student_ID, name, grade = record.split() # splits the record into variables 
            print(f'{student_ID:<4}{name:<7}{grade}') # displays the data from the text file
            counter += 1 # counts the count
            totalGrades += float(grade) # total grade, casted grade to float

# displays the total, count, and average            
print(f'Class grade total: {totalGrades:.2f}')
print(f'Total entries: {counter}')
print(f'Class grade average: {totalGrades / counter}')
