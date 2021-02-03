#!/usr/bin/env python

# Covid19Vaccini
#
# Consumes open data about Covid-19 in Italy

import urllib.request, urllib.parse, json
import pandas as pd

BASE_URL = 'https://github.com/italia/covid19-opendata-vaccini/blob/master/dati/'

class Covid19Vaccini(object):

    def __build_url(self, url):
        url = urllib.parse.urljoin(BASE_URL, url)
        return '{}?{}'.format(url, 'raw=true')

    def __getter(self, url):
        with urllib.request.urlopen(self.__build_url(url)) as u:
            data = json.loads(u.read().decode())
            df = pd.DataFrame(pd.json_normalize(data, 'data'))
            return df

    @property
    def anagrafica_vaccini_summary_latest(self):
        return self.__getter('anagrafica-vaccini-summary-latest.json')

    @property
    def consegne_vaccini_latest(self):
        return self.__getter('consegne-vaccini-latest.json')

    @property
    def last_update_dataset(self):
        return self.__getter('last-update-dataset.json')

    @property
    def punti_somministrazione_latest(self):
        return self.__getter('punti-somministrazione-latest.json')

    @property
    def somministrazioni_vaccini_latest(self):
        return self.__getter('somministrazioni-vaccini-latest.json')

    @property
    def somministrazioni_vaccini_summary_latest(self):
        return self.__getter('somministrazioni-vaccini-summary-latest.json')

    @property
    def vaccini_summary_latest(self):
        return self.__getter('vaccini-summary-latest.json')
