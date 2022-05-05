# -*- coding: utf-8 -*-

"""
Vi gjentar rentebergningseksempelet med for-løkke istedenfor
while løkke. Regner da f.eks 10 år fremover i tid
"""

rentefot = 2.8 # prosent per år
saldo = 10000

for år in range(10):
    renter = saldo*rentefot/100
    saldo += renter  
    print(f"Etter {år+1} år er det {round(saldo)} kr på konto.")
