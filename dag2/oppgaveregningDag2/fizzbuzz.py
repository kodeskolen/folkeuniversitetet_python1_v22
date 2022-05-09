#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FizzBuzz

Programmet skal skrive ut alle tallene fra 1-100,
men alle tall som er delelig med 3 skal erstattes med "Fizz",
alle tall som er delelig med 5 skal erstatt "Buzz",
og alle tall som er delelig med både 3 og 5 skal erstattes med "FizzBuzz"

Eksempel på utskrift:
1, 2, Fizz, 4, Buzz, 6, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz...

1. Hvordan finne ut om et tall er delelig på et annet?
    %-operator (modulo)
2. Hvordan gå gjennom en samling tall?
3. Hvordan sjekke om et tall er delelig på 3, 5, eller begge?

(4. Rekkefølge if-operatorer)
(5. Legge til range)
"""

# MODULO-operatoren: %
# Gir rest av en heltallsdivisjon.

# Eksempler
# 11 // 5 == 2, rest: 1
# 11 % 5 == 1

# 20 // 7 == 2, rest: 6
# 20 % 7 == 6

# 9 // 3 = 3, rest: 0
# 9 % 3 = 0

# Kan også tenkes på som: er det første tallet delelig med det andre?
# Hvis resultatet er 0 er svaret ja.


tallListe = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

for tall in tallListe:
    if (tall % 5 == 0 and tall % 3 == 0):
        print("FizzBuzz")
    elif (tall % 3 == 0):
        print("Fizz")
    elif (tall % 5 == 0):
        print("Buzz")
    else:
        print(tall)



# Repetisjon av tall 0-n
#for i in range(20):
#    print(i%3)
