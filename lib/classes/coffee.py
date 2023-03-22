# from classes.order import Order

class Coffee:
    def __init__(self, name):
        self._name = name
        self.orderss = []
        self.customerss = []

    def get_name(self):
        return self._name
    def set_name(self, name):
        return 'Cannot change name'
    name = property(get_name, set_name)

    def orders(self):
        return self.orderss
    
    def customers(self):
        return list(set(self.customerss))
    
    def num_orders(self):
        return len(self.orderss)
    
    def average_price(self):
        return sum([o.price for o in self.orderss]) / len(self.orderss)