#tuple
tup=(1,5,6,112,12,34,"Green",True) #can not change the element
print(type(tup),tup)
print(len(tup))
#negetive indexing
print(tup[-2])
if 3421 in tup:
    print("Yes 3421 in tup")

tup_2=tup[1:5]
print(tup_2)
tup_3=tup[1:5:2]
print(tup_3)
