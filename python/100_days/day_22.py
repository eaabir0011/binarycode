# #list_in_python

# marks=[3,4,5,6,7,"harry",True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# if "harry" in marks:
#     print("Yes")


#Abir self work

# a=["Abir","Ety","Harry","Lamiya","Sabik","Jabir",True,3,4,5,6,]
# print("The data type of a is",type(a))
# print("The lentgh of a is",len(a))
# for _ in range(0,len(a),1):
#     print(a[_])
#     print("The data type of ",a[_],"is",type(a[_]))


#get input in list
li=[]

amount=int(input("How much value you would like to input for your list?"))
for _ in range(0,amount,1):
    print("Enter the value",_+1)
    li_value=input()
    li.append(li_value)#collected from AI but I don't know

print("Your list is:",li)
print("The lenght of your list is:",len(li))
#list slcing
#print(li[1,len(li),3])


#list comprehension
# lst=[i for i in range(4)]
# print(lst)