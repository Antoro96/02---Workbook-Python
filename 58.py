month_31 = [1, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

if year %400 == 0:
  isLeapyear = True
elif year %100 == 0:
  isLeapyear = False
elif year %4 == 0:
  isLeapyear = True
else:
  isLeapyear = False


if isLeapyear == True:
  if day == 31 and month < 12:
    day = 1
    month = month + 1
  elif day == 31 and month == 12:
    day = 1
    month = month + 1
    year = year + 1
  elif month in month_31 and day< 31:
    day = day + 1
  elif month in month_31 and day == 31:
    month = month + 1
  elif month in month_30 and day< 30:
    day = day + 1
  elif month in month_30 and day == 30:
    month = month + 1
    day = 1
  elif month == 2 and day < 29:
    day = day + 1
  elif month == 2 and day == 29:
    month = 3
    day = 1

  
  print("Year: %d" %(year))
  print("Month: %d" %(month))
  print("Day: %d" %(day))
  


else:
  if day == 31 and month < 12:
    day = 1
    month = month + 1
  elif day == 31 and month == 12:
    day = 1
    month = month + 1
    year = year + 1
  elif month in month_31 and day< 31:
    day = day + 1
  elif month in month_31 and day == 31:
    month = month + 1
  elif month in month_30 and day< 30:
    day = day + 1
  elif month in month_30 and day == 30:
    day = 1
    month = month + 1
  elif month == 2 and day < 28:
    day = day + 1
  elif month == 2 and day == 28:
    month = 3
    day = 1

  #print(year,"-", month,"-", day,"-")
  
  print("Year: %d" %(year))
  print("Month: %d" %(month))
  print("Day: %d" %(day))