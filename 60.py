TOTAL_SPACES = 38
BLACK_SPACES = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
RED_SPACES = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
GREEN_SPACES = [0, 00]

number = int(input("Enter a number of roulette: "))

if number in BLACK_SPACES:
    print("The spin resulted in", number,"...")
    print("Pay", number)
    print("Pay Black")
    print("Pay Odd")
    print("Pay 1 to 18")
elif number in RED_SPACES:
    print("The spin resulte in", number,"...")
    print("Pay", number)
    print("Pay Red")
    print("Pay Even")
    print("Pay 19 to 36")
elif number in GREEN_SPACES:
    if number == 0:
        print("Pay", number)
    elif number == 00:
        print("Pay", number)
    else:
        print("Not exist")
else:
    print("Not valid.")