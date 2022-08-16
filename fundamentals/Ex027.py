'''
Write a program that reads a person's full name, then displays the first and last name separately.

Ex: Ana Maria de Souza
First: Ana
Last: Souza
'''

fullname = str(input('Enter your full name: ')).strip()
name = fullname.split()
print('Nice to meet you!')
print('Your first name is {}'.format(name[0]))
print('Your last name is {}'.format(name[len(name)-1]))
