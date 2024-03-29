#MAP FILTER REDUCE  only used in list
# print("Hi I'm Python. I'm ready to do your task")
#map
def cube(x):
    value=x**3
    return value

li=[1,2,3,4,5]
newl=list(map(cube, li))
print(newl)
# map works for every iliments with a function  

#filter
def filter_function(a):
    return a>=3 

newl=list(filter(filter_function, li))
print(newl)

#reduce
def a_function(x,y):
    return x+y
# we have to import reduce function from functools  
from functools import reduce
newli=[1,5,6,1,4]
value=reduce(a_function,newli)
print(value) 