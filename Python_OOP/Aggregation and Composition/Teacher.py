from Student import Student

class Teacher:
    def __init__(self,name,department,gender,specialization):
        self.name=name
        self.gender=gender
        self.department=department
        #Aggregation
        self.specialization=specialization
        #Composition
        self.student=Student('Ammar','FA24-BCS-137')
    def print_info(self):
        print(self.name,self.department,self.gender,self.specialization.degree_name,self.specialization.type,self.student.reg_no)