"""Unreliable_car client program."""
from prac_09.unreliable_car import UnreliableCar
# create object from UnreliableCar Class
car1 = UnreliableCar("Run_test1", 100, 90)
car2 = UnreliableCar("Run_test2", 100, 10)
# try to drive
car1.drive(60)
car2.drive(100)

print(car1)
print(car2)
