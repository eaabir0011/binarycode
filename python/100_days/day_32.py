
# s1={1,2,3,4,5}
# s2={3,9,8}
# print(s1.union(s2))
# s1 .update(s2)
# city={"Dhaka","Chattogram","Sylhet","Barishal","Khulna"}
# town={"Nework","Las Vegas","California","San Fransisco"}
# print(city.union(town))
# print(city.intersection(town))
# place1={"CRB","Coxes Bazar","khagrachari","Bandarban","Neval","Sea Beach"}
# place2={"Bandarban","CDA","Coxes Bazar","Alutila","Balo char","Dengarchar"}
# print("This is union oparation", place1.union(place2))
# print(place1)
# print(place2)
# print("This is inter section oparetion", place1 .intersection(place2))
# print('This is symantic operation', place1.symmetric_difference(place2))
# s1 .update(place2)
# print("The Updated Set",s1)

muslim_country={"philistain","Bangladesh","Pakistan","Saudi Arab","Qatar","Turkey","Viyetnam"}
nonmuslim_country={"USA","Canda","Australia","India","Israel","Uk","Crotia","Finland","Swizerland"}
#union and update 
print(muslim_country.union(nonmuslim_country))
muslim_country.update(nonmuslim_country)
print("Updated muslim countries are",muslim_country)
#actually both of the function is almost same


#intersection and intersection update
group1={"Abir","Sabik","Jabir","tasim","tahmid","sadman","Jara","Tashfeen".upper()}
group2={"Aurpa","Raifa","Ishadi","Iftia","Sakin","Abir","Sabik","Jabir"}
print(group1 .intersection(group2))
group2 .intersection_update(group1)
print("The Updated group is ", group2)

#symmetreic
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

#symmetric_difference_update
s1={1,12,21,3,4,5,65}
s2={1,2,3,34,3,4,56,6,5}
s1.symmetric_difference_update(s2)
print("The updated symmetric difference set is ", s1)

#difference and difference update (A/B or A-b in mathematics)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

s={1,2,3,4,5,6,7,8,9}
f={2,4,6,8,10}
print(s)
print(f)
print(s.difference(f))
x=f .difference_update(s)
print(x)

#is this(dis) joint?
set1={1,2,3,5,7}
set2={0,2,4,6,8}
print(set1.isdisjoint(set2))

body={0,1,2,3,4,5,6,7,8,9,10}
body1={0,11,12,13,14,15,16,17,18,19,20}
print(body .isdisjoint(body1))

#is super set (issuperset())
print(set1 .issuperset(set2))

f1={i for i in range(10)}
f2={a for a in range(20)}
print(f1)
print(f2)
print(f1 .issuperset(f2))
print(f2 .issuperset(f1))

# is sub set?? issubset()
print(f1 .issubset(f2))
print(f2 .issubset(f1))
