a = None
if a:
    print("a is true")
else:
    print("a is false")


# check given year is leap year
year = int(input("Enter a year(YYYY)"))
if year%4 == 0:
    print(f"The year {year} is leap year")
else:
    print(f"The year {year} is not leap year")

#in one statement
print("leap year") if year %4 == 0 else print("not leap") 

# login Authentication
un = "Neeta"
pw = "Thorat"
user_name = input("Enter user name: ")
password = input("Enter password: ")
if user_name == un:
    if pw == password:
        print("Both username and password is correct")
    else:
        print("Username is correct but password is incorrect")
else:
    print("Username is incorrect")

# Eligibility criteria for admission
maths = int(input("Enter marks of maths: "))
Physics = int(input("Enter marks of Physics: "))
Chemistry = int(input("Enter marks of Chemistry: "))
if (maths >=65 and Physics >=55 and Chemistry >=50 and (maths+Physics+Chemistry) >=180) or maths+Physics >=140 :
    print("Congratulations !!! you are eligible for admission....")
else:
    print("Sorry you are not eligible for admission")