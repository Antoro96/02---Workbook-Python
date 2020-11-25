year = int(input("Enter a year: "))


if year %400 == 0:
    isLeapYear = True
elif year %100 == 0:
    isLeapYear = False
elif year %4 == 0:
    isLeapYear = True
else:
    isLeapYear = False

if isLeapYear == True:
    print("This", year, "is a leap year.")
else:
    print("This", year, "is not a leap year.")