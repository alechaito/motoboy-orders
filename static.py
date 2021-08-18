from motoboy import *
from order import *
from store import *

#stores
store_1 = Store(1, 0.05)
store_2 = Store(2, 0.05) 
store_3 = Store(3, 0.15)

stores = [store_1, store_2, store_3]

# Motoboys
moto_1 = Motoboy(1, 2, [store_1, store_2, store_3])
moto_2 = Motoboy(2, 2, [store_1, store_2, store_3])
moto_3 = Motoboy(3, 2, [store_1, store_2, store_3])
moto_4 = Motoboy(4, 2, [store_1], 1)
moto_5 = Motoboy(5, 3, [store_1, store_2, store_3])

motoboys = [moto_1, moto_2, moto_3, moto_4, moto_5]

order_1 = Order(50, store_1)
order_2 = Order(50, store_1)
order_3 = Order(50, store_1)
order_4 = Order(50, store_2)
order_5 = Order(50, store_2)
order_6 = Order(50, store_2)
order_7 = Order(50, store_2)
order_8 = Order(50, store_3)
order_9 = Order(50, store_3)
order_10 = Order(100, store_3)

orders = [order_1, order_2, order_3, order_4, order_5, order_6, order_7, order_8, order_9, order_10]
