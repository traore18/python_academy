class Vehicle():
    engine_running = False
    number_wheels = 2
    number_doors = 2
    registration_plate = ""
    owner = ""

    def __init__(self, registration, owner_name):
        self.registration_plate = registration
        self.owner = owner_name

    def __str__(self):
        return '%s' % (self.registration_plate)

    def start_engine(self):
        self.engine_running = True

    def stop_engine(self):
        self.engine_running = False


class Car(Vehicle):
    number_wheels = 4
    has_radio = True


class Truck(Vehicle):
    number_wheels = 18
    has_trailer = False

    def attach_trailor(self):
        if not self.has_trailor:
            self.has_trailer = True

    def detach_trailor(self):
        if self.has_trailor:
            self.has_trailor = False


class VehicleNode():
	left = None
	right = None
	
	def __init__(self, vehicle):
		self.vehicle = vehicle
			
			
class VehicleRegisterTree():
	self.root = None
			
class VehicleRegister():
    vehicles = []

    def add_vehicle(self, vehicle):
        if self.find_vehicle(vehicle.registration_plate):
            return False
        self.vehicles.append(vehicle)
        return True

    def find_vehicle(self, registration):
        for vehicle in self.vehicles:
            if vehicle.registration_plate == registration:
                return vehicle

    def list_vehicles(self):
        for vehicle in self.vehicles:
            print vehicle


register = VehicleRegister()

import random
import string


def generate_registration():
    choices = string.uppercase + string.digits
    registration = ''.join(random.sample(choices, 10))
    return registration

for i in range(10):
    registration = generate_registration()
    name = ''.join(random.sample(string.lowercase, 5))
    car = Car(registration, name)
    while not register.add_vehicle(car):
        car.registration_plate = generate_registration()

register.list_vehicles()
