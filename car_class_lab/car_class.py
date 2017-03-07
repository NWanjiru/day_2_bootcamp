class Car(object):
  """Takes in the type, model and name of a vehicle and uses those arguments to 
  instansiate different vehicles"""
  
    num_of_doors = 4
    
    def __init__(self, model = 'GM', name = 'General', car_type = 'saloon', speed = 0):
        self.car_type = car_type
        self.model = model
        self.name = Car(name)
        self.speed = speed
        
    def Car(self,name,model,car_type,speed):
      if self.name == 'porshe' or self.name == 'Koenigsegg':
        self.num_doors = 2
        return(self.num_of_doors)
      else:
        return(self.num_of_doors)
