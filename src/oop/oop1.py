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
class Vehicle():
  pass
  
class FlightVehicle(Vehicle):
  pass
  # Baseclass is Vehicle

class Starship(FlightVehicle):
  pass
  # Baseclass is FlightVehicle

class GroundVehicle(Vehicle):
  pass
  # Baseclass is Vehicle

class Car(GroundVehicle):
  pass
  # Baseclass is GroundVehicle

class Motorcycle(GroundVehicle):
  pass
  # Baseclass is GroundVehicle

class Airplane(FlightVehicle):
  pass
  # Baseclass is FlightVehicle