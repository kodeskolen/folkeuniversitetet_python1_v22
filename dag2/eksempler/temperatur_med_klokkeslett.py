# -*- coding: utf-8 -*-

"""
Vi ser på en liste med temperaturer. Klarer vi å finne maks?
"""

temperaturer = [-15.5,  -18.0,  -17.4,  -18.5,  -19.9,  -20.9,
                -21.5,  -22.0,  -20.5,  -18.6,  -15.6,  -13.5,
                -10.5,   -9.0,   -7.9,   -7.1,   -9.1,  -12.2,
                -14.8,  -16.5,  -16.8,  -15.3,  -17.6,  -19.7]

maks = temperaturer[0]
kl_når_det_er_varmest = 0

for kl in range(24):
    temp = temperaturer[kl]
    if temp > maks:
        maks = temp
        kl_når_det_er_varmest = kl
       
print("Høyeste temperatur denne dagen var", maks)
print("Det var klokken", kl_når_det_er_varmest)
