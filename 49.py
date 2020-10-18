magnitude = float(input("Enter the magnitude: "))

if magnitude < 2:
    print("The earthquake is micro.")
elif 2 <= magnitude < 3:
    print("The earthquake is very minor.")
elif 3 <= magnitude < 4:
    print("The earthquake is minor.")
elif 4 <= magnitude < 5:
    print("The earthquake is light.")
elif 5 <= magnitude < 6:
    print("The earthquake is moderate.")
elif 6 <= magnitude < 7:
    print("The earthquake is strong.")
elif 7 <= magnitude < 8:
    print("The earthquake is major.")
elif 8 <= magnitude < 10:
    print("The earthquake is great.")
elif magnitude >= 10:
    print("The earthquake is meteoric.")
