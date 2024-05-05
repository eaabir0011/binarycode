while True:
    print("Write Exit from quite this programme")
    print("\nThis Programme doesn't support float numbers ".upper())
    year=input('Give the  me the year I wil check is this year is a leap year or not?')
    if (year=="exit"):
        break

    year=int(year)
    if year%4==0 and year%100!=0:
        print(year, 'is a leap year')
    elif year%4==0 and year%400==0 and year%100==0:
        print(year, 'is a leap year')
    else:
        print(year, 'is not a leap year')