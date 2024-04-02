# todays class about method 

class student:
    def __init__(self,name,id):
        self.name = name 
        self.id = id
    
    def details(self):
        print(f"Name: {self.name} & ID: {self.id}")

    def insert(self,name,id):
        self.name=input("Name:")
        self.id=input("ID:")

s1 = student("Dickinson", 14) 
s2 = student("Robin",15)
# s1.details()
s3=student()
s3.insert()