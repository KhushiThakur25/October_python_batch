n = int(input("Enter the value for n"))
count = 0
while n > 0:
    count += 1
    #print("Value of count is:",count)
    n //= 10
    #print("current value of n is:",n)
print("The digits are present in a number is:",count)
