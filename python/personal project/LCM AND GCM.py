def numbers_fun(num_1,num_2):
    if(num_1>num_2):
        max=num_1
        min=num_2
    else:
        max=num_2
        min=num_1
    #Check activity
    #start Calculation of gcd
    counter=max
    while(counter>1):
        max/counter
        min/counter
        if(max%counter==0 and min%counter==0): #logic 
            break
        else:
            counter=counter-1            
    gcd=counter
    lcd =(num_1*num_2)/gcd
    print ("The Gcd is",gcd,"The Lcd is",lcd)

while True:
    print("This programe only supports GCD and LCD between two number")
    num_1=int(input("Input the first number:"))
    num_2=int(input("input the second number:"))
    numbers_fun(num_1,num_2)
    print("If you want to continue more press on Y or press N for exit")
    user=input()
    if (user!="y" and user=="n"):
        break 

exit()
