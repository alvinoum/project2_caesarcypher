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


input_name = input ('Enter your name: ') # Ask for the user’s Name
print ('Hello ', input_name) # Displays user input


MAX_KEY_SIZE = 26 # Sets limit of 26 integers 1-26

def getMode(): # Deciding to Encrypt or Decrypt
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
            # print: display follow text to user
            print('Enter either "encrpyt" or "e" or "d" or "decrypt".')

def getMessage(): # Getting the Message from the Player
    # print: display to the user
    print('Enter your message here:')
    #return - gets the input of encrypt or decrypt and give it back to the program.
    #input() have the user define a string
    return input()

def getKey(): # Getting the Key from the Player
    key = 0 # If 0 is entered, the user is prompted
    while True:
        print('Enter your key number (1-%s)' % (MAX_KEY_SIZE)) # Intructions
        key = int(input()) # Limits user key input to integer
        if (key >=1 and key <= MAX_KEY_SIZE): # Limits key to 1-26 (MAX_KEY_SIZE)
            return key # Loops if key is not within range
        
def getTranslatedMessage(mode, message, key): # Encrypt or Decrypt the message with the given Key
    if mode[0] == 'd': # if mode is equal to d, enter decrypt mode.
        key = -key # changes key to work backwards.
    translated = '' # traslated is a created string of the result.
    
    for symbol in message: # loops over each letter (symbol).
        if symbol.isalpha(): # only encrypts letters and ignore the others.
            num = ord(symbol) # num variable holds the integer ordinal value. ordinal value means ranking.
            num += key # shifts the value using the key. Let the decryption/encryption begin!
            
            if symbol.isupper(): # limits input to only uppercase letters.
                if num > ord('Z'): # of variable is greater than rank Z
                    num -= 26 # go backwards
                elif num < ord('A'): # else if variable is less than rank A
                    num += 26 # go forward
                    
                elif symbol.islower(): # limits input to also lowercase letters
                    if num > ord('z'): # of variables greaters than rank z
                        num -=26 # go backwards
                    elif num < ord('a'): # of variables less than rank a
                        num +=26 # go forwards
                
                translated += chr(num) # "concatenates the encrypted/decrypted character to the translated string." aka turns "h e l l o" to "hello"
            else:
                translated += symbol # "concatenates the original symbol to the translated string. Therefore, spaces, numbers, punctuation marks, and other characters won’t be encrypted or decrypted." aka leaves the non letters as they are.
            return translated # displays the concatenated characters.

mode = getMode() # defining function
message = getMessage() # defining function
key = getKey() # defining function

print('Your translated text is:') # Prompt
print(getTranslatedMessage(mode, message, key)) # Output of function