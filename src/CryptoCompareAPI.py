################################################################################
#                                                                              #
#  CryptoCompareAPI.py                                                         #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, datetime, time, math, requests
from datetime import date, timedelta, datetime
import numpy as np

class TradeHistory:
    # Class data
    baseUrl = 'https://min-api.cryptocompare.com/data/histominute'

    btcusdData = []
    btcusdTimes = []
    #btcusdOpens = []
    btcusdCloses = []
    btcusdHighs = []
    btcusdLows = []
    btcusdRange = ''
    btcusdDelta = ''

    ethusdData = []
    ethusdTimes = []
    #ethusdOpens = []
    ethusdCloses = []
    ethusdHighs = []
    ethusdLows = []
    ethusdRange = ''
    ethusdDelta = ''

    # Initializer
    def __init__(self):
        self.getTradeHistory()
        self.separateData()
        self.computePriceRange()
        self.computePriceDelta()

    # Receive trade history from CryptoCompare
    ############################################################################
    def getTradeHistory(self):
        # TODO: Allow parameter to set day range
        btcusdParams = '?fsym=BTC&tsym=USD&limit=1440&e=Gemini'
        ethusdParams = '?fsym=ETH&tsym=USD&limit=1440&e=Gemini'

        # Get BTCUSD trades
        response = requests.request('GET', self.baseUrl+btcusdParams)
        btcusdHistory = json.loads(response.text)
        self.btcusdData = btcusdHistory['Data']

        # Get ETHUSD trades
        response = requests.request('GET', self.baseUrl+ethusdParams)
        ethusdHistory = json.loads(response.text)
        self.ethusdData = ethusdHistory['Data']

    # Separates trade history data into relevant lists for further computations
    ############################################################################
    def separateData(self):
        self.btcusdTimes = [int(item['time']) for item in self.btcusdData]
        #self.btcusdOpens = [float(item['open']) for item in self.btcusdData]
        self.btcusdCloses = [float(item['close']) for item in self.btcusdData]
        self.btcusdHighs = [float(item['high']) for item in self.btcusdData]
        self.btcusdLows = [float(item['low']) for item in self.btcusdData]

        self.ethusdTimes = [int(item['time']) for item in self.ethusdData]
        #self.ethusdOpens = [float(item['open']) for item in self.ethusdData]
        self.ethusdCloses = [float(item['close']) for item in self.ethusdData]
        self.ethusdHighs = [float(item['high']) for item in self.ethusdData]
        self.ethusdLows = [float(item['low']) for item in self.ethusdData]

    # Calculates the price range during time period
    ############################################################################
    def computePriceRange(self):
        btcusdMaxHigh = max(self.btcusdHighs)
        btcusdMinLow = min(self.btcusdLows)
        self.btcusdRange = ('${:,.2f}'.format(btcusdMinLow)
                            + ' - '
                            + '${:,.2f}'.format(btcusdMaxHigh))

        ethusdMaxHigh = max(self.ethusdHighs)
        ethusdMinLow = max(self.ethusdLows)
        self.ethusdRange = ('${:,.2f}'.format(ethusdMinLow)
                            + ' - '
                            + '${:,.2f}'.format(ethusdMaxHigh))

    # Calculates the change from current price, x-hours ago
    ############################################################################
    def computePriceDelta(self):
        self.btcusdDelta = (float(self.btcusdData[-1]['open'])
                            - float(self.btcusdData[0]['open']))

        self.ethusdDelta = (float(self.ethusdData[-1]['open'])
                            - float(self.ethusdData[0]['open']))

        # Use format ($100) for negative price
        if self.btcusdDelta < 0:
            self.btcusdDelta = self.btcusdDelta * -1.0
            self.btcusdDelta = '(' + '${:,.2f}'.format(self.btcusdDelta) + ')'
        else:
            self.btcusdDelta = '${:,.2f}'.format(self.btcusdDelta)

        if self.ethusdDelta < 0:
            self.ethusdDelta = self.ethusdDelta * -1.0
            self.ethusdDelta = '(' + '${:,.2f}'.format(self.ethusdDelta) + ')'
        else:
            self.ethusdDelta = '${:,.2f}'.format(self.ethusdDelta)

    # Sends data to main window
    ############################################################################
    def getData(self):
        btcusdTuple = ( self.btcusdTimes, self.btcusdCloses,
                        self.btcusdRange, self.btcusdDelta)
        ethusdTuple = ( self.ethusdTimes, self.ethusdCloses,
                        self.ethusdRange, self.ethusdDelta)

        return [btcusdTuple, ethusdTuple]