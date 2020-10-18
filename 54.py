VIOLET = 380
BLUE = 450
GREEN = 495
YELLOW = 570
ORANGE = 590
RED = 620
TOP = 750

WAVELENGTH = "The color is %s."

wavelength = int(input("Enter the wavelength in nanometers. Choose 380 - 750: "))
    
if VIOLET <= wavelength < BLUE:
    print(WAVELENGTH % ('violet'))
         
elif BLUE <= wavelength < GREEN:
    print(WAVELENGTH % ('blue'))
          
elif GREEN <= wavelength < YELLOW:
    print(WAVELENGTH % ('green'))
          
elif YELLOW <= wavelength < ORANGE:
    print(WAVELENGTH % ('yellow'))
          
elif ORANGE <= wavelength < RED:
    print(WAVELENGTH % ('orange'))
          
elif RED <= wavelength < TOP:
    print(WAVELENGTH % ('red'))
          
else:
    print("Choose 380 - 750.\n")
