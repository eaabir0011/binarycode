"""Decorator"""
def dec_1(func):
    def mdf():
        for i in range(1,20): 
            print("*",end="")
        func()
        for i in range(1,20): 
            print("*",end="")
    return mdf

@dec_1
def greet():
    print("\n Hello Welcome To Coding World in Binary Code ")
        
"""main programing"""
greet()