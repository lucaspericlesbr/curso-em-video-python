'''
Write a program to approve the bank loan to buy a house. Ask the value of the home, the buyer's salary and how many years he will pay.
The monthly installment cannot exceed 30% of the salary or else the loan will be denied.
'''

house = float(input('House value: R$'))
salary = float(input('Buyers salary: R$'))
years = int(input('How many years of funding? '))

installment = house / (years * 12)
minimum = salary * 30 / 100

print('To pay for a house of R${:.2f} in {} years.'.format(house, years), end='')
print('The installment will be R${:.2f}.'.format(installment))

if installment <= minimum:
    print('Loan can be GRANTED!!!')
else:
    print('loan DENIED!!!')
