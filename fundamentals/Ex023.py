'''
make a program that reads a number from 0 to 9999 and shows each separate digit on the screen.

Ex:
Type a number: 1834
unit:4 ten:3 hundred:8 thousand:1
'''

num = int(input('Type a number: '))

unit = num // 1 % 10
ten = num // 10 % 10
hundred = num // 100 % 10
thousand = num // 1000 % 10

print('Unit: {}'.format(unit))
print('Ten: {}'.format(ten))
print('Hundred: {}'.format(hundred))
print('Thousand: {}'.format(thousand))

