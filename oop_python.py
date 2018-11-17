class Vehicle:
	def __init__(self,number_of_wheels,type_of_tank,seating_capacity,max_velocity):
		self.number_of_wheels = number_of_wheels
		self.type_of_tank = type_of_tank
		self.seating_capacity = seating_capacity
		self.max_velocity = max_velocity

	
	@property
	def number_of_wheels(self):
		return self.number_of_wheels

	@number_of_wheels.setter
	def set_number_of_wheels(self,number):
		self.number_of_wheels = number		



	def make_noise(self):
		print("VRUUUUUUM")	


tesla_model_s = Vehicle(4, 'electric', 5, 250)
print(tesla_model_s.make_noise())	
print(tesla_model_s.number_of_wheels)
tesla_model_s.number_of_wheels = 2
print(tesla_model_s.number_of_wheels)
	