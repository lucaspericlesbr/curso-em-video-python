'''
Write a program that reads three numbers and shows which is the largest and which is the smallest.
'''

a = int(input('First value: '))
b = int(input('Second value: '))
c = int(input('Third value: '))

lower = a
if b < a and b < c:
    lower = b
if c < a and c < b:
    lower = c

highest = a
if b > a and b > c:
    highest = b
if c > a and c > b:
    highest = c

print('The lowest value entered was {}'.format(lower))
print('The highest value entered was {}'.format(highest))