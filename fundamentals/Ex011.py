'''Make a program that reads the width and height of a wall in meters, calculate its area and the amount of paint needed to paint it, knowing that each liter of paint, paints an area of ​​2m².'''

width = float(input('Wall width: '))
height = float(input('Wall height: '))
area = width * height 
print('Its wall has the dimension of {} x {} and its area is {}m².'.format(width, height, area))
paint = area / 2
print('To paint this wall, you need {}l of paint'.format(paint))