wish = input("Tell me whether you want to (1) encrypt or (2) decrypt")

if wish == (1):
    
    plaintext = input("Please enter a word: ")
    cipherText = " "
    plaintextPosition= 0

    while plaintextPosition < len(plaintext):
         plaintextChar = plaintext[plaintextPosition]
         ASCIIValue = ord(plaintextChar)
         ASCIIValue = ASCIIValue - 3
         cipherText = cipherText + chr(ASCIIValue)
         plaintextPosition = plaintextPosition + 1

    print(str(cipherText))
else:


      ciphertext = input("Please enter a word: ")
      plaintext = " "
      ciphertextPosition = 0

      while ciphertextPosition < len(ciphertext):
         
         ciphertextChar = ciphertext[ciphertextPosition]
         ASCIIValue = ord(ciphertextChar)
         ASCIIValue = ASCIIValue + 3
         plaintext = plaintext + chr(ASCIIValue)
         ciphertextPosition = ciphertextPosition + 1

      print(str(plaintext))


    
