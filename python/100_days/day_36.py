#try except code
#exception handling
a=input("Give me a number so that I can give you a multiple table")
print(f" multiplication table of {a} is:")
try:
    for i in range(10):
        print(f"{a} X {i+1} = {int(a)*(i+1)}")
except:
    print("Invalid Input")

print("Programme Terminated")