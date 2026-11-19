class Student:
    def set_details(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age

    def showDetails(self):
        print("Name :",self.name)
        print("Age  :",self.age)
        print("Email:",self.email)

    def updateData(self,email,name,age):
        self.email = email
        self.name = name
        self.age = age

student1 = Student();
# 
student1.set_details("Thayub","thayub@gmail.com",17)
student1.showDetails()

