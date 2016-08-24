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
    root = None

    def add_vehicle(self, vehicle):
        if self.root is None:
            self.root = VehicleNode(vehicle)
            return True
        else:
            if self.find_vehicle(vehicle.registration_plate):
                return False
            else:
                self._add(vehicle, self.root)
                return True

    def _add(self, vehicle, node):
        if (vehicle.registration_plate < node.vehicle.registration_plate):
            if node.left is not None:
                self._add(vehicle, node.left)
            else:
                node.left = VehicleNode(vehicle)
        else:
            if node.right is not None:
                self._add(vehicle, node.right)
            else:
                node.right = VehicleNode(vehicle)

    def find_vehicle(self, registration):
        if self.root is not None:
            return self._find(registration, self.root)

    def find_owner(self, registration):
        vehicle = self.find_vehicle(registration)
        return vehicle.owner if vehicle else None

    def _find(self, registration, node):
        if node.vehicle.registration_plate == registration:
            return node.vehicle
        elif registration < node.vehicle.registration_plate and node.left is not None:
            self._find(registration, node.left)
        elif registration > node.vehicle.registration_plate and node.right is not None:
            self._find(registration, node.right)

    def list_vehicles(self):
        if self.root is not None:
            self._list_vehicles(self.root)

    def _list_vehicles(self, node):
        if node is not None:
            self._list_vehicles(node.left)
            print node.vehicle.registration_plate + ' '
            self._list_vehicles(node.right)


class VehicleRegisterList():
    vehicles = []

    def add_vehicle(self, vehicle):
        if self.find_vehicle(vehicle.registration_plate):
            return False
        self.vehicles.append(vehicle)
        return True

    def find_owner(self, registration):
        vehicle = self.find_vehicle(registration)
        return vehicle.owner if vehicle else None

    def find_vehicle(self, registration):
        for vehicle in self.vehicles:
            if vehicle.registration_plate == registration:
                return vehicle

    def list_vehicles(self):
        for vehicle in self.vehicles:
            print vehicle


import random
import string
import time

random.seed(1)


def generate_registration():
    choices = string.uppercase + string.digits
    registration = ''.join(random.sample(choices, 10))
    return registration

# Binary Tree
register_tree = VehicleRegisterTree()

for i in range(10000):
    registration = generate_registration()
    name = ''.join(random.sample(string.lowercase, 5))
    car = Car(registration, "Douno")
    register_tree.add_vehicle(car)

import sys
if len(sys.argv) > 1:
    register_tree.list_vehicles()
    print register_tree.find_owner(sys.argv[1])
