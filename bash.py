class VehicleRegistry():

	def print_vehicles(self, *kwargs):
		for car in kwargs["cars"]:
			print car
		for truck in kwargs["trucks"]:
			print truck
		bikes = kwargs.get("bikes", [])