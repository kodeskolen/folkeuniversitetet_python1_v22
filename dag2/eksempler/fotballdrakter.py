# -*- coding: utf-8 -*-

"""
Vi har en liste med fotballspillere og en liste med
ubrukte draktnummer. Vi lager et program for å tildele 
draktnummer til spillerene tilfeldig.
"""

from random import shuffle

personer = ["Terje", "Jonas", "Emil", 
            "Maja", "Silje", "Aida", "Fredrik"]

draktnummer = [8, 11, 27, 29, 40, 66, 71, 83, 90, 98]

shuffle(draktnummer)
shuffle(personer)

index = 0
while index < len(personer):
    print(f"{personer[index]} skal få {draktnummer[index]}")
    index = index + 1

print()
print("Ubrukte drakter:")
while index < len(draktnummer):
    print(draktnummer[index])
    index = index + 1