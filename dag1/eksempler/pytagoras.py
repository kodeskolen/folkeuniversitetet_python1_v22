# -*- coding: utf-8 -*-

"""
Regne ut lengdene på rettsidet trekant med pytagoras

Opphøyd i skrives ** i Python
"""

from math import sqrt

a = float(input("Lengde på kortside 1: "))
b = float(input("Lengde på kortside 2: "))

c = sqrt(a**2 + b**2)

print(f"Langsiden i trekanten er: {c}")