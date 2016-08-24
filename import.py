import sys


class VehicleRegistry():
	vehicles = []

	def add(self, vehicles):
		self.vehicles.append(vehicle)

	def print_vehicles(self):
		for vehicle in self.vehicle:
			print vehicle

if len(sys.argv) > 1:
	vr = VehicleRegistry()
	i = 1
	while i < len (sys.argv):
		 vr.add(sys.argv[i])
		 i = i + 1

		 vr.print_vehicles
