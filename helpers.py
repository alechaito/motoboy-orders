from static import motoboys, orders

import random
from tabulate import tabulate


def get_motoboy_by_id(id):
    """
    Parameters
    ----------
    agr1 : int
        This is the id from motoboy what you want search
    Returns
    -------
    Motoboy Object
        Return first motoboy object what match with id
    """
    try:
        return list(filter(lambda motoboy: motoboy.id == int(id), motoboys))[0]
    except IndexError:
        print("Motoboy with this id do not exist...")


def select_motoboy_to_delivery_order(order):
    """
    This function will select one motoboy to deliver and add order to him.

    It will check if has any motoboy with exclusivity.

    Parameters
    ----------
    agr1 : Order Object
        This is used to match if any motoboy has exclusivity
    Returns
    -------
    bool
        Return true ever
    """
    motoboy_selected = list(filter(lambda motoboy: motoboy.exclusivity ==
                                   int(order.store.id), motoboys))
    if not motoboy_selected:
        motoboy_selected = random.choice(motoboys)
    else:
        motoboy_selected = motoboy_selected[0]

    motoboy_selected.add_order(order)
    return True


def send_orders():
    """
    This function is just to map orders to select_motoboy_to_delivery_order function.
    """
    print('Sending orders ... \n')
    list(map(select_motoboy_to_delivery_order, orders))


def get_motoboy_order_info(order, motoboy):
    """
    This function will be used by a map function to create array containing
    detailed infos about orders associated with a motoboy.

    Parameters
    ----------
    agr1 : Order Object
        This is used to get order infos
    agr2 : Motoboy Object
        This is used to get motoboy infos
    Returns
    -------
    array
        Array containing details from order of each motoboy
    """
    return [order.store.id, order.value, motoboy.win_by_order(order)]


def make_motoboy_info(motoboy):
    """
    This function will print all information about motoboy, order and store.

    Parameters
    ----------
    agr1 : Motoboy Object
        This is used to get motoboy infos
    """
    print(repr(motoboy))
    if not motoboy.orders_received:
        print('Not received any order...')
    else:
        motoboy_order_info = map(lambda order: get_motoboy_order_info(
            order, motoboy), motoboy.orders_received)
        print(tabulate(motoboy_order_info, headers=[
            "Store ID", "Order Value", "Comission"]))
    print('---------------------------- \n')


def check_motoboys_orders(motoboys=None):
    """
    This function will map motoboys with a make_motoboy_info

    Parameters
    ----------
    agr1 : Array of Motoboy Objects
        This is used to get info from each motoboy
    """
    list(map(make_motoboy_info, motoboys))
