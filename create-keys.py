from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


# Create a private key
print('Generating new key...')
private_key = rsa.generate_private_key(
    public_exponent=3,  # 65537,
    key_size=768,
)

pem = private_key.private_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PrivateFormat.TraditionalOpenSSL,
   encryption_algorithm=serialization.NoEncryption()
)

print('Writing private key...')
with open('./example.pem', 'wb') as f:
    f.write(pem)

public_key = private_key.public_key()
pem_pub = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print('Writing public key...')
with open('./example.pub', 'wb') as f:
    f.write(pem_pub)
