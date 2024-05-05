class cat():
    def __init__(self,color,action) -> None:
        self.color = color
        self.action = action 
        
    def view(self):
        print(self.color,"color cat is ",self.action)
    
    def compare(self,ct):
        if(self.action == ct.action):
            print("both cats are", self.action)
        else:
            print("They are doing different action")

c1=cat("brown","eating")
c2=cat("","")
c2.color = "white"
c2.action = "sleeping"
c1.view()
c2.view()
c1.compare(c2)
c1.action = "sleeping"
c2.compare(c1)
cat_3=cat("","")
c1.compare(cat_3)
c2.compare(cat_3)