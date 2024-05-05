#I'm making this programe for calculate the factorial
def factorial(n):
    #I caqlled a function that name is factorial which will recieve only one integer
    result=1 #for finding result i've need a varriable
    for i in range(0,n,1):
        result=result*(i+1) #main activity of this programe
        #update the i and multiple with result
    return result

    
print("Hey this is python who is all time ready for help you".capitalize())
while True:
    x=int(input("Give the number for calculate the value of factorial"))
    final=factorial(x)
    print(x,"!=",final)
    user=input("Do you want to continue? If yes press 'Y and hit the enter button'")
    if (user!="y"):
        break
exit()
