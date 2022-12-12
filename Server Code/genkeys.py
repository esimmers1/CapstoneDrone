from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP as pkrsa

# generate keypair
key = RSA.generate(2048)

# export private key
f = open("privatekey.pem", "wb+")
f.write(key.export_key('PEM'))
f.close()

# export public key
f = open("publickey.pem", "wb+")
f.write(key.public_key().export_key(format='PEM'))
f.close()

# ensure keys are valid by testing them
pubkey = RSA.import_key(open("publickey.pem", "r").read())
message = pkrsa.new(key).encrypt(b"Key generation successful!")

prikey = RSA.import_key(open("privatekey.pem").read())
print(pkrsa.new(key).decrypt(message).decode("UTF-8"))
