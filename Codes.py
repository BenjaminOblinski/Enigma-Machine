# Course: CS 30
# Period: 3
# Date created: 12/02/2021
# Date last modified:
# Name: Benjamin Oblinski
# Description: A file that stores the cipher functions used by the main file

# Alphabet used by some codes for refrence
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Morse code dictionary used by the morse code functions
morseDict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
             'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
             'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
             'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
             'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
             'z': '--..', '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....', '7': '--...',
             '8': '---..', '9': '----.', '0': '-----'}


def atbashEncode(userCode):
    """ A is replaced with Z, B with y """
    print('\nCipher Text:')
    # Remove spaces and make all text lowercase
    a = userCode.lower()
    text = a.replace(' ', '')
    try:
        for letter in text:
            # Match a to z, b to y
            x = alphabet.index(letter) + 1
            y = 26 - x
            encodedText = alphabet[y]
            print(encodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()


def atbashDecode(userCode):
    """ Z is replaced with A, y with b"""
    print('\nPlain Text:')
    # Remove spaces and make all text lowercase
    a = userCode.lower()
    text = a.replace(' ', '')
    try:
        for letter in text:
            # match z to a, y to b
            x = alphabet.index(letter) + 1
            y = 26 - x
            encodedText = alphabet[y]
            print(encodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    print()


def a1z26Encode(userCode):
    """ A is replaced with 1, b with 2"""
    print('\nCipher Text:')
    # Remove spaces and make all text lowercase
    a = userCode.lower()
    text = a.replace(' ', '')
    try:
        for letter in text:
            # Match each letter to its place in the alphabet
            encodedText = alphabet.index(letter) + 1
            print(encodedText, end=",")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    print()


def a1z26Decode(userCode):
    """ 1 is replaced with a, 2 with b"""
    print('\nPlain Text:')
    # Split the codes string into a
    # List of each individual ltter
    text = userCode.split()
    try:
        for letter in text:
            # replace a number from 1-26 with a letter
            decodedText = chr(int(letter) + 96)
            print(decodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    print()


def ceasarEncode(userCode):
    """ uses a key to rotate 2 alphabtes for encryption """
    rotation = input('Rotate aplpabet by: ')
    print('\nCipher Text:')
    # Remove spaces and make all text lowercase
    a = userCode.lower()
    text = a.replace(' ', '')
    try:
        for letter in text:
            # Match each letter to a letter from the other alphabet
            x = alphabet.index(letter) + int(rotation)
            if x > 25:
                x = x - 26
            encodedText = alphabet[x]
            print(encodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('\nInvalid Entry')
        pass
    print()


def ceasarDecode(userCode):
    """ uses a key to rotate 2 alphabtes for encryption """
    rotation = input('Rotate aplpabet by: ')
    print('\nPlain Text:')
    # Remove spaces and make all text lowercase
    a = userCode.lower()
    text = a.replace(' ', '')
    try:
        for letter in text:
            # Match each letter to a letter from the other alphabet
            x = alphabet.index(letter) - int(rotation)
            encodedText = alphabet[x]
            print(encodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    print()


def asciiEncode(userCode):
    """ Rreplaces characters with their ASCII number """
    print('\nCipher Text:')
    # Remove all spaces from the input text
    text = userCode.replace(' ', '')
    try:
        for letter in text:
            # Change each letter in a number
            encodedText = ord(letter)
            print(encodedText, end=" ")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    print()


def asciiDecode(userCode):
    """ Replaces numbers with the letter or symbol that they coresond to """
    print('\nPlain Text:')
    # Split the codes string into a
    # List of each individual ltter
    a = userCode.split()
    try:
        for letter in a:
            decodedText = chr(int(letter))
            # Change each number into an letter
            print(decodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    print()


def binaryEncode(userCode):
    """ Rreplaces characters with their Binary number """
    print('\nCipher Text:')
    length = 1
    codeSplit = []
    # Remove spaces from the userCode
    userCodeNoSpaces = userCode.replace(' ', '')
    try:
        for i in range(0, len(userCodeNoSpaces), length):
            # Change each letter into a binary number
            a = userCodeNoSpaces[i:i+length]
            codeSplit.append(a)
        for letter in codeSplit:
            encodedText = bin(ord(letter)).replace('b', '')
            print(encodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    print()


def binaryDecode(userCode):
    """ Replaces numbers with the letter or symbol that they coresond to """
    print('\nPlain Text:')
    binaryLength = 8
    codeSplit = []
    try:
        # Split the number every 8 characters
        for i in range(0, len(userCode), binaryLength):
            # Change each number into a letter
            a = userCode[i:i+binaryLength]
            codeSplit.append(a)
        # Decode the numbers into letters
        for letter in codeSplit:
            number = int(letter, 2)
            encodedText = chr(number)
            print(encodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    print()


def morseEncode(userCode):
    """ Replaces numbers with the pattern they corresond to """
    print('\nCipher Text:')
    # Remove spaces and make all text lowercase
    userCodeNoSpaces = userCode.replace(' ', '')
    a = userCodeNoSpaces.lower()
    try:
        for letter in a:
            # Match each letter to a pattern in the morseDict
            encodedText = morseDict[letter]
            print(encodedText, end=' ')
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')

    print()


def morseDecode(userCode):
    """ Replaces patterns with the number they corresond to """
    print('\nPlain Text:')
    # Split the codes string into a
    # List of each individual ltter
    a = userCode.split()
    # Flip the morse dictionary for decoding
    morseDict2 = {value: key for key, value in morseDict.items()}
    try:
        for letter in a:
            # Match each pattern to a letter in the morseDict
            decodedText = morseDict2[letter]
            print(decodedText, end='')
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    print()
