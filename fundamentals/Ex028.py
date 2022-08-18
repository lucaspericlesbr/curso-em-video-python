'''
Write a program that makes the computer "think" of an integer between 0 and 5 and ask the user to try to find which number the computer chose.
The program should write to the screen if the user won or lost.
'''

from random import randint
from time import sleep

computer = randint(0, 5) # makes the computer "think"
print('-=-' * 20)
print("I'll think of a number between 0 and 5, try to guess...")
print('-=-' * 20)
player = int(input('What number did I think of? ')) # player tries to guess
print('PROCESSING...')
sleep(3)
if player == computer:
    print('CONGRATULATIONS! You managed to beat me.')
else:
    print('I won! I thought of the number {} and not the {}!'.format(computer, player))