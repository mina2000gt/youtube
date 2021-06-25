cipher = open('chall.txt','rb').read().strip()

key = b'secret'
flag = b''
for i, c in enumerate(cipher):
    tmp = c ^ key[i % len(key)]
    flag += tmp.to_bytes(1, 'big')
print(flag)