from Crypto.Cipher import AES
from os import urandom

encrypted = open('output.txt','r').read().strip()
encrypted = bytes.fromhex(encrypted)

for i in range(256):
    for j in range(256):
        key = b'Thisistestkey!' + i.to_bytes(1,'big') + j.to_bytes(1,'big')
        cipher = AES.new(key, AES.MODE_ECB)
        p = cipher.decrypt(encrypted)
        if b'mctf{' in p:
            print(p)