import rsa

def generate_keys():
    (public_Key, private_Key) = rsa.newkeys(1024)
    with open('keys/public_Key.pem', 'wb') as file:
        file.write(public_Key.save_pkcs1('PEM'))

    with open('keys/private_Key.pem', 'wb') as file:
        file.write(private_Key.save_pkcs1('PEM'))

def load_keys():
    
    with open('keys/public_Key.pem', 'rb') as file:
        public_key = rsa.PublicKey.load_pkcs1(file.read())

    with open('keys/private_Key.pem', 'rb') as file:
        private_Key = rsa.PrivateKey.load_pkcs1(file.read())

    return public_key, private_Key

def encryption(message, key):
    return rsa.encrypt(message.encode('ascii'), key)

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext,key).decode('ascii')
    except:
        return False
    
def sign_sha1(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-1')

def verify_sha1(message,signature, key):
    try:
        rsa.verify(message.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False
    


generate_keys()
public_Key, private_Key = load_keys()

message = input("Enter a message : ")
ciphertext = encryption(message,public_Key)

signature = sign_sha1(message, private_Key)

plaintext = decrypt(ciphertext, private_Key)

print(f'Cipher text: {ciphertext}')
print(f'Signature: {signature}')

if plaintext:
    print(f'Plain text: {plaintext}')
else:
    print('Could not decrypt the message.')

if verify_sha1(plaintext,signature, public_Key):
    print('Signature verified!!')
else:
    print('Could not verify the message signature!!')
