from Crypto.Cipher import AES
cipher = AES.new('KEY',AES.MODE_CBC,'IV')
plaintext = "This is plaintext"
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)
