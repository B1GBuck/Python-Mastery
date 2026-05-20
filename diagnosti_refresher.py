class CustomOrder:
    business_name = "M3"
    
    def __init__(self, customer_name, item_type, quantity, price):
        self.customer_name = customer_name
        self.item_type = item_type
        self.quantity = quantity
        self.price = price
    
    def order_summary(self):
        return f"Order for {self.customer_name}: {self.quantity} x {self.item_type} @ {self.price} each"

Order1 = CustomOrder("Dre", "Shirt", 9, 15.99)
Order2 = CustomOrder("Tony", "Pants", 9, 35.99)


print(Order1.order_summary())
print(Order1.business_name)
print(Order2.order_summary())
