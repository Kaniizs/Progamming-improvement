"""Practicing about OOP (Object-Oriented Programming)"""

# Read a csv files
import csv

class Item:
    # Class attribute
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    
    # Method must have at least 1 parameter
    # Magic methods
    # Constructor name __init__
    def __init__(self, name: str, price: float, quantity:int):
        """
        Initialize a data
        """

        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to than zero!"

        # Assign to a self objects
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Execute actions
        self.all.append(self)

    def calculate_total_price(self):
        """
        A method that calculate the price of items.
        """
        return self.price * self.quantity

    def discount(self):
        # Method that pull an attributes from class level no matters what.
        # Ex. self.price = self.price * Item.pay_rate

        # Method that used an attributes from instance level, if not it will use from class level instead.
        ## Override a self instance.
        self.price = self.price * self.pay_rate
        return self.price
    
    @classmethod
    def instantiate_from_csv(cls):
        """
        Read a csv files. and input it into class.
        """
        with open('items.csv' , 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item( 
                name=item.get('name'),
                price=float(item.get('price')),    
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(self):
        """
        is_integer() : return True if a number is an integer, else return False
        """
        if isinstance(self, float):
            # Count out the floats that are point zero
            return self.is_integer()
        elif isinstance(self, int):
            return True
        return False
        

    def __repr__(self):
        """
        Represent an instances
        """
        if self.quantity == 1:
            return f"Item('{self.name}', {self.price} , {self.quantity} left)"
        return f"Item('{self.name}', {self.price} , {self.quantity} lefts)"


if __name__ == "__main__":
    print(Item.is_integer(7.2))
    # print(Item.all)
    # print(Item.__dict__) # All of attributes for Class level
    # print(item1.__dict__) # All of attributes for instance level
