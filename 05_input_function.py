# input function
#   -> use to take input from user
#   -> input function always take input as string data type and return it.
a = input()   # without argument
b = input("Enter a name: ")  # with argument

a = input("Enter number1: ")
b = input("Enter number2: ")
print(a+b)
print(int(a)+int(b))   # type casting in print function

a = int(input("Enter first number: "))  #type casting at taking input from user
b = int(input("Enter second number: "))
print(a+b)