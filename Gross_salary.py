salary = int(input("Enter your basic salary.."))
if salary <= 10000:
    HRA = 20/100 * salary
    DA = 80/100 * salary
    gross_salary = salary + HRA + DA
    
elif salary <= 20000:
    HRA = 25/100 * salary
    DA = 90/100 * salary
    gross_salary = salary + HRA + DA
    
else:
    HRA = 30/100 * salary
    DA = 95/100 * salary
    gross_salary = salary + HRA + DA

print("Your gross salary is:",gross_salary)
