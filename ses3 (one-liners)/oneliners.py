# Opg 1 "Alphabet List Comprehensions"
# Create a list of capital letters in the english alphabet
capital_letters = [chr(letter) for letter in range(ord('A'),ord('Z')+1)]

print(capital_letters)
# Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
capital_letters = [chr(letter) for letter in range(65, 91) if letter not in (70, 75, 80, 85)]

# Create a list of capital letter from from the english aplhabet, but exclude every second between F & O
capital_letters = [chr(letter) for letter in range(65, 91) if letter not in (70, 86, 2)]


# Opg 2 "Clothes List Comprehension"
# From 2 lists, using a list comprehension, create a list containing:
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

list = [(color, size) for color in colors for size in sizes]
print(list)
# If the tuple pair is in the following list, it should not be added to the comprehension generated list.
soled_out = [('Black', 'm'), ('White', 's')]

list = [(color, size) for color in colors for size in sizes if (color, size) not in soled_out]
print(list)

# Opg 3 "list Comprehension exercises"
# Create a list of even numbers from 0 to 20.
even_numbers = [number for number in range(0, 21)][::2]
even_numbers = [number for number in range(0, 21) if number % 2 == 0]
print(even_numbers)
# Create a list of squares of numbers from 1 to 10.
square_numbers = [square_number**2 for square_number in range(1,11)]
square_numbers = [square_number*square_number for square_number in range(1,11)]
print(square_numbers)

# Create a list of all the vowels in a given string.
String = 'Heysa jeg er fantastisk cool, og jeg elsker banan.'
vowels = [vowel for vowel in String if vowel.lower() in 'aeiouyæøå']
print(vowels)

# Create a list of common elements in two given lists. (could this be done with the use of another datastructure?)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = set(list1).intersection(set(list2))
print('Common elements:', common_elements)


# Create a list of words from a given string that have more than 4 and less than 8 letters.
list = [word for word in String.split() if 4<len(word)<8]
print(list)

# Opg 4 "flatten a list"
list_of_lists = [
    [1, 2, 3],
    [4, 5],
    [6],
    [7, 8, 9],
]
flat_list = sum(list_of_lists, [])
flat_list = [item for sublist in list_of_lists for item in sublist]
print(flat_list)

# Opg 5 "Sort a Text"
# Create a function that takes a string as a parameter and returns a list.
# The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.
def sort_something(string):
    for i in ['a', 'e', 'i', 'o', 'u', 'y', ' ']:
        string = string.lower().replace(i,'')
    
    return sorted(string)


print(sort_something('Hello how are you'))

# Opg 6 "Sort a list"
# Create a list of strings with names in it.
l = ['Claus', 'Ib', 'Per', 'Arne', 'Jan']

# Sort this list by using the sorted() build in function.
sorted_names = sorted(l)
print(sorted_names)

# Sort the list in reversed order.
reversed = sorted(l, reverse=True)
print(reversed)

# Sort the list on the lenght of the name.
length = sorted(l, key=len)
print(length)

# Sort the list based on the last letter in the name.
def last(s):
    return s[-1]
sorted(l, key=last)

# Sort the list in a way that the names that has an ‘a’ in it should be sorted first (still alphabetically).
def a_in(s):
    if 'a' in s.lower():
        return True
    return False
sorted(l, key=a_in)