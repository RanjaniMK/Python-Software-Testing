from car import Car
from driver import Driver

class Cat:
    def __init__(self, name, age):
        self.name=name
        self.age=age


my_cat=Cat("Whiskers", 3)


my_car=Car("Toyota","Camry",2014)
me = Driver("Ken",35)
print(f"{me.age} years old {me.name} is driving {my_car.make} {my_car.model} {my_car.year}")


friends_car=Car("Toyota", "Rav4", 2020)
friend= Driver("Yang", 40)
print(f"My friend {friend.age} years old {friend.name} is driving {friends_car.make} {friends_car.model} {friends_car.year}")

print(f"My car has {my_car.wheels} wheels")
print(f"My friend's car {friends_car.wheels} has wheels")