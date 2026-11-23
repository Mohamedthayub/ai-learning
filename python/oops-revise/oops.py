class Vehicle:
    def __init__(self,name,no,year,color):
        self.name = name
        self.no = no
        self.year = year
        self.color = color

    def showDetails(self):
        print("Vehicle Name  :",self.name)
        print("Vehicle Number:",self.no)
        print("Vehicle Color :",self.color)
    

vehicle1 = Vehicle("Virtus","TN72FJ2024","2023","White")
vehicle1.showDetails()
