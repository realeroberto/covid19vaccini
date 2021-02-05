#!/usr/bin/env python

# covid19vaccini
#
# Consumes open data about Covid-19 in Italy

import uuid
import yaql
from datetime import date
from covid19vaccini import Covid19Vaccini

# Uses https://github.com/reale/anguis as key-store layer
from anguis.s3 import AnguisS3

BUCKET = '69303b61-a751-44f6-8b23-eb8f2ace3ccb'
store = AnguisS3(BUCKET, create=True)

when = date.isoformat(date.today())

try:
    # Retrieve data from S3 store
    df = store[when]
except:
    # Retrieve data from data source
    df = Covid19Vaccini.Covid19Vaccini().somministrazioni_vaccini_latest
    store[when] = df

# Print data
print(df)
