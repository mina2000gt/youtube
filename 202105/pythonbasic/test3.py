from Crypto.Cipher import AES

cipher = AES.new('KEY'.zfill(16),AES.MODE_CBC,'IV'.zfill(16))
plaintext = 'This is plaintext'.zfill(32)
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)
