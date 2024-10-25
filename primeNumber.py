n = int(input("Enter the value for n.."))
# n = 7

prime = True
for i in range(2,n//2):
    
    if(n % i == 0):
        print("Number is not prime..")
        prime = False
        break
if prime:
    print("Number is prime..")

