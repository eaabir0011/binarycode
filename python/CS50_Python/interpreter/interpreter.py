x,y,z=input("expression").split(" ")
a1=float(x)
a2=float(z)

if(y == "+"):
    print(a1+a2)
elif(y=="-"):
    print(a1-a2)
elif(y=="*"):
    print(a1*a2)
elif(y=="/" and a2!=0):
    print(a1/a2)
else:
    pass