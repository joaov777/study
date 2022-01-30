

class Dog:

    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
    
    def set_name(self, name):
        self.name = name

    def bark(self):
        print("bark")

    def run(self):
        print(f"{self.name} is running...")

#-------------------------------------------#

ralf = Dog("Tim")
caramelo = Dog()

ralf.bark()

caramelo.set_name("Mike")
caramelo.set_age(22)

print(ralf.name)
print(ralf.get_name())
print(f"The dog named {caramelo.get_name()} is {caramelo.get_age()} years old!!")
caramelo.run()