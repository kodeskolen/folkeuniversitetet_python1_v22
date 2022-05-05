# -*- coding: utf-8 -*-

"""
Her bruker vi en for-løkke til å løkke over et navn.
Først enkel telling av tegn, deretter en mer
fancy versjon for å kun telle bokstaver.
"""

# Eksempel 1: Løkk over bokstaver og skriv dem ut
navn = "Andreas"
for bokstav in navn:
    print(bokstav)
    
# Eksempel 2: Løkk over tegn i navn. Tell alt som ikke er mellomrom
# Nb: Denne vil for eksempel telle bindestrek
navn = "Anne Mari"
antall = 0
for tegn in navn:
    if tegn != " ":
        antall += 1
print(f"Du har {antall} bokstaver i navnet ditt")

# Eksempel 3: Tell kun bokstaver
navn = "Anne-Mari"
bokstaver = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅabcdefghijklmnopqrstuvwxyzæøå'

antall = 0
for tegn in navn:
    if tegn in bokstaver:
        antall += 1
print(f"Du har {antall} bokstaver i navnet ditt")