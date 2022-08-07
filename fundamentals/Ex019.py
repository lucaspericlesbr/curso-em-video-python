'''A teacher wants to raffle four students to erase the board. Make a program that helps him, reading their name and writing the name of the chosen one.'''

from random import choice

n1 = str(input('Enter a name of the first student: '))
n2 = str(input('Enter a name of the second student: '))
n3 = str(input('Enter a name of the third student: '))
n4 = str(input('Enter a name of the fourth student: '))
list = [n1, n2,n3, n4]
chosen = choice(list)
print('The chosen student was {}'.format(chosen))