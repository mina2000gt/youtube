cipher = open('encryption','rb').read()
key = b'KEY'
plain = b''
for i in range(len(cipher)):
    p = cipher[i] ^ key[i % len(key)]
    plain += p.to_bytes(1, 'big')
print(plain)
