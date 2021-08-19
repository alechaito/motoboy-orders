class Order:

    def __init__(self, value, store):
        self.value = value
        self.store = store

    def __repr__(self):
        return f"""Order value: {self.value}, \
        Store id: {self.store.id} \
        Store comission: {self.store.comission}
        """
