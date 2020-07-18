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
# vehicle is the base class
class Vehicle:  # vehicle is the base class
    pass

class GroundVehicle(Vehicle): # GroundVehicle is a child class of Vehicle
    pass

class Car(GroundVehicle): # car is a child class of GroundVehicle
    pass

class Motorcycle(GroundVehicle): # Motorcycle is a child class of GroundVehicle
    pass

class FlightVehicle(Vehicle): #FlightVehicle is a child class of the Vehicle class
    pass

class Airplane(FlightVehicle): # Airplane is a child class of the class FlightVehicle
    pass

class Starship(FlightVehicle): # Starship is a child class of the class FlightVehicle
    pass