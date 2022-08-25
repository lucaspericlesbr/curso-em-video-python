'''
Write a program that reads an employee's salary and calculates the amount of his raise.
For salaries greater than R$1,250.00, calculate a 10% increase. For those below or equal, the increase is 15%.
'''

salary = float(input('What is the salary of the employee? '))

if salary <= 1250:
    new = salary + (salary * 15 / 100)
else:
    new = salary + (salary * 10 / 100)

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salary, new))