class Vehicle():
	engine_running = False
	number_wheels = 2
	number_doors = 2
	manufacturer = ""

	def __init__(self, manufacturer_name):
		self.manufacturer = manufacturer_name

	def __str__(self):
		return '%s %s Door' % (self.manufacturer, self.number_doors)

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

car = Car("Ford")
print car
print "Car Running: %s" % str(car.engine_running)
car.start_engine()
print "Car made by %s" % car.manufacturer
print "Car Running: %s" % str(car.engine_running)
print "Car has %d wheels" % car.number_wheels
print "Car has %d doors" % car.number_doors
print "Car has radio: %s" % str(car.has_radio)

truck = Truck("BigRig")
print "Truck made by %s" % truck.manufacturer
print "Truck has %d wheels" % truck.number_wheels
print "Truck running %s" % str(truck.engine_running)