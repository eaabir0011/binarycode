#programe of coke 
def main():
    i = 50
    total_user=0
    while True:
        print("Amount Due:",i)
        gvn_coin=int(input("Insert  Coin:"))
        if(gvn_coin != 25 and gvn_coin != 5 and gvn_coin != 10 ):
            return main()
        else:
            i = i - gvn_coin
            total_user = total_user + gvn_coin
            if(i == 0 or i <= 0 and total_user> 50):
                print("Change Owed:", total_user-50)
                break 

if (__name__ == "__main__"):
    main()