################################################################################
#                                                                              #
#  EncryptDecryptData.py                                                       #
#  Author: Cody Johnson <codyj@protonmail.com>                                 #
#                                                                              #
################################################################################

from Crypto import Random
from Crypto.Cipher import AES
import os, random, struct, hashlib

# Encrypt file
################################################################################
def encryptFile(key, iFile, oFile=None, chunkSize=64*1024):
    # Use SHA256 for key
    key = hashlib.sha256(key.encode('utf-8')).digest()

    # Set output file name
    if not oFile:
        oFile = iFile.split('.')[0] + '.enc'

    # Generate IV
    iv = Random.new().read(16)

    # Setup encryptor
    encryptor = AES.new(key, AES.MODE_CBC, iv)

    # Get filesize of input file
    fileSize = os.path.getsize(iFile)

    # Open decrypted file & file for saving encrypted data
    with open(iFile, 'rb') as inF:
        with open(oFile, 'wb') as outF:
            outF.write(struct.pack('<Q', fileSize))
            outF.write(iv)
            while True:
                chunk = inF.read(chunkSize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outF.write(encryptor.encrypt(chunk))

    # Remove decrypted file
    os.remove(iFile)

# Decrypt file
################################################################################
def decryptFile(key, iFile, oFile=None, chunkSize=24*1024):
    # Use SHA256 for key
    key = hashlib.sha256(key.encode('utf-8')).digest()

    # Set output file name
    if not oFile:
        oFile = os.path.splitext(iFile)[0].split('.')[0] + '.json'

    # Open encrypted file for reading
    with open(iFile, 'rb') as inF:
        # Read original file size
        originalFileSize = struct.unpack('<Q',
        inF.read(struct.calcsize('Q')))[0]

        # Read IV
        iv = inF.read(16)

        # Setup decryptor
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        # Open file to save decrypted data
        with open(oFile, 'wb') as outF:
            while True:
                chunk = inF.read(chunkSize)
                if len(chunk) == 0:
                    break;
                outF.write(decryptor.decrypt(chunk))
            outF.truncate(originalFileSize)

    # Remove encrypted file
    os.remove(iFile)
