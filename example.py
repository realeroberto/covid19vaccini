#!/usr/bin/env python

# Covid19Vaccini
#
# Consumes open data about Covid-19 in Italy

import sys
from Covid19Vaccini import Covid19Vaccini

df = Covid19Vaccini.Covid19Vaccini().somministrazioni_vaccini_latest

if len(sys.argv) > 1:
    area = sys.argv[1]
    print(df[df['area'] == area])
else:
    print(df)
