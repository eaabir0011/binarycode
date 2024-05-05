class person:
    name = "Abir"
    occupation = "Softwere Developer"
    networth = 50
    def info(self):
        print(f"{self.name} is a {self.occupation} in profession and earn {self.networth}")

a=person()
b=person()
a.name = "Sabik"
a.occupation = "Businessman"
b.name = "Jabir"
b.occupation = "Service Holder"
b.networth = 80
a.info()
b.info()
