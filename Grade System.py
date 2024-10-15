print("Here , we are going to calculate your grade..")
physics = int(input("Enter your marks in physics.."))
chemistry = int(input("Enter your marks in chemistry.."))
maths = int(input("Enter your marks in maths.."))
hindi = int(input("Enter your marks in hindi.."))
english = int(input("Enter your marks in english.."))
total = physics + chemistry + hindi + maths + english
per = total * 0.2
if(per >= 90):
    print("Your grade is A")
elif (per >=80 and per <90):
    print("Your grade is B")
elif (per >= 70 and per < 80):
    print("Your grade is C")
elif (per >= 60 and per < 70):
    print("Your grade is D")
else:
    print("You are failed")
