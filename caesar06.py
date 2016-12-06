# Caesar Cipher
# By Alvin L. Oum
# Based on https://inventwithpython.com/chapter14.html

# Write a Python 3 program to:
# Ask for the user’s Name (and display it back)
# Ask if the user would like to Encrypt or Decrypt
# Ask a user for a their text – either plaintext or cyphertext (based on first question)
# Ask for the Key (should be a number between 1 – 26)
# Based on first question, either:
# Encrypt string by shifting letters +key  
# Decrypt string by shifting letters -key
# Add input data sanitization and error handling
# Only accept numeric input for key – integers only.  No alpha characters  (sanitize input)
# Only accept lowercase alpha characters for string – no numbers or other characters
# Key should be greater than 3
# Encrypt/decrypt to use standard alphabet – no ASCII special characters
# “Graceful” and informative error messages
# BONUS POINTS:  figure out a way to graphically display results (you will need to research importing python modules)

# Changelog
# caesar1   ask for name
# caesar2   printing question
# caesar3   created function and started to enter notes
# caesar4   created a changelog
# caesar5   

# Ask for the user’s Name (and display it back)
input_name = input ('Enter your name: ')
print ('Hello ', input_name)

# Sets limit of 26 integers 1-26
MAX_KEY_SiZE = 26

# Ask if the user would like to Encrypt or Decrypt
print ('Do you wish to Encrypt or Decrypt?')

# def = defining a function
# getMode(): is the of the function
def getMode():
    # "while" is a loop that repeastedly executes a target statement as long as the given condition is true.
    # "True" is a bool type value that is valid
    while True:
        # "print('')" is sending a string function
        print('Do you wish to encrypt or decrypt a message? ')
        # mode is a value we created to equal input() and lower() as = is defining
        # input() is a built in function to allow the user to assign a value to the string.
        # lower() is convert the text to lowercase
        # we are defining mode as the input by the user changed to lowercase.
        mode = input().lower()
        # "if" execute if statement is true
        # mode - creared value of input().lower()
        # "in" appears to be enclosed within the list
        # "'encrpyt e decrypt d'" is the list. It could also be written as ['encrypt', 'e', 'decrypt', 'd'].
        # ".spilt()" Python has a very neat function for breaking up strings into smaller strings. The split function splits a single string into a string array using the separator defined. If no separator is defined, whitespace is used. -www.pythonforbeginners.com/dictionary/python-split
        if mode in 'encrpyt e decrypt d'.split():
            # return: "This function will return the first character in mode as long as mode is equal to 'encrypt', 'e', 'decrypt', or 'd'. Therefore, getMode() will return the string 'e' or the string 'd' (but the user can type in either “e”, “encrypt”, “d”, or “decrypt”.)" -Inventwithpython
            # mode - created value of input().lower()
            return mode
        # else: excute if statement is false
        else:
            print('Enter either "encrpyt" or "e" or decypt" or decrypt".')