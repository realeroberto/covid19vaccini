#!/usr/bin/env python

# OpendataVaccini
#
# Consumes open data about Covid-19 in Italy

import sys
from OpendataVaccini import OpendataVaccini

df = OpendataVaccini.OpendataVaccini().somministrazioni_vaccini_latest

if len(sys.argv) > 1:
    area = sys.argv[1]
    print(df[df['area'] == area])
else:
    print(df)
