"""
Ashton Mahatoo
9/28/2023

"""


import rsa
import os
import fileinput
from cryptography.fernet import Fernet 


#file_to_be_encrypted = input("What is the name of you would like to encrypt?? ")
#new_file_name = open(file_to_be_encrypted, "rb")

fernet_key_file = open("key_file.txt", "rb")
fernet_key = fernet_key_file.read()
fernet_cipher = Fernet(fernet_key)



