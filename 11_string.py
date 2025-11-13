# STRING
#   -> Sequence of character in quote
#   -> IMMUTABLE

#Single Quote
print('Hello')

# Double Quote
print("Python")

# Tripple Quote
print('''I am "Neeta", i am from 'pune' ''')

# formating string
#   -> % operator(old style)
#   -> %s is placeholder for string and %d is placeholder for int value
#   -> Currently not in use

name = "Neeta"
age = 36

print("My name is %s and my age is %d " %(name, age))

#   -> str.format() method
#   ->flexible and strong

print("My name is {} and my age is{}" .format(name,age))

# can give index or keyword
print("My name is {0} and my age is{1}" .format(name,age))
print("My name is {name} and my age is{age}" .format(name= 'nit',age= 2))

#   -> f string
print(f"My name is {name} and my age is{age}")
print(f"last year i am {age -1}")

# ESCAPE CHARACTER (Special character)

#   -> \n is use for new line
print("I am Neeta. \nI live in pune") 

#   -> \t is use for tab
print("Hello\tWorld")

#   -> \"  \" it is for double quote
print("Hello world, i am \"Neeta\" ")

#   -> \'  \' it is for double quote
print("Hello world, i am \'Neeta\' ")

# STRING INDEXING
#   -> Access single character from particular string
#   ->Start from 0 in positive index from left to right
#   ->Start from -1 in negative index from right to left

name = "neeTa thoRat"
print(name[0])  # first character of string
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])  # blank space is also character
print(name[6])
print(name[7])
print(name[8])
print(name[9])
print(name[10])
print(name[11])
print(name[-1]) #last character of string
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
print(name[-7])
print(name[-8])
print(name[-9])
print(name[-10])
print(name[-11])
print(name[-12])

# STRING SLICING

#   ->by default start index = 0 & end index = length of string
#   -> start index < end index
#   -> all 4 print statement give whole string
print(name[:])
print(name[0:])
print(name[:len(name)])
print(name[::])

print(name[0:6])    # it gives from index 0 to index 5

print(name[::-1])   # it gives reverse string

print(name[0:len(name):2])  # Alternative values. Every 2nd value. skip 1 character

print(name[::3])    # Every 3rd value skip 2 character

print(name[-2:])    #last 2 character

# String methods or functions
print(len(name))    # gives length of string
print(name)
print(name.upper())     # convert string to uppercase

print(name.lower())     # convert string to lowercase 
print(name.casefold())  # convert string to lowercase 

print(name.capitalize())  # Convert first character of string to uppercase
print(name.title())     # convert first character of each word of string to uppercase

print(name.count('e'))  # it gives number of occurance of specific character

print(name.find("e"))   # it gives index of first occurance of that character

print(name.split('T'))  # string split at given charater and return in list
print(name.split(' '))

print(name.replace('a','b'))    # replace every first value present in string by second value

a ="  neeta  "
b ="  thorat  "
print(len(a))
print(len(b))
print(a)
print(a.strip())    #it remove whitespace from starting and from ending
print(a.strip()+b)

print(a+b)
print(a.strip()+b.strip())

print(a.lstrip()) # it remove white space from starting or from left
print(a.rstrip()+b) # it remove white space from ending or from right

