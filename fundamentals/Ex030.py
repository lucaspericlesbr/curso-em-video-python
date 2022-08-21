'''
Create a program that reads an integer and shows on the screen whether it is even or odd.
'''

number = int(input('Tell me any number: '))
result = number % 2

if result == 0:
    print('The number {} is even!'.format(number))
else:
    print('The number {} is odd!'.format(number))