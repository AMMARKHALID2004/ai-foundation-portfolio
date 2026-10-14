#You can loop through objects just like normal list or tuple etc
class Customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("Asalam U Alaikum",self.name)

c1=Customer("Ammar Khalid",21)
c2=Customer("Minahil",20)
c3=Customer("Urwa",20)
c4=Customer("Ali",17)
c5=Customer("Ahmad",24)

L=[c1,c2,c3,c4,c5]
for i in L:
    print(i.name,i.age)
for i in L:
    i.greet()