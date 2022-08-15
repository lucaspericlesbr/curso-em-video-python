'''
Write a program that reads a sentence from the keyboard and displays:
- How many times does the letter "a" appear;
- What position does she first appear in?;
- What position did she last appear in?;
'''

phrase = str(input('Type a phrase: ')).upper().strip()
print('The letter A appears {} times in the sentence.'.format(phrase.count('A')))
print('The first letter A appeared at position {}.'.format(phrase.find('A')+1))
print('The last letter A appeared at position {}.'.format(phrase.rfind('A')+1))