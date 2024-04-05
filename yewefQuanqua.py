import string

def encrypt(plainText,key):
    cipherText = ""
    for letter in plainText:
        # find the vowel of the key that correlates with current charachter
        vowel = (ord(letter)-4608)%8
        # concatinate the vowel with the letter
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
# print(encrypt("ለሉሊላሌልሎሏ","H"))
print(encrypt("ለሉሊላሌልሎሏ","ሀ"))
print(decrypt("ለሀሉሁሊሂላሃሌሄልህሎሆሏሇ","U"))
print(attack("ለሀሉሁሊሂላሃሌሄልህሎሆሏሇ"))