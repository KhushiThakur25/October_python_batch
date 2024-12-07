try:
    a = int(input("Enter the value of a"))
    b = int(input("Enter the value of b"))

    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
except ZeroDivisionError as msg:
    #print("You can't divide an integer by 0.")
    print(msg)

except Exception as msg:
    print(msg)
else:
    print("sum of a and b is:",add)
    print("sub of a and b is:",sub)
    print("mul of a and b is:",mul)
    print("div of a and b is:",div)
finally:
    print("Hello, i'm always executed..")
