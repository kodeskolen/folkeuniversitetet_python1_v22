# -*- coding: utf-8 -*-

"""
Eksempler som viser hvordan range funksjonen brukes
for å løkke over tallrekker
"""

# Om du bruker bare ett argument i range
# Da går vi fra og med 0 opp til (men ikke med) argumentet
for tall in range(10):
    print(tall)
# Gir 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    
# Om du gir to tall går vi fra og med startverdien,
# og til (men ikke med) sluttverdien)
for tall in range(5, 11):
    print(tall)
# Gir 5, 6, 7, 8, 9, 10

# Om du gir tre tall går vi fra og med, til (men ikke med)
# i steg av det tredje tallet
for tall in range(1, 11, 2):
    print(tall)
# Gir 1, 3, 5, 7, 9