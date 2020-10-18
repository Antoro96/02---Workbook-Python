month = input("Enter the name of the month: ")
day = int(input("Enter the day number:"))

if month == "January" or month == "February":
    season = "Winter"
elif month == "March":
    if day <20:
        season = "Winter"
    else:
        season = "Spring"
elif month == "April" or month == "May":
    season = "Spring"
elif month == "June":
    if day<20:
        season == "Spring"
    else:
        season == "Summer"
elif month == "July" or month =="August":
    season = "Summer"
elif month == "September":
    if day<20:
        season = "Summer"
    else:
        season = "Autumn"
elif month == "October" or month=="November":
    season = "Autumn"
elif month == "December":
    if day < 20:
        season = "Autumn"
    else:
        season = "Winter"

print("The", day, "of the", month, "is in the", season)


    

