# -*- coding: utf-8 -*-

"""
Bygg opp en liste med navn vha input
"""

from random import shuffle

personer = []

navn = input("Skriv inn navn (eller 'slutt' for å slutte): ")

while navn != 'slutt':
    personer.append(navn)
    navn = input("Skriv inn navn (eller 'slutt' for å slutte): ")


shuffle(personer)

index = 0
while index < len(personer):
    print(f"Spiller {index+1} er {personer[index]}")
    index = index + 1


