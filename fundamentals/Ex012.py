'''
Write an algorithm that reads the price of a product and shows its new price, with 5% discount.
'''

price = float(input('Please enter the actual product price: '))
discount = price - (price * 5 / 100)

print('The product that cost {:.2f} in the promotion with a discount of 5% will cost {:.2f}.'.format(price, discount))