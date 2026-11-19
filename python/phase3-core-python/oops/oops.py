class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def showUserDetails(self):
        print("User name  :",self.name)
        print("User email :",self.email)



user1 = User("Thayub","thayub@gmail.com")
user2 = User("Buyath","buyath@gmail.com")
user1.showUserDetails()
user2.showUserDetails()