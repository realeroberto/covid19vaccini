#!/usr/bin/env python

# covid19vaccini
#
# Consumes open data about Covid-19 in Italy

import sys
import uuid
from anguis.gdrive import AnguisGdrive
from covid19vaccini import Covid19Vaccini

df = Covid19Vaccini.Covid19Vaccini().somministrazioni_vaccini_latest

if len(sys.argv) > 1:
    area = sys.argv[1]
    subset = df[df['area'] == area]
else:
    subset = df

# Google Driver API must be enabled
cache = AnguisGdrive()
cache[str(uuid.uuid4())] = subset

print(subset)
