################################################################################
#                                                                              #
#  GeminiPublicAPI.py                                                          #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

# https://docs.gemini.com/websocket-api/#market-data

import json, datetime, urllib
from urllib.request import urlopen

class Ticker:
    # Class data
    baseUrl = 'https://api.gemini.com/v1/'

    symbols = []        # List of symbols (ex. 'btcusd')
    btcusdTicker = {}
    ethusdTicker = {}

    # Initializer
    def __init__(self):
        self.getSymbols()
        self.updateTickers()

    # Gets list of symbols from Gemini: ["btcusd", "ethusd", "ethbtc"]
    ############################################################################
    def getSymbols(self):
        response = urlopen(self.baseUrl + '/symbols')
        self.symbols = json.loads(response.read())

    # Updates ticker data
    ############################################################################
    def updateTickers(self):
        for symbol in self.symbols:
            if symbol == 'btcusd':
                postUrl = "/pubticker/btcusd"
                response = urlopen(self.baseUrl + postUrl)
                self.btcusdTicker = json.loads(response.read())
            elif symbol == 'ethusd':
                postUrl = "/pubticker/ethusd"
                response = urlopen(self.baseUrl + postUrl)
                self.ethusdTicker = json.loads(response.read())
            #elif symbol == 'ethbtc':
                #postUrl = "/pubticker/ethbtc"
                #response = urlopen(self.baseUrl + postUrl)
                #self.tickers[2] = json.loads(response.read())
            else:
                continue

    # Sends data to main window
    ############################################################################
    def getData(self):
        return (self.btcusdTicker, self.ethusdTicker)