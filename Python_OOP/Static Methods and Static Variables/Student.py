class Student:
    __id=1
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.id=Student.__id
        Student.__id=Student.__id+1
    @staticmethod
    def get_id():
        return Student.__id
s1=Student("John Cena",55)
s2=Student("Ammar Khalid",21)
print(s2.id)

