class employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}bd@gmail.com"
    
    def explain(self):
        return f"This is the employe {self.fname} {self.lname}"
    @property
    def email(self):
        if(self.fname == None or self.lname == None):
            return "Email is not set. Please use setter for using email"
        return f"{self.fname}.{self.lname}bd@gmail.com"

    # making setter a setter takes a attribute and change other other attributes basis on the input 
    @email.setter
    def email(self,string):
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]
    
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
    
bd_lover = employee("Allama","Sayeedi")
bd_hater = employee("Sheikh","Hasina")
# print(bd_lover.explain())
bd_lover.fname = "doctor"
print(bd_lover.explain())
# print(bd_lover.email)
bd_lover.email = "fuck.duck@gmail.com"

del bd_lover.email
print(bd_lover.email)
