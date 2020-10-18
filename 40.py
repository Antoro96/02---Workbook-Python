side1 = int(input("Enter the lenght of first side: "))
side2 = int(input("Enter the lenght of second side: "))
side3 = int(input("Enter the lenght of third side: "))

if side1 == side2 == side3:
    print("It's an Equilater triangle.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("It's an Isosceles triangle.")
else:
    print("It's a Scalen triangle.")


