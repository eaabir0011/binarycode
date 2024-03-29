import os as os 
x=os.getcwd()
print(x)
# if(not os.path.exists("Python_Data")):
#     os.mkdir("Python_Data")
    
# for i in range(0,100):
#     os.mkdir(f"Python_Data/Day_{i+1}")
folders=os.listdir("Python_Data")
for folder in folders:
    print(folder)
    print(os.listdir(f"Python_Data/{folder}"))
print("Programme Terminated")
