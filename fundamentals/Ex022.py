'''
Make a program that reads a person's full name and shows:
• The name with all uppercase and lowercase letters.
• How many letters in all (without considering spaces).
• How many letters have the first name.
'''

fullname = str(input('Enter your full name here: ')).strip()

print('Your name in capital letters is: {}'.format(fullname.upper()))
print('Your name in lower case is: {}'.format(fullname.lower()))
print('Your name has a total of {} letters.'.format(len(fullname) - fullname.count(' ')))
print('Your first name has {} letters'.format(fullname.find(' ')))

#separate = fullname.split()
#print('His first name is {} and he has {} letters'.format(separate[0], len(separate[0])))
