print("Find Your Cousin")
cousin=[]
while True:
    cousin_name=input("Give your cousin Name (write \'none\' if you have no one or no else left):")
    if(cousin_name=="none"):
        break
    else:
        cousin.append(cousin_name)

if(len(cousin)==0):
    print("You have No cousin Sorry!")
else:
    print(f"You have {len(cousin)} cousins and name of your cousins are {cousin}")