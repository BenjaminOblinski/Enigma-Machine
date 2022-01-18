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

vigenereTable = {'a': 'j', 'b': 'g', 'c': 'p', 'd': 'i', 'e': 'c',
                 'f': 's', 'g': 'b', 'h': 'v', 'i': 'n', 'j': 't',
                 'k': 'f', 'l': 'l', 'm': 'x', 'n': 'e', 'o': 'y',
                 'p': 'm', 'q': 'r', 'r': 'u', 's': 'k', 't': 'o',
                 'u': 'd', 'v': 'h', 'w': 'a', 'x': 'z', 'y': 'w',
                 'z': 'q'}

def atbashEncode(userCode):
    """ A is replaced with Z, B with y """
    print('\nCipher Text:')
    # Remove spaces and make all text lowercase
    # userCode stores the message that the user inputs
    a = userCode.lower()
    # a stores the user code in all lowercase
    text = a.replace(' ', '')
    # text stores the user code with no spaces and all lowercase
    try:
        for letter in text:
            # Match a to z, b to y
            # x stores the index of the letter + 1
            x = alphabet.index(letter) + 1
            # y stores the opposite value of the x value
            y = 26 - x
            # encodedtext stores the userCode after it has been encoded
            encodedText = alphabet[y]
            print(encodedText, end="")
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
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
    # a stores the user code in all lowercase
    text = a.replace(' ', '')
    # text stores the usercode with no spaces and all lowercase
    try:
        for letter in text:
            # match z to a, y to b
            x = alphabet.index(letter) + 1
            # x stores the index of the letter + 1
            y = 26 - x
            # y stores the opposite value of the x value
            decodedText = alphabet[y]
            # decodedText stores the userCode after it has been decoded
            print(decodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()


def a1z26Encode(userCode):
    """ A is replaced with 1, b with 2"""
    print('\nCipher Text:')
    # Remove spaces and make all text lowercase
    a = userCode.lower()
    # a stores the user code in all lowercase
    text = a.replace(' ', '')
    # text stores the usercode with no spaces and all lowercase
    try:
        for letter in text:
            # Match each letter to its place in the alphabet
            # encodedtext stores the userCode after it has been encoded
            encodedText = alphabet.index(letter) + 1
            print(encodedText, end=",")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()


def a1z26Decode(userCode):
    """ 1 is replaced with a, 2 with b"""
    print('\nPlain Text:')
    # Split the codes string into a
    # List of each individual ltter
    text = userCode.split()
    # text stores the user code split into each word
    try:
        for letter in text:
            # replace a number from 1-26 with a letter
            # decodedText stores the userCode after it has been decoded
            decodedText = chr(int(letter) + 96)
            print(decodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    except OverflowError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()


def ceasarEncode(userCode):
    """ uses a key to rotate 2 alphabtes for encryption """
    rotation = input('Rotate aplpabet by: ')
    print('\nCipher Text:')
    # Remove spaces and make all text lowercase
    a = userCode.lower()
    # a stores the user code in all lowercase
    text = a.replace(' ', '')
    # text stores the user code with no spaces and all lowercase
    try:
        for letter in text:
            # Match each letter to a letter from the other alphabet
            x = alphabet.index(letter) + int(rotation)
            if x > 25:
                x = x - 26
            encodedText = alphabet[x]
            # encodedtext stores the userCode after it has been encoded
            print(encodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('\nInvalid Entry')
        pass
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()


def ceasarDecode(userCode):
    """ uses a key to rotate 2 alphabtes for encryption """
    rotation = input('Rotate aplpabet by: ')
    print('\nPlain Text:')
    # Remove spaces and make all text lowercase
    a = userCode.lower()
    # a stores the user code in all lowercase
    text = a.replace(' ', '')
    # text stores the user code with no spaces and all lowercase
    try:
        for letter in text:
            # Match each letter to a letter from the other alphabet
            x = alphabet.index(letter) - int(rotation)
            # decodedText stores the userCode after it has been decoded
            decodedText = alphabet[x]
            print(decodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()


def asciiEncode(userCode):
    """ Rreplaces characters with their ASCII number """
    print('\nCipher Text:')
    # Remove all spaces from the input text
    text = userCode.replace(' ', '')
    # text stores the user code with no spaces
    try:
        for letter in text:
            # Change each letter in a number
            encodedText = ord(letter)
            # encodedtext stores the userCode after it has been encoded
            print(encodedText, end=" ")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    except OverflowError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()


def asciiDecode(userCode):
    """ Replaces numbers with the letter or symbol that they coresond to """
    print('\nPlain Text:')
    # Split the codes string into a
    # List of each individual ltter
    a = userCode.split()
    # a stores the user code split into each word
    try:
        for letter in a:
            # decodedText stores the userCode after it has been decoded
            decodedText = chr(int(letter))
            # Change each number into an letter
            print(decodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    except OverflowError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()


def binaryEncode(userCode):
    """ Rreplaces characters with their Binary number """
    print('\nCipher Text:')
    length = 1
    codeSplit = []
    # Remove spaces from the userCode
    userCodeNoSpaces = userCode.replace(' ', '')
    # userCodeNoSpaces stores the usercode with no spaces
    try:
        for i in range(0, len(userCodeNoSpaces), length):
            # Change each letter into a binary number
            a = userCodeNoSpaces[i:i+length]
            codeSplit.append(a)
        for letter in codeSplit:
            encodedText = bin(ord(letter)).replace('b', '')
            # encodedtext stores the userCode after it has been encoded
            print(encodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()


def binaryDecode(userCode):
    """ Replaces numbers with the letter or symbol that they coresond to """
    print('\nPlain Text:')
    binaryLength = 8
    # length of each section of ciphertext
    codeSplit = []
    try:
        # Split the number every 8 characters
        for i in range(0, len(userCode), binaryLength):
            # Change each number into a letter
            a = userCode[i:i+binaryLength]
            # a stores ascii vlaue of the text
            codeSplit.append(a)
        # Decode the numbers into letters
        for letter in codeSplit:
            number = int(letter, 2)
            # number stores the ascii value of the letter
            # decodedText stores the userCode after it has been decoded
            decodedText = chr(number)
            print(decodedText, end="")
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()


def morseEncode(userCode):
    """ Replaces numbers with the pattern they corresond to """
    print('\nCipher Text:')
    # Remove spaces and make all text lowercase
    userCodeNoSpaces = userCode.replace(' ', '')
    a = userCodeNoSpaces.lower()
    # a stores the user code in all lowercase
    try:
        for letter in a:
            # Match each letter to a pattern in the morseDict
            # encodedtext stores the userCode after it has been encoded
            encodedText = morseDict[letter]
            print(encodedText, end=' ')
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()


def morseDecode(userCode):
    """ Replaces patterns with the number they corresond to """
    print('\nPlain Text:')
    # Split the codes string into a
    # List of each individual ltter
    a = userCode.split()
    # a stores the user code split into each word
    # Flip the morse dictionary for decoding
    morseDict2 = {value: key for key, value in morseDict.items()}
    try:
        for letter in a:
            # Match each pattern to a letter in the morseDict
            decodedText = morseDict2[letter]
            # decodedText stores the userCode after it has been decoded
            print(decodedText, end='')
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()


def vigenereEncode(userCode):
    """ Replaces letters with the letters they corresond to """
    print('\nCipher Text:')
    # Remove spaces and make all text lowercase
    userCodeNoSpaces = userCode.replace(' ', '')
    a = userCodeNoSpaces.lower()
    # a stores the user code in all lowercase
    try:
        for letter in a:
            # Match each letter to a pattern in the vigenereTable
            # encodedtext stores the userCode after it has been encoded
            encodedText = vigenereTable[letter]
            print(encodedText, end='')
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()


def vigenereDecode(userCode):
    """ Replaces letters with the number they corresond to """
    print('\nPlain Text:')
    # Split the codes string into a
    # List of each individual ltter
    userCodeNoSpaces = userCode.replace(' ', '')
    a = userCodeNoSpaces.lower()
    # a stores the user code split into each word
    # Flip the vigenereTable for decoding
    vigenereTable2 = {value: key for key, value in vigenereTable.items()}
    try:
        for letter in a:
            # Match each pattern to a letter in the morseDict
            decodedText = vigenereTable2[letter]
            # decodedText stores the userCode after it has been decoded
            print(decodedText, end='')
    except KeyError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invalid Entry')
        pass
    except ValueError:
        # If the user inputs a symbol the code does not understand
        # Print invalid entry and restart the code
        print('Invlaid Entry')
        pass
    print()