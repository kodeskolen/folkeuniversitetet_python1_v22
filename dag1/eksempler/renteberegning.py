# -*- coding: utf-8 -*-

"""
Eksempel på en løkke, hvor vi regner med årlige renter
"""

saldo = 10000
rente = 2.8 # prosent rente per år
vekstfaktor = 1 + rente/100
år = 0

while saldo < 20000:
    saldo = saldo * vekstfaktor
    år = år + 1
    print(f"Etter {år} år har du {round(saldo)} kr")

