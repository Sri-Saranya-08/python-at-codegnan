Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1,num2,num3=10,20,30
>>> print(num1)
10
>>> print(20)
20
>>> print(30)
30
>>> num1=num2=num3=10
>>> print(num1)
10
>>> print(num2,num3)
10 10
>>> 
>>> a,b=10,20
>>> print(id(a), id(b))
140710718727368 140710718727688
>>> a,b=256,256
>>> print(id(a), id(b))
140710718735240 140710718735240
>>> 
>>> a=10
>>> b=20
>>> 
>>> a,b=10,20
>>> print(id(a), id(b))
140710718727368 140710718727688
>>> a,b=b,a
>>> print(id(a), id(b))
140710718727688 140710718727368
>>> print(a,b)
20 10
