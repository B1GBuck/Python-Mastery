class CustomOrder:
    business_name = "M3"
    @classmethod
    def update_business_name(cls, new_name):
        cls.business_name = new_name
    
    @staticmethod
    def validate_price(price):
        return price > 0
    
    @staticmethod
    def validate_quantity(quantity):
        return quantity > 0
    
    def __init__(self, order_id, customer_name, item_type, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.item_type = item_type
        self.quantity = quantity
        self.price = price
    
    def __str__(self):
        return f"{self.order_id} Order for {self.customer_name}: {self.quantity} x {self.item_type} @ {self.price} each"
    
    def __repr__(self):
        return f"CustomOrder({self.order_id}, '{self.customer_name}', '{self.item_type}', {self.quantity}, {self.price})"
    
    def __eq__(self, other):
        return self.order_id == other.order_id
    
    def apply_discount(self, percent):
        return float(self.price - (self.price * percent / 100))
    
    def is_bulk(self):
        return self.quantity >= 5

order1 = CustomOrder(789754908987, "Dre", "Watches", 10, 6000)
print(order1)
print(order1.apply_discount(10))
print(order1.is_bulk())

order2 = CustomOrder(7843796702, "Blaike", "Shoes", 4, 2500)
print(order2)
print(order2.apply_discount(10))
print(order2.is_bulk())

order3 = CustomOrder(789754908987, "Tanya", "Underwear", 10, 6000)
print(order3)
print(order3.apply_discount(10))
print(order3.is_bulk())

print(order1.business_name)

CustomOrder.update_business_name("Made by Mia G")

print(order1.business_name)
print(order2.business_name)


print(CustomOrder.validate_price(0))
print(CustomOrder.validate_quantity(3))

print(repr(order1))
print(repr(order2))


print(order1)
print(order2)
print(order3)

print(order1 == order2)
print(order1 == order3)

print(repr(order1))











