'''
Escreva um programa que leia a velocidade de um carro. Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite.
'''

velocity = float(input('What is the current speed of the car? '))

if velocity > 80:
    print('FINED! You have exceeded the permitted limit which is 80km/h')
    ticket = (velocity - 80) * 7
    print('You must pay a fine of R${:.2f}!'.format(ticket))
    
print('Have a good day! Drive safely!')