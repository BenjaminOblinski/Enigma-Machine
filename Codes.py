# Course: CS 30
# Period: 3
# Date created: 12/02/2021
# Date last modified:
# Name: Benjamin Oblinski
# Description: A mock-Enigma Machine that can encode and decode messages
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

""" Atbash ENCODE """
def atbashEncode(userCode):
    print('\nCipher Text:')
    a = userCode.lower()
    text = a.replace(' ', '')
    for letter in text:
        x = alphabet.index(letter) + 1
        y = 26 - x
        encodedText = alphabet[y]
        print(encodedText, end="")
    print()


""" Atbash DECODE """
def atbashDecode(userCode):
    print('\nPlain Text:')
    a = userCode.lower()
    text = a.replace(' ', '')
    for letter in text:
        x = alphabet.index(letter) + 1
        y = 26 - x
        encodedText = alphabet[y]
        print(encodedText, end="")
    print()


""" a1z26 ENCODE """
def a1z26Encode(userCode):
    print('\nCipher Text:')
    a = userCode.lower()
    text = a.replace(' ','')
    for letter in text:
        encodedText = alphabet.index(letter) + 1
        print(encodedText, end=",")
    print()


""" a1z26 DECODE """
def a1z26Decode(userCode):
    print('\nPlain Text:')
    text = userCode.split()
    for letter in text:
        decodedText = chr(int(letter) + 96)
        print(decodedText, end="")
    print()


""" ceasar ENCODE """
def ceasarEncode(userCode):
    rotation = input('Rotate aplpabet by: ')
    print('\nCipher Text:')
    a = userCode.lower()
    text = a.replace(' ', '')
    for letter in text:
        x = alphabet.index(letter) + int(rotation)
        if x > 25:
            x = x - 26
        encodedText = alphabet[x]
        print(encodedText, end="")
    print()


""" ceasar DECODE """
def ceasarDecode(userCode):
    rotation = input('Rotate aplpabet by: ')
    print('\nPlain Text:')
    a = userCode.lower()
    text = a.replace(' ', '')
    for letter in text:
        x = alphabet.index(letter) - int(rotation)
        encodedText = alphabet[x]
        print(encodedText, end="")
    print()


""" ascii ENCODE """
def asciiEncode(userCode):
    print('\nCipher Text:')
    text = userCode.replace(' ', '')
    for letter in text:
        encodedText = ord(letter)
        print(encodedText, end=" ")
    print()


""" ascii DECODE """
def asciiDecode(userCode):
    print('\nPlain Text:')
    a = userCode.split()
    for letter in a:
        decodedText = chr(int(letter))
        print(decodedText, end="")
    print()


""" binary ENCODE """
def binaryEncode(userCode):
    print('\nCipher Text:')
    length = 1
    codeSplit = []
    userCodeNoSpaces = userCode.replace(' ', '')
    for i in range(0, len(userCodeNoSpaces), length):
        a = userCodeNoSpaces[i:i+length]
        codeSplit.append(a)
    for letter in codeSplit:
        encodedText = bin(ord(letter)).replace('b', '')
        print(encodedText, end="")
    print()


""" Binary DECODE """
def binaryDecode(userCode):
    print('\nPlain Text:')
    binaryLength = 8
    codeSplit = []
    for i in range(0, len(userCode), binaryLength):
        a = userCode[i:i+binaryLength]
        codeSplit.append(a)
    for letter in codeSplit:
        number = int(letter, 2)
        encodedText = chr(number)
        print(encodedText, end="")
    print()
