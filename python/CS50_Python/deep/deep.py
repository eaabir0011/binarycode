answer=input("What is the Answer to the Question of life the universe and Everything?")
answer=answer.lstrip().rstrip()
if(answer=="42" or answer.lower()=="forty-two" or answer.lower()=="forty two"):
    print("Yes")
else:
    print("No")