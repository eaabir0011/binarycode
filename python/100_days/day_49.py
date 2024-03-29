#read write and append for a file 
# f=open("myfile.txt","r")
# print(f.read())
# f.close()
# with open("writting_file.txt","w") as file_1:
#   # file_1=open("writtng_file.txt","w")
#   msg=input("Give your text to add the file ")
#   file_1.write(msg)
#   print(file_1)

# with open("writting_file.txt","a") as file_2:
#   msg1=input("Give your text here for added more lines in your text")
#   file_2.write(msg1)
#   print(file_2.read())

# while True:
#   with open ("D:\Programing\Coding_Generator\Python\100_dayes_of_python\day_49.txt","a") as file_3:
#     msg=input("Give your Message for text file else Stop ")
#     if(msg=="stop"):
#       break
#     file_3.write(msg)


with open("D:\Programing\Coding_Generator\Python\Hundred_dayes_of_python\day_49.txt","a") as file:
    file.writelines("\n This is a new line ")
with open("D:\Programing\Coding_Generator\Python\Hundred_dayes_of_python\day_49.txt") as file:
    print(file.readlines())
