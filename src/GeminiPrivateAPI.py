################################################################################
#                                                                              #
#  GeminiPrivateAPI.py                                                         #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

# https://docs.gemini.com/websocket-api/#order-events
# https://docs.gemini.com/rest-api/#private-api-invocation

import json, datetime, urllib, time, base64, hmac, hashlib, requests
from hashlib import sha384
from urllib.request import urlopen

class GeminiPrivateAPI:
    # Class data
    baseUrl = ''
    account = {}            # Account data
    #balances = []           # List of balance info from Gemini
    #trades = []             # List of trades info from Gemini
    error = ''              # Error string

    # Initializer
    def __init__(self, account):
        self.account = account

        if self.account['isSandbox']:
            self.baseUrl = 'https://api.sandbox.gemini.com/v1/'
        else:
            self.baseUrl = 'https://api.gemini.com/v1/'

    # Generates b64-encoded payload
    ############################################################################
    def generatePayload(self, request, symbol=None):
        nonce = int(round(time.time()*1000))
        apiKey = self.account.get('apiKey')
        secret = self.account.get('secretKey')

        if symbol == None:
            payload = {
                'request': request,
                'nonce': nonce,
            }
        else:
            payload = {
                'request': request,
                'nonce': nonce,
                'symbol': symbol
            }

        return base64.b64encode(str.encode(json.dumps(payload)))

    # Generates signature
    ############################################################################
    def generateSignature(self, b64):
        secret = self.account.get('secretKey')

        return hmac.new(str.encode(secret), b64, hashlib.sha384).hexdigest()

    # Generates header
    ############################################################################
    def generateHeaders(self, b64, sig):
        apiKey = self.account.get('apiKey')

        headers = {
            'Content-Type': "text/plain",
            'Content-Length': "0",
            'X-GEMINI-APIKEY': apiKey,
            'X-GEMINI-PAYLOAD': b64,
            'X-GEMINI-SIGNATURE': sig,
            'Cache-Control': "no-cache"
        }
        return headers

    # Receive balances from Gemini
    ############################################################################
    def getBalances(self):
        baseUrl = self.baseUrl + 'balances'
        b64Payload = self.generatePayload('/v1/balances')
        signature = self.generateSignature(b64Payload)
        headers = self.generateHeaders(b64Payload, signature)

        response = requests.request("POST", baseUrl, headers=headers)
        response = json.loads(response.text)
        if self.validResponse(response):
            return response
        else:
            return self.error

    # Get past trades
    ############################################################################
    def getTrades(self, symbol):
        baseUrl = self.baseUrl + 'mytrades'
        b64Payload = self.generatePayload('/v1/mytrades', symbol)
        signature = self.generateSignature(b64Payload)
        headers = self.generateHeaders(b64Payload, signature)

        response = requests.request("POST", baseUrl, headers=headers)
        response = json.loads(response.text)
        if self.validResponse(response):
            self.trades = response
            return response
        else:
            return self.error

    # Validate response data
    ############################################################################
    def validResponse(self, response):
        if isinstance(response, list):
            return True
        else:
            reason = response['reason']
            message = response['message']
            self.error = 'Balance error: ' + reason
            return False