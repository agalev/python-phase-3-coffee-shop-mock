# from classes.order import Order

class Customer:
    def __init__(self, name):
        self._name = name
        self.orderss = []
        self.coffeess = []
            
    def get_name(self):
        return self._name
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0 and len(name) < 16:
            self._name = name
        else:
            return False
    name = property(get_name, set_name)
    def orders(self):
        return self.orderss
    
    def coffees(self):
        return list(set(self.coffeess))
    
    def create_order(self, coffee, price):
        from lib.classes.order import Order
        Order(self, coffee, price)