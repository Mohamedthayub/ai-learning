class Product:
    def createProduct(self,name,price,description,rating):
        self.name = name
        self.price = price
        self.description = description
        self.rating = rating

    def showDetails(self):
        print("Product Name :",self.name)
        print("Product Price:",self.price)
        print("Product Description:",self.description)
        print("Product Rating :",self.rating)

    def updatePrice(self,price):
        self.price = price

    def updateName(self,name):
        self.name = name

    def updateDescription(self,description):
        self.description = description

    def updateRating(self,rating):
        self.rating = rating

Product1 = Product()
Product1.createProduct("Apple 17 pro max",20000,"Sleek, intuitive devices connecting work, creativity, and everyday life seamlessly.","5 Stars")
Product1.showDetails()
Product1.updateName("Apple MacBook Pro Max")
Product1.showDetails()