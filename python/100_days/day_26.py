#Good morning sir
import time
times= time .strftime("%H:%M:%S")
print(times)
hour=int(time .strftime("%H"))
minute=time .strftime("%M")
second=time .strftime("%S")
print("The time is:",hour,minute,second)
if(hour>0 and hour<=12):
    print("Good Morning")
elif(hour>12 and hour<=15):
    print("Good Noon")
elif(hour>15 and hour<=18):
    print("Good Afternoon")
elif(hour>18 and hour<=20):
    print("Good Evening")
elif(hour>20 and hour<24):
    print("Good Night")
else:
    print("No in time zone")