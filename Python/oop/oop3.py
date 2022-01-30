import random

class Item:

    # class attribute --> accessible through all Item instances or directly --> shared with all the instances.
    pay_rate = 0.8

    #all items organized in a list
    all_items = []

    # magic methods (__init__ is one of them ==> constructor)
    def __init__(self, name:str, price:float, quantity=0):

        # run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # instance attributes ==> assign to self object --> not shared with any other instances but the self instance
        # "self" key-word refers to instance level. "self" refers to the instance itself being created
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute by default
        Item.all_items.append(self)

    # this is a regular method. It takes the "self" (instance) as its parameter
    def calculate_total_price(self):
        return self.price * self.quantity

    # this is a class method. It takes the "cls" (class) as its parameter
    # the chagne here affects the class attribute and consequently all instances accessing the class attributes (shared among all objects)
    @classmethod
    def change_pay_rate(cls, new_pay_rate):
        cls.pay_rate = new_pay_rate 

    # static method --> it takes nothing as a parameter (no cls or self)
    # looks like a normal method (function inside a blass) but it acts like a function (functionality outside the class)
    @staticmethod
    def greet_person(user_name):
        print(f"Hello, {user_name}")

    @staticmethod
    def create_id():
        random_number = random.randint(10000,19999)
        return random_number
        

    # method (function inside a class) accessing the class attribute to calculate discount
    def apply_discount(self):
        
        ## below, if Item.pay_rate was used, then the pay_rate for different instances could not be changed (it is hardcoded to the class attribute)
        #self.price = self.price * Item.pay_rate 
        self.price = self.price * self.pay_rate

    # displaying the objects more friendly
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
        
    # property decorator creates the getter --> the name of the method must be exactly the same as the attribute
    @property
    def name(self):
        return self._name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    # setter decorator creates the setter --> the name of the method must be exactly the same as the attribute
    @name.setter
    def name(self, name):
        self._name = name

    def set_price(self, price):
        self.price = price

    def set_quantity(self, quantity):
        self.quantity = quantity


###-----------------------------------### 

# creating the instances manually
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
Item3 = Item("Cable", 10, 5)
Item4 = Item("Mouse", 50, 5)
Item5 = Item("Keyboard", 75, 5)

print(item1.calculate_total_price())

# accessing the pay rate directly without using any instance or through the instance
print(Item.pay_rate)
print(item1.pay_rate)


# The magic method __dict__ shows all elements of either a Class or Instance (stored as dictionaries)
# Class attributes 
#print(Item.__dict__) 

# Instance attributes
#print(item1.__dict__)

# Applying discount of 80% on the phone price
item1.apply_discount()
print(f"The discount for the {item1.name} was {item1.get_price()}")

# Laptops have only 30% discount --> the Class attribute can be changed on the fly for the specific instance
item2.pay_rate = 0.3
item2.apply_discount()
print(f"The discount for the {item2.name} was {item2.get_price()}")

# printing all items (objects) presented on a list
for instance in Item.all_items:
    print(instance.name)

item1.name = "Printer"

print(f"The name of the first item will changed to {item1.name}")
print(f"The pay rate before: {Item.pay_rate}")

# changing the pay rate directly to the class method for this purpose
# pay_rate is a class attribute and it is shared with all instances 
Item.change_pay_rate(0.4)

# Accessing the pay rate straight from the class
print(f"The pay rate now: {Item.pay_rate}")

# Acessing the pay rate through the object
print(f"The pay rate for {item1.name} is {item1.pay_rate}")

# Static method creating the random ID for the user
# The static method could have also be accessed by Item.create_id()
print(f"ID {item1.create_id()} automatically created for {item1.name}")

# printing all objects in a more friendly way
print(Item.all_items)
