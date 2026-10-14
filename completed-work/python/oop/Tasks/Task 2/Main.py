from Location import Location
class Main:
    def __init__(self):
        print("_____Enter the Starting Points______ ")

        start_x=int(input("Enter the starting x-axis: "))
        start_y = int(input("Enter the starting y-axis: "))

        dest_x = int(input("Enter the destination x-axis: "))
        dest_y = int(input("Enter the destination y-axis: "))

        self.location=Location(start_x,start_y,dest_x,dest_y)
        print(self.location.reflected_axis())




if __name__=="__main__":
    app=Main()


