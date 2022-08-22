'''
Develop a program that asks the distance of a trip in KM. Calculate the ticket price, charging R$0.50 per KM for trips of up to 200KM and R$0.45 for longer trips.
'''

distance = float(input('How far is your trip? '))
print('You are about to start a {}KM journey.'.format(distance))
price = distance * 0.50 if distance <= 200 else distance * 0.45
print('And the price of your ticket will be R${:.2f}'.format(price))