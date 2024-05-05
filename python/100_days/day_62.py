# access modifier
class Employe:
    def __init__(self):
        self.__name = " Abir "
    pass

a = Employe()
# cannot access directly but access indrectly 
# print(a.__name)
print(a._Employe__name)