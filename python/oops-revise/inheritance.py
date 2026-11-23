class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def showAge(self):
        print(self.age)

    def showName(self):
        print(self.name)


class Teacher(Student):

    def showTeacherName(self):
        print(self.name)
        print(self.age)

    def  deleteStudent(self):
        print("Teacher  can Delete the Student")

class Corresspondent(Teacher):
    def showCorrespondent(self):
        print("Corresspondent can delete Teacher")



t1 = Teacher("buyath",20)
t1.showTeacherName()
t1.deleteStudent()
c1 = Corresspondent("Sheik",50)

c1.showCorrespondent();