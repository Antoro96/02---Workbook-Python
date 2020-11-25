RADIO_WAVES = 3e9
MICRO_WAVES = 3e12
INFRARED_LIGHT = 4.3e14
VISIBLE_LIGHT = 7.5e14
ULTRAVIOLET_LIGHT = 3e17
X_RAYS = 3e19
GAMMA_RAYS = []

FREQUENCY = "The frequency is %s"

frequency = float(input("Enter a value of frequency: "))

if frequency < RADIO_WAVES:
  print(FREQUENCY %("Radio Waves.")) 
elif RADIO_WAVES <= frequency < MICRO_WAVES:
  print(FREQUENCY %("Micro waves."))
elif MICRO_WAVES <= frequency < INFRARED_LIGHT:
  print(FREQUENCY %("Infrared light"))
elif INFRARED_LIGHT <= frequency < VISIBLE_LIGHT:
  print(FREQUENCY %("Visible light."))
elif VISIBLE_LIGHT <= frequency < ULTRAVIOLET_LIGHT:
  print(FREQUENCY %("Ultraviolet light."))
elif ULTRAVIOLET_LIGHT <= frequency < X_RAYS:
  print(FREQUENCY %("X rays."))
else:
  print(FREQUENCY %("Gamma Rays."))