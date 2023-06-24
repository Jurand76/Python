import os
import hashlib
import string

# reading link from user

def inputLink():
    inputText = input('Enter URL: ');
    if len(inputText) < 3:
        print('Bad URL - too short')
        return 'Error'
    if not '.' in inputText:
        print('Bad URL - no dot in URL')
        return 'Error'
    return inputText

# reading database

def readDatabase():
    if os.path.exists(fileName):
        file = open(fileName, "r")
        for line in file:
            readLine = line.rstrip()
            link, shorten = readLine.split(' ')
            linksDatabase[link] = shorten

# hashing - MD5 encryption

def convertToHash(text):
    hashObject = hashlib.new('md5')
    hashObject.update(text.encode('utf-8'))
    hashHex = hashObject.hexdigest()
    return int(hashHex, 16)

# shortening - using Base62 algorithm

def encodeBase62(hash):
    baseChars = string.digits + string.ascii_letters
    baseSize = len(baseChars)
    base62 = ''
    while hash > 0:
        hash, remainder = divmod(hash, baseSize)
        base62 = baseChars[remainder] + base62
    return base62
    
# saving new shortened link to file

def saveToFile(text1, text2):
    if os.path.exists(fileName):
        file = open(fileName, "a")
        file.write('\n' + userLink + ' ' + shortened)
        file.close()
    else:
        print('Database file generated!')
        file = open(fileName, "w")
        file.write(userLink + ' ' + shortened)
        file.close()

# global variables

linksDatabase = {}
currentDir = os.getcwd()
fileName = currentDir + r'\links.txt';

# getting link from user

userLink = inputLink()

# checking link in database file and converting if not exists

readDatabase()
if userLink in linksDatabase:
    print('Shortened link exists in database: ' + linksDatabase[userLink])
else:
    converted = convertToHash(userLink)
    shortened = encodeBase62(converted)[0:10]
    saveToFile(userLink, shortened)
    print('Shortened link: ' + shortened)
    



