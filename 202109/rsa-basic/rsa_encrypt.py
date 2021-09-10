from Crypto.Util.number import bytes_to_long, getPrime
#plaintextを数字に変換
plaintext = b'This is a plaintext'
m = bytes_to_long(plaintext)
#p,q,nを計算
p = getPrime(1024)
q = getPrime(1024)
n = p*q
# eは65537を使うことが多い
e = 65537
# 暗号化
c = pow(m, e, n)
# ciphertextとしてファイルに書き込み
out = open('cipher','w')
out.write("p = "+str(p)+'\n')
out.write("q = "+str(q)+'\n')
out.write("n = "+str(n)+'\n')
out.write("e = "+str(e)+'\n')
out.write("c = "+str(c)+'\n')