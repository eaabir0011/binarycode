def main(stment):
    while True:
        int1,prmpt,int2 = stment.partition("/")
        int1=int(int1)
        int2=int(int2)
        try:
            result = (int1/int2)*100
            if(result<= 1):
                print("E")
            elif(result>=100):
                print("F")
            else:
                print(f"{result}%")
            break
        except ValueError or ZeroDivisionError:
            return main()

if(__name__ == "__main__"):
    x =main(input("Fraction "))
    