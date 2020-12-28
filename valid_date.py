date = input("Enter the date in dd/mm/yy format: ")
day, month, year = date.split('/')
day = int(day)
month = int(month)
year = int(year)

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
	max_days = 31
elif month==4 or month==6 or month==9 or month==11:
	max_days = 30

elif year%4==0 and year%100!=0 or year%400==0:
	max_days = 29
else:
	max_days = 28

if month<1 or month>12:
	print("Entered date is invalid, please check the range of date.")
elif day<1 or day>max_days:
	print("Entered date is invalid, please check the range of day.")
else:
	print("Entered date is valid.")



