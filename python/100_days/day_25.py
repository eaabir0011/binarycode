#tuple class 2
#
countries=("Spain", "Italy", "England", "Germany", "France",  "India")
temp=list(countries)
print(temp)
temp.pop(5)
temp.append("USA")
countries=tuple(temp)
print(countries)

