# Class definition
class Student:
    def __init__(self, name, dob, mob):
        self.name = name
        self.dob = dob
        self.mob = mob

    # Decorator
    @staticmethod
    def deco(func):
        def mdeco(self):
            func(self)
            print("Details".upper().center(50))
        return mdeco

    
    # Setter for Name
    @property
    def name(self):
        return self._name.upper()
    
    @name.setter
    def name(self, value):
        self._name = value
        nm = value.split(" ")
        self.fname = nm[0]
        self.lname = nm[-1]
    
    # Email Property
    @property
    def email(self):
        return f"{self.fname}.{self.lname}.{self.id}@college.com".lower()
    
    # ID Property
    @property
    def id(self):
        x1 = self.dob.split("/")
        return f"{x1[2]}{x1[1]}4218{x1[0]}"
    
    # Show Details Method
    
    def show_details(self):
        return f"Name: {self.name}\nID: {self.id}\nDOB: {self.dob}\nMobile: {self.mob}\nEmail: {self.email}"
