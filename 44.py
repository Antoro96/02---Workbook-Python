month = input("Enter the name of the month: ")
day = int(input("Enter the day: "))

if month == "January" and day == 1:
    print("January 1st is New Year's Day.")
elif month == "December" and day == 25:
    print("December 25th is Christmas")
elif month == "July" and day == 1:
    print("July 1st is Canada Day.")
else:
    print("There's not Holidays!")
    exit()
