UNACCEPTABLE = 0.0
ACCEPTABLE = 0.4
MERITORIOUS = 0.6
RAISE = 2400.00

rating = float(input("Enter the rating:\n"))
  
if UNACCEPTABLE <= rating < ACCEPTABLE:
    print("Performance is unacceptable.")
    print()
    
elif ACCEPTABLE <= rating < MERITORIOUS:
    print("Performance is acceptable.")
    print()
    
elif MERITORIOUS <= rating:
    print("Performance is meritorious.")
    
totalRaise = RAISE * rating
totalRaise = round(totalRaise, 2)
  
print("Total raise is $%.2f." % (totalRaise))
