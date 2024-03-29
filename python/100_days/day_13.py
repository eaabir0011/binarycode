#String_method
# Strings is immutable any body can't change a string. 

#uppercase function
a="Abir"
print(a. upper())
#lowercase function
print(a. lower())
# if any string have special character at tail side we can remove this by rstrip function
#this function can remove special charecter from tail side
b="**^&baby !!***"
print(b .rstrip("!,*"))
#replace in string
print(a .replace("Abir","Tutor_Harry"))
#if I want to include more function inside a function the process is 
print("\nThis is the process how to include more function inside a function")
print("\n",a .replace("Abir","Tutor_Harry") .upper())
# replace function more
c="Abir####Abir****Tutor_Harry"
print(c .replace("Abir","Tutor_Harry") .upper() .rstrip("#,*"))
#split 
#this funtion made a string to a list by special characeter
a="Abir_Tutor_Harry"
print(a.split("_"))
#capitalazed
a="abir is big dog"
print(a .capitalize())
print("Here in this string I have inputed small letter a but the output comes capital A")
b="introduction TO Python"
print('I\'d written here')
print(b .capitalize())
#Center()
str="I\'ve a girlfriend who\'s name is Lamiya Muntakim"
print(len(str))
print(len(str. center(50)))
print(a .count("abir"))
#endswith()
#this function basically check a string ends with the destinated character or symbol
#let's give an example
str_1="Hello everyone. This is Abir. Abir is learning python. what a great!!!!!!"
print(str_1 .endswith("!"))
# Here in my string finished with ! thats why result comes true

str="once there was a king name midas"
print(str.find("was"))

a_string="I love porn. My favorite porn star is Ava Adam, Angela White, Tina kay, India Summer, Eva Notty"
for i in a_string:
    print(i)
print(a_string.index("Ava Adam"))
print(a_string .find("A Adam"))
print(a_string.isalnum())

name_string="My name is Sheikh Iftekhar Hossain Abir"
print(name_string.swapcase())
print(name_string.title())
print("Now I'm Exiting Remember my name I'm Python your Friend")
exit()