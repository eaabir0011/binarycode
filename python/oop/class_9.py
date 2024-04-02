class dog():
    def __init__(self,name,color):
        self.name = name
        self.color= color
    
    def update_color(self,color):
        self.color=color

    def poke(self):
        print(self.name+"'s color is",self.color)

d1=dog("Tom","brown")
d2=dog("robert","white")
d2.update_color("black")
d1.update_color("white")
d1.poke()
print("\nprint with __dict__ module:",d1.__dict__)
d2.poke()
print("\nprint with __dict__ module:",d2.__dict__)
# print(dir(d1))