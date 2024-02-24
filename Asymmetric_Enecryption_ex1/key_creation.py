
# This file generates the public and private keys and stores it in the KEY folder


import rsa


def keyCreation():

    (publicKey, privateKey) = rsa.newkeys(1024)

    with open("publicKey.pem", "wb") as public:
        public.write(publicKey.save_pkcs1("PEM"))

    with open("privateKey.pem", "wb") as private:
        private.write(privateKey.save_pkcs1("PEM"))

    