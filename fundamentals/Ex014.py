'''
Write a program that converts a typed temperature in ºC to ºF.
'''

celsius = float(input('Enter the temperature in degrees celsius: '))
fahrenheit = ((9 * celsius) / 5) + 32

print('The temperature of {}ºC corresponds to {}ºF'.format(celsius, fahrenheit))