class Student(): 
    def __init__(self,name,id):
        # name = self.name 
        # instance variable
        
        # id=self.id 
        # instance variable

        self.name = name 
        self.id = id
#========================================================

# data manipulate ::: variable= class name 
s1 = Student("Dickinson", 14) 
s2 = Student("Robin",15)

# to know memory address 
print("Memory Address of S1", s1)
print("Memory Address of S2", s2)

print(s1.name)
print(s2.name)
print(s1.id)
print(s2.id)
s2.id=55
print('s2',s2.id)