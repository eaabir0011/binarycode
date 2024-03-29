# is vs ==
# is works with memory address
#== works with value
a=4 
b="4"
print(a is b)
print(a==b)

c=["Abir","Arib","Kaiyum","Saif"]
d=["Abir","Arib","Kaiyum","Saif"]
print(c is d) #location of objects in memory
print(c == d) #value

e=["Ipti","Tahosin","Jubayir"]
f=["Udoy","Nohan","Hannan"]
print(e is f)
print(e==f) 
print(c is e)
g=3 
h=3  
print(g is h)
print(g==h)
