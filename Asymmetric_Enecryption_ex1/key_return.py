
# This loads and returns the public and private key onto a publicKey and privateKey variable.

import rsa


def keyReturn():
    with open("publicKey.pem", "rb") as public:
        publicKey = rsa.PublicKey.load_pkcs1(public.read())

    with open("privateKey.pem", "rb") as private:
        privateKey = rsa.PrivateKey.load_pkcs1(private.read())

    return publicKey, privateKey
    #return print(b"\nThis is the private key: ".decode()
    #,privateKey,"\n\nAnd this is the public key: " , publicKey,"\n")