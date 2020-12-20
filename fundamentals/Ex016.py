'''Write a program that reads any real number on the keyboard and shows in your screen your integer.

Ex: Enter a value: 6.127
The value 6.127 has the integer 6'''

from math import trunc 

num = float(input('Enter a value: '))
integer = trunc(num)
print('The value entered was {} and your integer is {}'.format(num, integer))