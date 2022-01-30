


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

    def calculate_total_price(self):
        return self.price * self.quantity

    # method (function inside a class) accessing the class attribute to calculate discount
    def apply_discount(self):
        
        ## below, if Item.pay_rate was used, then the pay_rate for different instances could not be changed (it is hardcoded to the class attribute)
        #self.price = self.price * Item.pay_rate 
        self.price = self.price * self.pay_rate

    # displaying the objects more friendly
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
        

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_name(self, name):
        self.name = name

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
print(f"The discount for the {item2.get_name()} was {item2.get_price()}")

# printing all items (objects) presented on a list
for instance in Item.all_items:
    print(instance.get_name())

# printing all objects in a more friendly way
print(Item.all_items)
