#       Assignment 4

#   1. Limit the decimal places to 2 digits using .format method and print result, for the variable pi = 3.14159265359

pi = 3.14159265359
print("The value of pi is {:.2f}".format(pi))

#   2. Extract characters from index 2 to 8 with a step of 2

my_string = 'Python Course'
print(my_string[2:9:2])

#   3. Slice to get only the middle character(s)

my_string = "Madhav"

def middleofstring(a):
    middle = int(len(a)/2)
    if len(a)%2 == 0:
        return a[middle-1:middle+1]
    else:
        return a[middle]
    
print(middleofstring(my_string))

#   4. Remove the first 3 and last 3 characters

my_string = "Regression Analysis"
print(my_string[3:-3])

#   5. Get the substring that starts 4 characters from the end to the last character

my_string = "Classification"
print(my_string[-4:])

# 6. How to reverse a string using python string method

print(my_string[::-1])

#   7.Write a python program to check wheather string is pallindrome or not

a = "iaia"
if a[:] == a[::-1]:
    print("Given string is pallindrome")
else:
    print("Given string is not pallindrome")