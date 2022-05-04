#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gjettelek

Programmet velger et tilfeldig tall mellom 1 og 100.
Spilleren gjetter på et tall, og får vite om gjettet var for lavt eller for høyt.
Deretter får spilleren gjette på nytt. Fortsett til de får riktig.

1. Velge tall
2. Ta inn input
3. Sjekk om fasit og gjett er like (hvis ikke, fortsett med nytt gjett)
4. Gi beskjed om for høyt eller lavt
5. Skriv ut antall forsøk
"""

from random import randint

fasit = randint(1, 100)   # randint gir tilfeldig heltall

#print(f"Fasiten er {fasit}")  # Til testing

gjett = int(input("Gjett på et tall mellom 1 og 100 "))
forsøk = 1

while gjett != fasit:
    if gjett < fasit:
        print("Gjettet var for lavt")
    elif gjett > fasit:
        print("Gjettet var for høyt")
    gjett = int(input("Gjett igjen: "))
    forsøk = forsøk + 1    # samme som å skrive 'forsøk += 1'

print("Helt riktig!")
print(f"Du brukte {forsøk} gjett.")