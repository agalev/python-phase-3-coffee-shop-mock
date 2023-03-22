from lib.classes.customer import Customer
from lib.classes.coffee import Coffee

class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all.append(self)
        coffee.orderss.append(self)
        coffee.customerss.append(customer)
        customer.orderss.append(self)
        customer.coffeess.append(coffee)

    def get_price(self):
        return self._price
    def set_price(self, price):
        if isinstance(price, int) and price > 0 and price < 11:
            self._price = price
        else:
            return 'Price must be between 1 and 10'
    price = property(get_price, set_price)

    def get_customer(self):
        return self._customer
    def set_customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            return 'Customer must be a Customer object'
    customer = property(get_customer, set_customer)

    def get_coffee(self):
        return self._coffee
    def set_coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            return 'Coffee must be a Coffee object'
    coffee = property(get_coffee, set_coffee)
