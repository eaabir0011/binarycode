import os
folders=int(input("How many folders do you like to make?"))
os.mkdir("Python Basic")
for i in range(0,folders,1):
    os.mkdir(f"Python Basic/Day_{i+1}")\
        
print("Programme Executed")