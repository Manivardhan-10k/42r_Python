from datetime import datetime ,timedelta 
print(datetime.now())   

#now  --> current date and time 

# 29/07/2025 
# 29/7/25 
# 7/29/25
# 25/7/29


#strptime  --> parse time from a string
# print(datetime.strptime("01/01/2020","%d/%m/%Y")) 
# print(datetime.strptime("january/10/03","%B/%d/%y")) 
# print(datetime.strptime("01/12/1999","%d/%m/%Y")) 

#strftime 
# print(datetime.strftime()) 
# now=datetime.now()
# print(now.strftime("%b/%d/%y %A %H:%M")) 
# print(now.strftime("%H:%S :%M  %a")) 

# %Y -> full year 2025 
# %y -> 25 
# %B  -> month name 
# %b -> short month name  
# %m -> month number 
# %A  --> weekday name 
# %a --> abbrevated name 
# H  --> hours in 24 format 
# I  --> 12 hour format 
# M  --> minutes
# S  -> seconds


#replace 

# cur=datetime.now()
# print(cur.replace(2024,1,1,23,55,32))

# venu_bday=datetime.strptime("1999/12/10","%Y/%m/%d") 
# venu_bday=venu_bday.replace(1947,8,15)
# print(venu_bday.weekday())
# print(datetime.now().weekday())
# print(datetime.now().isoweekday()) 



# print(datetime.now() + timedelta(days=28)) 
# print(datetime.now() - timedelta(days=90,hours=10,seconds=50))



# ist + 5+:30
#gmt 

# print(datetime.now().isoformat())
print(datetime.now().date())
print((datetime.now() + timedelta(hours=100)).time()) 
print((datetime.now()   -   datetime.strptime("1/1999/12","%d/%Y/%m")))

