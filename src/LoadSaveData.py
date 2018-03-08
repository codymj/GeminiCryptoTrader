################################################################################
#                                                                              #
#  LoadSaveData.py                                                             #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

import sys, json, os.path
from EncryptDecryptData import *
from PyQt5.QtWidgets import QFileDialog

# Loads settings
################################################################################
def loadSettings(userLoad=False):
    settings = {}
    settingsPath = '../data/Settings.json'

    # If no user-specified path
    if not userLoad:
        if not os.path.exists(settingsPath):
            settings = {
                'encrypted':  False,
                'password':   ''
            }
        else:
            with open(settingsPath, 'r') as f:
                settings = json.load(f)
    else:
        fileName = QFileDialog.getOpenFileName(None,
        'Browse for Settings.json', '.', 'Settings.json')
        if os.path.exists(fileName[0]):
            with open(fileName[0], 'r') as f:
                settings = json.load(f)
            settingsPath = fileName[0]
        else:
            settings = {
                'encrypted':  False,
                'password':   ''
            }

    return settings, settingsPath

# Saves settings to file
################################################################################
def saveSettings(settings, settingsPath, userSave=False):
    # If no user-specified path
    if not userSave:
        if not os.path.exists(settingsPath):
            settingsPath = '../data/Settings.json'
        with open(settingsPath, 'w') as f:
            json.dump(settings, f)
    else:
        fileName = QFileDialog.getSaveFileName(None,
        'Save Settings.json', '.', 'Settings.json')
        with open(fileName[0], 'w') as f:
            json.dump(settings, f)

# Loads last used account data from Accounts.json file
################################################################################
def loadAccounts(settings, password, userLoad=False):
    accounts = []
    accountsPath = ''

    # If encrypted
    if not settings['encrypted']:
        # If no user-specified file path
        if not userLoad:
            accountsPath = '../data/Accounts.json'
            if os.path.exists(accountsPath):
                with open(accountsPath, 'r') as f:
                    accounts = json.load(f)
        else:
            fileName = QFileDialog.getOpenFileName(None,
            'Browse for Accounts.json', '.', 'Accounts.json')
            if os.path.exists(fileName[0]):
                with open(fileName[0], 'r') as f:
                    accounts = json.load(f)
                accountsPath = fileName[0]
            else:
                accountsPath = '../data/Accounts.json'
    else:
        # If no user-specified file path
        if not userLoad:
            accountsPath = '../data/Accounts.enc'
            if os.path.exists(accountsPath):
                decryptFile(password, accountsPath)
                with open('../data/Accounts.json', 'r') as f:
                    accounts = json.load(f)
                encryptFile(password, accountsPath)
        else:
            fileName = QFileDialog.getOpenFileName(None,
            'Browse for Accounts.enc', '.', 'Accounts.enc')
            if os.path.exists(fileName[0]):
                decryptFile(password, fileName[0])
                newFileName = os.path.dirname(os.path.abspath(fileName[0]))
                newFileName = newFileName + '/Accounts.json'
                with open(newFileName, 'r') as f:
                    accounts = json.load(f)
                accountsPath = newFileName

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
def saveAccounts(accounts, accountsPath, settings, password, userSave=False):
    if not userSave:
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
    else:
        fileName = QFileDialog.getSaveFileName(None,
        'Save Accounts', '.', '*.json, *.enc')
        with open(fileName[0], 'w') as f:
            json.dump(accounts, f)
        newAccountsPath = fileName[0]
        if settings['encrypted']:
            encryptFile(password, newAccountsPath)
