#global segment 
global directory, file_name, file_type, num_question, num_option, file_path,file_link
def open_previous():
    global file_link
    file_link=repr(input("Give me your saved file link "))

def creat_file():
    import os
    directory = input("Give me the directory where you would like to create the file: ")
    file_name = input("Give the file name: ")
    file_type = input("Give the file type: ")
    
    # Combine directory, file name, and file type to create the file path
    file_path = os.path.join(directory, f"{file_name}.{file_type}")
    # Wrap the file_path in repr() if you want to print it with quotes
    # file_link = repr(file_path)
    return file_path

def question():
    creat_file()
    #Question Source Maker
    print("This segment is made for where the question have to save just asked it here")
    #making questions
    num_question=int(input("How many question do you like to ask?"))
    num_option=int(input("How many options there will be?"))     
    with open(file_path, "a") as main_file:
        # Open the file in "a" (append) mode
        for i in range(1,num_question+1,1):
            question_number=str(i)
            global question_value
            questio_value=input(f"Write your Question {i} here:")
            globals()[question]=questio_value
            main_file.write(f"{question_number}.{question_value}\n")
            for _ in range(1,num_option+1):
            #this segment for asking option 
                option=str(_)
                option_value=input(f"\nGive the option {_} here")
                globals()[option]=option_value
                main_file.writelines(f"{option}.{option_value}\n")
        
def answer():
    #making condditon for opening previous saved file or open the recent file
    with open(file_link,"r") as main_file:
        print(main_file.readlines())

#main_page 
while True:
    ask=input("What do you would like to do? \n1.Ask new question  \n2.answer the previous questions")
    if(ask=="1"):
        question()
    else:
        answer()