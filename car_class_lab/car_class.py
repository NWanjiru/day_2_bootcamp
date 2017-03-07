class Car(object):
	"""Takes in the type, model and name of a vehicle and uses those arguments to instansiate different vehicles"""
	num_of_doors = 4
	num_of_wheels = 4
	car_list = []
	def __init__(self, name='General', model ='GM', car_type = None, speed = 0):
		Car.car_list.append(self)
		self.name = name
		self.model = model
		self.car_type = car_type
		self.speed = speed

	def car_properties(self,car_type):
		
		if car_type == 'Porshe' or car_type == 'Koenigsegg':
			self.num_of_doors = 2
			return self.num_of_doors


		if car_type == 'trailer':
			self.num_of_wheels = 8
			return self.num_of_wheels
		else:
			return self.num_of_wheels
			


	