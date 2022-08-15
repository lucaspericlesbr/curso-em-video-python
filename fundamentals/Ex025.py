'''
Make a program that reads a person's name and tells if they have "silva" in their name
'''

name = str(input('What is your full name? '))
print('does your name have silva? {}'.format('silva' in name.lower()))