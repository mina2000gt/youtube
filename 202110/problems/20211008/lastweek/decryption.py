plain_start = b'\x89\x50\x4E\x47\x0D\x0A'
dat = open('chall','rb').read()
key = b''
for i in range(6):
    key += (plain_start[i] ^ dat[i]).to_bytes(1, 'big')
print(key)

out = b''
for i in range(len(dat)):
    out += (dat[i] ^ key[i%len(key)]).to_bytes(1, 'big')
open('recover.png','wb').write(out)