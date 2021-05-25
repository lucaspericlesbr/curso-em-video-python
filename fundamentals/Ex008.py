'''
Write a program that reads a value in meters and displays it converted to centimeters and millimeters.
'''

num = float(input('Enter a value in meters: '))
print('The value {}m converted to {:.0f}cm and {:.0f}mm.'.format(num, (num*100), (num*1000)))

# CHALLENGE #
# Write a code with all convertions

'''num = float(input('Enter a value in meters: '))
km = num / 1000
hm = num / 100
dam = num / 10
dm = num * 10
cm = num * 100
mm = num * 1000
print('The value entered in meters was {}m, converted to: \nKm = {}km \nHm = {}hm \nDam = {}dam \nDm = {:.0f}dm \nCm = {:.0f}cm \nMm = {:.0f}mm'.format(num, km, hm, dam, dm, cm, mm))'''