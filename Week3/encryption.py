# Encryption Program
#1: plaintext ← read(‘Plaintext:’)
#2: cipherTest ← “ ”
#3: alphabet ← “XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC”
#4: plaintextPosition ← 0
#5: while (plaintextPosition < length(plaintext)) do
#6: plaintextChar ← plaintext[plaintextPosition]
#7: alphabetPosition ← 3
#8: while plaintextChar ̸= alphabet[alphabetPosition] do
#9: alphabetPosition ← alphabetPosition + 1
#10: end while
#11: alphabetPosition ← alphabetPosition - 3
#12: cipherText ← cipherText + alphabet[alphabetPosition]
#13: plaintextPosition ← plaintextPosition + 1
#14: end while
#15: display(cipherText)

plaintext = input("Please input some plaintext: ")
cipherText = "  "
alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
plaintextPosition = 0
while plaintextPosition < len(plaintext):
    plaintextChar = plaintext[plaintextPosition]
    alphabetPosition = 3
    while plaintextChar != alphabet[alphabetPosition]:
        alphabetPosition = alphabetPosition + 1
        
    alphabetPosition = alphabetPosition - 3
    cipherText = cipherText + alphabet[alphabetPosition]
    plaintextPosition = plaintextPosition + 1
     
print(cipherText)
