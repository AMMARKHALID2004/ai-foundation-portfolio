#Objects of our custom classes are mutable in Python
#They can be changed while being on the same memory location
class Customer:
    def __init__(self,name):
        self.name=name

def hello(cust):
        print("Hi", cust.name)
        print(id(cust))
        cust.name= "Ali Hassan"
        print("Hi", cust.name)
        print(id(cust))


customer=Customer("Ammar Khalid")
hello(customer)