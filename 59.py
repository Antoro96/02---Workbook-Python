licensePlate = input("Enter the license plate:\t")
  
if len(licensePlate) == 6:  
    for thing in licensePlate[:3]:
      if thing.isalpha() and thing.isupper():
        string += thing
    
    
elif thing.isnumeric():
        string += thing
  
  if string == licensePlate:
    status = 'older'
    
  string = ''
  
  if len(licensePlate) == 7:  
    for thing in licensePlate[:4]:
      if thing.isnumeric():
        string += thing
    
    for thing in licensePlate[4:]:
      if thing.isalpha() and thing.isupper():
        string += thing
      
  if string == licensePlate:
    status = 'newer'
    
  try:
    status
    
  except NameError:
    status = ''
    
  if status == 'older':
    print("This license plate is valid for an older style license plate.")
    
  elif status == 'newer':
    print("This license plate is valid for a newer style license plate.")
    
  elif status == '':
    print("This license plate is not valid for an older or newer style license plate.")
    
  blah = input("Press enter to continue:\t")
  
  print()
