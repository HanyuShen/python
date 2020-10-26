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

plaintext = input("Please enter a word :")
cipherText ="  "
plaintextPosition = 0

while (plaintextPosition < len(plaintext)):
    plaintextChar = plaintext[plaintextPosition]
    ASCIIValue = ord(plaintextChar)
    ASCIIValue = ASCIIValue - 3
    cipherText = cipherText + chr(ASCIIValue)
    plaintextPosition = plaintextPosition + 1
    

print(cipherText)
