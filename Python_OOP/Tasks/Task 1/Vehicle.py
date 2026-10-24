class Vehicle:
    def __init__(self,capacity):
        self.capacity=capacity
    def calculate_fare(self):
        fare=self.capacity*100
        return fare
    def print_fare(self):
        print("The total fare of the vehicle is :" + str(self.calculate_fare()))