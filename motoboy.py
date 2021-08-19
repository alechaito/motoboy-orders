import names


class Motoboy:

    def __init__(self, id, charge_value, exclusivity=None):
        self.id = id
        self.charge_value = charge_value
        self.name = names.get_full_name()
        self.total_win = 0
        self.total_orders = 0
        self.exclusivity = exclusivity
        self.orders_received = []

    def __repr__(self):
        return f"""Motoboy id: {self.id}, \
        Name: {self.name}, \
        TotalWin: {self.total_win} \
        """

    def win_by_order(self, order):
        return order.value * order.store.comission + self.charge_value

    def add_order(self, order):
        self.total_orders += 1
        self.total_win += self.win_by_order(order)
        self.orders_received.append(order)
