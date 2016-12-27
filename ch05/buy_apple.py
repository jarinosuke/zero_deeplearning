from layer import *

apple = 100
apple_num = 2
tax = 1.1

# layer
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()


# forward
apple_price = mul_apple_layer.forward(apple, apple_num)
price  = mul_tax_layer.forward(apple_price, tax)

print(price)
