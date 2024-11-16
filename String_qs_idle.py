Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
st = "Hello world"
st[10:0:-1]
'dlrow olle'
st[10:-1:-1]
''
st[10:-12:-1]
'dlrow olleH'
st[::-1]
'dlrow olleH'
st = "123456"
st[::-1]
'654321'
print(st[::-1])
654321
for i in st:
    print(i)

1
2
3
4
5
6
st = "Hello world"
for i in st:
    print(i)

H
e
l
l
o
 
w
o
r
l
d
for i in st.split():
    print(i)

Hello
world
for i in st.split():
    print(f"{i} -> {len(i)}")

Hello -> 5
world -> 5
st.split()
['Hello', 'world']
st = "This is python language , and this is too easy"
for i in st.split():
    print(f"{i} -> {len(i)}")

This -> 4
is -> 2
python -> 6
language -> 8
, -> 1
and -> 3
this -> 4
is -> 2
too -> 3
easy -> 4
rev = st
rev
'This is python language , and this is too easy'
st = "abcd"
rev = st[::-1]
rev
'dcba'
if rev == st:
    print("string is palindrome..")
else:
    print("string is not palindrome..")

string is not palindrome..
st = "aba"
rev = st[::-1]
rev
'aba'
if rev == st:
    print("string is palindrome..")
else:
    print("string is not palindrome..")

string is palindrome..
>>> st = st.split()
>>> st
['aba']
>>> st = "This is the python code."
>>> st = st.split()
>>> st
['This', 'is', 'the', 'python', 'code.']
>>> rev=st[::-1]
>>> rev
['code.', 'python', 'the', 'is', 'This']
>>> " ".join(rev)
'code. python the is This'
>>> st = "This is the python code."
>>> for i in st.split():
...     if len(i)%2 == 0:
...         print(i)
... 
This
is
python
