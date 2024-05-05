# object oriented programing 
# constructor 
class person:
    def __init__(self,name, occ, networth):
        self.name = name
        self.occ = occ 
        self.networth = networth 
        pass
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a=person("Abir", "Softwere Developer", 50)
b = person("Sabik", "Businessman", 80)
c= person(a.name, b.occ, 70)
a.info()
b.info()
c.info()