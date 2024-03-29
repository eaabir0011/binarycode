#global vs local 
x=4
# print(x)
def hello():
    global x
    x=5
    y=-10
    print("The Local varriable y is ",y)
 
    
hello()
print(f"The Global X is {x}")