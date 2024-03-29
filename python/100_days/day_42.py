marks=[12,56,94,36,24,1,24]
index=0 
for mark in marks:
    print(mark)
    if (index==3):
        print("Harry is awesome")
    index+=1
    
cousin=["Abir"," Sabik","Jabir","Tasim","Tahmid"]
for index, name in enumerate(cousin,start=2):
    print(name)
    print("He is Gammer") if (index==3) else""

string_1=" Abir is a fuckish boy who always love sex" 
print(len(string_1))
for index, i in enumerate(string_1,start=1):
    print(i)
    print(" He is fuckish ") if(index==len(string_1)) else""