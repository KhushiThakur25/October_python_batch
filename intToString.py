dic = {1:'one',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',0:'Zero'}
n = int(input("Enter the value.."))
li = []
while n > 0:
    rem = n%10
    li.append(dic.get(rem))
    n //= 10
li = li[::-1]
print(li)

print(" ".join(li))

