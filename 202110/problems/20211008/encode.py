from FLAG import flag
from base64 import b64encode
from random import randint

cipher = flag
repeat = randint(15,30)
for _ in range(repeat):
    cipher = b64encode(cipher)
open('out.txt','wb').write(cipher)