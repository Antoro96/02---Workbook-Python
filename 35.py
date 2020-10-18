years_human = int(input("Enter dog's age in human years: "))

if years_human <0:
    print("Age must be a positive number! ")
    exit()
elif years_human <=2:
    years_dog = years_human * 10.5
else:
    years_dog = 21 + (years_human - 2)/ 4

print("The dog's age in dog's years is: ", years_dog)
    
