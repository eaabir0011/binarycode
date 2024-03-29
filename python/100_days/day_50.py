#readlines method is used for a lots of line in file 
file_path=r"D:\Programing\Coding_Generator\Python\Hundred_dayes_of_python\day_50.txt"
# with open(file_path,"r") as main_file:
#     while True:
#         line=main_file.readlines()
#         if not line:
#             break
#         print(line)
        
# main_file.close()

#writelines in used for write a lots of line in programme
marks=[12,56,94,36,24,1,24]
with open(file_path,"a") as main_file:
    for mark in marks:
        main_file.write(str(mark) + '\n')