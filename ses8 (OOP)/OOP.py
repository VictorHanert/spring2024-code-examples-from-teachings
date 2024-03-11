class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_info(self):
        return (self.title, self.author)

# Define a Simple Class: Create a class named Animal. Add two instance attributes: 
# name and species, and initialize them through the constructor (__init__ method).
    
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def get_info(self):
        return f'name: {self.name}, species: {self.species}'

dog = Animal('Pluto', 'Labrador')

