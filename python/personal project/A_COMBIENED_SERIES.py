def series ():
    a=int(input("Give the starting number:"))    
    b=int(input("Give the ending number:"))
    p=int(input("How much would be the power?:"))
    d=int(input("What would be the difference between?"))
    counter=a
    num=0
    result=0
    for _ in range(a,b+1,d):
        num=counter
        num=num**p
        counter=counter+d
        result=result+num
        print(num, end=("+"))
    
    print("\nThe result is:",result)
print("This is a programe for series . You can give a starting point, ending point, power, difference as you wish. So use this programe and enjoy the math".capitalize())
while True:
    series()
    print("Do you like to continue if yess press 'Y' else it will close ")
    user=input()
    if (user!="Y"):
        break
exit()

