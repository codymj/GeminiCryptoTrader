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
    account = {}            # Account data
    balances = []           # List of balance info from Gemini
    error = ''              # Error string

    # Initializer
    def __init__(self, account):
        self.account = account

    # Receive balances from Gemini
    ############################################################################
    def getBalances(self):
        if self.account['isSandbox']:
            baseUrl = 'https://api.sandbox.gemini.com/v1/balances'
        else:
            baseUrl = 'https://api.gemini.com/v1/balances'
        nonce = int(round(time.time()*1000))
        apiKey = self.account.get('apiKey')
        secret = self.account.get('secretKey')
        request = '/v1/balances'

        payload = {'request': request, 'nonce': nonce}
        b64 = base64.b64encode(str.encode(json.dumps(payload)))

        signature = hmac.new(str.encode(secret),
            b64, hashlib.sha384).hexdigest()

        headers = {
            'Content-Type': "text/plain",
            'Content-Length': "0",
            'X-GEMINI-APIKEY': apiKey,
            'X-GEMINI-PAYLOAD': b64,
            'X-GEMINI-SIGNATURE': signature,
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", baseUrl, headers=headers)

        response = json.loads(response.text)
        if self.validResponse(response):
            self.balances = response
            return self.balances
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