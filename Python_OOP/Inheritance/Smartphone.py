from Phone import Phone
class Smartphone(Phone):
    def __init__(self,name,ram,os):
        print("Executing child constructor")
        self.name=name
        self.ram=ram
        self.os=os
    def print_info(self):
        print(self.name,self.ram,self.os)

smartphone =Smartphone("Samsung",16,'Android')
#This will throw an error because here only the constructor of child class is executed
smartphone.print_year()

