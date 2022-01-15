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

""" Atbash ENCODE """
def atbashEncode(userCode):
    """ A is replaced with Z, B with y """
    print('\nCipher Text:')
    # Remove spaces and make all text lowercase
    a = userCode.lower()
    text = a.replace(' ', '')
    try:
        for letter in text:
            x = alphabet.index(letter) + 1
            y = 26 - x
            encodedText = alphabet[y]
            print(encodedText, end="")
    except KeyError:
        print('Invlaid Entry')
        pass
    print()


""" Atbash DECODE """
def atbashDecode(userCode):
    """ Z is replaced with A, y with b"""
    print('\nPlain Text:')
    # Remove spaces and make all text lowercase
    a = userCode.lower()
    text = a.replace(' ', '')
    try:
        for letter in text:
            x = alphabet.index(letter) + 1
            y = 26 - x
            encodedText = alphabet[y]
            print(encodedText, end="")
    except KeyError:
        print('Invalid Entry')
        pass
    print()


""" a1z26 ENCODE """
def a1z26Encode(userCode):
    """ A is replaced with 1, b with 2"""
    print('\nCipher Text:')
    # Remove spaces and make all text lowercase
    a = userCode.lower()
    text = a.replace(' ','')
    try:
        for letter in text:
            encodedText = alphabet.index(letter) + 1
            print(encodedText, end=",")
    except KeyError:
        print('Invalid Entry')
        pass
    print()


""" a1z26 DECODE """
def a1z26Decode(userCode):
    """ 1 is replaced with a, 2 with b"""
    print('\nPlain Text:')
    # Split the codes string into a 
    # List of each individual ltter
    text = userCode.split()
    try:
        for letter in text:
            decodedText = chr(int(letter) + 96)
            print(decodedText, end="")
    except KeyError:
        print('Invalid Entry')
        pass
    print()


""" ceasar ENCODE """
def ceasarEncode(userCode):
    """ uses a key to rotate 2 alphabtes for encryption """
    rotation = input('Rotate aplpabet by: ')
    print('\nCipher Text:')
    # Remove spaces and make all text lowercase
    a = userCode.lower()
    text = a.replace(' ', '')
    try:
        for letter in text:
            x = alphabet.index(letter) + int(rotation)
            if x > 25:
                x = x - 26
            encodedText = alphabet[x]
            print(encodedText, end="")
    except KeyError:
        print('\nInvalid Entry')
        pass
    print()


""" ceasar DECODE """
def ceasarDecode(userCode):
    """ uses a key to rotate 2 alphabtes for encryption """
    rotation = input('Rotate aplpabet by: ')
    print('\nPlain Text:')
    # Remove spaces and make all text lowercase
    a = userCode.lower()
    text = a.replace(' ', '')
    try:
        for letter in text:
            x = alphabet.index(letter) - int(rotation)
            encodedText = alphabet[x]
            print(encodedText, end="")
    except KeyError:
        print('Invalid Entry')
        pass
    print()


""" ascii ENCODE """
def asciiEncode(userCode):
    """ Rreplaces characters with their ASCII number """
    print('\nCipher Text:')
    # Remove all spaces from the input text
    text = userCode.replace(' ', '')
    try:
        for letter in text:
            encodedText = ord(letter)
            print(encodedText, end=" ")
    except KeyError:
        print('Invalid Entry')
        pass
    print()


""" ascii DECODE """
def asciiDecode(userCode):
    """ Replaces numbers with the letter or symbol that they coresond to """
    print('\nPlain Text:')
    # Split the codes string into a 
    # List of each individual ltter
    a = userCode.split()
    try:
        for letter in a:
            decodedText = chr(int(letter))
            print(decodedText, end="")
    except KeyError:
        print('Invalid Entry')
        pass
    print()


""" binary ENCODE """
def binaryEncode(userCode):
    """ Rreplaces characters with their Binary number """
    print('\nCipher Text:')
    length = 1
    codeSplit = []
    # Remove spaces from the userCode
    userCodeNoSpaces = userCode.replace(' ', '')
    try:
        for i in range(0, len(userCodeNoSpaces), length):
            a = userCodeNoSpaces[i:i+length]
            codeSplit.append(a)
        for letter in codeSplit:
            encodedText = bin(ord(letter)).replace('b', '')
            print(encodedText, end="")
    except KeyError:
        print('Invalid Entry')
        pass
    print()


""" Binary DECODE """
def binaryDecode(userCode):
    """ Replaces numbers with the letter or symbol that they coresond to """
    print('\nPlain Text:')
    binaryLength = 8
    codeSplit = []
    try:
        # Split the number every 8 characters
        for i in range(0, len(userCode), binaryLength):
            a = userCode[i:i+binaryLength]
            codeSplit.append(a)
        # Decode the numbers into letters
        for letter in codeSplit:
            number = int(letter, 2)
            encodedText = chr(number)
            print(encodedText, end="")
    except KeyError:
        print('Invalid Entry')
        pass
    print()

""" morse ENCODE """
def morseEncode(userCode):
    """ Replaces numbers with the pattern they corresond to """
    print('\nCipher Text:')
    # Remove spaces and make all text lowercase
    userCodeNoSpaces = userCode.replace(' ', '')
    a = userCodeNoSpaces.lower()
    try:
        for letter in a:
            encodedText = morseDict[letter]
            print(encodedText, end=' ')
    except KeyError:
        print('Invalid Entry')
        
    print()

""" morse DECODE """
def morseDecode(userCode):
    """ Replaces patterns with the number they corresond to """
    print('\nPlain Text:')
    # Split the codes string into a 
    # List of each individual ltter
    a = userCode.split()
    # Flip the morse dictionary for decoding
    morseDict2 = {value:key for key, value in morseDict.items()}
    try:
        for letter in a:
            decodedText = morseDict2[letter]
            print(decodedText, end='')
    except KeyError:
        print('Invalid Entry')
        pass
    print()
