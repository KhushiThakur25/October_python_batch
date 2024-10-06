#ladder if-else...
n = int(input("Enter the value.."))
if n < 0:
    print("Number is negative..")
elif n > 0:
    print("Number is positive..")
else:
    print("Zero")

#nested-if-else...
gender = input("Enter the gender of the person..")
age = int(input("Enter the age:"))
if age >= 18:
    print("Yes, u can enter.")
    if gender == "male":
        print("Welcome to party!")
    else:
        print("Sorry ! but ur gender is not allowed..")
else:
    print("you are not adult..")
