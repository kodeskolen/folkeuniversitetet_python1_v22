# -*- coding: utf-8 -*-

"""
En muffinsoppskrift!
"""

n = int(input("Hvor mange muffins vil du lage? "))

if n >= 4:
    print(f"Til {n} muffins trenger du:")
    print(f"- {12*n} gram smør")
    print(f"- {0.2*n} dl sukker")
    print(f"- {n/3} egg")
    print(f"- {0.4*n} dl hvetemel")
    print(f"- {0.25*n} gram bakepulver")
    
else:
    print("Så få muffins kan du ikke bake")