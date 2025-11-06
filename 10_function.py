# python function
#   -> block of code that perform specific task
#   ->Increase code readability and reusability

# Types of function
#   -> Built in function
#   -> User defined function

# create or define a simple function
def greetings():
    print("Welcome to python")

# call or execute a function    
greetings()

# create a function with parameter
def addnum(a,b):    # a & b are parameter
    c = a+b
    print(f"Addition of {a} and {b} is: {c}")

d = int(input("Enter first number: "))
e = int(input("Enter second number: "))

# calling function with arguments
addnum(d,e)      # d & e are arguments

# using return statement in function
def sub(a,b):
    return a-b     # after this statement function ends

# call function
result = sub(d,e)
print(f"subtraction is: {result}")    # have to use print with return to print output

# Pass statement
#   -> It is placeholder
#   -> Does nothing
#   -> To create empty function

def blanckfunction():
    pass

# Types of function argument
#   1. Required Argument
#   2. Default Argument
#   3. Keyword Argument
#   4. Arbitrary Positionnal Argument(*srgs)
#   5. Arbitrary Keywords Arguments(**kwargs)

#   1. Required Argument
def greet(name):
    print("Hello,",name)

greet('Neeta')

#   2. Default Argument
#   -> if value cant provide when function called then default value is used.
def greet1(name, msg = "Hello dear,"):
    print(f"{msg} {name}")

greet1('Niti')

#   3. Keyword Argument
def greet2(name,msg):
    print(f"{msg}, {name}")

greet2(msg = "hello", name = "Neeta")    # sequence of argument is not necessary

#   4. Arbitrary Positionnal Argument(*srgs)
#   -> * is used to accept any number of positional argument
#   -> Arguments are stored as tuple.
def addnum(*args):
    result = sum(args)
    return result

print(addnum(2,3,4))

#   5. Arbitrary Keywords Arguments(**kwargs)
#   -> Arguments are stored in dictionary
#   -> Arguments with name
#   -> ** are used at starting

def stud_info(**a):
    print(f"Student information = {a}")

stud_info(name = 'Neeta', Age = 20, City = 'Pune')

