#class and object
#object oriented propgramming 
class person:
    name="Abir"
    age=21
    profession="student and teacher and a learner"
    salary=2000
    def info(self):
        print(f"{self.name} is a {self.profession}")
a=person()
# print(f"Age is {a.age}")
# a.name="Shirina"
# print(a.name)
# a.profession="singer"
# print(a.profession)
a.info()