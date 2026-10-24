from Vehicle import Vehicle
class Bus(Vehicle):

    def __init__(self):
        super().__init__(50)

    def calculate_fare(self):
       fare=super().calculate_fare()
       total_fare=fare + (10*fare)/100
       return total_fare

    def print_fare(self):
        print("The total fare of the bus is: "+ str(self.calculate_fare()))
