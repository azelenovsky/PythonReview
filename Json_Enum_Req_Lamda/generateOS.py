import os
h = [9,8,7,4,5,6,3,2,1,5,5]



#g = [os.path.join(z, fname)
#     for z, x, c in os.walk("C:\\Users\Andrey\Documents\Data")
#     for fname in c in '.py' in i]
#print(g)

price = { 'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}

new_price = {}
for i in price.keys():
    new_price[i] = round(price[i] * 0.85, 2)

print(new_price)

new_price2 = {k: round(price[k] * .85, 2) for k in price.keys()}
print(new_price2)
