from random import choice


class Car:

    def __init__(self):
        self.colour=""
        self.brand=""
        self.model=""
        self.force=0
        self.radius=0

        self.menu()
    def menu(self):
        self.colour=input("Enter the colour of the car: ")
        self.brand =input("Enter the brand of the car: ")
        self.model =input("Enter the model of the car: ")
        self.force=float(input("Enter the force of the car: "))
        self.radius=float(input("Enter the radius: "))

        choice=int(input("Press 1 if you want to proceed "))
        if choice==1:
            choice1=0
            print("""How would you like to proceed?
               1.Calculate the average of the car: 
               2.Calculate the Torque of the Car: 
                """)
            choice1=int(input())
            if choice1==1:
                self.calculate_avg()
            elif choice1==2:
                self.calculate_Torque()
            else:
                print("Invalid choice")
        else:
            print("Exiting!!!")




    def calculate_avg(self):
        distance_travelled=float(input("Enter distance travelled in KM's: "))
        fuel=float(input("Enter the amount of fuel in Litres: "))
        avg=distance_travelled/fuel
        print("The average of the car is: ",avg," KM/L")
    def calculate_Torque(self):
        torque=self.force*self.radius
        print("The torque of the car is: ",torque)
