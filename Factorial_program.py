n = int(input("Enter the value of n.."))
fact = 1
'''i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)'''


while n > 0:
    fact *= n
    n -= 1
print(fact)

'''
for i in range(1,n+1):
    fact *= i
print("Factorial is:",fact)'''

'''for i in range(n,1,-1):
    fact *= i
print("Factorial is:",fact)'''
