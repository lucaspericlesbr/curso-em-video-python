'''The same teacher from the previous challenge wants to raffle the students' work order. Make a program that reads the names of the four students and shows the order drawn.'''

from random import shuffle 

n1 = str(input('Enter a name of the first student: '))
n2 = str(input('Enter a name of the second student: '))
n3 = str(input('Enter a name of the third student: '))
n4 = str(input('Enter a name of the fourth student: '))
list = [n1, n2, n3, n4]
shuffle(list)
print('The order of presentation will be: ')
print(list)