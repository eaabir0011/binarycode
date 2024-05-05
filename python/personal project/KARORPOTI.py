print("This Programme is made for quiz programme")

#code of questions
ques_num=int(input("How much Question dou you need??"))
num_option=int(input("How many options per question?"))
list_of_option=[]
for i in range(1,ques_num+1,1):
    question_name="Question"+str(i)
    question_value=input(f"Give the question number {i}")
    globals()[question_name]=question_value
    if(question_value=="none"):
        break
    #now this time I'll make the option part
    for _ in range(1,num_option+1,1):#making mcq process
        option_name="Option"+str(_)
        option_value=input(f"Option_{_}")
        globals()[option_name]=option_value
    correct_answer=int(input(f"Correct Answer for Question{i} is :"))

#segment for the candidet
marks=0 
prize=0
print("You will get 1000 Bdt for each question")
for a in range(1,ques_num+1,1):
    print(question_name,question_value)
    for b in range(1,num_option+1,1):
        print("\n ",option_name)
        
    ask_answer=int(input("What is the correct answer?"))
    if(ask_answer==correct_answer):
        marks=marks+1
        prize=prize+1000
        print("Congratulation Your Answer is correct")
    else:
        print(f"Sorry your answer is wrong. The correct answer is option{correct_answer}")
print(f"Your total score is {marks} and your earning is {prize}")