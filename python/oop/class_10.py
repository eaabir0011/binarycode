# in this tutorial we will see about the set and get method
# set method used to update a value
# get method used to show the updated result

class book():
    def __init__(self,name,author):
        self.name = name
        self.author = author
        self.price = 0

    def set_price(self,price):
        self.price=price

    def get_price(self):
        return self.price
    
    def details(self):
        print("book",self.name)
        print("Author:",self.author)
        print("Price",self.price,"$")
