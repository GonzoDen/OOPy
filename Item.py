import csv


class Item:
    #class attribute, available for both class and instance level
    #__dict__ magic class attribute
    default_discount = 0.1 #The pay rate after 20% discount
    all = []

    #methods that  starts with "__" are called magic methods
    #init is the function that created automatically aka contructor in Java
    def __init__(self, name:str, price:float, quantity=0):
        #Run validations to the received arguments
        assert price > 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        #Assign to self Object
        self.__name = name #name is a private
        self.price = price
        self.quantity = quantity #quantity=0 is a default value

        #append instance to the list
        Item.all.append(self)

    #ENCAPSULATION IN PY
    #GETTER
    @property
    def name(self):
        return self.__name

    #SETTER
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Your name is too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * (1 -self.default_discount)

    #made as a class method to avoid being available for instances
    #@ is a decorators, i.e. functions that you can use before other functions
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    #static methods do not send class/instance as the 1st arg
    @staticmethod
    def is_integer(num):
        #
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    #this is usually done to avoid
    """for item in Item.all:
    print(item.name)"""
    def __repr__(self):
        #return the full info about instances both for parental and child class
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"





