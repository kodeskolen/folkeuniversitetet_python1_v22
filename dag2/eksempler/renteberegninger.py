# -*- coding: utf-8 -*-

"""
Repetisjon fra dag 1. Vi bruker en løkke til å gjenta
en årlig renteberegning.
"""

saldo = 10000
rentefot = 2.8 # i prosent
år = 0

while saldo < 20000:
    renter = saldo*rentefot/100
    saldo = saldo + renter
    år = år + 1
    print(f"Etter {år} år har du {round(saldo)} kr.")

