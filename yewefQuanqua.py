import string
ha = "ሇ"
def letterToNumber(m):
    return string.ascii_lowercase.index(m)
print(ord(ha))
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

print(encrypt("ለሉሊላሌልሎሏ","ሀ"))
print(decrypt("ለሀሉሁሊሂላሃሌሄልህሎሆሏሇ","U"))