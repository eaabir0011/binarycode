class house:
    def __init__(self):
        self.window = 4
        self. door = 2
    
    def view(self):
        print ("Windows", self.window, "& doors", self.door)

h1 = house()
h2 = house()

h1.window = 6
h2.door = 4
h1.view()
h2.view()
