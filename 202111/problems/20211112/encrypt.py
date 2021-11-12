from Crypto.Cipher import AES
from flag import FLAG

r = len(FLAG) % 16
f = FLAG.ljust(len(FLAG) + 16 - r).encode()

key = b'testtesttesttest'
cipher = AES.new(key, AES.MODE_ECB)
c = cipher.encrypt(f).hex()
open('output.txt','w').write(f'{c}')