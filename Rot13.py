import re
import string

while (True):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    outphrase = ''

    phrase = input(' [+] Please Enter phrase to be processed here, or type (quit) to exit. :> ')

    if phrase == 'quit':
        break

    #test = [pos for pos, char in enumerate(phrase) if char == '_']

    #result = re.findall('[a-z]',phrase)

    for char in phrase:
        if (char == '_'):
            outphrase += '_'
        elif char == '{':
            outphrase += '{'
        elif char == '}':
            outphrase += '}'
        elif char == '!':
            outphrase += '!'
        else:
            outphrase += abc[(abc.find(char) + 13) %26]

    print(outphrase)

    
print('Goodbye! Come again!')