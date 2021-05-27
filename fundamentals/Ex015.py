'''
Write a program that asks how many kilometers a rental car has driven and the number of days it has been rented. Calculate the price to pay, knowing that the car costs US $ 60 per day and US $ 0.15 per kilometer driven.
'''

days = int(input('How many days was it rented? '))
km = float(input('How many kilometers traveled? '))
total = (60 * days) + (0.15 * km)

print('The total amount to be paid is US${:.2f}.'.format(total))