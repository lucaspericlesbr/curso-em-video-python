'''
Make a program that reads the name of a city and tells whether or not it starts with the name "saint".
'''

city = str(input('What city were you born in? '))
print(city[:5].upper() == 'SAINT')