'''
Develop a program that reads a student's two grades, calculates and displays their average.
'''

n1 = float(input('students first grade: '))
n2 = float(input('Student second grande: '))
average = (n1 + n2) / 2

print('The average between {:.1f} and {:.1f} is equal to: {:.1f}'.format(n1, n2, average))