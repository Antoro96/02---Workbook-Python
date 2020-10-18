day = int(input("Enter the number of day: "))
month = input("Enter the month: ")

if month == "January":
    if day<20:
        zodiacsign = "Capricorn"
    else:
        zodiacsign = "Acquarius"
elif month == "February":
    if day <19:
        zodiacsign = "Acquarius"
    else:
        zodiacsign = "Pisces"
elif month == "March":
    if day <21:
        zodiacsign = "Pisces"
    else:
        zodiacsign = "Aries"
elif month == "April":
    if day <20:
        zodiacsign = "Aries"
    else:
        zodiacsign = "Taurus"
elif month == "May":
    if day <21:
        zodiacsign = "Taurus"
    else:
        zodiacsign = "Gemini"
elif month == "June":
    if day<21:
        zodiacsign = "Gemini"
    else:
        zodiacsign = "Cancer"
elif month == "July":
    if day<23:
        zodiacsign = "Cancer"
    else:
        zodiacsign = "Leo"
elif month == "August":
    if day<23:
        zodiacsign = "Leo"
    else:
        zodiacsign = "Virgo"
elif month == "September":
    if day<23:
        zodiacsign = "Virgo"
    else:
        zodiacsign = "Libra"
elif month == "October":
    if day<23:
        zodiacsign = "Libra"
    else:
        zodiacsign = "Scorpio"
elif month == "November":
    if day<22:
        zodiacsign = "Scorpio"
    else:
        zodiacsign = "Sagittarius"
elif month == "December":
    if day<22:
        zodiacsign = "Sagittarius"
    else:
        zodiacsign = "Capricorn"

print("The", day, "of", month, "has got", zodiacsign)
