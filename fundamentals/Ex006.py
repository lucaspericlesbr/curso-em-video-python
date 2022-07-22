'''
Create an algorithm that reads a number and shows its double, triple and square root.
'''

n = int(input('Enter a value: '))
print('The value entered was {}, your double is {}, your triple is {} and your square root is {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))
