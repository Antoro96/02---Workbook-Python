oddSet = ['a', 'c', 'e', 'g']
evenSet = ['b', 'd', 'f', 'h']
oddNumbers = [1,3,5,7]
evenNumbers = [2,4,6,8]

letter = input("Enter the letter: ")
number = int(input("Enter the number: "))

if letter in oddSet and number in oddNumbers:
    print("The square is black.")
elif letter in evenSet and number in oddNumbers:
    print("The square is white.")
elif letter in evenSet and number in evenNumbers:
    print("The square is black.")
elif letter in oddSet and number in evenNumbers:
    print("The square is white.")
else:
    print("Letter has to be a letter.")
