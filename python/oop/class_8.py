# object oriented program 
class car:
    def __init__(self, name, model):
        self.name = name
        self.model_year = model
        self.wheel = 4
    
    def view(self):
        print(f"model number of {self.name} is { self.model_year}")
        print(f"this is a {self.wheel} possess car")

c1=car("BMW",2024)
c1.view()