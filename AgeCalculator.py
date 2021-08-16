from datetime import date

username_input=input("Hi, what is your name?  ")

user_input=input("Hi "+username_input+" what is your date of Birth? ")

print (user_input)


##todaydate=todaysdate.strftime("%d/%m/%Y")
#print ("Today's date is the ", todaydate)

def calculateage(user_input):
    todaysdate=date.today()
    age=todaysdate.year-user_input.year
    ((todaysdate.month, todaysdate.day) <
         (user_input.month, user_input.day))
 
    return age
     
# Driver code
print(calculateage, "years")
