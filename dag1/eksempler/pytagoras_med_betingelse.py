# -*- coding: utf-8 -*-

"""
Regne ut lengdene på rettsidet trekant med pytagoras

Opphøyd i skrives ** i Python
"""

from math import sqrt

svar = input("Hva vil du regne ut, kortside eller langside?")

if svar == "kortside":
    a = float(input("Lengde på kjent kortside: "))
    c = float(input("Lengde på langside: "))
    
    b = sqrt(c**2 - a**2)
    print(f"Kortsiden i trekanten er: {b}")
    
elif svar == "langside":
    a = float(input("Lengde på kortside 1: "))
    b = float(input("Lengde på kortside 2: "))

    c = sqrt(a**2 + b**2)
    print(f"Langsiden i trekanten er: {c}")
    
else:
    print("Jeg skjønner ikke svaret ditt.")