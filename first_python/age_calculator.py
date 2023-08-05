 
from datetime import date


bornYear = int(input("Enter the year that you born: "))

thisYear = date.today().year

print("your age is: " + str(thisYear - bornYear))

