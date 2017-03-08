class Car(object):
	"""Takes in the type, model and name of a vehicle and uses those arguments to instansiate different vehicles"""
	num_of_doors = 4
	num_of_wheels = 4
	speeed = 0
	drive = 0
	car_list = []

	def __init__(self, name='General', model ='GM', car_type = None):
		Car.car_list.append(self)
		self.name = 'General'
		self.model = 'GM'
		self.car_type = None
		

	def count_doors(self,name):
		cars = {}
		my_list =[]
		if isinstance(self.name, Car):
			return True
		for self.name in car_type:
			if self.name == 'Porshe' or self.name == 'Koenigsegg':
				self.num_of_doors = 2
				cars[x] = self.num_of_doors
			else:
				cars[x] = self.num_of_doors
		for key in cars.keys():
			my_list.append(cars[key])
		return(my_list)

	def count_wheels(self):
		pass

