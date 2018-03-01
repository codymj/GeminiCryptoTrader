################################################################################
#                                                                              #
#  GeminiPublicAPI.py                                                          #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

# https://docs.gemini.com/websocket-api/#market-data

import json, datetime, urllib, websocket
from urllib.request import urlopen

class GeminiPublicAPI:
    # Class data
    baseUrl = ''
    symbols = []        # List of symbols: ["btcusd", "ethusd", "ethbtc"]

    # Initializer
    def __init__(self):
        self.baseUrl = 'https://api.gemini.com/v1/'
        self.getSymbols()

    # Updates ticker data
    ############################################################################
    def getTickers(self):
        btcusdTicker = {}   # btcusd ticker data
        ethusdTicker = {}   # ethusd ticker data

        for symbol in self.symbols:
            if symbol == 'btcusd':
                postUrl = "/pubticker/btcusd"
                response = urlopen(self.baseUrl + postUrl)
                btcusdTicker = json.loads(response.read())
            elif symbol == 'ethusd':
                postUrl = "/pubticker/ethusd"
                response = urlopen(self.baseUrl + postUrl)
                ethusdTicker = json.loads(response.read())
            #elif symbol == 'ethbtc':
                #postUrl = "/pubticker/ethbtc"
                #response = urlopen(self.baseUrl + postUrl)
                #self.tickers[2] = json.loads(response.read())
            else:
                continue

        return [btcusdTicker, ethusdTicker]

    # Gets symbol list from Gemini
    ############################################################################
    def getSymbols(self):
        response = urlopen(self.baseUrl + '/symbols')
        self.symbols = json.loads(response.read())
