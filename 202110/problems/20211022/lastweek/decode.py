from Crypto.Util.number import long_to_bytes
dat = open('chall','r').read()
dat = dat.replace('00000000','0')
dat = dat.replace('11111111','1')
dat = int(dat,2)
print(long_to_bytes(dat))