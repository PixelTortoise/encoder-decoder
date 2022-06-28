from dis import dis
import string
import random
loop = True
dbannedchars = ['*', '_', '~', '`', '>', '|']

encchars = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
encchars = list(encchars)
char = '\\'
for idx, ele in enumerate(encchars):
        encchars[idx] = ele.replace(char, '')

while loop == True:
    dfquestion = input('Would you like to make the key discord friendly? (no characters like *, _, ~, `, >, |) y or n ')

    if dfquestion == 'y':
        discordfriendly = True
        loop = False

    elif dfquestion == 'n':
        discordfriendly = False
        loop = False
    
    else:
        print('Invalid Syntax!')
        loop = True

if discordfriendly == True:

    for i in dbannedchars:

        char = i
        for idx, ele in enumerate(encchars):
            encchars[idx] = ele.replace(char, '')
        
enclen = len(encchars)

usablechars = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + ' ' + string.digits
usablechars = list(usablechars)

keyname = str(input('What would you like to name your key? '))

try:
    keytxt = open('keys/{}key.txt'.format(keyname), 'w')
    keys = ''

    for i in list(usablechars):
        termlen = random.randint(5, 10)

        for i in range(0, termlen):
            keys += random.choice(encchars)

        keys += '\n'

    keytxt.write(keys)
    keytxt.close()
    print('Key made successfully!')
    cont = input()

except:
    print('Something went wrong! Make sure that the keys file exists!')
    cont = input()
