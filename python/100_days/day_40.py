#exercise_no_4
def coding():
    text=input("Give Your Plane Message:")
    words=text.split(" ")
    for word in words():
        if(len(word<=2)):
            for i in range(len(word),0,-1):
                pass
            else:
                pass
    print("Your Secret Message is:")
def decoding():
    text=input("Give Your Secret Message:")
    pass
while True:
    print("Which actvity do you like to perform? \n1. Coding \n2.Decoding")
    x=int(input("Write the activity number"))
    if (x==1):
        coding()
    elif(x==2):
        decoding()
    else:
        print("!!!!!! ERROR!!!!!!  No Programe Fpund")
        break

    