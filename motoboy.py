import names

class Motoboy:

    def __init__(self, id, charge_value, stores, exclusivity = None):
        self.id = id
        self.charge_value = charge_value
        self.stores = stores # array from 0 to 2
        self.name = names.get_full_name()
        self.total_win = 0
        self.total_orders = 0
        self.exclusivity = exclusivity
        self.orders_received = []
    
    def win_by_order(self, order):
        return order.value * order.store.comission +  self.charge_value
    

    def add_order(self, order):
        self.total_orders += 1
        self.total_win += self.win_by_order(order)
        self.orders_received.append(order)
        """print("Motoboy {} received new order / Winned: {} / Total_win: {} / Total orders: {}".format(
            self.name,
            self.win_by_order(order),
            self.total_win,
            self.total_orders
        ))
        print("-------------------------- \n")"""
