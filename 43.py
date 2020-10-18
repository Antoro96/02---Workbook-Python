GEORGE_WASHINGTON = 1
THOMAS_JEFFERSON = 2
ABRAHAM_LINCOLN = 5
ALEXANDER_HAMILTON = 10
ANDREW_JACKSON = 20
ULYSSES_S_GRANT = 50
BENJAMIN_FRANKLIN = 100

number = int(input("Enter the number of banknote: "))

if number == GEORGE_WASHINGTON:
    note = "Whashington"
elif number == THOMAS_JEFFERSON:
    note = "Jefferson"
elif number == ABRAHAM_LINCOLN:
    note = "Lincoln"
elif number == ALEXANDER_HAMILTON:
    note = "Hamilton"
elif number == ANDREW_JACKSON:
    note = "Jackson"
elif number == ULYSSES_S_GRANT:
    note = "Grant"
elif number == BENJAMIN_FRANKLIN:
    note = "Franklin"
else:
    note = ""

if note == "":
    print("There's an error message!")
    exit()
else:
    print("The individual of the banknote is", note)
    
