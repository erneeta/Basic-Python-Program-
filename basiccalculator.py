# creating function for addition
def add(n1,n2):
    return n1 + n2

# creating function for subtraction
def sub(n1,n2):
    return n1 - n2

# creating function for multiplication
def mult(n1,n2):
    return n1 * n2

# creating function for division
def div(n1,n2):
    return n1 / n2

# creating function for addition
def avg(n1,n2):
    return (n1 + n2)/2

# user interface for selecting operation
print("Select any ONE operation from following\n"\
        "1. Addition\n"\
        "2. Subtraction\n"\
        "3. Multiplication\n"\
        "4. Division\n"\
        "5. Average")

# taking choice of operation from user
n = int(input("Enter your choice of operation: "))

# taking numbers from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if n == 1:
    print(f"{num1} + {num2} = {add(num1,num2)}")
elif n == 2:
    print(f"{num1} - {num2} = {sub(num1,num2)}")
elif n == 3:
    print(f"{num1} * {num2} = {mult(num1,num2)}")
elif n == 4:
    print(f"{num1} / {num2} = {div(num1,num2)}")
elif n == 5:
    print(f"({num1} + {num2})/2 = {avg(num1,num2)}")
else:
    print("Enter valid choice number:")