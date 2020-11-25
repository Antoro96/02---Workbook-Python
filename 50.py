from math import sqrt

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant <0:
    print("Number of roots: 0")
elif discriminant == 0:
    root = (-b + sqrt(discriminant))/ (2 * a)
    print("Number of roots: 1 Root: %f, %f" % (root))
elif discriminant >0:
    root1 = (-b + sqrt(discriminant))/ (2 * a)
    root2 = (-b - sqrt(discriminant))/ (2 * a)
    print("Number of roots: 2 Roots: %f, %f" % (root1, root2))
    
