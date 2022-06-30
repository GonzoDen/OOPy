class Item:

    #methods that  starts with "__" are called magic methods
    def __init__(self):
        pass

    def calculate_total_price(self, price, quantity):
        return price * quantity


item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 10

item2 = Item()
item2.name = "Mac"
item2.price = 1000
item2.quantity = 3

print(item1.calculate_total_price(price=item1.price, quantity=item1.quantity))

#item1 = Item()
#str = str("4")
#same