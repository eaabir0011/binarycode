print("Hey this is python your friend. How are ypu man? Welcome you once more again to my world".title())
#topic Dictionary
abir_result={
    "Bangla":90,
    "English":100
}

print(type(abir_result))
print(abir_result["English"])

employe_id={
    344:"Abir",
    56:"Sabik",
    34:"Jabir"    
}
print(employe_id)
print(employe_id[56])

#access system we can access a dictionary 2 ways

print(employe_id[344])
print(employe_id.get(341))
#multiple key access
print(employe_id.keys()) #for using key
print(employe_id.values()) #for using value
for i in employe_id.keys():
    print(i)
for _ in employe_id.values():
    print(_)
#print("Hey I'm Python Your Programme Helper Who is exiting Good Bye".title())
#exit()

info={"Name":"Abir","Age":21,"Proffesion":"App Designer and Web Developer"}
print(info.keys())
print(info.values())
for i in info.keys():
    print(f"The {i} of value is {info[i]}")

for key,value in info.items():
    print(f" {key} : {value}")