# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle is base class
class Vehicle: 
    def __init__(self, name):
        self.name = name
        pass

#ground vehicle inherits vehicle 
class GroundVehicle(Vehicle):
    def __init__(self, name):
        self.name = name
        pass

#flight vehicle inherits vehicle
class FlightVehicle(Vehicle):
    def __init__(self, name):
        self.name = name
        pass

#Car inherits groundvehicle
class Car(GroundVehicle):
    def __init__(self, name):
        self.name = name
        pass

#Motorcycle inherits groundvehicle
class Motorcycle(GroundVehicle):
    def __init__(self, name):
        self.name = name
        pass
#airplane inherits flightvehicle
class Airplane(FlightVehicle):
    def __init__(self, name):
        self.name = name
        pass       

#starship inherits flightvehicle
class Starship(FlightVehicle):
    def __init__(self, name):
        self.name = name
        pass           