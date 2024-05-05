"""making Funcion"""
def fruit(s):
    chl={
        
        "apple"             :130,
        "avocado"           :50,
        "banana"            :110,
        "cantaloupe"        :50,
        "grapes"            :90,
        "honeydew melon"    :50,
        "kiwifruit"         :90,
        "lemon"             :15,
        "lime"              :20,
        "nectarine"         :60,
        "orang"             :80,
        "peach"             :60,
        "pear"              :100,
        "pineapple"         :50,
        "plums"             :70,
        "strawberries"      :50,
        "sweet cherries"    :100,
        "tangerine"         :50,
        "watermelon"        :80
    }
    if (s in chl.keys()):
        print("Calories:",chl[s]) 
    else:
        print("")
    

"""Execution of function and executive programe s"""
if (__name__ == "__main__"):
    frt=fruit(input("Item: ").lower())

