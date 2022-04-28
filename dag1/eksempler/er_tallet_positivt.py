# -*- coding: utf-8 -*-

"""
Sjekk om et tall er positivt
"""

tall = float(input("Gi meg et tall: "))

if tall > 0:
    print("Tallet er positivt")

elif tall < 0:
    print("Tallet er negativt")
    
else:
    print("Tallet er akkurat null")