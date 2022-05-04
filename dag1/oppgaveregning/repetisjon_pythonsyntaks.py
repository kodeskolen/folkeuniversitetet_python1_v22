#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Repetisjon av Python-syntaks
"""

a = 1
b = 2
# Print med flettestreng
print(f"Tallet a er {a} og tallet b er {b}")

# Print med komma
print("Tallet er a", a, "og tallet b er", b)

# Datatyper
print(Hei verden!)   # gir feilmelding
print("Hei verden!") # riktig


# Matematiske operatorer
# +
resultat = a + b

# -
resultat = a - b

# /
resultat = a / b  # gir et desimaltall

# *   (gange/multiplikasjon)
resultat = a * b

# **  (potens/opphøyd i)
resultat = a**b

# if-else
if a == b:
    print("Jeg kjøres kun om testen er sann")
else:
    print("Ellers kjører jeg")

if a == b:
    print("a er lik b")
elif a < b:
    print("a er mindre enn b")
else:
    print("a er større enn b")