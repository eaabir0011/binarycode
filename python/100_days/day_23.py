l=[1,2,3,4,6]
print(l)

#for addded any value at last index of a list
l.append(7)
print(l)



# give the list accroding to orderly ascendingly
l=[45,11,12,34,56,77,90]
print(l.sort())


#descending
l.sort(reverse=True)
print(l)

#the privous format again
l.reverse()
print(l)


#index tell us is a number in  a list ?
#print(l.index(4))
#here 4 is not in a list thats why an eror is coming


#Help us to find how many times a value listed in a list
print(l.count(11))


#this use to make a copy of a list
m=l.copy()
m[0]=0
print("\n",m,l)


#we use this for insert a value in the list
l.insert(2,675)
print(l )


#Work with 2 list
m=["Abir","Sabik","Jabir"]
# l.extend(m) #means break the m and input all the items at the last of l
# print(l )
#another process 
k=l+m #here actuall I'm merging m list
print(k)
#same like first and second methods(just unlock once )


