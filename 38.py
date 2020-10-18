month = str(input("Enter the name of a month: "))

if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "Dicember":
    days = 31
elif month == "April" or month == "June" or month == "September" or month == "November":
    days = 30
elif month == "February":
    days = "28 or 29"
else:
    print("This is not the name of a month!")
    exit()

print("There are", days, "days in it.")
