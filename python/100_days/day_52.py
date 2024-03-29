#lambda function 
#lambda formate:: 
# #name_of_function= lambda(which items it will take input): (formula of what the function will returrn)
square=lambda x: x**2
print(square(25))

#basically we use lambda function insted of using od def in python 
# for more example 

cube=lambda x:(x**3)
x=int(input("Give the number to know the cubic result of your desire number "))
print(f"Cube of {x} is {cube(x)}")

#multiple input in a function 
avg=lambda x,y,z : ((x+y+z)/3)
print(avg(3,5,4))