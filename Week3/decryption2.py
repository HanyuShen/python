#1: plaintext ← read(‘Plaintext:’)
#2: cipherTest ← “ ”
#3: plaintextPosition ← 0
#4: while (plaintextPosition < length(plaintext)) do
#5: plaintextChar ← plaintext[plaintextPosition]
#6: ASCIIValue ← GetASCIIValue(plaintextChar)
#7: ASCIIValue ← ASCIIValue - 3
#8: cipherText ← cipherText + GetCharValue(ASCIIValue)
#9: plaintextPosition ← plaintextPosition + 1
#10: end while
#11: display(cipherText)


ciphertext = input("Please enter a word :")
plainText ="  "
ciphertextPosition = 0

while (ciphertextPosition < len(ciphertext)):
    ciphertextChar = ciphertext[ciphertextPosition]
    ASCIIValue = ord(ciphertextChar)
    ASCIIValue = ASCIIValue + 3
    plainText = plainText + chr(ASCIIValue)
    ciphertextPosition = ciphertextPosition + 1
    

print(plainText)
