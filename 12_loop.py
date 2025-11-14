# LOOP in PYTHON

# 1. While loop
#   -> check condition before iteration
#   -> Iterate as long as condition is true
#   -> while loop can be use with else statement when condition is false then else statement can execute

# write a number from 1 to 5
n = 1
while n<6:
    print(n)
    n +=1

# Write a table of 3
print("Table of 3")
n=1
while n<11:
    a = n * 3
    print(a)
    n +=1
else:
    print("Completed the table of 3")


# 2. For loop
#   -> it iterate over sequence(list,tuple,string,range)
#   -> execute for each element in that sequence

# String
name = "Neeta"
for a in name:
    print(a)

# list
shopping_list =['pen','Notebook','cable','pendrive']
for b in shopping_list:
    print(b)

# tuple
odd_tuple = (1,3,5,7,9)
for c in odd_tuple:
    print(c)

# range
for d in range(6):  # range(stop)  by default start value is 0
    print(d)    # it prints 0 1 2 3 4 5 stop value is excluded

print('write a table for 3')
for e in range(1,11):   # range(start,stop)
    num = 3 * e
    print(num)

# Write odd number from 1 to 10
for f in range (1,11,2):    # range(start,stop,step)
    print(f)
else: 
    print("End of for loop")


# Pass Break Continue
#   -> Pass statement is placeholder it does nothing
#   -> Break statement terminate loop and exiting it immediately.
#   -> Continue statement skip current iteration

print("while with pass")
number = 1
while number < 5:
    pass
    number += 1
print("-------------")

print("while with break")
n = 0
while n < 5:
    if n == 3:
        break
    print(n) 
    n += 1
print("-------------")

print("While with continue")
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n) 
print("-------------")

print("While with pass with if")
n = 0
while n < 5:
    n += 1
    if n == 3:
        pass
    print(n) 
print("-------------")

print("for with pass")
for a in range(5):
    pass        
print("----------")

print("for with break")
for a in range(5):
    if a == 3:
        break
    print(a)
print("----------")

print("for with continue")
for a in range(5):
    if a == 3:
        continue
    print(a)
print("----------")

print("for with pass with if else")
for a in range(5):
    if a == 3:
        pass
    print(a)
print("----------")

# infinite loop but in controlled way
while True:
    a =input("Enter exit to stop!!!")
    if a == 'exit':
        print("Congratulation you are out from infinity loop")
        break   #it is use to get out of infinite
    print("Sorry, you stuck in infinite loop")

# Nested Loop
a = 1
while a <= 3:
    b = 1
    while b <= 3:
        print(b)
        b += 1
    print("The iteration number is ",a)
    a +=1
    
for a in range(3):
    for b in range(1,4):
        print(b)
    print("The iteration number is",a)

#find prime number from 1 to 10
print("Prime numbers")
for n in range(2,10):
    for a in range(2,n):
        if n % a == 0:
            break
    else:
        print(n)