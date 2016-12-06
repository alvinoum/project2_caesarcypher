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


# By Alvin L. Oum

# Ask for username
input_name = input ('Enter your name: ')
print ('Hello ', input_name)
