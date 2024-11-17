Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
maxs = 0
li = [30,60,50,80,100,23]
sec = 0
for i in range(len(li)):
    if li[i] > maxs:
        sec = maxs
        maxs = li[i]

maxs
100
sec
80
maxs,sec = 0,0
li = [30,60,50,80,100,90]
for i in range(len(li)):
    if li[i] > maxs:
        sec = maxs
        maxs = li[i]

sec
80
maxs,sec = 0,0
li = [30,60,50,80,100,90]
for i in range(len(li)):
    if li[i] > maxs:
        sec = maxs
        maxs = li[i]
    if li[i] < maxs and li[i] > sec:
        sec = li[i]

sec
90
li = [30,60,120,80,100,90]
maxs = 0
for i in range(len(li)):
    if li[i] > maxs:
        maxs = li[i]

maxs
120
li.index(80)
3
li[3]
80
maxs,sec = 0,0
li = [30,60,50,80,100,90]
for i in range(len(li)):
    if li[i] > maxs:
        sec = maxs
        maxs = li[i]
    if li[i] < maxs and li[i] > sec:
        sec = li[i]

sec
90
sums = 0
li = [30,60,50,80,100,90]
for i in li:
    sums += i

sums
410
for i in li:
    print(i)

30
60
50
80
100
90
li = [[1,2,3],[4,5,6],[7,8,9]]
>>> li
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> li[0]
[1, 2, 3]
>>> li[0][1]
2
>>> for i in range(len(li)):
...     print(li[i])
... 
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
>>> for i in range(len(li)):
...     for j in range(len(li[0])):
...         print(li[i][j]**2)
... 
1
4
9
16
25
36
49
64
81
