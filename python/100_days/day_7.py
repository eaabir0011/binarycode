# print(15%6)
# print(15//6)
#making a calculator
num_1=input("\n Give your first number")
operator=input("\n Select your operator")
num_2=input("\nGive your second number")
num_1=int(num_1)
num_2=int(num_2)
if (operator=="+"):
    print(num_1+num_2)
elif (operator=="-"):
    if (num_1>num_2):
        print(num_1-num_2)
    else:
        print(num_2-num_1)
elif (operator=="*"):
    print(num_1*num_2)
elif (operator=="/"):
    if (num_2==0):
        priint("math error")
    else:
        print(num_1/num_2)
        print("Solid is:", num_1//num_2)
        print("Remainder is:", num_1%num_2)
else:
    print("This programe only supports \"\nAddition\" \n\"Substraction\"\n\"Multipicaioin\"\n\"Division\"")