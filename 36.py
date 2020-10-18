letter = str(input("Enter a letter of the alphabet: "))

if letter == "a" or letter == "e" or letter == "i" or letter =="o" or letter == "u" :
    print(letter, " is a vowel")
elif letter == "y":
    print("Sometimes", letter, "is a vowel and sometimes", letter, "is a consonant")
else:
    print(letter, "is a consonant")
