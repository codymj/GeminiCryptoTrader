################################################################################
#                                                                              #
#  LoadSaveData.py                                                             #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path
from EncryptDecryptData import *
from PyQt5.QtWidgets import QMessageBox, QFileDialog

# Loads settings
################################################################################
def loadSettings(userLoad=False):
    settings = {}
    settingsPath = '../data/Settings.json'

    if not os.path.exists(settingsPath):
        settings = {
            'encrypted':  False,
            'password':   ''
        }
    else:
        with open(settingsPath, 'r') as f:
            settings = json.load(f)

    return settings, settingsPath

# Saves settings to file
################################################################################
def saveSettings(settings, settingsPath):
    if not os.path.exists(settingsPath):
        settingsPath = '../data/Settings.json'

    with open(settingsPath, 'w') as f:
        json.dump(settings, f)

# Loads last used account data from Accounts.json file
################################################################################
def loadAccounts(settings, password, userLoad=False):
    accounts = []
    accountsPath = ''

    # If encrypted
    if not settings['encrypted']:
        # If not a user-specified file path
        if not userLoad:
            accountsPath = '../data/Accounts.json'
        # else:
            # Set user-specified file path
        # Open and load
        if os.path.exists(accountsPath):
            with open(accountsPath, 'r') as f:
                accounts = json.load(f)
    else:
        # If not a user-specified file path
        if not userLoad:
            accountsPath = '../data/Accounts.enc'
        # else:
            # Set user-specified file path
        # Decrypt, open, load, encrypt
        if os.path.exists(accountsPath):
            decryptFile(password, accountsPath)
            with open('../data/Accounts.json', 'r') as f:
                accounts = json.load(f)
            encryptFile(password, accountsPath)

    return accounts, accountsPath

# Returns last used account
################################################################################
def getLastUsedAccount(accounts):
    lastUsedAccount = {}

    for account in accounts:
        if account['lastUsed'] == True:
            lastUsedAccount = account

    return lastUsedAccount

# Saves accounts to file
################################################################################
def saveAccounts(accounts, accountsPath, settings, password):
    if settings['encrypted']:
        if not os.path.exists(accountsPath):
            print('ERROR:  Account file is missing. Cannot save.')
            return
        else:
            decryptFile(password, accountsPath)
            with open(accountsPath, 'w') as f:
                json.dump(accounts, f)
            encryptFile(password, accountsPath)
    else:
        if not os.path.exists(accountsPath):
            accountsPath = '../data/Accounts.json'
        with open(accountsPath, 'w') as f:
            json.dump(accounts, f)

