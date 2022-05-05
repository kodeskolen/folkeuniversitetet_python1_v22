# -*- coding: utf-8 -*-

"""
Det ble spurt hvordan man kan generere helt tilfeldige navn
i Python. Det finnes ikke funksjonalitet i standardbibliotekene
til Python for dette - men vi kan enkelt installere en ekstrapakke,
la oss se litt på dette.

Det finnes sikkert mange pakker som kan gjøre dette, men et
kjapt google søk ledet oss til en pakke som heter 'names'.

Om vi prøver å importere denne får vi en feilmelding fordi
Python ikke finner den. Så da må vi først installere den.
I Consollen (til høyre) kan du skrive 
    %pip install names
Pip er et verktøy for å installere Python-pakker på en enkel
måte. Det er ikke alltid den fungerer inne i Spyder, men
om du har en vanlig Anaconda-installasjon bør dette gå.
"""

import names

# Lag ett tilfeldig navn
print(names.get_full_name())

# Lag 10 tilfeldige fornavn
print()
for n in range(10):
    print(names.get_first_name())
    

# Lag 5 jentenavn
print()
for n in range(5):
    print(names.get_first_name(gender='female'))

