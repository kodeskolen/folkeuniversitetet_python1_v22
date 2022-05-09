#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
round
nøstede funksjonskall
"""

# round runder av et desimaltall.
round(3.333333)  # gir 3

# kan også spesifisere antall desimaler
round(3.333333, 2) # gir 3.33

a = 121
b = 19
c = a / b  # 6.368421052631579


print(round(c, 2))

# Python evaluerer nøstede funksjonskall fra innerst til ytterst
# 1. print( round(c, 2) )
# 2. print( 6.37 )