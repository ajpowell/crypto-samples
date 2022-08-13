# from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

'''
Python venv
===========
Full details here: https://docs.python.org/3/library/venv.html
Short version:
    python3 -m venv ./venv
    source ./venv/bin/activate on Mac/Linux 
    or 
    .\\venv\\Scripts\\Activate.ps1 on Windows

'''


# Read in private key from file
print('Loading private key...')
with open('./example.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )


# Read in public key from file
print('Loading public key...')
with open('./example.pub', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )


print('Encrypting data...')
message = b"encrypted data"

# Encrypt some data
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print('Cipher text: {}'.format(base64.b64encode(ciphertext)))

# Decrypt the data
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print('Plain text : {}'.format(plaintext))
