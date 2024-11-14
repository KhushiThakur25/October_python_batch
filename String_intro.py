Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
st = "This is python class"
type(st)
<class 'str'>
a = 'c'
type(a)
<class 'str'>
st[5]
'i'
st[6]
's'
st[5] = 'o'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    st[5] = 'o'
TypeError: 'str' object does not support item assignment
st.upper()
'THIS IS PYTHON CLASS'
st
'This is python class'
m = st.upper()
m
'THIS IS PYTHON CLASS'
st.lower()
'this is python class'
st.capitalize()
'This is python class'
st.title()
'This Is Python Class'
st.swapcase()
'tHIS IS PYTHON CLASS'
"Hello" == "hello"
False
"Hello".casefold() == "hello".casefold()
True
st = "   This is python language   "
st.strip()
'This is python language'
st.rstrip()
'   This is python language'
st.lstrip()
'This is python language   '
st = "   This is python language****"
st.rstrip("*")
'   This is python language'
st.index('i')
5
st.rindex('i')
8
st.index('z')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    st.index('z')
ValueError: substring not found
st.find('i')
5
st.rfind('i')
8
st.find('z')
-1
st = "This is your house and this is mine"
st.split()
['This', 'is', 'your', 'house', 'and', 'this', 'is', 'mine']
st = st.split()
st
['This', 'is', 'your', 'house', 'and', 'this', 'is', 'mine']
for i in st:
    print(i)

This
is
your
house
and
this
is
mine
" ".join(st)
'This is your house and this is mine'
",".join(st)
'This,is,your,house,and,this,is,mine'
"-".join(st)
'This-is-your-house-and-this-is-mine'
" ?".join(st)
'This ?is ?your ?house ?and ?this ?is ?mine'
st = "This is my house "
st.replace('i','q')
'Thqs qs my house '
st.replace('i','q',1)
'Thqs is my house '
st.count('i')
2
len(st)
17
st.isupper()
False
st.islower()
False
st.capitalize()
'This is my house '
st.iscapitalize()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    st.iscapitalize()
AttributeError: 'str' object has no attribute 'iscapitalize'. Did you mean: 'capitalize'?
st.istitle()
False
st.isnumeric()
False
st.endswith('e')
False
>>> st.endswith(' ')
True
>>> st.startswith('')
True
>>> st.startswith('T')
True
>>> st.isdigits()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    st.isdigits()
AttributeError: 'str' object has no attribute 'isdigits'. Did you mean: 'isdigit'?
>>> st.isdigit()
False
>>> st.partition('m')
('This is ', 'm', 'y house ')
>>> st[5:10]
'is my'
>>> st[5:13:2]
'i yh'
