from static import *

import random
import argparse
import sys

# Created using python3.7

def main():
    global motoboys, stores, orders
    
    send_orders()
    while True:
        motoboy_id = input("Send motoboy_id or 0 to get all or ctrl+c to exit:")
        if(int(motoboy_id) == 0):
            check_motoboys_orders()
        else:
            motoboy = select_motoboy_by_id(int(motoboy_id)) 
            if(motoboy != None): 
                check_motoboy_orders(motoboy)


def select_motoboy_by_id(id):
    global motoboys

    for motoboy in motoboys:
        if(motoboy.id == id):
            return motoboy

    print("Motoboy with id: {} not exist...".format(id))
    return None

def send_orders():
    global orders
    print("Sending orders ... \n")
    for order in orders:
        motoboy_selected = order.check_exclusivity(motoboys)
        if(motoboy_selected == None):
            motoboy_selected = random.choice(motoboys)
        motoboy_selected.add_order(order)

def check_motoboys_orders():
    for index, motoboy in enumerate(motoboys):
        print("Motoboy id : {}, Name: {}".format(motoboy.id, motoboy.name))
        if(len(motoboy.orders_received) == 0):
            print("Not received any order...")
        for order in motoboy.orders_received:
            print("Received order from store: {}, Value; R${}, Comission: R${}".format(
                order.store.id,
                order.value,
                motoboy.win_by_order(order)
            ))
        print("Total winned: R${}".format(motoboy.total_win))
        print("---------------------------- \n")

def check_motoboy_orders(motoboy):
    print("Motoboy id : {}, Name: {}".format(motoboy.id, motoboy.name))
    if(len(motoboy.orders_received) == 0):
        print("Not received any order...")
    for order in motoboy.orders_received:
        print("Received order from store: {}, Value; R${}, Comission: R${}".format(
            order.store.id,
            order.value,
            motoboy.win_by_order(order)
        ))
    print("Total winned: R${}".format(motoboy.total_win))
    print("---------------------------- \n")


main()