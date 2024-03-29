# Exercise_5
# game of snack water gun 
# snack will hunted by gun 
# gun will hunted by water 
# water will hunted by snack

#Computing system 
item="0"
score=0    
print("Launch The game")
#user system
while True:
    import random
    x=random.randint(-1,1)
    if(x==-1):
        item="water"
    elif(x==0):
        item="gun"
    else:
        item="snack"
    user=input("Press S for Snack and W for water and G for gun. To exit press E ")
    if (user.capitalize()=="E" or user.capitalize!="G" or user.capitalize()!="W" or user.capitalize()!="S"):
        break
    #logic of game
    if(user=="s" and item=="water"):
        score=score+1
    elif(user=="g" and item=="snack"):
        score=score+1
    elif(user=="w" and item=="gun"):
        score=score+1
    else:
        score=score
        
print("Your Score is", score)

# main game
