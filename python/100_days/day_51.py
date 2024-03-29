#seek()
file=r"D:\Programing\Coding_Generator\Python\Hundred_dayes_of_python\day_51.txt"
# with open(file, 'r') as main:
#     #print(type(main))
#     main.seek(10)
#     print(main.read())
#     print(main.tell())
#     main.close()
    
with open(file,"a+") as main:
    main.write("\nHi I am python ")
    main.truncate(5)
    print(main.readlines())