'''
Make an algorithm that reads an employee's salary and shows his new salary, with a 15% increase.
'''

salary = float(input("What is the employee's salary? "))
increase = salary + (salary * 15 / 100)

print('An employee who earned US${:.2f}, with a 15 percent increase, starts earning US${:.2f}.'.format(salary, increase))