# not uploaded 
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # executive function 
    s=""
    if(len(s)>=2 and len(s)<=6):
        if(s[0] == 0):
            return False
        else: 
            if(s[-2].isalnum and s[0:2].isalpha):
                return True
            else:
                return False
        

"""Executing main program"""
if(__name__ == "__main__"):
    main()
