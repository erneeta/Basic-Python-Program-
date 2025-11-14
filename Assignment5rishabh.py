# Assignment 5
#   -> 1. Print while loop in one line
n = 1
while n < 11:
    a = n*2
    print(a, end=' ')
    n +=1

#   -> 2. Write star(*) pattern in loop
n = int(input("Enter the number of row"))
for a in range(1,n+1):        #outerloop for row
    for i in range(1,a+1):     #innerloop for column
        print("*",end="")       #to print * without new line
    print()                      # move to next line

for a in range(1, n+1):
    print("*" * a)

# For inverted triangle
for a in range(n,0,-1):
    for i in range(1,a+1):
        print("*",end="")
    print()

for a in range(n,0,-1):
    print("*" * a)

# for pyramid
for a in range(1,n+1):
    print(" "*(n-a),end="")
    print("*"*(2*a-1))

#   -> 3. find factorial of given number
n = int(input("Enter a number to calculate factorial: "))
def fact(num):
    result = 1
    while num>0:
        result *= num
        num -= 1
    return result
print(f"The factorial of {n} is {fact(n)}")

#   -> 4. Count vowels in the string
name = input("Enter a string: ")
vowel = "aeiou"
count = 0
for char in name:
    if char.lower() in vowel:
        count += 1
print(f"There are {count} vowels present in {name}")

#   -> find the longest word in a sentence using for loop
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f"The longest word of sentence is : {longest_word}")

#   -> DO while loop in python

while True:
    num = int(input("Enter a number greater than 10"))
    if num > 10:
        print("number is right!!!")
        break
    else:
        print("Enter valid num")
         
#   -> write first n numbers in fibonacci series
def fibo(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        print(a)       
        a, b = b , a+b
        
        count +=1

num = int(input("Enter a number: "))
fibo(num)