MICROWAVE = 3 * 10 ** 9
INFRARED = 3 * 10 ** 12
VISIBLE = 4.3 * 10 ** 14
ULTRAVIOLET = 7.5 * 10 ** 14
X = 3 * 10 ** 17
GAMMA = 3 * 10 ** 19

frequency = int(input("Enter the frequency of the radiation: "))

if frequency < MICROWAVE:
  print("Radio Waves\n")

elif MICROWAVE <= frequency < INFRARED:
  print("Microwaves\n")

elif INFRARED <= frequency < VISIBLE:
  print("Infrared Light\n")

elif VISIBLE <= frequency < ULTRAVIOLET:
  print("Visible Light\n")

elif ULTRAVIOLET <= frequency < X:
  print("Ultraviolet Light\n")
  
elif X <= frequency < GAMMA:
  print("X-rays\n")
  
elif frequency >= GAMMA:
  print("Gamma Rays\n")
