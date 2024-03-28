import string

def encrypt(plainText,key):
    cipherText = ""
    for letter in plainText:
        vowel = (ord(letter)-4608)%8
        cipherText+=(letter+chr(ord(key)+vowel))
    return cipherText

def decrypt(cipherText,key):
    plainText = ""
    even = True
    for letter in cipherText:
        if(even):
            plainText+=letter
            even = False
        else: 
            even = True
    return plainText

def attack(cipherText):
    plainText = ""
    i=0
    for letter in cipherText:
        if(i%2 == 0):
            plainText += letter
        i+=1
    return plainText

# Test Cases
print(encrypt("ለሉሊላሌልሎሏ","ሀ"))
print(attack("ለሀሉሁሊሂላሃሌሄልህሎሆሏሇ"))
print(decrypt("ለሀሉሁሊሂላሃሌሄልህሎሆሏሇ","U"))