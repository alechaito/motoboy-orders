class Order:

    def __init__(self, value, store):
        self.value = value
        self.store = store
    

    def check_exclusivity(self, motoboys):
        for motoboy in motoboys:
            if(self.store.id == motoboy.exclusivity):
                return motoboy
        return None