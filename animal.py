class vehicle():
	engine_running = False
	number_wheels = 2
	number_doors = 2
	registration_plate = ""
	owner = ""

	def __init__(self, registration):
		self.registration_plate = registration
		self.owner = owner_name

	def __str__(self):
		return '%s' % (self.registration_plate)

	def start_engine(self):
		self.engine_running = True

	def stop_engine(self):
		self.engine_running = False


class Car(vehicle):
	number_wheels = 4
	has_radio = True

class truck(vehicle):
	number_wheels = 18
	has_trailer = False

	def attach_trailor(self):
		if not self.has_trailor:
			self.has_trailer = True

	def detach_trailor(self):
		if self.has_trailor:
			self.has_trailor = False

			
			
class vehicleregister():
	vehicles = []
	
	def add_vehicle(self, vehicle):
		self.vehicle.append(vehicle)
	
	def find_vehicule(self, registration):
		for vehicle in self_vehicles:
			if vehicle.registration_plate == registration:
				return vehicle
	
	def list_vehicles(self):
		for vehicle in self.vehicle:
			print vehicle
	
car = Car("HY123", "Mariame")
truck = Truck("KL987", "Douno")

register = vehicleregister()

register.add_vehicle(car)
register.add_vehicle(truck)

car_two = register

	
