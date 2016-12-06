# Caesar Cipher Source Code
# https://inventwithpython.com/chapter14.html

MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message:')
    return input()