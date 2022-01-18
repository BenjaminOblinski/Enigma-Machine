# Course: CS 30
# Period: 3
# Date created: 12/02/2021
# Date last modified:
# Name: Benjamin Oblinski
# Description: A codex Machine that can encode and decode messages

import sys
import time
# Import ciphers from the 'Codes' file
from codes import atbashEncode, atbashDecode, a1z26Encode, a1z26Decode, \
                  ceasarEncode, ceasarDecode, asciiEncode, asciiDecode, \
                  binaryEncode, binaryDecode, morseEncode, morseDecode, \
                  vigenereEncode, vigenereDecode

# Dictionary of the chiphers with short write ups
codes = {'atbash  ': 'A = z, B = y, etc',
         'a1z26   ': 'A = 1, B = 2, etc',
         'ceasar  ': 'Uses a key to rotate an alphabet',
         'ascii   ': 'Used in computers to display text',
         'binary  ': 'Used by computers to transmit data',
         'morse   ': 'Used to send messages with \
pulses of light or sound'}

# Lists of acceptable responses
accpetableCodes = ['atbash', 'a1z26', 'ceasar', 'ascii', 'binary', \
'morse', 'vigenere']
accpetableModes = ['E', 'D', 'Quit']


def mainMenu():
    """ The Main function that controls the menu """
    print('################# Codex MACHINE #################')

    # Choose mode segment of the menu
    y = False
    while y == False:
        # Codes repeatadle asks you to choose a mode until
        # You give an acceptable resopnse
        # Once you give a correct response, the code breaks out of the loop
        print('Encode or Decode E/D, or type quit to exit')
        chooseMode = input('-> ')
        # chooseMode stores the mode the user has chosen
        if chooseMode.title() in accpetableModes:
            y = True
        else:
            y = False
            print('\nInvalid Entry\n')
        if chooseMode.lower() == 'quit':
            # IF user types quit, close the program
            print('System closed')
            sys.exit()

    # Choose code segment of the menu
    print('Code Options:')
    # Print options that the user can choose from
    for code in codes:
        print(f" {code} - {codes[code]}")
    print('\nRemember, you can type \'stop\' when using a \
code to return to the main menu\n')
    print('You can also quit when asked to choose a mode by typing \'quit\'')

    x = False
    while x == False:
        # Codes repeatadle asks you to choose a code until
        # You give an acceptable resopnse
        # Once you give a correct response, the code breaks out of the loop
        print('What code/cihper would you like to use?')
        chooseCode = input('-> ')
        # chooseCode stores the users choice of cipher to us
        if chooseCode in accpetableCodes:
            x = True
        else:
            x = False
            print('Invlaid Entry')

    if chooseMode.title() == 'E':
        # If users selects encode mode, run the encode function
        encode(chooseCode)
    elif chooseMode.title() == 'D':
        # If users selects decode mode, run the decode function
        decode(chooseCode)


def encode(chooseCode):
    """ When called the encode funtion asks the player
    to choose from the avalible codes in encode mode
    """
    print('\nType what you want to encode')

    if chooseCode.lower() == 'atbash':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nPlain Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            atbashEncode(userCode)
            # Run the encode function with
            # the user input as the argument

    elif chooseCode.lower() == 'a1z26':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nPlain Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            a1z26Encode(userCode)
            # Run the encode function with
            # the user input as the argument

    elif chooseCode.lower() == 'ceasar':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nPlain Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            ceasarEncode(userCode)
            # Run the encode function with
            # the user input as the argument

    elif chooseCode.lower() == 'ascii':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nPlain Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            asciiEncode(userCode)
            # Run the encode function with
            # the user input as the argument

    elif chooseCode.lower() == 'binary':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nPlain Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            binaryEncode(userCode)
            # Run the encode function with
            # the user input as the argument

    elif chooseCode.lower() == 'morse':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nPlain Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            morseEncode(userCode)
            # Run the encode function with
            # the user input as the argument

    elif chooseCode.lower() == 'vigenere':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nPlain Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            vigenereEncode(userCode)
            # Run the encode function with
            # the user input as the argument


def decode(chooseCode):
    """ When called the encode funtion asks the player
    to choose from the avalible codes in decode mode
    """
    print('\nType what you want to decode')

    if chooseCode == 'ascii':
        # If the user is using ascii, remind them to put spaces
        # between each encoded letter
        print('Type the numbers with spaces between each \'letter\'')

    if chooseCode == 'morse':
        # If using morse code, remind users how to type the characters
        print('Type the morse code with spaces between characters')
        print('Type a long pulse as - and short pulses as .')

    if chooseCode == 'a1z26':
        # If the user is using a1z26, remind them to put spaces
        # between each encoded letter
        print('Type the numbers with spaces between each \'letter\'')

    if chooseCode.lower() == 'atbash':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nCipher Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            atbashDecode(userCode)
            # Run the encode function with
            # the user input as the argument

    elif chooseCode.lower() == 'a1z26':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nCipher Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            a1z26Decode(userCode)
            # Run the encode function with
            # the user input as the argument

    elif chooseCode.lower() == 'ceasar':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nCipher Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            ceasarDecode(userCode)
            # Run the encode function with
            # the user input as the argument

    elif chooseCode.lower() == 'ascii':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nCipher Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            asciiDecode(userCode)
            # Run the encode function with
            # the user input as the argument

    elif chooseCode.lower() == 'binary':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nCipher Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            binaryDecode(userCode)
            # Run the encode function with
            # the user input as the argument

    elif chooseCode.lower() == 'morse':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nCipher Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            morseDecode(userCode)
            # Run the encode function with
            # the user input as the argument

    elif chooseCode.lower() == 'vigenere':
        while True:
            # userCode stores the message that the user inputs
            userCode = input('\nPlain Text:\n')
            # Ask user for input
            if userCode == 'stop':
                # if user types stop, break from the loop
                break
            vigenereDecode(userCode)
            # Run the encode function with
            # the user input as the argument


while True:
    mainMenu()
    # Call main menu
    print('\n')
    # Space
    time.sleep(1)
    # wait 1 second
