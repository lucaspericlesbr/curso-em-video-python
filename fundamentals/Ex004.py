'''
Make a program that reads something on the keyboard and shows on the screen its primitive type and all possible information about it.
'''

a = input('Type something: ')

print('The primitive type of this value is: ', type(a))
print('Only spaces? ', a.isspace())
print('Is it a number? ', a.isnumeric())
print('Is it alphabetical? ', a.isalpha())
print('Is it alphanumeric? ', a.isalnum())
print('Is it uppercase? ', a.isupper())
print('Is it in lower case? ', a.islower())
print('Is it capitalized? ', a.istitle())
