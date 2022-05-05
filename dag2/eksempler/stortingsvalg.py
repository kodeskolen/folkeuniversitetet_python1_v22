# -*- coding: utf-8 -*-

"""
Når var det stortingsvalg?
Hvis vi husker at det sist var stortingsvalg i 2021,
og at det er hvert fjerde år. Så kan vi bruke
en for-løkke med range på følgende måte:
"""

for år in range(2021, 1960, -4):
    print(år)
    
# Var det stortingsår i 1985?
if 1985 in range(2021, 1960, -4):
    print("Det var stortingsvalg i 1985")
else:
    print("Det var ikke stortingsvalg i 1985")