# object oriented programing 
# constructor 
class person:
    name="abir"
    occ="developer"
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a=person()
print(a.name)
print(a.info())