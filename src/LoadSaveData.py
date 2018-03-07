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
def loadSettings():
    settings = {}
    settingsDir = 'Settings.json'

    if not os.path.exists(settingsDir):
        msg = QMessageBox()
        msg.setText('No settings file found.')
        msg.setInformativeText('What would you like to do?')
        msg.setStandardButtons(QMessageBox.Open | QMessageBox.Ignore)
        returnVal = msg.exec_()

        # Browse for file
        if returnVal == QMessageBox.Open:
            fileName = QFileDialog.getOpenFileName(self,
                'Browse for Settings.json', '.', 'Settings.json')
            if os.path.exists(fileName[0]):
                with open(fileName[0], 'r') as f:
                    settings = json.load(f)
                settingsDir = fileName[0]
            else:
                self.settings = {
                    'encrypted':  False,
                    'password':   ''
                }
        else:
            settings = {
                'encrypted':  False,
                'password':   ''
            }
    else:
        with open(settingsDir, 'r') as f:
            settings = json.load(f)

    return settings, settingsDir

# Saves settings to file
################################################################################
def saveSettings(settings, settingsDir):
    if not settingsDir:
        settingsDir = 'Settings.json'

    with open(settingsDir, 'w') as f:
        json.dump(settings, f)

# Loads last used account data from Accounts.json file
################################################################################
def loadAccounts(settings, password):
    accounts = []
    accountsDir = ''

    # No account files found. Browse or create new files
    if (not settings['encrypted'] and not os.path.exists('Accounts.json')):
        msg = QMessageBox()
        msg.setText('No Accounts.json file found.')
        msg.setInformativeText('What would you like to do?')
        msg.setStandardButtons(QMessageBox.Open | QMessageBox.Ignore)
        returnVal = msg.exec_()

        # Browse for file
        if returnVal == QMessageBox.Open:
            fileName = QFileDialog.getOpenFileName(self,
                'Browse for Accounts.json', '.', 'Accounts.json')
            if os.path.exists(fileName[0]):
                with open(fileName[0], 'r') as f:
                    accounts = json.load(f)
                accountsDir = fileName[0]
            else:
                return
        else:
            return
    # No account files found. Browse or create new files
    elif settings['encrypted'] and not os.path.exists('Accounts.enc'):
        msg = QMessageBox()
        msg.setText('No Accounts.enc file found.')
        msg.setInformativeText('What would you like to do?')
        msg.setStandardButtons(QMessageBox.Open | QMessageBox.Ignore)
        returnVal = msg.exec_()

        # Browse for file
        if returnVal == QMessageBox.Open:
            fileName = QFileDialog.getOpenFileName(self,
                'Browse for Accounts.enc', '.', 'Accounts.enc')
            if os.path.exists(fileName[0]):
                decryptFile(password, fileName[0])
                newFileName = os.path.dirname(os.path.abspath(fileName[0]))
                newFileName = newFileName + '/Accounts.json'
                with open(newFileName, 'r') as f:
                    accounts = json.load(f)
                accountsDir = newFileName
            else:
                return
        else:
            return
    # Load accounts
    elif not settings['encrypted'] and os.path.exists('Accounts.json'):
        with open('Accounts.json', 'r') as f:
            accounts = json.load(f)
    # Decrypt
    elif settings['encrypted'] and os.path.exists('Accounts.enc'):
        decryptFile(password, 'Accounts.enc')
        with open('Accounts.json', 'r') as f:
            accounts = json.load(f)
    # Else ???
    else:
        print('ERROR: Account files missing.')
        return

    # Save and re-encrypt if necessary
    saveAccounts(accounts, accountsDir, settings, password)

    return accounts, accountsDir

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
def saveAccounts(accounts, accountsDir, settings, password):
    if not accountsDir:
        accountsDir = 'Accounts.json'
    with open(accountsDir, 'w') as f:
        json.dump(accounts, f)

    # Encrypt data
    if settings['encrypted']:
        encryptFile(password, accountsDir)
