Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = (2,34,6,465,558,2)
>>> type(n)
<class 'tuple'>
>>> n[0]
2
>>> n[0] = 65
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    n[0] = 65
TypeError: 'tuple' object does not support item assignment
>>> len(n)
6
>>> n.count(2)
2
>>> n.index(2)
0
>>> max(n)
558
min(n)
2
sum(n)
1067
n.append(2)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    n.append(2)
AttributeError: 'tuple' object has no attribute 'append'
temp = list(n)
temp
[2, 34, 6, 465, 558, 2]
type(temp)
<class 'list'>
temp.index(465)
3
temp[3] = 460
temp
[2, 34, 6, 460, 558, 2]
n = tuple(temp)
n
(2, 34, 6, 460, 558, 2)
type(n)
<class 'tuple'>
n[::-1]
(2, 558, 460, 6, 34, 2)
st = {1,1,1,,2,3,2,12,12,12,156,4,5}
SyntaxError: invalid syntax
st = {1,1,1,8,2,3,2,12,12,12,156,4,5}
type(st)
<class 'set'>
st
{1, 2, 3, 4, 5, 8, 12, 156}
len(st)
8
s = {}
type(s)
<class 'dict'>
t = set()
t
set()
s1 = {1,2,3,4}
s2 = {4,5,6}
s1.union(s2)
{1, 2, 3, 4, 5, 6}
s1
{1, 2, 3, 4}
s1.update(s2)
s1
{1, 2, 3, 4, 5, 6}
s1.intersection(s2)
{4, 5, 6}
s2.issubset(s1)
True
s1.issuperset(s2)
True
s1.isdisjoint(s2)
False
s1.intersection_update(s2)
s1
{4, 5, 6}
s1
{4, 5, 6}
s1.add(65)
s1
{65, 4, 5, 6}
s1.add(34)
s1
{65, 34, 4, 5, 6}
s1.remove(4)
s1
{65, 34, 5, 6}
s1.pop()
65
s1
{34, 5, 6}
s1[0]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s1[0]
TypeError: 'set' object is not subscriptable
del s1
s1
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    s1
NameError: name 's1' is not defined
s2
{4, 5, 6}
s2.clear()
s2
set()
s1 = {1,2,3,4}
s1.remove(5)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s1.remove(5)
KeyError: 5
s1.discard(5)
s2 = {3,5,6,8}
s1.difference(s2)
{1, 2, 4}
s1.symmetric_difference(s2)
{1, 2, 4, 5, 6, 8}
