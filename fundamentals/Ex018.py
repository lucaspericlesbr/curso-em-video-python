'''Make a program that reads any angle and shows on the screen the value of the sine, cosine and tangent of that angle.'''

from math import radians, sin, cos, tan
angle = float(input('Enter value of angle in degrees: '))
# convert the angle typed in degree to radian to calculate your value
sine = sin(radians(angle))
print('The sine of {} degress is {:.2f}'.format(angle, sine))
cosine = cos(radians(angle))
print('The cosine of {} degrees is {:.2f}'.format(angle, cosine))
tangent = tan(radians(angle))
print('The tangent of {} degrees is {:.2f}'.format(angle, tangent))
