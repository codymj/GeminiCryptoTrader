################################################################################
#                                                                              #
#  GeminiPublicAPI.py                                                          #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

# https://docs.gemini.com/websocket-api/#market-data

import json, datetime, websocket, urllib
from urllib.request import urlopen

class MarketData:
    # Class data
    baseUrl = ''        # Base URL
    account = {}        # Account data
    symbols = []        # List of symbols (ex. 'btcusd')
    tickers = []        # Ticker data

    # Initializer
    def __init__(self, account):
        # Set account
        self.account = account

        # Set base URL
        if self.account['isSandbox']:
            self.baseUrl = 'https://api.sandbox.gemini.com/v1/'
        else:
            self.baseUrl = 'https://api.gemini.com/v1/'

        # Build tickers structure
        btcusd = {}
        ethusd = {}
        ethbtc = {}
        self.tickers.append(btcusd)     # tickers[0] = btcusd data
        self.tickers.append(ethusd)     # tickers[1] = ethusd data
        self.tickers.append(ethbtc)     # tickers[2] = ethbtc data

        # Get data from Gemini
        self.symbols = self.getSymbols()

    # Gets list of symbols from Gemini: ["btcusd", "ethusd", "ethbtc"]
    ############################################################################
    def getSymbols(self):
        response = urlopen(self.baseUrl + '/symbols')
        return json.loads(response.read())

    # Updates ticker data
    ############################################################################
    def updateTickers(self):
        for symbol in self.symbols:
            if symbol == 'btcusd':
                postUrl = "/pubticker/btcusd"
                response = urlopen(self.baseUrl + postUrl)
                self.tickers[0] = json.loads(response.read())
            elif symbol == 'ethusd':
                postUrl = "/pubticker/ethusd"
                response = urlopen(self.baseUrl + postUrl)
                self.tickers[1] = json.loads(response.read())
            elif symbol == 'ethbtc':
                postUrl = "/pubticker/ethbtc"
                response = urlopen(self.baseUrl + postUrl)
                self.tickers[2] = json.loads(response.read())
            else:
                return
