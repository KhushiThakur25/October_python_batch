Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dic = {}
type(dic)
<class 'dict'>
dic['name'] = "Riya"
dic
{'name': 'Riya'}
dic['age'] = 23
dic
{'name': 'Riya', 'age': 23}
dic['age']
23
dic.values()
dict_values(['Riya', 23])
dic.keys()
dict_keys(['name', 'age'])
t = dic.copy()
t
{'name': 'Riya', 'age': 23}
t.clear()
t
{}
dic2 = {'marks':82,'div':'II'}
dic.update(dic2)
dic
{'name': 'Riya', 'age': 23, 'marks': 82, 'div': 'II'}
dic.popitem()
('div', 'II')
dic
{'name': 'Riya', 'age': 23, 'marks': 82}
dic.pop('age')
23
dic
{'name': 'Riya', 'marks': 82}
dic.items()
dict_items([('name', 'Riya'), ('marks', 82)])
dic.get('name')
'Riya'
li = {'name','age','roll no','marks'}
dict.fromkeys(li,1)
{'age': 1, 'name': 1, 'roll no': 1, 'marks': 1}
dic
{'name': 'Riya', 'marks': 82}
dic.update(dic2)
dic
{'name': 'Riya', 'marks': 82, 'div': 'II'}
dic['marks'] = [74,89,56,74,58]
dic
{'name': 'Riya', 'marks': [74, 89, 56, 74, 58], 'div': 'II'}
dic['marks'][2]
56
dic['marks'] = {'hindi':56,'eng':74,"maths":89}
dic
{'name': 'Riya', 'marks': {'hindi': 56, 'eng': 74, 'maths': 89}, 'div': 'II'}
dic['marks']['eng']
74
dic = {1:'one',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',0:'Zero'}
n = int(input("Enter the value.."))
Enter the value..6523
org= n

=========== RESTART: E:/September_PythonBatch/intToString.py ===========
Enter the value..1213
['Three', 'one', 'Two', 'one']
>>> 
=========== RESTART: E:/September_PythonBatch/intToString.py ===========
Enter the value..121
['one', 'Two', 'one']
>>> 
=========== RESTART: E:/September_PythonBatch/intToString.py ===========
Enter the value..1234
['Four', 'Three', 'Two', 'one']
>>> 
=========== RESTART: E:/September_PythonBatch/intToString.py ===========
Enter the value..1234
['one', 'Two', 'Three', 'Four']
>>> 
=========== RESTART: E:/September_PythonBatch/intToString.py ===========
Enter the value..12345
['one', 'Two', 'Three', 'Four', 'Five']
one Two Three Four Five
