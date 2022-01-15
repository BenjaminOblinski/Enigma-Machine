## Python Codex Machine
#### This program can encode and decode messages in a variety of ciphers. 
- Atbash
- A1Z26
- Ceasar Shift
- ASCII
- Binary
#### This porgram is intended to aid players of mystery games that often include coded messages and clues. Many ARG games, mystery novels and board games will use ciphers to hide clues. 
#### There are many encoder/decoder cites avalible on the internet, but most only allow you to use one specific cipher. To use a diffrent cipher you must find a new website. This program combines all the most popular codes in one place
### Instructions for Use
#### Begin by choosing a mode to use the codex in. The codex is capable of encoding (taking regular words and encrypting them) and decoding (taking an encrypted message and changing it to readable english. Type 'e' to encode and 'd' to decode. Caps are not important.
#### Once you have chosen a mode, you must choose a method of encryption. The program will promt you to choose from a selection of various codes. 
#### Once you have chosen a code to use, type in what you want to encode/decode and hit enter. The codex will return the encoded/decoded message. After you encode/decode one message you will be promted to input another message. Once you have chosen a code to use, you will remain in that codes loop until you stop the program or type 'stop'. Typing 'stop' will return you to the main menu. Type 'quit' when promted to choose a mode to quit the program
#### Codes marked 'simple subsitiution' mean that any given letter of the plaintext (the readable message) is only and always swapped with on letter in the ciphertext (the unreadable encoded text). For example, the atbash cipher says a = z. Everytime you time 'a' in the plaintext, a 'z' will be returned in the ciphertext. No two letters can be encrypted as the same character. This makes for a code that is relativley simple to break. 
#### Codes marked 'polyalphabetic' are more secure. A poly alphabetic cipher uses multiple alphabets and a key word to encrypt the plaintext. A polyalphabetic cipher is more secure that a simple substitution because any two given letters can be encoded as the same letter depending on the key word. 
#### Some codes will ask you to give a key word. This can be any word of your choice. 
#### Some codes will ask you to give a key. This number is index two sets of alphabets. For example, if the key is 1, a = b, b = c. If the key is 2, a = c, b = d. This can be any number, but it is reccomended it be 1-25. Note that a key of 0, 26, or any multiple of 26 will result in a code where a = a, and will not encrypt anything. 
### Characters to avoid
#### It is okay to use spaces when inputting plain text. The code will remove those spaces for you.
#### When putting in ciphertext to decode, it is important to enter the message as the program asks you to. Some will ask you to enter code with spaces between each 'letter'.
#### Characters like emojis, punctuation, or other text symbols cannot be used in the codes used in this program. 
