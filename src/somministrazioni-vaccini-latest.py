#!/usr/bin/env python

import sys
import urllib.request, json
import pandas as pd

URL = 'https://github.com/italia/covid19-opendata-vaccini/blob/master/dati/somministrazioni-vaccini-latest.json?raw=true'

with urllib.request.urlopen(URL) as url:
    data = json.loads(url.read().decode())
    df = pd.DataFrame(pd.json_normalize(data, 'data'))

if len(sys.argv) > 1:
    area = sys.argv[1]
    print(df[df['area'] == area])
else:
    print(df)
