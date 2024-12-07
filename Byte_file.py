file = open("Dic_file.png",'rb')
data = file.read()
print(data)
file.close()

file = open('Dic_file1.png','wb')
file.write(data)
file.close()