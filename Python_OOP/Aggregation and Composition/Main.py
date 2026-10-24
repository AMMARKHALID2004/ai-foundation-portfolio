from Teacher import Teacher
from Student import Student
from Specialization import Specialization

specialization=Specialization('Computer Science','Masters')
teacher=Teacher("Abdul Karim Shahid",'Computer Science','Male',specialization)
student=Student('Ammar Khalid','FA24-BCS-137')
if __name__=='__main__':
    print(teacher.print_info())
