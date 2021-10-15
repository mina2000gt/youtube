from base64 import b64decode

plain = open('out.txt','rb').read().strip()
for i in range(30):
    plain = b64decode(plain)
    if b'mctf{' in plain:
        print('i=',i)
        print(plain)
        break