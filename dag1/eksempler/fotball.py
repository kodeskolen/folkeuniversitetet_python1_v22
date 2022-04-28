# -*- coding: utf-8 -*-

"""
Dette programmet regner ut volumet av en fotball.

Kommentarer:
    - Importerer pi som variabel (kunne også definert den selv)
    - Funksjonen round kan runde av tall for oss
"""

from math import pi

radius = 12 # cm
volum = 4*pi*radius**3/3

# Dele på 1000 for å regne om til liter
volum = volum/1000

print("Volumet av en fotball er", round(volum, 1), "liter")
