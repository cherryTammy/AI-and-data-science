city=input("which city are you in ?")
temperature=float(input("please enter the temperature"))
if temperature>35:
    print("it's very hot today")
    
if temperature>25:
    print("great day to go outside")
    
else :
    print("grab a jacket before going outside")
    
if temperature>35:
    print("scorching hot")
elif temperature>25:
    print("warm and sunny")
elif temperature>15:
    print("cool and brezzy")
else:
    print("cold stay warm")
     
import datetime
import calendar
now=datetime.datetime.now()
print("the time is ",now)
print(calendar.calendar(now.year))

    
    
