class cat:
    def __init__(self,name,activity) -> None:
        self.name = name 
        self.activity = activity
        pass
    
    def view(self,num,clr):
        num = num + 5
        clr1 = clr
        clr1[0]= "green"
        print("Method Inside", num)
        print("method Inside",clr)
        pass

     
color=["Black", "red","yellow","blue"]
c1 = cat("white","jumping")
c1.view()