def func_1():
    try:
        li=[1,2,3,4,5,6]
        x=int(input("Please enter your index number: "))
        print(li[x])
        return 1
    except:
        print("Some Error Occured")
        return 0
    finally:
        print("I always executed")

y=func_1()
print(y)
