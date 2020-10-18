big = [1, 3, 5, 7, 8, 10, 12]
small = [4, 6, 9, 11]

def leap(a):
  
  if a % 400 == 0:
    return True
  
  elif a % 100 == 0:
    return False
  
  elif a % 4 == 0:
    return True
  
  else:
    return False

while True:
  year = int(input("Enter the year:\t"))
  month = int(input("Enter the month:\t"))
  day = int(input("Enter the day:\t"))
  
  if leap(year):
    if day == 31 and month < 12:
      month += 1
      day = 1
    elif day == 31 and month == 12:
      month = 1
      day = 1
      year += 1
    elif month in big and day < 31:
      day += 1
    elif month in small and day < 30:
      day += 1
    elif month in small and day == 30:
      month += 1
      day = 1
    elif month == 2 and day == 29:
      month = 3
      day = 1
    elif month == 2 and day < 29:
      day += 1
    
    print()
    print("Year: %d" % (year))
    print("Month: %d" % (month))
    print("Day: %d" % (day))
    print()
  
  elif leap(year) == False:
    if day == 31 and month < 12:
      month += 1
      day = 1
    elif day == 31 and month == 12:
      month = 1
      day = 1
      year += 1
    elif month in big and day < 31:
      day += 1
    elif month in small and day < 30:
      day += 1
    elif month in small and day == 30:
      month += 1
      day = 1
    elif month == 2 and day == 28:
      month = 3
      day = 1
    elif month == 2 and day < 28:
      day += 1
    
    print()
    print("Year: %d" % (year))
    print("Month: %d" % (month))
    print("Day: %d" % (day))
    print()
    
