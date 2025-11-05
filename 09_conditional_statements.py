# CONDITIONAL STATEMENTS
#   1. If statement
# code of if is execute only the condition is true

age = int(input("Enter age: "))
if age > 18:
    print("You are adult")

#   2. IF Else statement
# alternative code is there to execute if the condition is false

age = int(input("Enter age: "))
if age > 18:
    print("You are adult")
else:
    print("you are not adult")

#   3. IF ELif Else statement
# it is use for multiple condition

marks = int(input("Enter marks: "))
if marks>=75:
    print("you are in distinction")
elif marks >=60:
    print("you are in first class")
elif marks >=50:
    print("You are in second class")
elif marks >=40:
    print("You are pass")
else:
    print("You are fail")

#   4. Nested if else statement
# Conditions are depend on each other

# find the number is positive even or odd 
n = int(input("Enter a number"))
if n>0:
    if n%2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive odd")
else:
    if n==0 :
        print("The number is zero")
    else:
        print("The number is negative")

#   5. Conditional Expression Ternory operator
# Shorthand way to write simple if-else

age = int(input("Enter your age"))
a = 'Adult' if age >=18 else 'Minor'
print(a)
