class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def display(self):
        print(self.name,self.email)

class Admin(User):
    def delete_user(self):
        print("Admin can delete the users")


class Owner(Admin):
    def deleteAdmin(self):
        print("Owners can delete the admins")


# user1 = 
admin1 = Admin("Thayub",'thayub@gmail.com')

owner1 = Owner("Kaja","kaja@gmail.com")

owner1.display();