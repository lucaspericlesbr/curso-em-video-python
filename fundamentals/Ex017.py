'''Write a promgram that reads the lenght of the opposite and adjacent side of a right triangle and show the length of the hypotenuse.'''

opp = float(input('Lenght of opposite side: '))
adj = float(input('Lenght of adjacent side: '))
hyp = (opp ** 2 + adj ** 2) ** (1/2) # the sum of the squares on the legs of a right triangle is equal to the square on the hypotenuse
print('The length of the hypotenuse is {:.2f}'.format(hyp))

'''Another way

from math import hypot

opp = float(input('Lenght of opposite side: '))
adj = float(input('Lenght of adjacent side: '))
hyp = hypot(opp, adj)
print('The length of the hypotenuse is {:.2f}'.format(hyp))'''