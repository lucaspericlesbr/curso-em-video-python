'''
Develop a program that reads the length of three lines and tells the user whether or not they can form a triangle.
'''

from uuid import RFC_4122


print('-='*20)
print('Triangle analyzer.')
print('-='*20)

r1 = float(input('First segment: '))
r2 = float(input('Second segment: '))
r3 = float(input('Third segment: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('The segments above CAN FORM TRIANGLE!')
else:
    print('The segments above CANNOT FORM TRIANGLE!')