for i in range(1,15):
    if(i==11):
        break
    #print(i)
    print("5 X",i,"=",5*i)
    
print("The programe is out of loop right now")

a=10
while(a>0):
    if(a==3):
        break
    print(a)
    a=a-1
print("Loop is broken")

for i in range(15):
    if(i==10):
        continue
    #skip the itretion
    print(i)

#do while loop
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break