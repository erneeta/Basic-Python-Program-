# Type casting in python

#types
# 1. Implicit type casting
#     -> By python interprter
#     -> To avoid data loss or error

a = 2
b = 2.5
c = a+b
print(type(a)) 
print(type(b))
print(type(c))
print(c)

a = 2+3j
b = 2.5
c = a+b
print(type(a))
print(type(b))
print(type(c))
print(c)


# 2. Explicit type casting
#       -> By programmer
#       -> Use built in function

# all data types are converted into string by using str() function
a = 23
b = str(a)
print(type(b))
print(b)

a = 23.5
b = str(a)
print(type(b))
print(b)

a = 23+2j
b = str(a)
print(type(b))
print(b)

a = [23,5]
b = str(a)
print(type(b))
print(b)

a = (23,5)
b = str(a)
print(type(b))
print(b)

a = {23,5}
b = str(a)
print(type(b))
print(b)


# string is converted to list tuple without losing any characterdatatype

a = "neeta thorat"
b = list(a)
c = tuple(a)
print(b)
print(c)

# string is converted to set but it loses repeated character
d = set(a)
print(d)

# string can not convert to dictionary

# only numerical value string can convert into similar numeric datatype

a = '1'
b = int(a)
print(b)
print(type(b))

a = '1.5'
b = float(a)
print(b)
print(type(b))

a = '1+2j'
b = complex(a)
print(b)
print(type(b))