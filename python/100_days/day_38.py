#raise keyword
a=input(" Enter a value between 5 to 9")
if(a!=" quit"):
    raise TypeError("other string doesn't support")
else:
    a=int(a)
    if(a<5 or a>9):
        raise ValueError(" Value should be between 5 to 9")
    
quit()    