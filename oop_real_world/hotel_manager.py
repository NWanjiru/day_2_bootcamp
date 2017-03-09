class HotelManager(object):
    """Takes in client's room_type and number of days they wish to book
     and calculates a discount based on the number of days in their stay"""

    def __init__(self,room_type):
        self.room_type = room_type

        if self.room_type == 'single' or self.room_type == 'double':
            return ('Kindly proceed to the boarding area.')
        else:
            return("We only provide 'single' and 'double' rooms.")

class Boarding(HotelManager):
    """calculates discount per day for the length of the stay"""

    def __init__(self,room_type):
        
        self.room_type = room_type
        self.single = 10000
        self.double = 20000
        self.discount = 500


    def single_room(self, num_of_days):

        if self.room_type == 'single':
            if num_of_days <= 5:
                self.discount = 0
                return(['No discount, maybe you should stay a little longer?', self.discount])
            
            else:
                
                self.single = (self.single * num_of_days) - ((num_of_days - 3) * self.discount)
                self.discount = (num_of_days - 3) * self.discount
                return([self.single,self.discount])

    def double_room(self, num_of_days):

        if self.room_type == 'double':
            if num_of_days <= 2:
                self.discount = 0
                return (['You accumulate discount after the second day', self.discount])

            elif num_of_days <= 4:
                self.double = (self.double* num_of_days) - self.discount
                return(['You only get discount for your last day', self.double, self.discount])

            else:
                self.double = (self.double * num_of_days) - ((num_of_days - 3) * self.discount)
                self.discount = self.discount *(num_of_days - 3)
                return([self.double, self.discount])

                
