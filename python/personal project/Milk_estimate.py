#day calculation
import datetime
ask=int(input("For which month do you like to calculate the bill of milk? Give me the month number like(for Jan you will input 1):"))
print("Invalid input") if (ask>12 or ask==0) else""
# month=datetime.datetime(ask)
# print(month)
if(ask==1 or ask==3 or ask==5 or ask==7 or ask==8 or ask==10 or ask==12):
    days=31 
elif(ask==2):
    days=28 
else:
    days=30 
    
strt_date=int(input("From which day of month do you like to calculate?"))
am_milk=0
escp_day=int(input("How many dayes you didn;t get milk? Tell me the number of days."))
#calculating the amount of milk
for i in range(strt_date,days,2):
    am_milk=am_milk+500
    
#total milk in month
am_milk=am_milk-(escp_day*500)
total_milk=am_milk/1000
price_rate=80
#amounmt of bill
bill=total_milk*price_rate
print(f"You have consumed {total_milk} L and your bill is {bill} BDT")