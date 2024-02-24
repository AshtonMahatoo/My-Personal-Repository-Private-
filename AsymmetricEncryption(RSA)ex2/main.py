import rsa
from key_creation import keyCreation
from key_return import keyReturn
from crypto import encryption, decryption

keyCreation()
publicKey, privateKey = keyReturn()

"""

################ Testing Input Files ###############

inputFileName = input(" Please enter the source filename you would like to encrypt!!: ")
inputFile = open(inputFileName, "rb")
read_content = inputFile.read()

# This New_File_Output.txt stores the content of the file entered in the Terminal
with open("New_File_Output.txt", "wb")as file: 
    file.write(read_content)

with open('New_File_Output.txt','rb')as file:
    original= file.read()

ciphertext = encryption(original,publicKey)
with open("ciphertext.txt", "wb") as file:
    file.write(ciphertext)
print(f"Ciphertext{ciphertext}")
############## End Of Test ###########
"""



message = input("What is your message??")
ciphertext = encryption(message, publicKey)
with open("ciphertext.txt", "wb") as file:
    file.write(ciphertext)
 
plain_text = decryption(ciphertext, privateKey)
with open("SLEEP", "wb") as file:
    file.write(ciphertext)
print(f"Cipher text:{ciphertext}")
print(f"Plain Text {plain_text}")

