from Item import Item


class Phone(Item):
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        #Call to super function to access parental class
        super().__init__(
            name, price, quantity
        )

        #Run validations to the received arguments
        assert broken_phones >= 0, f"Number of Broken Phones {broken_phones} is not greater than or equal to zero"

        #Assign to self Object
        self.broken_phones = broken_phones