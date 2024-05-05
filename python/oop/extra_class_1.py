class chocolate:
    def __init__(self,company,name,flavour,price):
        self.company = company
        self.name = name 
        self.flavour = flavour 
        self.price = price
    def set_value(self, company,name,flavour,price):
        self.company=company
        self.name = name
        self.flavour = flavour
        self.price=price

    def get_value(self):
        return self.company, self.name, self.flavour, self.price
    
    def details(self):
        print("Your Chocolate is ",self.name," a flavour of ", self.flavour,"price", self.price)
        print("It is a Product of ",self.company)


cndy_1=chocolate("Pran", "Chocolate Layer", "Chocolate",5)
cndy_2 = chocolate("Olympic", "pulse","mango + spicy ", 3)

while True:
    print("This is a Candy Shop")
    print("1. Add New Candy \n2. know details about a Candy \n3. Sell A Candy \n4. Update details \n5. Exit The Shop and Close the Program ")
    srvc_name = int(input("Name of Service"))
    if(srvc_name == 1):
        print("Service is not available write now So wait for our developer's work ").upper()
        
    elif(srvc_name == 2):
        cndy_1.details()
        
    elif(srvc_name == 3):
        pass
    elif(srvc_name == 4):
        cndy_1.set_value()
        
    elif(srvc_name == 5):
        break
    