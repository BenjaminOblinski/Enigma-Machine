# Course: CS 30
# Period: 3
# Date created: 12/02/2021
# Date last modified:
# Name: Benjamin Oblinski
# Description: A mock-Enigma Machine that can encode and decode messages
import time
from Codes import atbashEncode, atbashDecode, a1z26Encode, a1z26Decode, ceasarEncode, ceasarDecode, asciiEncode, asciiDecode, binaryEncode, binaryDecode

codes = {'atbash  ': 'Simple Substitution. A = z, B = y, etc',
         'a1z26   ': 'Simple Substitution. A = 1, B = 2, etc',
         'ceasar  ': 'Simple Substitution. Uses a key to rotate an alphabet',
         'ascii   ': 'Simple Substitution. Used in computers to display text',
         'binary  ': 'Simple Substitution. Used by computers to transmit data'}

accpetableCodes = ['atbash', 'a1z26', 'ceasar', 'ascii', 'binary']
accpetableModes = ['E', 'D']

def mainMenu():
    print('################# ENIGMA MACHINE #################')

    # Choose mode segment of the menu
    y = False
    while y == False:
        print('Encode or Decode E/D')
        chooseMode = input('-> ')
        if chooseMode.title() in accpetableModes:
            y = True
        else:
            y = False
            print('\nInvalid Entry\n')

    # Choose code segment of the menu
    print('Code Options:')
    for code in codes:
        print(f" {code} - {codes[code]}")
    print()

    x = False
    while x == False:
        print('What code/cihper would you like to use?')
        chooseCode = input('-> ')
        if chooseCode in accpetableCodes:
            x = True
        else:
            x = False
            print('Invlaid Entry')

    if chooseMode.title() == 'E':
        encode(chooseCode)
    elif chooseMode.title() == 'D':
        decode(chooseCode)


def encode(chooseCode):
    print('\nType what you want to encode')

    if chooseCode.lower() == 'atbash':
        while True:
            userCode = input('\nPlain Text:\n')
            if userCode == 'stop':
                break
            atbashEncode(userCode)

    elif chooseCode.lower() == 'a1z26':
        while True:
            userCode = input('\nPlain Text:\n')
            if userCode == 'stop':
                break
            a1z26Encode(userCode)

    elif chooseCode.lower() == 'ceasar':
        while True:
            userCode = input('\nPlain Text:\n')
            if userCode == 'stop':
                break
            ceasarEncode(userCode)
    
    elif chooseCode.lower() == 'ascii':
        while True:
            userCode = input('\nPlain Text:\n')
            if userCode == 'stop':
                break
            asciiEncode(userCode)

    elif chooseCode.lower() == 'binary':
        while True:
            userCode = input('\nPlain Text:\n')
            if userCode == 'stop':
                break
            binaryEncode(userCode)


def decode(chooseCode):
    print('\nType what you want to decode')

    if chooseCode == 'ascii':
        print('Type the numbers with spaces between each \'letter\'')

    if chooseCode == 'a1z26':
        print('Type the numbers with spaces between each \'letter\'')

    if chooseCode.lower() == 'atbash':
        while True:
            userCode = input('\nCipher Text:\n')
            if userCode == 'stop':
                break
            atbashDecode(userCode)

    elif chooseCode.lower() == 'a1z26':
        while True:
            userCode = input('\nCipher Text:\n')
            if userCode == 'stop':
                break
            a1z26Decode(userCode)

    elif chooseCode.lower() == 'ceasar':
        while True:
            userCode = input('\nCipher Text:\n')
            if userCode == 'stop':
                break
            ceasarDecode(userCode)

    elif chooseCode.lower() == 'ascii':
        while True:
            userCode = input('\nCipher Text:\n')
            if userCode == 'stop':
                break
            asciiDecode(userCode)

    elif chooseCode.lower() == 'binary':
        while True:
            userCode = input('\nCipher Text:\n')
            if userCode == 'stop':
                break
            binaryDecode(userCode)

while True:
    mainMenu()
    print('\n')
    time.sleep(1)
