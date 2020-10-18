AP = 4.0
A = 3.85
AM = 3.5
BP = 3.15
B = 2.85
BM = 2.5
CP = 2.15
C = 1.85
CM = 1.5
DP = 1.15
D = 0.85

gp = float(input("Enter the grade points:\n"))
   

if gp >= AP:
    LETTER = 'A+'
elif AP > gp >= A:
    LETTER = 'A'
elif A > gp >= AM:
    LETTER = 'A-'
elif AM > gp >= BP:
    LETTER = 'B+'
elif BP > gp >= B:
    LETTER = 'B'
elif BM > gp >= BM:
    LETTER = 'B-'
elif BM > gp >= CP:
    LETTER = 'C+'
elif CP > gp >= C:
    LETTER = 'C'
elif C > gp >= CM:
    LETTER = 'C-'
elif CM > gp >= DP:
    LETTER = 'D+'
elif DP > gp >= D:
    LETTER = 'D'
elif D:
    LETTER = 'E'
  
print("The vote in letter is:", LETTER)
