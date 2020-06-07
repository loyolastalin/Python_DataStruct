import math

print(math.ceil(2.9))
print(math.floor(2.9))

# https://docs.python.org/3/library/math.html

# if else statement
# and, or , not for logical operator
amount =100
product = 'vegitable'
discount=0
if(amount>100 and product == 'vegitable'):
    discount = amount*0.10
elif(amount== 100 and product == 'vegitable'):
    discount = 10
else:
    discount = 1
print('For amount {} the discount {}'.format(amount, discount))

