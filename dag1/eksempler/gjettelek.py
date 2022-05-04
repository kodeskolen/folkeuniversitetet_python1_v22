"""
Programmet velger et tilfeldig tall mellom 1 og 100.
Spilleren gjetter på på et tall, og får vite om gjettet var riktig,
for lavt eller for høyt.
Deretter får spilleren gjette på nytt. Fortsett til de treffer
"""


from random import randint

# Velg tilfeldig tall mellom 1 og 100
fasit = randint(1, 100)
gjett = int(input("Gjett på et tall mellom 1 og 100"))
forsøk = 1

while gjett != fasit:
    if gjett < fasit:
        print("Gjettet var for lavt")
    elif gjett > fasit:
        print("Gjettet var for høyt")
    gjett = int(input("Gjett igjen: "))
    forsøk = forsøk + 1

print("Helt riktig!")
print(f"Du brukte {forsøk} gjett")