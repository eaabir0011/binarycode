# inheritence 
class employe:
    def __init__(self,name,id):
        self.name =   name
        self.id = id

    def view(self):
        print(f"{self.id} is {self.name}")

class programmar(employe):
    def languages(self):
        print("Default Programming Language is Python ")
    def all_details(self):
        print(f"Employe {self.name} ID {self.id}")

"""main program"""
emp_1=employe("Kaium",10)
emp_2=employe("Arib", 23)
emp_1.view()
emp_3=programmar("Masud", 79)
emp_3.all_details()