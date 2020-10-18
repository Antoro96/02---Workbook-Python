level = int(input("Enter a sound level in decibel: "))

if level > 131:
    print("The noise is too loud!")
elif level == 130:
    print ("Jackhammer")
elif level >= 106:
    print("Gas Iawnmower")
elif level >= 70:
    print("Alarm Clock")
elif level >= 40:
    print("Quiet Room")
else:
    print("The noise is too quite!")
    
