plain = b"Oh! You're genius! Thank you for watching!!"
key = b'KEY'
cipher = b''
for i in range(len(plain)):
    c = plain[i] ^ key[i%len(key)]
    cipher += c.to_bytes(1, 'big')
open('encryption','wb').write(cipher)
