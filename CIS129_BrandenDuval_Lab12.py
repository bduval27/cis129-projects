# Module 12: Lab 12
# Branden Duval
# December 1, 2024
# This program creates a class called 'Pet,' then asks the user for the specifics of their pet, and finally displays what the user had input

# the class initialization
class Pet:
    def __init__(self, name = 'Null', species = 'Null', age = -1): # changed 'type' to 'species' to not override Python function type()
        self._name = name       # private variable for the name of the pet
        self._species = species # private variable for the species of the pet
        self._age = age         # private variable for the age of the pet

    # name getter
    @property
    def name(self):
        return self._name
    
    # name setter
    @name.setter
    def name(self, name):
        if type(name) is not str:  
            raise TypeError # sanitizes input by looking for strings only
        elif len(name.strip()) < 1: 
            raise ValueError # sanitizes input by denying name lengths smaller than 1 character
        
        self._name = name
    
    # species getter
    @property
    def species(self):
        return self._species
    
    # species setter
    @species.setter
    def species(self, species):
        if type(species) is not str: 
            raise TypeError # sanitizes input by looking for strings only
        elif len(species.strip()) < 1:
            raise ValueError # sanitizes input by denying species name lengths smaller than 1 character
        
        self._species = species
    
    # age getter
    @property
    def age(self):
        return self._age
    
    # age setter
    @age.setter
    def age(self, age):
        if type(age) is not int: 
            raise TypeError # sanitizes input by denying anything other than an integer
        elif age < 0 or age > 120: # oldest recorded bird is Cocky Bennett who lived 120 years old
            raise ValueError
        
        self._age = age

# declare 
animal = Pet()

# storing the pet name based off of user input
inputName = input('Please enter Pet name: ')
animal.name = inputName

# storing the pet species based off of user input
inputSpecies = input('Please enter species of Pet: ')
animal.species = inputSpecies

# storing the pet age based off of user input
inputAge = int(input('Please enter Pet age: '))
animal.age = inputAge

# displays the results
print('The pet name is :',animal.name)
print('The pet type is :',animal.species)
print('The pet age is :',animal.age)