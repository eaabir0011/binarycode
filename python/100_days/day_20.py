#functio()
# for i in range(15):
#     print("\n",i+1)

def gmean(a,b):
    mean=(a*b)/(a+b)
    print("The gmean is:",mean)

def greater(a,b):
    if(a>b):
        print("The Largest Number is:",a)
        print("The smallest NUmber is:",b)
    elif(a<b):
        print("The largest number is:",b)
        print("The smallest number is:",a)
    else:
        print("They are equal")

def lessthen(a,b):
    pass


a=int(input("Give the first integer:"))
b=int(input("Give the second integer:"))
greater(a,b)
gmean(a,b)
