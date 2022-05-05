# -*- coding: utf-8 -*-

"""
Her lager vi først en liste med navn. Denne stokker 
vi om på å skriver ut i tilfeldig rekkefølge.

Siden vi her løkker med while-løkke må vi bruke indeksering,
men det er enklere med en for-løkke (vist som ekstra på bunn)
"""

from random import shuffle

personer = ["Terje", "Jonas", "Emil", 
            "Maja", "Silje", "Aida", "Fredrik"]

# Sortere liste
personer.sort()

# Stokke om på liste
shuffle(personer)

index = 0
while index < len(personer):
    print(f"Spiller {index+1} er {personer[index]}")
    index = index + 1

# Alternativ fremgangsmåte med for-løkke. Betydlig enklere.
# nr = 1
# for navn in personer:
#     print(f"Spiller {nr} er {navn}")
#     nr += 1