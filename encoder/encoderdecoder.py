import string
from textwrap import indent

chars = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + ' ' + string.digits
chars = list(chars)

while True:
    loop = True
    keyname = str(input('What is the name of the key file? (the part of the name before the "key" part) '))

    try:
        key = open('keys/{}key.txt'.format(keyname), 'r')
        print('Opened {}key.txt!'.format(keyname))

        keys = key.readlines()
        char = '\n'
        for idx, ele in enumerate(keys):
            keys[idx] = ele.replace(char, '')
        key.close()
        
        while loop == True:
            encdecr = str(input('Encrypt or decrypt? (e or d) '))

            if encdecr == 'e':
                loop = False

                text = str(input('What would you lke to encrypt? '))
                text = list(text)
                encryptmessage = ''

                for i in text:
                    position = chars.index(i)
                    encryptmessage += keys[position] + ' '

                print('Your encrypted message is:\n{}\n'.format(encryptmessage))

            elif encdecr == 'd':
                loop = False
                decodedmsg = ''
                
                encodedmsg = str(input('What is the encoded message you would like to decode? '))
                encodedmsg = encodedmsg.split(' ')

                for i in encodedmsg:
                    position = keys.index(i)
                    decodedmsg += chars[position]

                print('Your decoded message is:\n{}\n'.format(decodedmsg))

            else:
                print('Invalid Syntax!\n')

    except:
        print('There was en error!\n')